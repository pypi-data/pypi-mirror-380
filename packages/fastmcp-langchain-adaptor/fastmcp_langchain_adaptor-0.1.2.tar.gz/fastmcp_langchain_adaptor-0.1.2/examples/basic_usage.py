#!/usr/bin/env python3
"""
Basic Usage Example - FastMCP LangChain Adaptor

This example demonstrates how to use the FastMCP LangChain Adaptor
to convert MCP tools into LangChain StructuredTools.
"""

import asyncio
import logging
from typing import Any

from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

from fastmcp_langchain_adaptor import mcp_to_langchain

# Enable debug logging to see what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def elicitation_handler(
    message: str,
    response_type: type,
    params: Any,
    context: Any,
) -> ElicitResult:
    """
    Handle elicitation requests from MCP tools.

    In a real application, this would show a UI dialog or prompt.
    For this example, we'll simulate user responses.
    """
    print(f"📝 Tool is asking: {message}")

    # Example: simulate user responses for common scenarios
    if "phone" in message.lower():
        # Tool asking which phone number to use
        choice = "mobile"  # Simulate user choosing mobile
        print(f"   → User response: {choice}")
        return ElicitResult(action="accept", content={"phone_type": choice})

    elif "confirm" in message.lower() or "delete" in message.lower():
        # Tool asking for confirmation
        confirm = "yes"  # Simulate user confirming
        print(f"   → User response: {confirm}")
        if confirm.lower() == "yes":
            return ElicitResult(action="accept", content={})
        else:
            return ElicitResult(action="reject", content={})

    # Default: accept with empty content
    print("   → User response: (default accept)")
    return ElicitResult(action="accept", content={})


def custom_progress_formatter(progress_dict: dict[str, Any]) -> str:
    """
    Custom formatter for progress messages.

    Args:
        progress_dict: Dict with keys 'progress', 'total', 'message'

    Returns:
        Formatted progress string
    """
    progress = progress_dict["progress"]
    total = progress_dict["total"]
    message = progress_dict.get("message", "")

    if total is not None:
        percentage = int((progress / total) * 100)
        return f"🔄 {percentage}% complete - {message}"
    else:
        return f"🔄 Progress: {progress} - {message}"


async def main():
    """Main example function."""
    print("🚀 FastMCP LangChain Adaptor - Basic Usage Example")
    print("=" * 60)

    # Create FastMCP client with elicitation support
    # Note: Replace with your actual MCP server URL
    mcp_server_url = "http://localhost:8000"  # Example URL

    try:
        # Create client with elicitation handler
        client = Client(mcp_server_url, elicitation_handler=elicitation_handler)

        # In a real scenario, you would:
        # 1. Start your MCP server
        # 2. Get the actual tools from the server

        # For this example, we'll create mock tools
        # In practice, you'd do: mcp_tools = await client.list_tools()

        print("📋 Converting MCP tools to LangChain StructuredTools...")

        # Convert with default settings (progress forwarding enabled)
        lc_tools_default = mcp_to_langchain(
            tools=[],  # Would be your actual MCP tools
            client=client,
        )

        # Convert with custom progress formatter
        lc_tools_custom = mcp_to_langchain(
            tools=[],  # Would be your actual MCP tools
            client=client,
            progress_formatter=custom_progress_formatter,
        )

        print(f"✅ Converted {len(lc_tools_default)} tools (default formatting)")
        print(f"✅ Converted {len(lc_tools_custom)} tools (custom formatting)")

        # Example of using the tools
        if lc_tools_default:
            print("\n🔧 Example tool usage:")
            tool = lc_tools_default[0]
            print(f"   Tool name: {tool.name}")
            print(f"   Description: {tool.description}")

            # Example invocation (would work with actual tools)
            # result = await tool.ainvoke({"argument": "value"})
            # print(f"   Result: {result}")

        print("\n📊 Features demonstrated:")
        print("   ✓ Basic MCP to LangChain tool conversion")
        print("   ✓ Progress callback forwarding to LangChain")
        print("   ✓ Custom progress message formatting")
        print("   ✓ Elicitation (user input) handling")
        print("   ✓ Error handling and logging")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Make sure your MCP server is running and accessible")


if __name__ == "__main__":
    asyncio.run(main())
