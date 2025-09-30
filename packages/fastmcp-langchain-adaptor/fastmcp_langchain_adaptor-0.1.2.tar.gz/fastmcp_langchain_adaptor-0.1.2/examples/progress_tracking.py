#!/usr/bin/env python3
"""
Advanced Usage Example - Progress Tracking with LangChain Callbacks

This example demonstrates how progress events from MCP tools are
forwarded through LangChain's callback system for monitoring and
observability.
"""

import asyncio
import logging
from typing import Any

from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult
from langchain_core.callbacks import BaseCallbackHandler

from fastmcp_langchain_adaptor import mcp_to_langchain

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProgressTrackingCallbackHandler(BaseCallbackHandler):
    """
    Custom callback handler that captures progress events from MCP tools.

    This demonstrates how to monitor tool execution progress using
    LangChain's standard callback system.
    """

    def __init__(self):
        super().__init__()
        self.progress_events: list[str] = []
        self.tools_called: list[str] = []

    def on_tool_start(
        self, serialized: dict[str, Any], input_str: str, **kwargs: Any
    ) -> None:
        """Called when a tool starts execution."""
        tool_name = serialized.get("name", "unknown")
        self.tools_called.append(tool_name)
        print(f"🔧 Tool started: {tool_name}")
        print(f"   Input: {input_str}")

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        """Called when a tool finishes execution."""
        print("✅ Tool completed")
        print(f"   Output: {output}")

    def on_tool_error(self, error: Exception, **kwargs: Any) -> None:
        """Called when a tool encounters an error."""
        print(f"❌ Tool error: {error}")

    def on_text(self, text: str, **kwargs: Any) -> None:
        """
        Called for text events, including progress updates.

        Progress events from MCP tools are forwarded here as text.
        """
        if "[progress]" in text:
            self.progress_events.append(text)
            print(f"📊 {text}")
        else:
            print(f"💬 {text}")

    def get_summary(self) -> dict[str, Any]:
        """Get a summary of captured events."""
        return {
            "tools_called": self.tools_called,
            "progress_events": self.progress_events,
            "total_progress_updates": len(self.progress_events),
        }


async def mock_elicitation_handler(
    message: str,
    response_type: type,
    params: Any,
    context: Any,
) -> ElicitResult:
    """Mock elicitation handler for demo purposes."""
    print(f"🤔 Tool requesting input: {message}")

    # Simulate different responses based on message content
    if "confirm" in message.lower():
        print("   → Auto-confirming for demo")
        return ElicitResult(action="accept", content={})
    elif "choice" in message.lower():
        print("   → Auto-selecting first option for demo")
        return ElicitResult(action="accept", content={"choice": "option1"})
    else:
        print("   → Auto-accepting for demo")
        return ElicitResult(action="accept", content={})


def create_custom_progress_formatter() -> callable:
    """
    Create a custom progress formatter function.

    This shows how you can customize the format of progress messages
    before they're sent to LangChain callbacks.
    """

    def formatter(progress_dict: dict[str, Any]) -> str:
        progress = progress_dict.get("progress", 0)
        total = progress_dict.get("total")
        message = progress_dict.get("message", "")

        if total is not None:
            percentage = int((progress / total) * 100)
            bar_length = 20
            filled_length = int(bar_length * progress / total)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            return f"🔄 [{bar}] {percentage}% - {message}"
        else:
            return f"🔄 Progress: {progress} - {message}"

    return formatter


async def simulate_mcp_tool_execution():
    """
    Simulate MCP tool execution with progress tracking.

    In a real scenario, this would be actual MCP tools from a server.
    """
    print("📋 Simulating MCP tool conversion and execution...")

    # Create FastMCP client (would connect to real MCP server)
    client = Client(
        "http://localhost:8000",  # Example URL
        elicitation_handler=mock_elicitation_handler,
    )

    # In practice, you'd get tools from: await client.list_tools()
    # For this demo, we'll simulate the conversion process

    # Create callback handler to track progress
    callback_handler = ProgressTrackingCallbackHandler()

    # Create custom progress formatter
    progress_formatter = create_custom_progress_formatter()

    print("🔄 Converting MCP tools with custom progress formatting...")

    # Convert tools (would be real MCP tools in practice)
    lc_tools = mcp_to_langchain(
        tools=[],  # Would be your actual MCP tools list
        client=client,
        progress_formatter=progress_formatter,
    )

    print(f"✅ Converted {len(lc_tools)} tools")

    # In a real scenario, you would invoke the tools like this:
    # for tool in lc_tools:
    #     result = await tool.ainvoke(
    #         {"argument": "value"},
    #         callbacks=[callback_handler]
    #     )

    # For demo purposes, let's simulate some progress events
    print("\n📊 Simulating tool execution with progress tracking...")

    # Simulate progress events being sent to callback
    callback_handler.on_tool_start({"name": "file_processor"}, "process large file")
    callback_handler.on_text("🔄 [████░░░░░░░░░░░░░░░░] 20% - Reading file...")
    callback_handler.on_text("🔄 [████████░░░░░░░░░░░░] 40% - Processing data...")
    callback_handler.on_text("🔄 [████████████░░░░░░░░] 60% - Analyzing content...")
    callback_handler.on_text("🔄 [████████████████░░░░] 80% - Generating results...")
    callback_handler.on_text("🔄 [████████████████████] 100% - Complete!")
    callback_handler.on_tool_end("File processed successfully with 150 records")

    # Show summary
    summary = callback_handler.get_summary()
    print("\n📈 Execution Summary:")
    print(f"   Tools called: {summary['tools_called']}")
    print(f"   Progress updates: {summary['total_progress_updates']}")
    print(f"   Progress events: {summary['progress_events']}")


async def demonstrate_langchain_agent_integration():
    """
    Demonstrate how MCP tools work with LangChain agents.

    This shows the full integration pipeline.
    """
    print("\n🤖 LangChain Agent Integration Demo")
    print("=" * 50)

    try:
        # This would be a real LangChain agent setup
        print("🧠 Setting up LangChain agent with MCP tools...")

        # Example agent setup (commented out to avoid dependencies)
        # from langchain.agents import create_openai_functions_agent
        # from langchain_openai import ChatOpenAI
        #
        # client = Client("http://localhost:8000")
        # mcp_tools = await client.list_tools()
        # lc_tools = mcp_to_langchain(mcp_tools, client=client)
        #
        # llm = ChatOpenAI(model="gpt-4")
        # agent = create_openai_functions_agent(llm, lc_tools, prompt)
        #
        # # Execute with progress tracking
        # callback_handler = ProgressTrackingCallbackHandler()
        # result = await agent.ainvoke(
        #     {"input": "Process the uploaded file and generate a summary"},
        #     callbacks=[callback_handler]
        # )

        print("✅ Agent would execute MCP tools with full progress visibility")
        print("📊 Progress events would flow through LangChain's callback system")
        print("🔍 Full observability without custom types or complex configuration")

    except Exception as e:
        print(f"ℹ️  Demo simulation: {e}")


async def main():
    """Main demonstration function."""
    print("🚀 FastMCP LangChain Adaptor - Advanced Progress Tracking")
    print("=" * 70)

    await simulate_mcp_tool_execution()
    await demonstrate_langchain_agent_integration()

    print("\n🎯 Key Benefits Demonstrated:")
    print("   ✓ Progress events forwarded through LangChain callbacks")
    print("   ✓ Custom progress formatting support")
    print("   ✓ Standard LangChain observability patterns")
    print("   ✓ No custom types needed")
    print("   ✓ Seamless integration with agents and chains")
    print("   ✓ Elicitation handling works transparently")


if __name__ == "__main__":
    asyncio.run(main())
