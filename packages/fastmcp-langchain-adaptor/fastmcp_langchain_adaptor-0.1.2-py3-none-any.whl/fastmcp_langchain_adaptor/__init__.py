"""
FastMCP LangChain Adaptor

A Python package that provides seamless integration between FastMCP
(Model Context Protocol) and LangChain, allowing you to use MCP tools
as LangChain StructuredTools.

Key Features:
- Convert FastMCP tools to LangChain StructuredTools
- Support for progress callbacks and async operations
- Comprehensive error handling and logging
- Direct integration with LangChain types

Example:
    ```python
    from fastmcp import Client
    from fastmcp_langchain_adaptor import mcp_to_langchain

    # Create FastMCP client
    client = Client("http://localhost:8000")

    # Get MCP tools and convert to LangChain tools
    mcp_tools = await client.list_tools()
    lc_tools = mcp_to_langchain(mcp_tools, client=client)

    # Use with LangChain agents
    agent = create_agent(llm, lc_tools)
    ```
"""

from .tools import mcp_to_langchain

__version__ = "0.1.1"
__author__ = "Daniel Shea"
__email__ = "daniel.shea@cisco.com"
__all__ = [
    "mcp_to_langchain",
]
