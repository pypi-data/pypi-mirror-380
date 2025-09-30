"""
Nia MCP Proxy Server - Lightweight server that communicates with Nia API
"""
import os
import logging
import json
import asyncio
import webbrowser
from typing import List, Optional, Dict, Any
from datetime import datetime
from urllib.parse import urlparse

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, Resource
from .api_client import NIAApiClient, APIError
from .project_init import initialize_nia_project
from .profiles import get_supported_profiles
from dotenv import load_dotenv
import json

# Load .env from parent directory (nia-app/.env)
from pathlib import Path
env_path = Path(__file__).parent.parent.parent.parent / ".env"
load_dotenv(env_path)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Changed from INFO to DEBUG for troubleshooting
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)
logger = logging.getLogger(__name__)

# TOOL SELECTION GUIDE FOR AI ASSISTANTS:
# 
# Use 'nia_web_search' for:
#   - "Find RAG libraries" → Simple search
#   - "What's trending in Rust?" → Quick discovery
#   - "Show me repos like LangChain" → Similarity search
#
# Use 'nia_deep_research_agent' for:
#   - "Compare RAG vs GraphRAG approaches" → Comparative analysis
#   - "What are the best vector databases for production?" → Evaluation needed
#   - "Analyze the pros and cons of different LLM frameworks" → Structured analysis
#
# The AI should assess query complexity and choose accordingly.

# Create the MCP server
mcp = FastMCP("nia-knowledge-agent")

# Global API client instance
api_client: Optional[NIAApiClient] = None

def get_api_key() -> str:
    """Get API key from environment."""
    api_key = os.getenv("NIA_API_KEY")
    if not api_key:
        raise ValueError(
            "NIA_API_KEY environment variable not set. "
            "Get your API key at https://trynia.ai/api-keys"
        )
    return api_key

async def ensure_api_client() -> NIAApiClient:
    """Ensure API client is initialized."""
    global api_client
    if not api_client:
        api_key = get_api_key()
        api_client = NIAApiClient(api_key)
        # Validate the API key
        if not await api_client.validate_api_key():
            # The validation error is already logged, just raise a generic error
            raise ValueError("Failed to validate API key. Check logs for details.")
    return api_client

# Tools

@mcp.tool()
async def index_repository(
    repo_url: str,
    branch: Optional[str] = None
) -> List[TextContent]:
    """
    Args:
        repo_url: GitHub repository URL (e.g., https://github.com/owner/repo or https://github.com/owner/repo/tree/branch)
        branch: Branch to index (optional, defaults to main branch)

    Important:
        - When started indexing, prompt users to either use check_repository_status tool or go to app.trynia.ai to check the status.
    """
    try:
        client = await ensure_api_client()
        
        # Start indexing
        logger.info(f"Starting to index repository: {repo_url}")
        result = await client.index_repository(repo_url, branch)
        
        repository = result.get("repository", repo_url)
        status = result.get("status", "unknown")
        
        if status == "completed":
            return [TextContent(
                type="text",
                text=f"✅ Repository already indexed: {repository}\n"
                     f"Branch: {result.get('branch', 'main')}\n"
                     f"You can now search this codebase!"
            )]
        else:
            # Wait for indexing to complete
            return [TextContent(
                type="text",
                text=f"⏳ Indexing started for: {repository}\n"
                     f"Branch: {branch or 'default'}\n"
                     f"Status: {status}\n\n"
                     f"Use `check_repository_status` to monitor progress."
            )]
            
    except APIError as e:
        logger.error(f"API Error indexing repository: {e} (status_code={e.status_code}, detail={e.detail})")
        if e.status_code == 403 or "free tier limit" in str(e).lower() or "indexing operations" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text", 
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Unexpected error indexing repository: {e}")
        error_msg = str(e)
        if "indexing operations" in error_msg.lower() or "lifetime limit" in error_msg.lower():
            return [TextContent(
                type="text",
                text=f"❌ {error_msg}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
            )]
        return [TextContent(
            type="text",
            text=f"❌ Error indexing repository: {error_msg}"
        )]

@mcp.tool()
async def search_codebase(
    query: str,
    repositories: Optional[List[str]] = None,
    include_sources: bool = True
) -> List[TextContent]:
    """
    Search indexed repositories using natural language.
    
    Args:
        query: Natural language search query.
        repositories: List of repositories to search (owner/repo or owner/repo/tree/branch).
        include_sources: default to True.
        
    Returns:
        Search results with relevant code snippets and explanations
    """
    try:
        client = await ensure_api_client()
        
        # Require explicit repository selection
        if not repositories:
            return [TextContent(
                type="text",
                text="🔍 **Please specify which repositories to search:**\n\n"
                     "1. Use `list_repositories` to see available repositories\n"
                     "2. Then call `search_codebase(\"your query\", [\"owner/repo1\", \"owner/repo2\"])`\n\n"
                     "**Example:**\n"
                     "```\n"
                     "search_codebase(\"How does auth work?\", [\"facebook/react\"])\n"
                     "```\n\n"
                     "**📌 Tip:** You can search specific folders using the exact format from `list_repositories`:\n"
                     "```\n"
                     "search_codebase(\"query\", [\"owner/repo/tree/branch/folder\"])\n"
                     "```"
            )]
        
        # Build messages for the query
        messages = [
            {"role": "user", "content": query}
        ]
        
        logger.info(f"Searching {len(repositories)} repositories")
        
        # Stream the response using unified query
        response_parts = []
        sources_parts = []
        follow_up_questions = []
        
        async for chunk in client.query_unified(
            messages=messages,
            repositories=repositories,
            data_sources=[],  # No documentation sources
            search_mode="repositories",  # Use repositories mode to exclude external sources
            stream=True,
            include_sources=include_sources
        ):
            try:
                data = json.loads(chunk)
                
                if "content" in data and data["content"] and data["content"] != "[DONE]":
                    response_parts.append(data["content"])
                
                if "sources" in data and data["sources"]:
                    logger.debug(f"Received sources data: {type(data['sources'])}, count: {len(data['sources'])}")
                    sources_parts.extend(data["sources"])
                
                if "follow_up_questions" in data and data["follow_up_questions"]:
                    follow_up_questions = data["follow_up_questions"]
                    logger.debug(f"Received {len(follow_up_questions)} follow-up questions")
                    
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse JSON chunk: {chunk}, error: {e}")
                continue
        
        # Format the response
        response_text = "".join(response_parts)
        
        if sources_parts and include_sources:
            response_text += "\n\n## Sources\n\n"
            for i, source in enumerate(sources_parts[:10], 1):  # Limit to 10 sources (matches backend)
                response_text += f"### Source {i}\n"
                
                # Handle both string sources (file paths) and dictionary sources
                if isinstance(source, str):
                    # Source is just a file path string
                    response_text += f"**File:** `{source}`\n\n"
                    continue
                elif not isinstance(source, dict):
                    logger.warning(f"Expected source to be dict or str, got {type(source)}: {source}")
                    response_text += f"**Source:** {str(source)}\n\n"
                    continue
                
                # Handle dictionary sources with metadata
                metadata = source.get("metadata", {})
                
                # Repository name
                repository = source.get("repository") or metadata.get("source_name") or metadata.get("repository")
                if repository:
                    response_text += f"**Repository:** {repository}\n"
                
                # File path
                file_path = source.get("file") or source.get("file_path") or metadata.get("file_path")
                if file_path:
                    response_text += f"**File:** `{file_path}`\n"
                
                # Content/preview
                content = source.get("preview") or source.get("content")
                if content:
                    # Truncate very long content
                    if len(content) > 500:
                        content = content[:500] + "..."
                    response_text += f"```\n{content}\n```\n\n"
                else:
                    # If no content, at least show that this is a valid source
                    response_text += f"*Referenced source*\n\n"
            
            # Add helpful text about read_source_content tool
            response_text += "\n💡 **Need more details from a source?**\n\n"
            response_text += "If you need more information from the source links provided above, use the `read_source_content` tool from the available tools provided by Nia to get full context about that particular source.\n"
        
        # Add follow-up questions if available
        if follow_up_questions:
            response_text += "\n\n## 🔍 Suggested Follow-up Questions\n\n"
            for i, question in enumerate(follow_up_questions, 1):
                response_text += f"{i}. {question}\n"
            response_text += "\n*These questions are based on the search results and can help you explore deeper insights.*\n"
        
        return [TextContent(type="text", text=response_text)]
        
    except APIError as e:
        logger.error(f"API Error searching codebase: {e} (status_code={e.status_code}, detail={e.detail})")
        if e.status_code == 403 or "free tier limit" in str(e).lower() or "indexing operations" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text", 
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Unexpected error searching codebase: {e}")
        error_msg = str(e)
        if "indexing operations" in error_msg.lower() or "lifetime limit" in error_msg.lower():
            return [TextContent(
                type="text",
                text=f"❌ {error_msg}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
            )]
        return [TextContent(
            type="text",
            text=f"❌ Error searching codebase: {error_msg}"
        )]

@mcp.tool()
async def search_documentation(
    query: str,
    sources: Optional[List[str]] = None,
    include_sources: bool = True
) -> List[TextContent]:
    """
    Search indexed documentation using natural language.

    Args:
        query: Natural language search query. Don't just use keywords or unstrctured query, make a comprehensive question to get the best results possible.
        sources: List of documentation identifiers to search. Preferred format is UUID, but also supports:
            - Source UUIDs - RECOMMENDED
            - Display names 
            - URLs
    Important:
        - UUIDs are the preferred identifier format for best performance
    """
    try:
        client = await ensure_api_client()
        
        # Require explicit source selection
        if not sources:
            return [TextContent(
                type="text",
                text="📚 **Please specify which documentation sources to search:**\n\n"
                     "1. Use `list_documentation` to see available sources and their UUIDs\n"
                     "2. Then call `search_documentation(\"your query\", [\"uuid1\", \"uuid2\"])`\n\n"
                     "**Supported identifier formats (UUIDs preferred):**\n"
                     "- UUIDs: `\"550e8400-e29b-41d4-a716-446655440000\"` - RECOMMENDED\n"
                     "- Display names: `\"Vercel AI SDK - Core\"`\n"
                     "- URLs: `\"https://docs.trynia.ai/\"`\n\n"
                     "**Example (preferred):**\n"
                     "```\n"
                     "search_documentation(\"API reference\", [\"550e8400-e29b-41d4-a716-446655440000\"])\n"
                     "```\n\n"
                     "**📌 Tip:** UUIDs provide best performance and reliability"
            )]
        
        # Build messages for the query
        messages = [
            {"role": "user", "content": query}
        ]
        
        logger.info(f"Searching {len(sources)} documentation sources")
        
        # Stream the response using unified query
        response_parts = []
        sources_parts = []
        follow_up_questions = []
        
        async for chunk in client.query_unified(
            messages=messages,
            repositories=[],  # No repositories
            data_sources=sources,
            search_mode="unified",  # Use unified mode for intelligent LLM processing
            stream=True,
            include_sources=include_sources
        ):
            try:
                data = json.loads(chunk)
                
                if "content" in data and data["content"] and data["content"] != "[DONE]":
                    response_parts.append(data["content"])
                
                if "sources" in data and data["sources"]:
                    logger.debug(f"Received doc sources data: {type(data['sources'])}, count: {len(data['sources'])}")
                    sources_parts.extend(data["sources"])
                
                if "follow_up_questions" in data and data["follow_up_questions"]:
                    follow_up_questions = data["follow_up_questions"]
                    logger.debug(f"Received {len(follow_up_questions)} follow-up questions for documentation")
                    
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse JSON chunk in documentation search: {chunk}, error: {e}")
                continue
        
        # Format the response
        response_text = "".join(response_parts)
        
        if sources_parts and include_sources:
            response_text += "\n\n## Sources\n\n"
            for i, source in enumerate(sources_parts[:10], 1):  # Limit to 10 sources (matches backend)
                response_text += f"### Source {i}\n"
                
                # Handle both string sources and dictionary sources
                if isinstance(source, str):
                    # Source is just a URL or file path string
                    response_text += f"**Document:** {source}\n\n"
                    continue
                elif not isinstance(source, dict):
                    logger.warning(f"Expected source to be dict or str, got {type(source)}: {source}")
                    response_text += f"**Source:** {str(source)}\n\n"
                    continue
                
                # Handle dictionary sources with metadata
                metadata = source.get("metadata", {})
                
                # URL or file
                url = source.get("url") or metadata.get("url") or metadata.get("source") or metadata.get("sourceURL")
                file_path = source.get("file") or source.get("file_path") or metadata.get("file_path") or metadata.get("document_name")
                
                if url:
                    response_text += f"**URL:** {url}\n"
                elif file_path:
                    response_text += f"**Document:** {file_path}\n"
                
                # Title if available
                title = source.get("title") or metadata.get("title")
                if title:
                    response_text += f"**Title:** {title}\n"
                
                # Add spacing after each source
                response_text += "\n"
            
            # Add helpful text about read_source_content tool
            response_text += "\n💡 **Need more details from a source?**\n\n"
            response_text += "If you need more information from the source links provided above, use the `read_source_content` tool from the available tools provided by Nia to get full context about that particular source.\n"
        
        # Add follow-up questions if available
        if follow_up_questions:
            response_text += "\n\n## 🔍 Suggested Follow-up Questions\n\n"
            for i, question in enumerate(follow_up_questions, 1):
                response_text += f"{i}. {question}\n"
            response_text += "\n*These questions are based on the documentation and can help you explore related topics.*\n"
        
        return [TextContent(type="text", text=response_text)]
        
    except APIError as e:
        logger.error(f"API Error searching documentation: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error searching documentation: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error searching documentation: {str(e)}"
        )]

# @mcp.tool()
# async def list_repositories() -> List[TextContent]:
    """    
    Returns:
        List of indexed repositories with their status
    """
    try:
        client = await ensure_api_client()
        repositories = await client.list_repositories()
        
        if not repositories:
            return [TextContent(
                type="text",
                text="No indexed repositories found.\n\n"
                     "Get started by indexing a repository:\n"
                     "Use `index_repository` with a GitHub URL."
            )]
        
        # Format repository list
        lines = ["# Indexed Repositories\n"]
        
        # Check if any repositories have folder paths (contain /tree/)
        has_folder_repos = any('/tree/' in repo.get('repository', '') for repo in repositories)
        
        for repo in repositories:
            status_icon = "✅" if repo.get("status") == "completed" else "⏳"
            
            # Show display name if available, otherwise show repository
            display_name = repo.get("display_name")
            repo_name = repo['repository']
            
            if display_name:
                lines.append(f"\n## {status_icon} {display_name}")
                lines.append(f"- **Repository:** {repo_name}")
            else:
                lines.append(f"\n## {status_icon} {repo_name}")
            
            lines.append(f"- **Branch:** {repo.get('branch', 'main')}")
            lines.append(f"- **Status:** {repo.get('status', 'unknown')}")
            if repo.get("indexed_at"):
                lines.append(f"- **Indexed:** {repo['indexed_at']}")
            if repo.get("error"):
                lines.append(f"- **Error:** {repo['error']}")
            
            # Add usage hint for completed repositories
            if repo.get("status") == "completed":
                lines.append(f"- **Usage:** `search_codebase(query, [\"{repo_name}\"])`")
        
        # Return without usage tips
        return [TextContent(type="text", text="\n".join(lines))]
        
    except APIError as e:
        logger.error(f"API Error listing repositories: {e} (status_code={e.status_code}, detail={e.detail})")
        # Check for free tier limit errors
        if e.status_code == 403 or "free tier limit" in str(e).lower() or "indexing operations" in str(e).lower():
            # Extract the specific limit message
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text", 
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Unexpected error listing repositories (type={type(e).__name__}): {e}")
        # Check if this looks like an API limit error that wasn't caught properly
        error_msg = str(e)
        if "indexing operations" in error_msg.lower() or "lifetime limit" in error_msg.lower():
            return [TextContent(
                type="text",
                text=f"❌ {error_msg}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
            )]
        return [TextContent(
            type="text",
            text=f"❌ Error listing repositories: {error_msg}"
        )]

# @mcp.tool()
# async def check_repository_status(repository: str) -> List[TextContent]:
    """
    Check the indexing status of a repository.
    
    Args:
        repository: Repository in owner/repo format
    """
    try:
        client = await ensure_api_client()
        status = await client.get_repository_status(repository)
        
        if not status:
            return [TextContent(
                type="text",
                text=f"❌ Repository '{repository}' not found."
            )]
        
        # Format status
        status_icon = {
            "completed": "✅",
            "indexing": "⏳",
            "failed": "❌",
            "pending": "🔄"
        }.get(status["status"], "❓")
        
        lines = [
            f"# Repository Status: {repository}\n",
            f"{status_icon} **Status:** {status['status']}",
            f"**Branch:** {status.get('branch', 'main')}"
        ]
        
        if status.get("progress"):
            progress = status["progress"]
            if isinstance(progress, dict):
                lines.append(f"**Progress:** {progress.get('percentage', 0)}%")
                if progress.get("stage"):
                    lines.append(f"**Stage:** {progress['stage']}")
        
        if status.get("indexed_at"):
            lines.append(f"**Indexed:** {status['indexed_at']}")
        
        if status.get("error"):
            lines.append(f"**Error:** {status['error']}")
        
        return [TextContent(type="text", text="\n".join(lines))]
        
    except APIError as e:
        logger.error(f"API Error checking repository status: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error checking repository status: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error checking repository status: {str(e)}"
        )]

@mcp.tool()
async def index_documentation(
    url: str,
    url_patterns: Optional[List[str]] = None,
    exclude_patterns: Optional[List[str]] = None,
    max_age: Optional[int] = None,
    only_main_content: Optional[bool] = True,
    wait_for: Optional[int] = None,
    include_screenshot: Optional[bool] = None,
    check_llms_txt: Optional[bool] = True,
    llms_txt_strategy: Optional[str] = "prefer"
) -> List[TextContent]:
    """
    Index documentation or website for intelligent search.
    
    Args:
        url: URL of the documentation site to index
        url_patterns: Optional list of URL patterns to include in crawling
        exclude_patterns: Optional list of URL patterns to exclude from crawling
    """
    try:
        client = await ensure_api_client()
        
        # Create and start indexing
        logger.info(f"Starting to index documentation: {url}")
        result = await client.create_data_source(
            url=url, 
            url_patterns=url_patterns,
            exclude_patterns=exclude_patterns,
            max_age=max_age,
            only_main_content=only_main_content,
            wait_for=wait_for,
            include_screenshot=include_screenshot,
            check_llms_txt=check_llms_txt,
            llms_txt_strategy=llms_txt_strategy
        )
        
        source_id = result.get("id")
        status = result.get("status", "unknown")
        
        if status == "completed":
            return [TextContent(
                type="text",
                text=f"✅ Documentation already indexed: {url}\n"
                     f"Source ID: {source_id}\n"
                     f"You can now search this documentation!"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"⏳ Documentation indexing started: {url}\n"
                     f"Source ID: {source_id}\n"
                     f"Status: {status}\n\n"
                     f"Use `check_documentation_status` to monitor progress."
            )]
            
    except APIError as e:
        logger.error(f"API Error indexing documentation: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error indexing documentation: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error indexing documentation: {str(e)}"
        )]

# @mcp.tool()
# async def list_documentation() -> List[TextContent]:
    """
    Returns:
        List of indexed documentation with their status
    """
    try:
        client = await ensure_api_client()
        sources = await client.list_data_sources()
        
        if not sources:
            return [TextContent(
                type="text",
                text="No indexed documentation found.\n\n"
                     "Get started by indexing documentation:\n"
                     "Use `index_documentation` with a URL."
            )]
        
        # Format source list
        lines = ["# Indexed Documentation\n"]
        
        for source in sources:
            status_icon = "✅" if source.get("status") == "completed" else "⏳"
            
            # Show display name if available, otherwise show URL
            display_name = source.get("display_name")
            url = source.get('url', 'Unknown URL')
            
            if display_name:
                lines.append(f"\n## {status_icon} {display_name}")
                lines.append(f"- **URL:** {url}")
            else:
                lines.append(f"\n## {status_icon} {url}")
            
            lines.append(f"- **ID:** {source['id']}")
            lines.append(f"- **Status:** {source.get('status', 'unknown')}")
            lines.append(f"- **Type:** {source.get('source_type', 'web')}")
            if source.get("page_count", 0) > 0:
                lines.append(f"- **Pages:** {source['page_count']}")
            if source.get("created_at"):
                lines.append(f"- **Created:** {source['created_at']}")
        
        return [TextContent(type="text", text="\n".join(lines))]
        
    except APIError as e:
        logger.error(f"API Error listing documentation: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error listing documentation: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error listing documentation: {str(e)}"
        )]

# @mcp.tool()
# async def check_documentation_status(source_id: str) -> List[TextContent]:
    """
    Args:
        source_id: Documentation source ID
        
    Returns:
        Current status of the documentation source
    """
    try:
        client = await ensure_api_client()
        status = await client.get_data_source_status(source_id)
        
        if not status:
            return [TextContent(
                type="text",
                text=f"❌ Documentation source '{source_id}' not found."
            )]
        
        # Format status
        status_icon = {
            "completed": "✅",
            "processing": "⏳",
            "failed": "❌",
            "pending": "🔄"
        }.get(status["status"], "❓")
        
        lines = [
            f"# Documentation Status: {status.get('url', 'Unknown URL')}\n",
            f"{status_icon} **Status:** {status['status']}",
            f"**Source ID:** {source_id}"
        ]
        
        if status.get("page_count", 0) > 0:
            lines.append(f"**Pages Indexed:** {status['page_count']}")
        
        if status.get("details"):
            details = status["details"]
            if details.get("progress"):
                lines.append(f"**Progress:** {details['progress']}%")
            if details.get("stage"):
                lines.append(f"**Stage:** {details['stage']}")
        
        if status.get("created_at"):
            lines.append(f"**Created:** {status['created_at']}")
        
        if status.get("error"):
            lines.append(f"**Error:** {status['error']}")
        
        return [TextContent(type="text", text="\n".join(lines))]
        
    except APIError as e:
        logger.error(f"API Error checking documentation status: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error checking documentation status: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error checking documentation status: {str(e)}"
        )]

# Combined Resource Management Tools

@mcp.tool()
async def rename_resource(
    resource_type: str,
    identifier: str,
    new_name: str
) -> List[TextContent]:
    """
    Rename a resource (repository or documentation) for better organization.

    Args:
        resource_type: Type of resource - "repository" or "documentation"
        identifier:
            - For repos: Repository in owner/repo format (e.g., "facebook/react")
            - For docs: UUID preferred, also supports display name or URL
    """
    try:
        # Validate resource type
        if resource_type not in ["repository", "documentation"]:
            return [TextContent(
                type="text",
                text=f"❌ Invalid resource_type: '{resource_type}'. Must be 'repository' or 'documentation'."
            )]

        # Validate name length
        if not new_name or len(new_name) > 100:
            return [TextContent(
                type="text",
                text="❌ Display name must be between 1 and 100 characters."
            )]

        client = await ensure_api_client()

        if resource_type == "repository":
            result = await client.rename_repository(identifier, new_name)
            resource_desc = f"repository '{identifier}'"
        else:  # documentation
            result = await client.rename_data_source(identifier, new_name)
            resource_desc = f"documentation source"

        if result.get("success"):
            return [TextContent(
                type="text",
                text=f"✅ Successfully renamed {resource_desc} to '{new_name}'"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to rename {resource_type}: {result.get('message', 'Unknown error')}"
            )]

    except APIError as e:
        logger.error(f"API Error renaming {resource_type}: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error renaming {resource_type}: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error renaming {resource_type}: {str(e)}"
        )]

@mcp.tool()
async def delete_resource(
    resource_type: str,
    identifier: str
) -> List[TextContent]:
    """
    Delete an indexed resource (repository or documentation).

    Args:
        resource_type: Type of resource - "repository" or "documentation"
        identifier:
            - For repos: Repository in owner/repo format (e.g., "facebook/react")
            - For docs: UUID preferred, also supports display name or URL
    """
    try:
        # Validate resource type
        if resource_type not in ["repository", "documentation"]:
            return [TextContent(
                type="text",
                text=f"❌ Invalid resource_type: '{resource_type}'. Must be 'repository' or 'documentation'."
            )]

        client = await ensure_api_client()

        if resource_type == "repository":
            success = await client.delete_repository(identifier)
            resource_desc = f"repository: {identifier}"
        else:  # documentation
            success = await client.delete_data_source(identifier)
            resource_desc = f"documentation source: {identifier}"

        if success:
            return [TextContent(
                type="text",
                text=f"✅ Successfully deleted {resource_desc}"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to delete {resource_desc}"
            )]

    except APIError as e:
        logger.error(f"API Error deleting {resource_type}: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error deleting {resource_type}: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error deleting {resource_type}: {str(e)}"
        )]

@mcp.tool()
async def check_resource_status(
    resource_type: str,
    identifier: str
) -> List[TextContent]:
    """
    Check the indexing status of a resource (repository or documentation).

    Args:
        resource_type: Type of resource - "repository" or "documentation"
        identifier:
            - For repos: Repository in owner/repo format 
            - For docs: Source ID (UUID format only)
    """
    try:
        # Validate resource type
        if resource_type not in ["repository", "documentation"]:
            return [TextContent(
                type="text",
                text=f"❌ Invalid resource_type: '{resource_type}'. Must be 'repository' or 'documentation'."
            )]

        client = await ensure_api_client()

        if resource_type == "repository":
            status = await client.get_repository_status(identifier)
            if not status:
                return [TextContent(
                    type="text",
                    text=f"❌ Repository '{identifier}' not found."
                )]
            title = f"Repository Status: {identifier}"
            status_key = "status"
        else:  # documentation
            status = await client.get_data_source_status(identifier)
            if not status:
                return [TextContent(
                    type="text",
                    text=f"❌ Documentation source '{identifier}' not found."
                )]
            title = f"Documentation Status: {status.get('url', 'Unknown URL')}"
            status_key = "status"

        # Format status with appropriate icon
        status_text = status.get(status_key, "unknown")
        status_icon = {
            "completed": "✅",
            "indexing": "⏳",
            "processing": "⏳",
            "failed": "❌",
            "pending": "🔄",
            "error": "❌"
        }.get(status_text, "❓")

        lines = [
            f"# {title}\n",
            f"{status_icon} **Status:** {status_text}"
        ]

        # Add resource-specific fields
        if resource_type == "repository":
            lines.append(f"**Branch:** {status.get('branch', 'main')}")
            if status.get("progress"):
                progress = status["progress"]
                if isinstance(progress, dict):
                    lines.append(f"**Progress:** {progress.get('percentage', 0)}%")
                    if progress.get("stage"):
                        lines.append(f"**Stage:** {progress['stage']}")
        else:  # documentation
            lines.append(f"**Source ID:** {identifier}")
            if status.get("page_count", 0) > 0:
                lines.append(f"**Pages Indexed:** {status['page_count']}")
            if status.get("details"):
                details = status["details"]
                if details.get("progress"):
                    lines.append(f"**Progress:** {details['progress']}%")
                if details.get("stage"):
                    lines.append(f"**Stage:** {details['stage']}")

        # Common fields
        if status.get("indexed_at"):
            lines.append(f"**Indexed:** {status['indexed_at']}")
        elif status.get("created_at"):
            lines.append(f"**Created:** {status['created_at']}")

        if status.get("error"):
            lines.append(f"**Error:** {status['error']}")

        return [TextContent(type="text", text="\n".join(lines))]

    except APIError as e:
        logger.error(f"API Error checking {resource_type} status: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error checking {resource_type} status: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error checking {resource_type} status: {str(e)}"
        )]

@mcp.tool()
async def list_resources(
    resource_type: Optional[str] = None
) -> List[TextContent]:
    """
    List indexed resources (repositories and/or documentation).

    Args:
        resource_type: Optional filter - "repository", "documentation", or None for all

    Returns:
        List of indexed resources with their status
    """
    try:
        # Validate resource type if provided
        if resource_type and resource_type not in ["repository", "documentation"]:
            return [TextContent(
                type="text",
                text=f"❌ Invalid resource_type: '{resource_type}'. Must be 'repository', 'documentation', or None for all."
            )]

        client = await ensure_api_client()
        lines = []

        # Determine what to list
        list_repos = resource_type in [None, "repository"]
        list_docs = resource_type in [None, "documentation"]

        if list_repos:
            repositories = await client.list_repositories()

            if repositories:
                lines.append("# Indexed Repositories\n")
                for repo in repositories:
                    status_icon = "✅" if repo.get("status") == "completed" else "⏳"

                    # Show display name if available, otherwise show repository
                    display_name = repo.get("display_name")
                    repo_name = repo['repository']

                    if display_name:
                        lines.append(f"\n## {status_icon} {display_name}")
                        lines.append(f"- **Repository:** {repo_name}")
                    else:
                        lines.append(f"\n## {status_icon} {repo_name}")

                    lines.append(f"- **Branch:** {repo.get('branch', 'main')}")
                    lines.append(f"- **Status:** {repo.get('status', 'unknown')}")
                    if repo.get("indexed_at"):
                        lines.append(f"- **Indexed:** {repo['indexed_at']}")
                    if repo.get("error"):
                        lines.append(f"- **Error:** {repo['error']}")

                    # Add usage hint for completed repositories
                    if repo.get("status") == "completed":
                        lines.append(f"- **Usage:** `search_codebase(query, [\"{repo_name}\"])`")
            elif resource_type == "repository":
                lines.append("No indexed repositories found.\n\n")
                lines.append("Get started by indexing a repository:\n")
                lines.append("Use `index_repository` with a GitHub URL.")

        if list_docs:
            sources = await client.list_data_sources()

            if sources:
                if lines:  # Add separator if we already have repositories
                    lines.append("\n---\n")
                lines.append("# Indexed Documentation\n")

                for source in sources:
                    status_icon = "✅" if source.get("status") == "completed" else "⏳"

                    # Show display name if available, otherwise show URL
                    display_name = source.get("display_name")
                    url = source.get('url', 'Unknown URL')

                    if display_name:
                        lines.append(f"\n## {status_icon} {display_name}")
                        lines.append(f"- **URL:** {url}")
                    else:
                        lines.append(f"\n## {status_icon} {url}")

                    lines.append(f"- **ID:** {source['id']}")
                    lines.append(f"- **Status:** {source.get('status', 'unknown')}")
                    lines.append(f"- **Type:** {source.get('source_type', 'web')}")
                    if source.get("page_count", 0) > 0:
                        lines.append(f"- **Pages:** {source['page_count']}")
                    if source.get("created_at"):
                        lines.append(f"- **Created:** {source['created_at']}")
            elif resource_type == "documentation":
                lines.append("No indexed documentation found.\n\n")
                lines.append("Get started by indexing documentation:\n")
                lines.append("Use `index_documentation` with a URL.")

        if not lines:
            lines.append("No indexed resources found.\n\n")
            lines.append("Get started by indexing:\n")
            lines.append("- Use `index_repository` for GitHub repositories\n")
            lines.append("- Use `index_documentation` for documentation sites")

        return [TextContent(type="text", text="\n".join(lines))]

    except APIError as e:
        logger.error(f"API Error listing resources: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 or "free tier limit" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                error_msg = f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
            else:
                error_msg += "\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Unexpected error listing resources: {e}")
        error_msg = str(e)
        if "indexing operations" in error_msg.lower() or "lifetime limit" in error_msg.lower():
            return [TextContent(
                type="text",
                text=f"❌ {error_msg}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
            )]
        return [TextContent(
            type="text",
            text=f"❌ Error listing resources: {error_msg}"
        )]

# Old individual tools (to be commented out after testing)

# @mcp.tool()
# async def delete_documentation(source_id: str) -> List[TextContent]:
    """
    Delete an indexed documentation source.
    
    Args:
        source_id: Documentation source ID to delete
    """
    try:
        client = await ensure_api_client()
        success = await client.delete_data_source(source_id)
        
        if success:
            return [TextContent(
                type="text",
                text=f"✅ Successfully deleted documentation source: {source_id}"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to delete documentation source: {source_id}"
            )]
            
    except APIError as e:
        logger.error(f"API Error deleting documentation: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error deleting documentation: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error deleting documentation: {str(e)}"
        )]

# @mcp.tool()
# async def delete_repository(repository: str) -> List[TextContent]:
    """
    Delete an indexed repository.
    
    Args:
        repository: Repository in owner/repo format
    """
    try:
        client = await ensure_api_client()
        success = await client.delete_repository(repository)
        
        if success:
            return [TextContent(
                type="text",
                text=f"✅ Successfully deleted repository: {repository}"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to delete repository: {repository}"
            )]
            
    except APIError as e:
        logger.error(f"API Error deleting repository: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit of 3 indexing operations. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error deleting repository: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error deleting repository: {str(e)}"
        )]

# @mcp.tool()
# async def rename_repository(repository: str, new_name: str) -> List[TextContent]:
    """
    Rename an indexed repository for better organization.
    
    Args:
        repository: Repository in owner/repo format
        new_name: New display name for the repository (1-100 characters)
    """
    try:
        # Validate name length
        if not new_name or len(new_name) > 100:
            return [TextContent(
                type="text",
                text="❌ Display name must be between 1 and 100 characters."
            )]
        
        client = await ensure_api_client()
        result = await client.rename_repository(repository, new_name)
        
        if result.get("success"):
            return [TextContent(
                type="text",
                text=f"✅ Successfully renamed repository '{repository}' to '{new_name}'"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to rename repository: {result.get('message', 'Unknown error')}"
            )]
            
    except APIError as e:
        logger.error(f"API Error renaming repository: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error renaming repository: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error renaming repository: {str(e)}"
        )]

# @mcp.tool()
# async def rename_documentation(source_id: str, new_name: str) -> List[TextContent]:
    """
    Rename a documentation source for better organization.
    
    Args:
        source_id: Documentation source ID
        new_name: New display name for the documentation (1-100 characters)
    """
    try:
        # Validate name length
        if not new_name or len(new_name) > 100:
            return [TextContent(
                type="text",
                text="❌ Display name must be between 1 and 100 characters."
            )]
        
        client = await ensure_api_client()
        result = await client.rename_data_source(source_id, new_name)
        
        if result.get("success"):
            return [TextContent(
                type="text",
                text=f"✅ Successfully renamed documentation source to '{new_name}'"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ Failed to rename documentation: {result.get('message', 'Unknown error')}"
            )]
            
    except APIError as e:
        logger.error(f"API Error renaming documentation: {e}")
        error_msg = f"❌ {str(e)}"
        if e.status_code == 403 and "lifetime limit" in str(e).lower():
            error_msg += "\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
        return [TextContent(type="text", text=error_msg)]
    except Exception as e:
        logger.error(f"Error renaming documentation: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error renaming documentation: {str(e)}"
        )]

@mcp.tool()
async def nia_web_search(
    query: str,
    num_results: int = 5,
    category: Optional[str] = None,
    days_back: Optional[int] = None,
    find_similar_to: Optional[str] = None
) -> List[TextContent]:
    """
    Search repositories, documentation, and other content using web search.
    
    Args:
        query: Natural language search query (e.g., "best RAG implementations", "trending rust web frameworks")
        num_results: Number of results to return (default: 5, max: 10)
        category: Filter by category: "github", "company", "research paper", "news", "tweet", "pdf"
        days_back: Only show results from the last N days (for trending content)
        find_similar_to: URL to find similar content
    """
    try:
        client = await ensure_api_client()
        
        logger.info(f"Searching content for query: {query}")
        
        # Use the API client method instead of direct HTTP call
        result = await client.web_search(
            query=query,
            num_results=num_results,
            category=category,
            days_back=days_back,
            find_similar_to=find_similar_to
        )
        
        # Extract results
        github_repos = result.get("github_repos", [])
        documentation = result.get("documentation", [])
        other_content = result.get("other_content", [])
        
        # Format response to naturally guide next actions
        response_text = f"## 🔍 Nia Web Search Results for: \"{query}\"\n\n"
        
        if days_back:
            response_text += f"*Showing results from the last {days_back} days*\n\n"
        
        if find_similar_to:
            response_text += f"*Finding content similar to: {find_similar_to}*\n\n"
        
        # GitHub Repositories Section
        if github_repos:
            response_text += f"### 📦 GitHub Repositories ({len(github_repos)} found)\n\n"
            
            for i, repo in enumerate(github_repos[:num_results], 1):
                response_text += f"**{i}. {repo['title']}**\n"
                response_text += f"   📍 `{repo['url']}`\n"
                if repo.get('published_date'):
                    response_text += f"   📅 Updated: {repo['published_date']}\n"
                if repo['summary']:
                    response_text += f"   📝 {repo['summary']}...\n"
                if repo['highlights']:
                    response_text += f"   ✨ Key features: {', '.join(repo['highlights'])}\n"
                response_text += "\n"
            
            # Be more aggressive based on query specificity
            if len(github_repos) == 1 or any(specific_word in query.lower() for specific_word in ["specific", "exact", "particular", "find me", "looking for"]):
                response_text += "**🚀 RECOMMENDED ACTION - Index this repository with Nia:**\n"
                response_text += f"```\nIndex {github_repos[0]['owner_repo']}\n```\n"
                response_text += "✨ This will enable AI-powered code search, understanding, and analysis!\n\n"
            else:
                response_text += "**🚀 Make these repositories searchable with NIA's AI:**\n"
                response_text += f"- **Quick start:** Say \"Index {github_repos[0]['owner_repo']}\"\n"
                response_text += "- **Index multiple:** Say \"Index all repositories\"\n"
                response_text += "- **Benefits:** AI-powered code search, architecture understanding, implementation details\n\n"
        
        # Documentation Section
        if documentation:
            response_text += f"### 📚 Documentation ({len(documentation)} found)\n\n"
            
            for i, doc in enumerate(documentation[:num_results], 1):
                response_text += f"**{i}. {doc['title']}**\n"
                response_text += f"   📍 `{doc['url']}`\n"
                if doc['summary']:
                    response_text += f"   📝 {doc['summary']}...\n"
                if doc.get('highlights'):
                    response_text += f"   ✨ Key topics: {', '.join(doc['highlights'])}\n"
                response_text += "\n"
            
            # Be more aggressive for documentation too
            if len(documentation) == 1 or any(specific_word in query.lower() for specific_word in ["docs", "documentation", "guide", "tutorial", "reference"]):
                response_text += "**📖 RECOMMENDED ACTION - Index this documentation with NIA:**\n"
                response_text += f"```\nIndex documentation {documentation[0]['url']}\n```\n"
                response_text += "✨ NIA will make this fully searchable with AI-powered Q&A!\n\n"
            else:
                response_text += "**📖 Make this documentation AI-searchable with NIA:**\n"
                response_text += f"- **Quick start:** Say \"Index documentation {documentation[0]['url']}\"\n"
                response_text += "- **Index all:** Say \"Index all documentation\"\n"
                response_text += "- **Benefits:** Instant answers, smart search, code examples extraction\n\n"
        
        # Other Content Section
        if other_content and not github_repos and not documentation:
            response_text += f"### 🌐 Other Content ({len(other_content)} found)\n\n"
            
            for i, content in enumerate(other_content[:num_results], 1):
                response_text += f"**{i}. {content['title']}**\n"
                response_text += f"   📍 `{content['url']}`\n"
                if content['summary']:
                    response_text += f"   📝 {content['summary']}...\n"
                response_text += "\n"
        
        # No results found
        if not github_repos and not documentation and not other_content:
            response_text = f"No results found for '{query}'. Try:\n"
            response_text += "- Using different keywords\n"
            response_text += "- Being more specific (e.g., 'Python RAG implementation')\n"
            response_text += "- Including technology names (e.g., 'LangChain', 'TypeScript')\n"
        
        # Add prominent call-to-action if we found indexable content
        if github_repos or documentation:
            response_text += "\n## 🎯 **Ready to unlock nia's tools**\n"
        
        # Add search metadata
        response_text += f"\n---\n"
        response_text += f"*Searched {result.get('total_results', 0)} sources using NIA Web Search*"
        
        return [TextContent(type="text", text=response_text)]
        
    except APIError as e:
        logger.error(f"API Error in web search: {e}")
        if e.status_code == 403 or "free tier limit" in str(e).lower() or "indexing operations" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text", 
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Error in NIA web search: {str(e)}")
        return [TextContent(
            type="text",
            text=f"❌ NIA Web Search error: {str(e)}\n\n"
                 "This might be due to:\n"
                 "- Network connectivity issues\n"
                 "- Service temporarily unavailable"
        )]

@mcp.tool()
async def nia_deep_research_agent(
    query: str,
    output_format: Optional[str] = None
) -> List[TextContent]:
    """
    Perform deep, multi-step research on a topic using advanced AI research capabilities.
    
    Args:
        query: Research question (e.g., "Compare top 3 RAG frameworks with pros/cons")
        output_format: Optional structure hint (e.g., "comparison table", "pros and cons list")
        
    Returns:
        Comprehensive research results with citations
    """
    try:
        client = await ensure_api_client()
        
        logger.info(f"Starting deep research for: {query}")
        
        # Use the API client method with proper timeout handling
        try:
            result = await asyncio.wait_for(
                client.deep_research(query=query, output_format=output_format),
                timeout=720.0  # 12 minutes to allow for longer research tasks
            )
        except asyncio.TimeoutError:
            logger.error(f"Deep research timed out after 12 minutes for query: {query}")
            return [TextContent(
                type="text",
                text="❌ Research timed out. The query may be too complex. Try:\n"
                     "- Breaking it into smaller questions\n"  
                     "- Using more specific keywords\n"
                     "- Trying the nia_web_search tool for simpler queries"
            )]
        
        # Format the research results
        response_text = f"## 🔬 NIA Deep Research Agent Results\n\n"
        response_text += f"**Query:** {query}\n\n"
        
        if result.get("data"):
            response_text += "### 📊 Research Findings:\n\n"
            
            # Pretty print the JSON data
            
            formatted_data = json.dumps(result["data"], indent=2)
            response_text += f"```json\n{formatted_data}\n```\n\n"
            
            # Add citations if available
            if result.get("citations"):
                response_text += "### 📚 Sources & Citations:\n\n"
                citation_num = 1
                for field, citations in result["citations"].items():
                    if citations:
                        response_text += f"**{field}:**\n"
                        for citation in citations[:3]:  # Limit to 3 citations per field
                            response_text += f"{citation_num}. [{citation.get('title', 'Source')}]({citation.get('url', '#')})\n"
                            if citation.get('snippet'):
                                response_text += f"   > {citation['snippet'][:150]}...\n"
                            citation_num += 1
                        response_text += "\n"
            
            response_text += "### 💡 RECOMMENDED NEXT ACTIONS WITH NIA:\n\n"
            
            # Extract potential repos and docs from the research data
            repos_found = []
            docs_found = []
            
            # Helper function to extract URLs from nested data structures
            def extract_urls_from_data(data, urls_list=None):
                if urls_list is None:
                    urls_list = []
                
                if isinstance(data, dict):
                    for value in data.values():
                        extract_urls_from_data(value, urls_list)
                elif isinstance(data, list):
                    for item in data:
                        extract_urls_from_data(item, urls_list)
                elif isinstance(data, str):
                    # Check if this string is a URL
                    if data.startswith(('http://', 'https://')):
                        urls_list.append(data)
                
                return urls_list
            
            # Extract all URLs from the data
            all_urls = extract_urls_from_data(result["data"])
            
            # Filter for GitHub repos and documentation
            import re
            github_pattern = r'github\.com/([a-zA-Z0-9-]+/[a-zA-Z0-9-_.]+)'
            
            for url in all_urls:
                # Check for GitHub repos
                github_match = re.search(github_pattern, url)
                if github_match and '/tree/' not in url and '/blob/' not in url:
                    repos_found.append(github_match.group(1))
                # Check for documentation URLs
                elif any(doc_indicator in url.lower() for doc_indicator in ['docs', 'documentation', '.readthedocs.', '/guide', '/tutorial']):
                    docs_found.append(url)
            
            # Remove duplicates and limit results
            repos_found = list(set(repos_found))[:3]
            docs_found = list(set(docs_found))[:3]
            
            if repos_found:
                response_text += "**🚀 DISCOVERED REPOSITORIES - Index with NIA for deep analysis:**\n"
                for repo in repos_found:
                    response_text += f"```\nIndex {repo}\n```\n"
                response_text += "✨ Enable AI-powered code search and architecture understanding!\n\n"
            
            if docs_found:
                response_text += "**📖 DISCOVERED DOCUMENTATION - Index with NIA for smart search:**\n"
                for doc in docs_found[:2]:  # Limit to 2 for readability
                    response_text += f"```\nIndex documentation {doc}\n```\n"
                response_text += "✨ Make documentation instantly searchable with AI Q&A!\n\n"
            
            if not repos_found and not docs_found:
                response_text += "**🔍 Manual indexing options:**\n"
                response_text += "- If you see any GitHub repos mentioned: Say \"Index [owner/repo]\"\n"
                response_text += "- If you see any documentation sites: Say \"Index documentation [url]\"\n"
                response_text += "- These will unlock NIA's powerful AI search capabilities!\n\n"
            
            response_text += "**📊 Other actions:**\n"
            response_text += "- Ask follow-up questions about the research\n"
            response_text += "- Request a different analysis format\n"
            response_text += "- Search for more specific information\n"
        else:
            response_text += "No structured data returned. The research may need a more specific query."
        
        return [TextContent(type="text", text=response_text)]
        
    except APIError as e:
        logger.error(f"API Error in deep research: {e}")
        if e.status_code == 403 or "free tier limit" in str(e).lower() or "indexing operations" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text", 
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited indexing."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Error in deep research: {str(e)}")
        return [TextContent(
            type="text",
            text=f"❌ Research error: {str(e)}\n\n"
                 "Try simplifying your question or using the regular nia_web_search tool."
        )]

@mcp.tool()
async def read_source_content(
    source_type: str,
    source_identifier: str,
    metadata: Optional[Dict[str, Any]] = None
) -> List[TextContent]:
    """
    Read the full content of a specific source file or document.
    
    Args:
        source_type: Type of source - "repository" or "documentation"
        source_identifier: 
            - For repository: "owner/repo:path/to/file.py"
            - For documentation: The source URL or document ID
        metadata: Optional metadata from search results to help locate the source
        
    Returns:
        Full content of the requested source with metadata
    """
    try:
        client = await ensure_api_client()
        
        logger.info(f"Reading source content - type: {source_type}, identifier: {source_identifier}")
        
        # Call the API to get source content
        result = await client.get_source_content(
            source_type=source_type,
            source_identifier=source_identifier,
            metadata=metadata or {}
        )
        
        if not result or not result.get("success"):
            error_msg = result.get("error", "Unknown error") if result else "Failed to fetch source content"
            return [TextContent(
                type="text",
                text=f"❌ Error reading source: {error_msg}"
            )]
        
        # Format the response
        content = result.get("content", "")
        source_metadata = result.get("metadata", {})
        
        # Build response with metadata header
        response_lines = []
        
        if source_type == "repository":
            repo_name = source_metadata.get("repository", "Unknown")
            file_path = source_metadata.get("file_path", source_identifier.split(":", 1)[-1] if ":" in source_identifier else "Unknown")
            branch = source_metadata.get("branch", "main")
            
            response_lines.extend([
                f"# Source: {repo_name}",
                f"**File:** `{file_path}`",
                f"**Branch:** {branch}",
                ""
            ])
            
            if source_metadata.get("url"):
                response_lines.append(f"**GitHub URL:** {source_metadata['url']}")
                response_lines.append("")
            
            # Add file info if available
            if source_metadata.get("size"):
                response_lines.append(f"**Size:** {source_metadata['size']} bytes")
            if source_metadata.get("language"):
                response_lines.append(f"**Language:** {source_metadata['language']}")
                
            response_lines.extend(["", "## Content", ""])
            
            # Add code block with language hint
            language = source_metadata.get("language", "").lower() or "text"
            response_lines.append(f"```{language}")
            response_lines.append(content)
            response_lines.append("```")
            
        elif source_type == "documentation":
            url = source_metadata.get("url", source_identifier)
            title = source_metadata.get("title", "Documentation")
            
            response_lines.extend([
                f"# Documentation: {title}",
                f"**URL:** {url}",
                ""
            ])
            
            if source_metadata.get("last_updated"):
                response_lines.append(f"**Last Updated:** {source_metadata['last_updated']}")
                response_lines.append("")
                
            response_lines.extend(["## Content", "", content])
        
        else:
            # Generic format for unknown source types
            response_lines.extend([
                f"# Source Content",
                f"**Type:** {source_type}",
                f"**Identifier:** {source_identifier}",
                "",
                "## Content",
                "",
                content
            ])
        
        return [TextContent(type="text", text="\n".join(response_lines))]
        
    except APIError as e:
        logger.error(f"API Error reading source content: {e}")
        if e.status_code == 403 or "free tier limit" in str(e).lower():
            return [TextContent(
                type="text",
                text=f"❌ {str(e)}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited access."
            )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Error reading source content: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error reading source content: {str(e)}"
        )]

@mcp.tool()
async def get_repository_hierarchy(
    repository: str,
    include_classes: bool = True,
    include_methods: bool = False,
    include_tree: bool = False
) -> List[TextContent]:
    """
    Get the file hierarchy for an indexed repository.

    Args:
        repository: Repository identifier in owner/repo format (e.g., "facebook/react")
        include_classes: Whether to include class names in the hierarchy (default: True)
        include_methods: Whether to include method names in the hierarchy (default: False)
        include_tree: Whether to include the full tree structure (default: False)

    Returns:
        Repository file hierarchy with statistics and structural information
    """
    try:
        client = await ensure_api_client()

        logger.info(f"Getting repository hierarchy for: {repository}")

        # Get the hierarchy data
        result = await client.get_repository_hierarchy(
            owner_repo=repository,
            include_classes=include_classes,
            include_methods=include_methods,
            include_tree=include_tree
        )

        # Format the response
        response_lines = []

        # Header
        response_lines.extend([
            f"# 🏗️ Repository File Hierarchy: {repository}",
            "",
            f"**Repository ID:** {result.get('repository_id', 'Unknown')}",
            f"**Generated:** {result.get('generated_at', 'Unknown')}",
            ""
        ])

        # Options used
        options = result.get("options", {})
        response_lines.extend([
            "**Options:**",
            f"- Include Classes: {'✅' if options.get('include_classes', include_classes) else '❌'}",
            f"- Include Methods: {'✅' if options.get('include_methods', include_methods) else '❌'}",
            f"- Include Tree: {'✅' if include_tree else '❌'}",
            ""
        ])

        # Statistics
        stats = result.get("stats", {})
        if stats:
            response_lines.extend([
                "## 📊 Statistics",
                ""
            ])

            if stats.get("total_files"):
                response_lines.append(f"📄 **Total Files:** {stats['total_files']:,}")
            if stats.get("total_directories"):
                response_lines.append(f"📁 **Total Directories:** {stats['total_directories']:,}")
            if stats.get("total_classes"):
                response_lines.append(f"🏷️ **Total Classes:** {stats['total_classes']:,}")
            if stats.get("total_methods"):
                response_lines.append(f"⚙️ **Total Methods:** {stats['total_methods']:,}")

            # File types breakdown
            if stats.get("file_types"):
                response_lines.extend([
                    "",
                    "**File Types:**"
                ])
                file_types = stats["file_types"]
                # Sort by count descending
                sorted_types = sorted(file_types.items(), key=lambda x: x[1], reverse=True)
                for ext, count in sorted_types[:10]:  # Show top 10
                    response_lines.append(f"- `{ext}`: {count:,} files")
                if len(sorted_types) > 10:
                    response_lines.append(f"- ... and {len(sorted_types) - 10} more types")

            response_lines.append("")

        # Hierarchy text
        hierarchy_text = result.get("hierarchy_text", "")
        if hierarchy_text:
            response_lines.extend([
                "## 🌳 File Hierarchy",
                "",
                "```",
                hierarchy_text,
                "```",
                ""
            ])

        # Tree structure if requested and available
        if include_tree and result.get("hierarchy_tree"):
            response_lines.extend([
                "## 🗂️ Detailed Tree Structure",
                "",
                "```json",
                json.dumps(result["hierarchy_tree"], indent=2),
                "```",
                ""
            ])

        # Usage tips
        response_lines.extend([
            "## 💡 Usage Tips",
            "",
            "- Use this hierarchy to understand the codebase structure before searching",
            "- Include methods for detailed function discovery",
            "- Use `search_codebase` with specific file paths found here",
            "- Reference file paths when using `read_source_content`"
        ])

        return [TextContent(type="text", text="\n".join(response_lines))]

    except APIError as e:
        logger.error(f"API Error getting repository hierarchy: {e}")

        if e.status_code == 404:
            return [TextContent(
                type="text",
                text=f"❌ Repository '{repository}' not found. Please check:\n\n"
                     "1. The repository name is correct (owner/repo format)\n"
                     "2. The repository has been indexed\n"
                     "3. You have access to this repository\n\n"
                     "Use `list_repositories` to see available repositories."
            )]
        elif e.status_code == 400:
            return [TextContent(
                type="text",
                text=f"❌ Repository not ready: {e.detail}\n\n"
                     f"The repository may still be indexing. Use `check_resource_status(\"repository\", \"{repository}\")` to check status."
            )]
        elif e.status_code == 403 or "free tier limit" in str(e).lower():
            if e.detail and "3 free indexing operations" in e.detail:
                return [TextContent(
                    type="text",
                    text=f"❌ {e.detail}\n\n💡 Tip: Upgrade to Pro at https://trynia.ai/billing for unlimited access."
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"❌ {str(e)}\n\n💡 Tip: You've reached the free tier limit. Upgrade to Pro for unlimited access."
                )]
        else:
            return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Unexpected error getting repository hierarchy: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error getting repository hierarchy: {str(e)}\n\n"
                 "Please check that:\n"
                 "- The repository identifier is correct\n"
                 "- The repository is fully indexed\n"
                 "- Your API connection is working"
        )]

# @mcp.tool()
# async def index_local_filesystem(
#     directory_path: str,
#     inclusion_patterns: Optional[List[str]] = None,
#     exclusion_patterns: Optional[List[str]] = None,
#     max_file_size_mb: int = 50
# ) -> List[TextContent]:
#     """
#     Index a local filesystem directory for intelligent search.
#
#     Args:
#         directory_path: Absolute path to the directory to index
#         inclusion_patterns: Optional list of patterns to include (e.g., ["ext:.py", "dir:src"])
#         exclusion_patterns: Optional list of patterns to exclude (e.g., ["dir:node_modules", "ext:.log"])
#         max_file_size_mb: Maximum file size in MB to process (default: 50)
#
#     Returns:
#         Status of the indexing operation
#
#     Important:
#         - Path must be absolute (e.g., /Users/username/projects/myproject)
#         - When indexing starts, use check_local_filesystem_status tool to monitor progress
#     """
#     try:
#         # Validate absolute path
#         if not os.path.isabs(directory_path):
#             return [TextContent(
#                 type="text",
#                 text=f"❌ Error: directory_path must be an absolute path. Got: {directory_path}\n\n"
#                      f"Example: /Users/username/projects/myproject"
#             )]
#
#         client = await ensure_api_client()
#
#         # Start indexing
#         logger.info(f"Starting to index local directory: {directory_path}")
#         result = await client.index_local_filesystem(
#             directory_path=directory_path,
#             inclusion_patterns=inclusion_patterns or [],
#             exclusion_patterns=exclusion_patterns or [],
#             max_file_size_mb=max_file_size_mb
#         )
#
#         if result.get("success"):
#             source_id = result["data"]["source_id"]
#             status_url = result["data"]["status_url"]
#
#             return [TextContent(
#                 type="text",
#                 text=(
#                     f"✅ Successfully started indexing local directory!\n\n"
#                     f"📁 **Directory:** `{directory_path}`\n"
#                     f"🆔 **Source ID:** `{source_id}`\n"
#                     f"📊 **Status:** Processing\n\n"
#                     f"**What happens next:**\n"
#                     f"• NIA is scanning and indexing your files in the background\n"
#                     f"• This process typically takes a few minutes depending on directory size\n"
#                     f"• Use `check_local_filesystem_status` with source ID `{source_id}` to monitor progress\n"
#                     f"• Once indexed, use `search_codebase` or `search_documentation` to search your files\n\n"
#                     f"📌 **Tip:** You can check the status at any time or visit [app.trynia.ai](https://app.trynia.ai) to monitor progress."
#                 )
#             )]
#         else:
#             return [TextContent(
#                 type="text",
#                 text=f"❌ Failed to start indexing: {result.get('detail', 'Unknown error')}"
#             )]
#
#     except APIError as e:
#         logger.error(f"API error indexing local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ API Error: {str(e)}\n\nStatus Code: {e.status_code}\nDetails: {e.detail}"
#         )]
#     except Exception as e:
#         logger.error(f"Unexpected error indexing local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ Error: An unexpected error occurred while indexing the directory: {str(e)}"
#         )]

# @mcp.tool()
# async def scan_local_filesystem(
#     directory_path: str,
#     inclusion_patterns: Optional[List[str]] = None,
#     exclusion_patterns: Optional[List[str]] = None,
#     max_file_size_mb: int = 50
# ) -> List[TextContent]:
#     """
#     Scan a local filesystem directory to preview what files would be indexed.
#
#     This tool helps you understand what files will be processed before actually indexing.
#
#     Args:
#         directory_path: Absolute path to the directory to scan
#         inclusion_patterns: Optional list of patterns to include (e.g., ["ext:.py", "dir:src"])
#         exclusion_patterns: Optional list of patterns to exclude (e.g., ["dir:node_modules", "ext:.log"])
#         max_file_size_mb: Maximum file size in MB to process (default: 50)
#
#     Returns:
#         Summary of files that would be indexed including count, size, and file types
#     """
#     try:
#         # Validate absolute path
#         if not os.path.isabs(directory_path):
#             return [TextContent(
#                 type="text",
#                 text=f"❌ Error: directory_path must be an absolute path. Got: {directory_path}\n\n"
#                      f"Example: /Users/username/projects/myproject"
#             )]
#
#         client = await ensure_api_client()
#
#         logger.info(f"Scanning local directory: {directory_path}")
#         result = await client.scan_local_filesystem(
#             directory_path=directory_path,
#             inclusion_patterns=inclusion_patterns or [],
#             exclusion_patterns=exclusion_patterns or [],
#             max_file_size_mb=max_file_size_mb
#         )
#
#         # Format the scan results
#         total_files = result.get("total_files", 0)
#         total_size_mb = result.get("total_size_mb", 0)
#         file_types = result.get("file_types", {})
#         files = result.get("files", [])
#         truncated = result.get("truncated", False)
#
#         response = f"📊 **Local Directory Scan Results**\n\n"
#         response += f"📁 **Directory:** `{directory_path}`\n"
#         response += f"📄 **Total Files:** {total_files:,}\n"
#         response += f"💾 **Total Size:** {total_size_mb:.2f} MB\n\n"
#
#         if file_types:
#             response += "**File Types:**\n"
#             # Sort by count descending
#             sorted_types = sorted(file_types.items(), key=lambda x: x[1], reverse=True)
#             for ext, count in sorted_types[:10]:  # Show top 10
#                 response += f"• `{ext}`: {count:,} files\n"
#             if len(sorted_types) > 10:
#                 response += f"• ... and {len(sorted_types) - 10} more types\n"
#             response += "\n"
#
#         if files:
#             response += f"**Largest Files (showing {min(len(files), 10)}):**\n"
#             for i, file_info in enumerate(files[:10]):
#                 size_mb = file_info["size"] / (1024 * 1024)
#                 response += f"{i+1}. `{file_info['path']}` ({size_mb:.2f} MB)\n"
#
#             if truncated:
#                 response += f"\n*Note: Showing first 100 files out of {total_files:,} total*\n"
#
#         if inclusion_patterns:
#             response += f"\n**Inclusion Patterns:** {', '.join(f'`{p}`' for p in inclusion_patterns)}\n"
#         if exclusion_patterns:
#             response += f"**Exclusion Patterns:** {', '.join(f'`{p}`' for p in exclusion_patterns)}\n"
#
#         response += "\n💡 **Next Step:** Use `index_local_filesystem` to index these files."
#
#         return [TextContent(type="text", text=response)]
#
#     except APIError as e:
#         logger.error(f"API error scanning local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ API Error: {str(e)}\n\nStatus Code: {e.status_code}\nDetails: {e.detail}"
#         )]
#     except Exception as e:
#         logger.error(f"Unexpected error scanning local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ Error: An unexpected error occurred while scanning: {str(e)}"
#         )]

# @mcp.tool()
# async def check_local_filesystem_status(source_id: str) -> List[TextContent]:
#     """
#     Check the indexing status of a local filesystem source.
#
#     Args:
#         source_id: The source ID returned when indexing was started
#
#     Returns:
#         Current status of the local filesystem indexing
#     """
#     try:
#         client = await ensure_api_client()
#         status = await client.check_local_filesystem_status(source_id)
#
#         # Format status response
#         status_text = status.get("status", "unknown")
#         progress = status.get("progress", 0)
#         message = status.get("message", "")
#         error = status.get("error")
#         directory_path = status.get("directory_path", "Unknown")
#         page_count = status.get("page_count", 0)  # Number of files
#         chunk_count = status.get("chunk_count", 0)
#
#         # Status emoji
#         status_emoji = {
#             "pending": "⏳",
#             "processing": "🔄",
#             "completed": "✅",
#             "failed": "❌",
#             "error": "❌"
#         }.get(status_text, "❓")
#
#         response = f"{status_emoji} **Local Filesystem Status**\n\n"
#         response += f"🆔 **Source ID:** `{source_id}`\n"
#         response += f"📁 **Directory:** `{directory_path}`\n"
#         response += f"📊 **Status:** {status_text.capitalize()}\n"
#
#         if progress > 0:
#             response += f"📈 **Progress:** {progress}%\n"
#
#         if message:
#             response += f"💬 **Message:** {message}\n"
#
#         if status_text == "completed":
#             response += f"\n✨ **Indexing Complete!**\n"
#             response += f"• **Files Indexed:** {page_count:,}\n"
#             response += f"• **Chunks Created:** {chunk_count:,}\n"
#             response += f"\nYou can now search this directory using `search_codebase` or the unified search!"
#         elif status_text in ["failed", "error"]:
#             response += f"\n❌ **Indexing Failed**\n"
#             if error:
#                 response += f"**Error:** {error}\n"
#             response += "\nPlease check your directory path and try again."
#         elif status_text == "processing":
#             response += f"\n🔄 Indexing is in progress...\n"
#             response += "Check back in a few moments or monitor at [app.trynia.ai](https://app.trynia.ai)"
#
#         return [TextContent(type="text", text=response)]
#
#     except APIError as e:
#         logger.error(f"API error checking local filesystem status: {e}")
#         if e.status_code == 404:
#             return [TextContent(
#                 type="text",
#                 text=f"❌ Source ID `{source_id}` not found. Please check the ID and try again."
#             )]
#         return [TextContent(
#             type="text",
#             text=f"❌ API Error: {str(e)}\n\nStatus Code: {e.status_code}\nDetails: {e.detail}"
#         )]
#     except Exception as e:
#         logger.error(f"Unexpected error checking local filesystem status: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ Error: An unexpected error occurred: {str(e)}"
#         )]

# @mcp.tool()
# async def search_local_filesystem(
#     source_id: str,
#     query: str,
#     include_sources: bool = True
# ) -> List[TextContent]:
#     """
#     Search an indexed local filesystem directory using its source ID.
#
#     To search local files:
#     1. First index a directory using `index_local_filesystem` - this will return a source_id
#     2. Use that source_id with this tool to search the indexed content
#
#     Args:
#         source_id: The source ID returned when the directory was indexed (required)
#         query: Your search query in natural language (required)
#         include_sources: Whether to include source code snippets in results (default: True)
#
#     Returns:
#         Search results with relevant file snippets and explanations
#
#     Example:
#         # After indexing returns source_id "abc123-def456"
#         search_local_filesystem(
#             source_id="abc123-def456",
#             query="configuration settings"
#         )
#
#     Note: To find your source IDs, use `list_documentation` and look for
#     sources with source_type="local_filesystem"
#     """
#     try:
#         # Validate inputs
#         if not source_id:
#             return [TextContent(
#                 type="text",
#                 text="❌ Error: 'source_id' parameter is required. Use the ID returned from index_local_filesystem."
#             )]
#
#         if not query:
#             return [TextContent(
#                 type="text",
#                 text="❌ Error: 'query' parameter is required"
#             )]
#
#         client = await ensure_api_client()
#
#         # Check if the source exists and is ready
#         logger.info(f"Checking status of source {source_id}")
#         try:
#             status = await client.get_data_source_status(source_id)
#             if not status:
#                 return [TextContent(
#                     type="text",
#                     text=f"❌ Source ID '{source_id}' not found. Please check the ID and try again."
#                 )]
#
#             source_status = status.get("status", "unknown")
#             if source_status == "processing":
#                 progress = status.get("progress", 0)
#                 return [TextContent(
#                     type="text",
#                     text=f"⏳ This source is still being indexed ({progress}% complete).\n\n"
#                          f"Use `check_local_filesystem_status(\"{source_id}\")` to check progress."
#                 )]
#             elif source_status == "failed":
#                 error = status.get("error", "Unknown error")
#                 return [TextContent(
#                     type="text",
#                     text=f"❌ This source failed to index.\n\nError: {error}"
#                 )]
#             elif source_status != "completed":
#                 return [TextContent(
#                     type="text",
#                     text=f"❌ Source is not ready for search. Status: {source_status}"
#                 )]
#         except Exception as e:
#             logger.warning(f"Could not check source status: {e}")
#             # Continue anyway in case it's just a status check issue
#
#         # Perform the search
#         logger.info(f"Searching local filesystem source {source_id} with query: {query}")
#
#         # Use the unified query endpoint with data_sources parameter
#         result = client.query_unified(
#             messages=[{"role": "user", "content": query}],
#             data_sources=[source_id],
#             include_sources=include_sources,
#             stream=False
#         )
#
#         # Parse the response
#         response_text = ""
#         async for chunk in result:
#             data = json.loads(chunk)
#             if "content" in data:
#                 response_text = data["content"]
#                 sources = data.get("sources", [])
#                 break
#
#         # Format the response nicely for local filesystem results
#         if response_text:
#             # Extract the local filesystem results section if present
#             if "**Local filesystem results" in response_text:
#                 # Keep the original response
#                 formatted_response = response_text
#             else:
#                 # Create our own formatted response
#                 formatted_response = f"🔍 **Search Results for Local Directory**\n"
#                 formatted_response += f"🔎 Query: \"{query}\"\n\n"
#                 formatted_response += response_text
#
#             # Add sources if available and requested
#             if include_sources and sources:
#                 formatted_response += "\n\n**📄 Source Details:**\n"
#                 for i, source in enumerate(sources[:5], 1):
#                     metadata = source.get("metadata", {})
#                     file_path = metadata.get("file_path", "Unknown file")
#                     formatted_response += f"\n{i}. `{file_path}`\n"
#
#                     # Add snippet of content
#                     content = source.get("content", "")
#                     if content:
#                         # Truncate to reasonable length
#                         lines = content.split('\n')[:10]
#                         snippet = '\n'.join(lines)
#                         if len(lines) > 10:
#                             snippet += "\n..."
#                         formatted_response += f"```\n{snippet}\n```\n"
#
#             return [TextContent(type="text", text=formatted_response)]
#         else:
#             return [TextContent(
#                 type="text",
#                 text=f"No results found for query: \"{query}\" in the indexed directory."
#             )]
#
#     except APIError as e:
#         logger.error(f"API error searching local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ API Error: {str(e)}\n\nStatus Code: {e.status_code}\nDetails: {e.detail}"
#         )]
#     except Exception as e:
#         logger.error(f"Unexpected error searching local filesystem: {e}")
#         return [TextContent(
#             type="text",
#             text=f"❌ Error: An unexpected error occurred: {str(e)}"
#         )]

# ===============================================================================
# CHROMA PACKAGE SEARCH INTEGRATION
# ===============================================================================
#
# Provides access to Chroma's Package Search MCP tools for searching actual
# source code from 3,000+ packages across multiple package registries.
# This integration enables AI assistants to search ground-truth code instead
# of relying on training data or hallucinations.
#
# Available Registries:
#   - py_pi: Python Package Index (PyPI) packages
#   - npm: Node.js packages from NPM registry
#   - crates_io: Rust packages from crates.io
#   - golang_proxy: Go modules from Go proxy
#   - ruby_gems: Ruby gems from RubyGems.org
#
# Authentication:
#   - Requires CHROMA_API_KEY environment variable
#   - Uses x-chroma-token header for API authentication
#
# Tools:
#   1. nia_package_search_grep: Regex-based code search
#   2. nia_package_search_hybrid: Semantic/AI-powered search
#   3. nia_package_search_read_file: Direct file content retrieval
#
# ===============================================================================

@mcp.tool()
async def nia_package_search_grep(
    registry: str,
    package_name: str,
    pattern: str,
    version: Optional[str] = None,
    language: Optional[str] = None,
    filename_sha256: Optional[str] = None,
    a: Optional[int] = None,
    b: Optional[int] = None,
    c: Optional[int] = None,
    head_limit: Optional[int] = None,
    output_mode: str = "content"
) -> List[TextContent]:
    """
    Executes a grep over the source code of a public package. This tool is useful for deterministically
    finding code in a package using regex. Use this tool before implementing solutions that use external
    packages. The regex pattern should be restrictive enough to only match code you're looking for, to limit
    overfetching.

    Required Args: "registry", "package_name", "pattern" Optional Args: "version", "language",
    "filename_sha256", "a", "b", "c", "head_limit", "output_mode"

    Parameters:
        a: The number of lines after a grep match to include
        b: The number of lines before a grep match to include
        c: The number of lines before and after a grep match to include
        filename_sha256: The sha256 hash of the file to filter for
        head_limit: Limits number of results returned. If the number of results returned is less than the
            head limit, all results have been returned.
        language: The languages to filter for. If not provided, all languages will be searched.
        output_mode: Controls the shape of the grep output. Accepted values:
            "content" (default): return content snippets with line ranges
            "files_with_matches": return unique files (path and sha256) that match
            "count": return files with the count of matches per file
        package_name: The name of the requested package. Pass the name as it appears in the package
            manager. For Go packages, use the GitHub organization and repository name in the format
            {org}/{repo}
        pattern: The regex pattern for exact text matching in the codebase. Must be a valid regex.
            Example: "func\\s+\\(get_repository\\|getRepository\\)\\s*\\(.*?\\)\\s\\{"
        registry: The name of the registry containing the requested package. Must be one of:
            "crates_io", "golang_proxy", "npm", "py_pi", or "ruby_gems".
        version: Optional
    """
    try:
        # Use API client for backend routing
        client = await ensure_api_client()
        logger.info(f"Searching package {package_name} from {registry} with pattern: {pattern}")

        # Execute grep search through backend
        result = await client.package_search_grep(
            registry=registry,
            package_name=package_name,
            pattern=pattern,
            version=version,
            language=language,
            filename_sha256=filename_sha256,
            a=a,
            b=b,
            c=c,
            head_limit=head_limit,
            output_mode=output_mode
        )

        # Handle raw Chroma JSON response
        if not result or not isinstance(result, dict):
            return [TextContent(
                type="text",
                text=f"No response from Chroma for pattern '{pattern}' in {package_name} ({registry})"
            )]

        # Extract results and version from raw Chroma response
        results = result.get("results", [])
        version_used = result.get("version_used")

        if not results:
            return [TextContent(
                type="text",
                text=f"No matches found for pattern '{pattern}' in {package_name} ({registry})"
            )]

        response_lines = [
            f"# 🔍 Package Search Results: {package_name} ({registry})",
            f"**Pattern:** `{pattern}`",
            ""
        ]

        if version_used:
            response_lines.append(f"**Version:** {version_used}")
        elif version:
            response_lines.append(f"**Version:** {version}")

        response_lines.append(f"**Found {len(results)} matches**\n")

        # Handle grep result format: {output_mode: "content", result: {content, file_path, start_line, etc}}
        for i, item in enumerate(results, 1):
            response_lines.append(f"## Match {i}")

            # Extract data from Chroma grep format
            if "result" in item:
                result_data = item["result"]
                if result_data.get("file_path"):
                    response_lines.append(f"**File:** `{result_data['file_path']}`")

                # Show SHA256 for read_file tool usage
                if result_data.get("filename_sha256"):
                    response_lines.append(f"**SHA256:** `{result_data['filename_sha256']}`")

                if result_data.get("start_line") and result_data.get("end_line"):
                    response_lines.append(f"**Lines:** {result_data['start_line']}-{result_data['end_line']}")
                if result_data.get("language"):
                    response_lines.append(f"**Language:** {result_data['language']}")

                response_lines.append("```")
                response_lines.append(result_data.get("content", ""))
                response_lines.append("```\n")
            else:
                # Fallback for other formats
                response_lines.append("```")
                response_lines.append(str(item))
                response_lines.append("```\n")

        # Add truncation message if present
        if result.get("truncation_message"):
            response_lines.append(f"⚠️ **Note:** {result['truncation_message']}")

        # Add usage hint for read_file workflow (grep tool)
        response_lines.append("\n💡 **To read full file content:**")
        response_lines.append("Copy a SHA256 above and use: `nia_package_search_read_file(registry=..., package_name=..., filename_sha256=\"...\", start_line=1, end_line=100)`")

        return [TextContent(type="text", text="\n".join(response_lines))]

    except Exception as e:
        logger.error(f"Error in package search grep: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error searching package: {str(e)}\n\n"
                 f"Make sure:\n"
                 f"- The registry is one of: crates_io, golang_proxy, npm, py_pi\n"
                 f"- The package name is correct\n"
                 f"- The pattern is a valid regex"
        )]

@mcp.tool()
async def nia_package_search_hybrid(
    registry: str,
    package_name: str,
    semantic_queries: List[str],
    version: Optional[str] = None,
    filename_sha256: Optional[str] = None,
    pattern: Optional[str] = None,
    language: Optional[str] = None
) -> List[TextContent]:
    """
    Searches package source code using semantic understanding AND optionally regex patterns.

    Required Args: "registry", "package_name", "semantic_queries"

    Optional Args: "version", "filename_sha256", "pattern", "language"

    Parameters:
        filename_sha256: The sha256 hash of the file to filter for
        language: The languages to filter for. If not provided, all languages will be searched.
        package_name: The name of the requested package. Pass the name as it appears in the package manager. For Go packages, use the GitHub organization and repository name in the format
            {org}/{repo}
        pattern: The regex pattern for exact text matching in the codebase. Must be a valid regex.
            Example: "func\\s+\\(get_repository\\|getRepository\\)\\s*\\(.*?\\)\\s\\{"
        registry: The name of the registry containing the requested package. Must be one of:
            "crates_io", "golang_proxy", "npm", "py_pi", or "ruby_gems".
        semantic_queries: Array of 1-5 plain English questions about the codebase. Example: ["how is
            argmax implemented in numpy?", "what testing patterns does axum use?"]
        version: Optional
    """
    try:
        # Use API client for backend routing
        client = await ensure_api_client()
        logger.info(f"Hybrid search in {package_name} from {registry} with queries: {semantic_queries}")

        # Execute hybrid search through backend
        result = await client.package_search_hybrid(
            registry=registry,
            package_name=package_name,
            semantic_queries=semantic_queries,
            version=version,
            filename_sha256=filename_sha256,
            pattern=pattern,
            language=language
        )

        # Handle raw Chroma JSON response
        if not result or not isinstance(result, dict):
            queries_str = "\n".join(f"- {q}" for q in semantic_queries)
            return [TextContent(
                type="text",
                text=f"No response from Chroma for queries:\n{queries_str}\n\nin {package_name} ({registry})"
            )]

        # Extract results and version from raw Chroma response
        results = result.get("results", [])
        version_used = result.get("version_used")

        if not results:
            queries_str = "\n".join(f"- {q}" for q in semantic_queries)
            return [TextContent(
                type="text",
                text=f"No relevant code found for queries:\n{queries_str}\n\nin {package_name} ({registry})"
            )]

        response_lines = [
            f"# 🔎 Package Semantic Search: {package_name} ({registry})",
            "**Queries:**"
        ]

        for query in semantic_queries:
            response_lines.append(f"- {query}")

        response_lines.append("")

        if version_used:
            response_lines.append(f"**Version:** {version_used}")
        elif version:
            response_lines.append(f"**Version:** {version}")
        if pattern:
            response_lines.append(f"**Pattern Filter:** `{pattern}`")

        response_lines.append(f"\n**Found {len(results)} relevant code sections**\n")

        # Handle hybrid result format: {id: "...", document: "content", metadata: {...}}
        for i, item in enumerate(results, 1):
            response_lines.append(f"## Result {i}")

            # Extract metadata if available
            metadata = item.get("metadata", {})
            if metadata.get("filename"):
                response_lines.append(f"**File:** `{metadata['filename']}`")

            # Show SHA256 for read_file tool usage (from metadata)
            if metadata.get("filename_sha256"):
                response_lines.append(f"**SHA256:** `{metadata['filename_sha256']}`")

            if metadata.get("start_line") and metadata.get("end_line"):
                response_lines.append(f"**Lines:** {metadata['start_line']}-{metadata['end_line']}")
            if metadata.get("language"):
                response_lines.append(f"**Language:** {metadata['language']}")

            # Get document content
            content = item.get("document", "")
            if content:
                response_lines.append("```")
                response_lines.append(content)
                response_lines.append("```\n")

        # Add truncation message if present
        if result.get("truncation_message"):
            response_lines.append(f"⚠️ **Note:** {result['truncation_message']}")

        # Add usage hint for read_file workflow (hybrid tool)
        response_lines.append("\n💡 **To read full file content:**")
        response_lines.append("Copy a SHA256 above and use: `nia_package_search_read_file(registry=..., package_name=..., filename_sha256=\"...\", start_line=1, end_line=100)`")

        return [TextContent(type="text", text="\n".join(response_lines))]

    except Exception as e:
        logger.error(f"Error in package search hybrid: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error in hybrid search: {str(e)}\n\n"
                 f"Make sure:\n"
                 f"- The registry is one of: crates_io, golang_proxy, npm, py_pi\n"
                 f"- The package name is correct\n"
                 f"- Semantic queries are provided (1-5 queries)"
        )]

@mcp.tool()
async def nia_package_search_read_file(
    registry: str,
    package_name: str,
    filename_sha256: str,
    start_line: int,
    end_line: int,
    version: Optional[str] = None
) -> List[TextContent]:
    """
    Reads exact lines from a source file of a public package. Useful for fetching specific code regions by
    line range.

    Required Args: "registry", "package_name", "filename_sha256", "start_line", "end_line" Optional Args:
    "version"

    Parameters:
        end_line: 1-based inclusive end line to read
        filename_sha256: The sha256 hash of the file to filter for
        package_name: The name of the requested package. Pass the name as it appears in the package
            manager. For Go packages, use the GitHub organization and repository name in the format
            {org}/{repo}
        registry: The name of the registry containing the requested package. Must be one of:
            "crates_io", "golang_proxy", "npm", "py_pi", or "ruby_gems".
        start_line: 1-based inclusive start line to read
        version: Optional
    """
    try:
        # Validate line range
        if end_line - start_line + 1 > 200:
            return [TextContent(
                type="text",
                text="❌ Error: Maximum 200 lines can be read at once. Please reduce the line range."
            )]

        if start_line < 1 or end_line < start_line:
            return [TextContent(
                type="text",
                text="❌ Error: Invalid line range. Start line must be >= 1 and end line must be >= start line."
            )]

        # Use API client for backend routing
        client = await ensure_api_client()
        logger.info(f"Reading file from {package_name} ({registry}): sha256={filename_sha256}, lines {start_line}-{end_line}")

        # Read file content through backend
        result = await client.package_search_read_file(
            registry=registry,
            package_name=package_name,
            filename_sha256=filename_sha256,
            start_line=start_line,
            end_line=end_line,
            version=version
        )

        # Handle raw Chroma response (read_file typically returns content directly)
        response_lines = [
            f"# 📄 Package File Content: {package_name} ({registry})",
            f"**File SHA256:** `{filename_sha256}`",
            f"**Lines:** {start_line}-{end_line}"
        ]

        if version:
            response_lines.append(f"**Version:** {version}")

        response_lines.append("\n```")
        # For read_file, Chroma typically returns the content directly as a string
        if isinstance(result, str):
            response_lines.append(result)
        elif isinstance(result, dict) and result.get("content"):
            response_lines.append(result["content"])
        else:
            response_lines.append(str(result))
        response_lines.append("```")

        return [TextContent(type="text", text="\n".join(response_lines))]

    except Exception as e:
        logger.error(f"Error reading package file: {e}")
        return [TextContent(
            type="text",
            text=f"❌ Error reading file: {str(e)}\n\n"
                 f"Make sure:\n"
                 f"- The registry is one of: crates_io, golang_proxy, npm, py_pi\n"
                 f"- The package name is correct\n"
                 f"- The filename_sha256 is valid\n"
                 f"- The line range is valid (1-based, max 200 lines)"
        )]

@mcp.tool()
async def nia_bug_report(
    description: str,
    bug_type: str = "bug",
    additional_context: Optional[str] = None
) -> List[TextContent]:
    """
    Submit a bug report or feature request.
    Args:
        description: Detailed description of the bug or feature request (10-5000 characters)
        bug_type: Type of report - "bug", "feature-request", "improvement", or "other" (default: "bug")
        additional_context: Optional additional context, steps to reproduce, or related information
    """
    try:
        client = await ensure_api_client()

        # Validate input parameters
        if not description or len(description.strip()) < 10:
            return [
                TextContent(
                    type="text",
                    text="❌ Error: Bug description must be at least 10 characters long."
                )
            ]

        if len(description) > 5000:
            return [
                TextContent(
                    type="text",
                    text="❌ Error: Bug description must be 5000 characters or less."
                )
            ]

        valid_types = ["bug", "feature-request", "improvement", "other"]
        if bug_type not in valid_types:
            return [
                TextContent(
                    type="text",
                    text=f"❌ Error: bug_type must be one of: {', '.join(valid_types)}"
                )
            ]

        if additional_context and len(additional_context) > 2000:
            return [
                TextContent(
                    type="text",
                    text="❌ Error: Additional context must be 2000 characters or less."
                )
            ]

        logger.info(f"Submitting bug report: type={bug_type}, description_length={len(description)}")

        # Submit bug report via API client
        result = await client.submit_bug_report(
            description=description.strip(),
            bug_type=bug_type,
            additional_context=additional_context.strip() if additional_context else None
        )

        if result.get("success"):
            return [
                TextContent(
                    type="text",
                    text=f"✅ Bug report submitted successfully!\n\n"
                         f"Thank you for your feedback. Your report has been sent to the development team "
                         f"and will be reviewed promptly.\n\n"
                         f"Reference ID: {result.get('message', '').split(': ')[-1] if ': ' in result.get('message', '') else 'N/A'}\n"
                         f"Type: {bug_type.title()}\n"
                         f"Status: The team will be notified immediately via email and Slack.\n\n"
                         f"You can also track issues and feature requests on our GitHub repository:\n"
                         f"https://github.com/nozomio-labs/nia/issues"
                )
            ]
        else:
            return [
                TextContent(
                    type="text",
                    text=f"❌ Failed to submit bug report: {result.get('message', 'Unknown error')}\n\n"
                         f"Please try again or contact support directly at support@trynia.ai"
                )
            ]

    except Exception as e:
        logger.error(f"Error submitting bug report: {e}")
        return [
            TextContent(
                type="text",
                text=f"❌ Error submitting bug report: {str(e)}\n\n"
                     f"Please try again or contact support directly at support@trynia.ai"
            )
        ]

# Context Sharing Tools

@mcp.tool()
async def save_context(
    title: str,
    summary: str,
    content: str,
    agent_source: str,
    tags: Optional[List[str]] = None,
    metadata: Optional[dict] = None,
    nia_references: Optional[dict] = None,
    edited_files: Optional[List[dict]] = None
) -> List[TextContent]:
    """
    Save a conversation context for cross-agent sharing.

    Args:
        title: A descriptive title for the context
        summary: Brief summary of the conversation
        content: Full conversation context - the agent should compact the conversation history but keep all important parts togethers, as well as code snippets. No excuses.
        agent_source: Which agent is creating this context (e.g., "cursor")
        tags: Optional list of searchable tags
        metadata: Optional metadata like file paths, repositories discussed, etc.
        nia_references: Structured data about NIA resources used during conversation
            Format: {
                "indexed_resources": [{"identifier": "owner/repo", "resource_type": "repository", "purpose": "Used for authentication patterns"}],
                "search_queries": [{"query": "JWT implementation", "query_type": "codebase", "resources_searched": ["owner/repo"], "key_findings": "Found JWT utils in auth folder"}],
                "session_summary": "Used NIA to explore authentication patterns and API design"
            }
        edited_files: List of files that were modified during conversation
            Format: [{"file_path": "src/auth.ts", "operation": "modified", "changes_description": "Added JWT validation", "key_changes": ["Added validate() function"]}]

    Returns:
        Confirmation of successful context save with context ID
    """
    try:
        # Validate input parameters
        if not title or not title.strip():
            return [TextContent(type="text", text="❌ Error: Title is required")]

        if len(title) > 200:
            return [TextContent(type="text", text="❌ Error: Title must be 200 characters or less")]

        if not summary or len(summary) < 10:
            return [TextContent(type="text", text="❌ Error: Summary must be at least 10 characters")]

        if len(summary) > 1000:
            return [TextContent(type="text", text="❌ Error: Summary must be 1000 characters or less")]

        if not content or len(content) < 50:
            return [TextContent(type="text", text="❌ Error: Content must be at least 50 characters")]

        if not agent_source or not agent_source.strip():
            return [TextContent(type="text", text="❌ Error: Agent source is required")]

        client = await ensure_api_client()

        logger.info(f"Saving context: title='{title}', agent={agent_source}, content_length={len(content)}")

        result = await client.save_context(
            title=title.strip(),
            summary=summary.strip(),
            content=content,
            agent_source=agent_source.strip(),
            tags=tags or [],
            metadata=metadata or {},
            nia_references=nia_references,
            edited_files=edited_files or []
        )

        context_id = result.get("id")

        return [TextContent(
            type="text",
            text=f"✅ **Context Saved Successfully!**\n\n"
                 f"🆔 **Context ID:** `{context_id}`\n"
                 f"📝 **Title:** {title}\n"
                 f"🤖 **Source Agent:** {agent_source}\n"
                 f"📊 **Content Length:** {len(content):,} characters\n"
                 f"🏷️ **Tags:** {', '.join(tags) if tags else 'None'}\n\n"
                 f"**Next Steps:**\n"
                 f"• Other agents can now retrieve this context using the context ID\n"
                 f"• Use `search_contexts` to find contexts by content or tags\n"
                 f"• Use `list_contexts` to see all your saved contexts\n\n"
                 f"🔗 **Share this context:** Provide the context ID `{context_id}` to other agents"
        )]

    except APIError as e:
        logger.error(f"API Error saving context: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error saving context: {e}")
        return [TextContent(type="text", text=f"❌ Error saving context: {str(e)}")]

@mcp.tool()
async def list_contexts(
    limit: int = 20,
    offset: int = 0,
    tags: Optional[str] = None,
    agent_source: Optional[str] = None
) -> List[TextContent]:
    """
    List saved conversation contexts with pagination and filtering.

    Args:
        limit: Number of contexts to return (1-100, default: 20)
        offset: Number of contexts to skip for pagination (default: 0)
        tags: Comma-separated tags to filter by (optional)
        agent_source: Filter by specific agent source (optional)

    Returns:
        List of conversation contexts with pagination info
    """
    try:
        # Validate parameters
        if limit < 1 or limit > 100:
            return [TextContent(type="text", text="❌ Error: Limit must be between 1 and 100")]

        if offset < 0:
            return [TextContent(type="text", text="❌ Error: Offset must be 0 or greater")]

        client = await ensure_api_client()

        result = await client.list_contexts(
            limit=limit,
            offset=offset,
            tags=tags,
            agent_source=agent_source
        )

        contexts = result.get("contexts", [])
        pagination = result.get("pagination", {})

        if not contexts:
            response = "📭 **No Contexts Found**\n\n"
            if tags or agent_source:
                response += "No contexts match your filters.\n\n"
            else:
                response += "You haven't saved any contexts yet.\n\n"

            response += "**Get started:**\n"
            response += "• Use `save_context` to save a conversation for cross-agent sharing\n"
            response += "• Perfect for handoffs between Cursor and Claude Code!"

            return [TextContent(type="text", text=response)]

        # Format the response
        response = f"📚 **Your Conversation Contexts** ({pagination.get('total', len(contexts))} total)\n\n"

        for i, context in enumerate(contexts, offset + 1):
            created_at = context.get('created_at', '')
            if created_at:
                # Format datetime for better readability
                try:
                    from datetime import datetime
                    dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    formatted_date = dt.strftime('%Y-%m-%d %H:%M UTC')
                except:
                    formatted_date = created_at
            else:
                formatted_date = 'Unknown'

            response += f"**{i}. {context['title']}**\n"
            response += f"   🆔 ID: `{context['id']}`\n"
            response += f"   🤖 Source: {context['agent_source']}\n"
            response += f"   📅 Created: {formatted_date}\n"
            response += f"   📝 Summary: {context['summary'][:100]}{'...' if len(context['summary']) > 100 else ''}\n"
            if context.get('tags'):
                response += f"   🏷️ Tags: {', '.join(context['tags'])}\n"
            response += "\n"

        # Add pagination info
        if pagination.get('has_more'):
            next_offset = offset + limit
            response += f"📄 **Pagination:** Showing {offset + 1}-{offset + len(contexts)} of {pagination.get('total')}\n"
            response += f"   Use `list_contexts(offset={next_offset})` for next page\n"

        response += "\n**Actions:**\n"
        response += "• `retrieve_context(context_id)` - Get full context\n"
        response += "• `search_contexts(query)` - Search contexts\n"
        response += "• `delete_context(context_id)` - Remove context"

        return [TextContent(type="text", text=response)]

    except APIError as e:
        logger.error(f"API Error listing contexts: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error listing contexts: {e}")
        return [TextContent(type="text", text=f"❌ Error listing contexts: {str(e)}")]

@mcp.tool()
async def retrieve_context(context_id: str) -> List[TextContent]:
    """
    Retrieve a specific conversation context by ID.

    Use this tool to get the full conversation context that was saved by
    another agent. Perfect for getting strategic context from Cursor
    when working in Claude Code.

    Args:
        context_id: The unique ID of the context to retrieve

    Returns:
        Full conversation context with metadata

    Example:
        retrieve_context("550e8400-e29b-41d4-a716-446655440000")
    """
    try:
        if not context_id or not context_id.strip():
            return [TextContent(type="text", text="❌ Error: Context ID is required")]

        client = await ensure_api_client()

        context = await client.get_context(context_id.strip())

        if not context:
            return [TextContent(
                type="text",
                text=f"❌ **Context Not Found**\n\n"
                     f"Context ID `{context_id}` was not found.\n\n"
                     f"**Possible reasons:**\n"
                     f"• The context ID is incorrect\n"
                     f"• The context belongs to a different user\n"
                     f"• The context has been deleted\n\n"
                     f"Use `list_contexts()` to see your available contexts."
            )]

        # Format the context display
        created_at = context.get('created_at', '')
        if created_at:
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                formatted_date = dt.strftime('%Y-%m-%d %H:%M UTC')
            except:
                formatted_date = created_at
        else:
            formatted_date = 'Unknown'

        updated_at = context.get('updated_at', '')
        if updated_at:
            try:
                from datetime import datetime
                dt = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
                formatted_updated = dt.strftime('%Y-%m-%d %H:%M UTC')
            except:
                formatted_updated = updated_at
        else:
            formatted_updated = None

        response = f"📋 **Context: {context['title']}**\n\n"
        response += f"🆔 **ID:** `{context['id']}`\n"
        response += f"🤖 **Source Agent:** {context['agent_source']}\n"
        response += f"📅 **Created:** {formatted_date}\n"
        if formatted_updated:
            response += f"🔄 **Updated:** {formatted_updated}\n"

        if context.get('tags'):
            response += f"🏷️ **Tags:** {', '.join(context['tags'])}\n"

        response += f"\n📝 **Summary:**\n{context['summary']}\n\n"

        # Add NIA References - CRITICAL for context handoffs
        # Use 'or {}' to handle cases where nia_references is None (not just missing)
        nia_references = context.get('nia_references') or {}
        if nia_references:
            response += "🧠 **NIA RESOURCES USED - RECOMMENDED ACTIONS:**\n"

            indexed_resources = nia_references.get('indexed_resources', [])
            if indexed_resources:
                response += "**📦 Re-index these resources:**\n"
                for resource in indexed_resources:
                    identifier = resource.get('identifier', 'Unknown')
                    resource_type = resource.get('resource_type', 'unknown')
                    purpose = resource.get('purpose', 'No purpose specified')

                    if resource_type == 'repository':
                        response += f"• `Index {identifier}` - {purpose}\n"
                    elif resource_type == 'documentation':
                        response += f"• `Index documentation {identifier}` - {purpose}\n"
                    else:
                        response += f"• `Index {identifier}` ({resource_type}) - {purpose}\n"
                response += "\n"

            search_queries = nia_references.get('search_queries', [])
            if search_queries:
                response += "**🔍 Useful search queries to re-run:**\n"
                for query in search_queries:
                    query_text = query.get('query', 'Unknown query')
                    query_type = query.get('query_type', 'search')
                    key_findings = query.get('key_findings', 'No findings specified')
                    resources_searched = query.get('resources_searched', [])

                    response += f"• **Query:** `{query_text}` ({query_type})\n"
                    if resources_searched:
                        response += f"  **Resources:** {', '.join(resources_searched)}\n"
                    response += f"  **Key Findings:** {key_findings}\n"
                response += "\n"

            session_summary = nia_references.get('session_summary')
            if session_summary:
                response += f"**📋 NIA Session Summary:** {session_summary}\n\n"

        # Add Edited Files - CRITICAL for code handoffs
        # Use 'or []' to handle cases where edited_files is None (not just missing)
        edited_files = context.get('edited_files') or []
        if edited_files:
            response += "📝 **FILES MODIFIED - READ THESE TO GET UP TO SPEED:**\n"
            for file_info in edited_files:
                file_path = file_info.get('file_path', 'Unknown file')
                operation = file_info.get('operation', 'modified')
                changes_desc = file_info.get('changes_description', 'No description')
                key_changes = file_info.get('key_changes', [])
                language = file_info.get('language', '')

                operation_emoji = {
                    'created': '🆕',
                    'modified': '✏️',
                    'deleted': '🗑️'
                }.get(operation, '📄')

                response += f"• {operation_emoji} **`{file_path}`** ({operation})\n"
                response += f"  **Changes:** {changes_desc}\n"

                if key_changes:
                    response += f"  **Key Changes:** {', '.join(key_changes)}\n"
                if language:
                    response += f"  **Language:** {language}\n"

                response += f"  **💡 Action:** Read this file with: `Read {file_path}`\n"
            response += "\n"

        # Add metadata if available
        # Use 'or {}' to handle cases where metadata is None (not just missing)
        metadata = context.get('metadata') or {}
        if metadata:
            response += f"📊 **Additional Metadata:**\n"
            for key, value in metadata.items():
                if isinstance(value, list):
                    response += f"• **{key}:** {', '.join(map(str, value))}\n"
                else:
                    response += f"• **{key}:** {value}\n"
            response += "\n"

        response += f"📄 **Full Context:**\n\n{context['content']}\n\n"

        response += f"---\n"
        response += f"🚀 **NEXT STEPS FOR SEAMLESS HANDOFF:**\n"
        response += f"• This context was created by **{context['agent_source']}**\n"

        if nia_references.get('search_queries'):
            response += f"• **RECOMMENDED:** Re-run the search queries to get the same insights\n"
        if edited_files:
            response += f"• **ESSENTIAL:** Read the modified files above to understand code changes\n"

        response += f"• Use the summary and full context to understand the strategic planning\n"

        return [TextContent(type="text", text=response)]

    except APIError as e:
        logger.error(f"API Error retrieving context: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error retrieving context: {e}")
        return [TextContent(type="text", text=f"❌ Error retrieving context: {str(e)}")]

@mcp.tool()
async def search_contexts(
    query: str,
    limit: int = 20,
    tags: Optional[str] = None,
    agent_source: Optional[str] = None
) -> List[TextContent]:
    """
    Search conversation contexts by content, title, or summary.

    Args:
        query: Search query to match against title, summary, content, and tags
        limit: Maximum number of results to return (1-100, default: 20)
        tags: Comma-separated tags to filter by (optional)
        agent_source: Filter by specific agent source (optional)

    Returns:
        Search results with matching contexts
    """
    try:
        # Validate parameters
        if not query or not query.strip():
            return [TextContent(type="text", text="❌ Error: Search query is required")]

        if limit < 1 or limit > 100:
            return [TextContent(type="text", text="❌ Error: Limit must be between 1 and 100")]

        client = await ensure_api_client()

        result = await client.search_contexts(
            query=query.strip(),
            limit=limit,
            tags=tags,
            agent_source=agent_source
        )

        contexts = result.get("contexts", [])

        if not contexts:
            response = f"🔍 **No Results Found**\n\n"
            response += f"No contexts match your search query: \"{query}\"\n\n"

            if tags or agent_source:
                response += f"**Active filters:**\n"
                if tags:
                    response += f"• Tags: {tags}\n"
                if agent_source:
                    response += f"• Agent: {agent_source}\n"
                response += "\n"

            response += f"**Suggestions:**\n"
            response += f"• Try different keywords\n"
            response += f"• Remove filters to broaden search\n"
            response += f"• Use `list_contexts()` to see all contexts"

            return [TextContent(type="text", text=response)]

        # Format search results
        response = f"🔍 **Search Results for \"{query}\"** ({len(contexts)} found)\n\n"

        for i, context in enumerate(contexts, 1):
            created_at = context.get('created_at', '')
            if created_at:
                try:
                    from datetime import datetime
                    dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    formatted_date = dt.strftime('%Y-%m-%d %H:%M UTC')
                except:
                    formatted_date = created_at
            else:
                formatted_date = 'Unknown'

            response += f"**{i}. {context['title']}**\n"
            response += f"   🆔 ID: `{context['id']}`\n"
            response += f"   🤖 Source: {context['agent_source']}\n"
            response += f"   📅 Created: {formatted_date}\n"
            response += f"   📝 Summary: {context['summary'][:150]}{'...' if len(context['summary']) > 150 else ''}\n"

            if context.get('tags'):
                response += f"   🏷️ Tags: {', '.join(context['tags'])}\n"

            response += "\n"

        response += f"**Actions:**\n"
        response += f"• `retrieve_context(context_id)` - Get full context\n"
        response += f"• Refine search with different keywords\n"
        response += f"• Use tags or agent filters for better results"

        return [TextContent(type="text", text=response)]

    except APIError as e:
        logger.error(f"API Error searching contexts: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error searching contexts: {e}")
        return [TextContent(type="text", text=f"❌ Error searching contexts: {str(e)}")]

@mcp.tool()
async def update_context(
    context_id: str,
    title: Optional[str] = None,
    summary: Optional[str] = None,
    content: Optional[str] = None,
    tags: Optional[List[str]] = None,
    metadata: Optional[dict] = None
) -> List[TextContent]:
    """
    Update an existing conversation context.

    Args:
        context_id: The unique ID of the context to update
        title: Updated title (optional)
        summary: Updated summary (optional)
        content: Updated content (optional)
        tags: Updated tags list (optional)
        metadata: Updated metadata (optional)

    Returns:
        Confirmation of successful update
    """
    try:
        if not context_id or not context_id.strip():
            return [TextContent(type="text", text="❌ Error: Context ID is required")]

        # Check that at least one field is being updated
        if not any([title, summary, content, tags is not None, metadata is not None]):
            return [TextContent(
                type="text",
                text="❌ Error: At least one field must be provided for update"
            )]

        # Validate fields if provided
        if title is not None and (not title.strip() or len(title) > 200):
            return [TextContent(
                type="text",
                text="❌ Error: Title must be 1-200 characters"
            )]

        if summary is not None and (len(summary) < 10 or len(summary) > 1000):
            return [TextContent(
                type="text",
                text="❌ Error: Summary must be 10-1000 characters"
            )]

        if content is not None and len(content) < 50:
            return [TextContent(
                type="text",
                text="❌ Error: Content must be at least 50 characters"
            )]

        if tags is not None and len(tags) > 10:
            return [TextContent(
                type="text",
                text="❌ Error: Maximum 10 tags allowed"
            )]

        client = await ensure_api_client()

        result = await client.update_context(
            context_id=context_id.strip(),
            title=title.strip() if title else None,
            summary=summary.strip() if summary else None,
            content=content,
            tags=tags,
            metadata=metadata
        )

        if not result:
            return [TextContent(
                type="text",
                text=f"❌ Error: Context with ID `{context_id}` not found"
            )]

        # List updated fields
        updated_fields = []
        if title is not None:
            updated_fields.append("title")
        if summary is not None:
            updated_fields.append("summary")
        if content is not None:
            updated_fields.append("content")
        if tags is not None:
            updated_fields.append("tags")
        if metadata is not None:
            updated_fields.append("metadata")

        response = f"✅ **Context Updated Successfully!**\n\n"
        response += f"🆔 **Context ID:** `{context_id}`\n"
        response += f"📝 **Title:** {result['title']}\n"
        response += f"🔄 **Updated Fields:** {', '.join(updated_fields)}\n"
        response += f"🤖 **Source Agent:** {result['agent_source']}\n\n"

        response += f"**Current Status:**\n"
        response += f"• **Tags:** {', '.join(result['tags']) if result.get('tags') else 'None'}\n"
        response += f"• **Content Length:** {len(result['content']):,} characters\n\n"

        response += f"Use `retrieve_context('{context_id}')` to see the full updated context."

        return [TextContent(type="text", text=response)]

    except APIError as e:
        logger.error(f"API Error updating context: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error updating context: {e}")
        return [TextContent(type="text", text=f"❌ Error updating context: {str(e)}")]

@mcp.tool()
async def delete_context(context_id: str) -> List[TextContent]:
    """
    Delete a conversation context.

    Args:
        context_id: The unique ID of the context to delete

    Returns:
        Confirmation of successful deletion

    Example:
        delete_context("550e8400-e29b-41d4-a716-446655440000")
    """
    try:
        if not context_id or not context_id.strip():
            return [TextContent(type="text", text="❌ Error: Context ID is required")]

        client = await ensure_api_client()

        success = await client.delete_context(context_id.strip())

        if success:
            return [TextContent(
                type="text",
                text=f"✅ **Context Deleted Successfully!**\n\n"
                     f"🆔 **Context ID:** `{context_id}`\n\n"
                     f"The context has been permanently removed from your account.\n"
                     f"This action cannot be undone.\n\n"
                     f"Use `list_contexts()` to see your remaining contexts."
            )]
        else:
            return [TextContent(
                type="text",
                text=f"❌ **Context Not Found**\n\n"
                     f"Context ID `{context_id}` was not found or has already been deleted.\n\n"
                     f"Use `list_contexts()` to see your available contexts."
            )]

    except APIError as e:
        logger.error(f"API Error deleting context: {e}")
        return [TextContent(type="text", text=f"❌ API Error: {str(e)}")]
    except Exception as e:
        logger.error(f"Error deleting context: {e}")
        return [TextContent(type="text", text=f"❌ Error deleting context: {str(e)}")]

# Resources

# Note: FastMCP doesn't have list_resources or read_resource decorators
# Resources should be registered individually using @mcp.resource()
# For now, commenting out these functions as they use incorrect decorators

# @mcp.list_resources
# async def list_resources() -> List[Resource]:
#     """List available repositories as resources."""
#     try:
#         client = await ensure_api_client()
#         repositories = await client.list_repositories()
#         
#         resources = []
#         for repo in repositories:
#             if repo.get("status") == "completed":
#                 resources.append(Resource(
#                     uri=f"nia://repository/{repo['repository']}",
#                     name=repo["repository"],
#                     description=f"Indexed repository at branch {repo.get('branch', 'main')}",
#                     mimeType="application/x-nia-repository"
#                 ))
#         
#         return resources
#     except Exception as e:
#         logger.error(f"Error listing resources: {e}")
#         return []

# @mcp.read_resource
# async def read_resource(uri: str) -> TextContent:
#     """Read information about a repository resource."""
#     if not uri.startswith("nia://repository/"):
#         return TextContent(
#             type="text",
#             text=f"Unknown resource URI: {uri}"
#         )
#     
#     repository = uri.replace("nia://repository/", "")
#     
#     try:
#         client = await ensure_api_client()
#         status = await client.get_repository_status(repository)
#         
#         if not status:
#             return TextContent(
#                 type="text",
#                 text=f"Repository not found: {repository}"
#             )
#         
#         # Format repository information
#         lines = [
#             f"# Repository: {repository}",
#             "",
#             f"**Status:** {status['status']}",
#             f"**Branch:** {status.get('branch', 'main')}",
#         ]
#         
#         if status.get("indexed_at"):
#             lines.append(f"**Indexed:** {status['indexed_at']}")
#         
#         lines.extend([
#             "",
#             "## Usage",
#             f"Search this repository using the `search_codebase` tool with:",
#             f'`repositories=["{repository}"]`'
#         ])
#         
#         return TextContent(type="text", text="\n".join(lines))
#         
#     except Exception as e:
#         logger.error(f"Error reading resource: {e}")
#         return TextContent(
#             type="text",
#             text=f"Error reading resource: {str(e)}"
#         )

# Server lifecycle

async def cleanup():
    """Cleanup resources on shutdown."""
    global api_client
    if api_client:
        await api_client.close()
        api_client = None

def run():
    """Run the MCP server."""
    try:
        # Check for API key early
        get_api_key()
        
        logger.info("Starting NIA MCP Server")
        mcp.run(transport='stdio')
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
    finally:
        # Run cleanup
        loop = asyncio.new_event_loop()
        loop.run_until_complete(cleanup())
        loop.close()