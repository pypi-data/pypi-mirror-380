"""
Test utilities and fixtures for fastmcp-langchain-adaptor tests.
"""

import asyncio
from typing import Any

import pytest


class MockMcpTool:
    """Mock MCP tool for testing."""

    def __init__(
        self,
        name: str,
        description: str = "",
        input_schema: dict[str, Any] | None = None,
    ):
        self.name = name
        self.description = description
        self.inputSchema = input_schema or {"type": "object", "properties": {}}


class MockTextContent:
    """Mock text content for MCP responses."""

    def __init__(self, text: str):
        self.text = text


class MockCallToolResult:
    """Mock result from MCP tool call."""

    def __init__(
        self,
        content: list[Any],
        data: Any | None = None,
        structured_content: Any | None = None,
    ):
        self.content = content
        self.data = data
        self.structured_content = structured_content


class MockClient:
    """Mock FastMCP client for testing."""

    def __init__(self, tools: list[MockMcpTool] | None = None):
        self._tools = tools or []
        self._call_results = {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def list_tools(self) -> list[MockMcpTool]:
        return self._tools

    async def call_tool(
        self,
        name: str,
        arguments: dict[str, Any],
        progress_handler: Any | None = None,
    ) -> MockCallToolResult:
        if name in self._call_results:
            result = self._call_results[name]
            # Simulate progress if handler is provided
            if progress_handler:
                await progress_handler(1.0, 1.0, "Tool execution complete")
            return result

        # Default response
        if progress_handler:
            await progress_handler(1.0, 1.0, "Tool execution complete")
        return MockCallToolResult(content=[MockTextContent('{"result": "success"}')])

    def set_tool_result(self, tool_name: str, result: MockCallToolResult):
        """Set the result for a specific tool call."""
        self._call_results[tool_name] = result


@pytest.fixture
def sample_mcp_tools() -> list[MockMcpTool]:
    """Sample MCP tools for testing."""
    return [
        MockMcpTool(
            name="simple_tool",
            description="A simple test tool",
            input_schema={
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "Input message"}
                },
                "required": ["message"],
            },
        ),
        MockMcpTool(
            name="no_args_tool",
            description="A tool with no arguments",
            input_schema={"type": "object", "properties": {}},
        ),
        MockMcpTool(
            name="complex_tool",
            description="A tool with complex schema",
            input_schema={
                "type": "object",
                "properties": {
                    "count": {"type": "integer", "description": "Number of items"},
                    "enabled": {"type": "boolean", "description": "Enable feature"},
                    "config": {
                        "type": "object",
                        "properties": {"timeout": {"type": "number"}},
                    },
                },
                "required": ["count"],
            },
        ),
    ]


@pytest.fixture
def mock_client() -> MockClient:
    """Mock FastMCP client for testing."""
    return MockClient()


@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
