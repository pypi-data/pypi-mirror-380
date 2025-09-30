"""
Integration tests for fastmcp-langchain-adaptor.

These tests verify the package works end-to-end but use mocked dependencies.
"""

from unittest.mock import MagicMock

import pytest

from fastmcp_langchain_adaptor import mcp_to_langchain
from tests.conftest import MockCallToolResult, MockClient, MockMcpTool, MockTextContent


class TestIntegration:
    """Integration tests for the complete workflow."""

    @pytest.mark.asyncio
    async def test_end_to_end_workflow(self):
        """Test the complete workflow from MCP tools to LangChain execution."""
        # Create mock MCP tools
        tools = [
            MockMcpTool(
                name="weather_tool",
                description="Get weather information",
                input_schema={
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name"}
                    },
                    "required": ["city"],
                },
            ),
            MockMcpTool(
                name="calculator",
                description="Perform calculations",
                input_schema={
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Mathematical expression",
                        }
                    },
                    "required": ["expression"],
                },
            ),
        ]

        # Create mock client with expected responses
        client = MockClient(tools)
        client.set_tool_result(
            "weather_tool",
            MockCallToolResult(
                content=[
                    MockTextContent('{"temperature": "22°C", "condition": "sunny"}')
                ]
            ),
        )
        client.set_tool_result(
            "calculator",
            MockCallToolResult(content=[MockTextContent('{"result": 42}')]),
        )

        # Convert to LangChain tools
        lc_tools = mcp_to_langchain(tools, client=client)

        # Verify conversion
        assert len(lc_tools) == 2
        assert lc_tools[0].name == "weather_tool"
        assert lc_tools[1].name == "calculator"

        # Test tool execution
        weather_result = await lc_tools[0].ainvoke({"city": "New York"})
        assert weather_result == {"temperature": "22°C", "condition": "sunny"}

        calc_result = await lc_tools[1].ainvoke({"expression": "6 * 7"})
        assert calc_result == {"result": 42}

    @pytest.mark.asyncio
    async def test_error_recovery(self):
        """Test error recovery in the complete workflow."""
        # Mix of working and broken tools
        tools = [
            MockMcpTool(name="working_tool", description="Works fine"),
            MockMcpTool(name="broken_tool", description="Will fail"),
        ]

        client = MockClient(tools)
        client.set_tool_result(
            "working_tool", MockCallToolResult(content=[MockTextContent("success")])
        )

        # Set up broken tool to raise exception
        async def failing_call_tool(name, arguments, progress_handler=None):
            if name == "broken_tool":
                raise Exception("Tool error")
            return MockCallToolResult(content=[MockTextContent("success")])

        client.call_tool = failing_call_tool

        # Convert tools (this should succeed even with one broken tool)
        lc_tools = mcp_to_langchain(tools, client=client)

        # Working tool should still work
        result = await lc_tools[0].ainvoke({})
        assert result == "success"

        # Broken tool should raise exception
        with pytest.raises(Exception, match="Tool error"):
            await lc_tools[1].ainvoke({})

    @pytest.mark.asyncio
    async def test_progress_handling_integration(self):
        """Test progress handling in the complete workflow."""
        tools = [MockMcpTool(name="slow_tool", description="A slow tool with progress")]

        client = MockClient(tools)

        # Mock run manager to capture progress calls
        mock_run_manager = MagicMock()
        progress_messages = []

        def capture_progress(text, verbose=True):
            progress_messages.append(text)

        mock_run_manager.on_text.side_effect = capture_progress

        # Set up tool with progress simulation
        async def slow_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                await progress_handler(25.0, 100.0, "Starting...")
                await progress_handler(50.0, 100.0, "Half way...")
                await progress_handler(100.0, 100.0, "Complete!")
            return MockCallToolResult(content=[MockTextContent("done")])

        client.call_tool = slow_call_tool

        # Convert and execute
        lc_tools = mcp_to_langchain(tools, client=client)
        # Call the coroutine directly with run_manager
        result = await lc_tools[0].coroutine(run_manager=mock_run_manager)

        # Verify results
        assert result == "done"
        assert len(progress_messages) == 3
        assert "Starting..." in progress_messages[0]
        assert "Half way..." in progress_messages[1]
        assert "Complete!" in progress_messages[2]

    @pytest.mark.asyncio
    async def test_elicitation_integration_workflow(self):
        """Test end-to-end elicitation workflow with multiple tools."""
        # Simulate an MCP server that has tools requiring elicitation

        class ElicitationMockClient:
            def __init__(self):
                self.elicitation_log = []

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

            async def call_tool(self, name, arguments, progress_handler=None):
                if name == "call_friend":
                    return await self._handle_call_friend(arguments, progress_handler)
                elif name == "send_email":
                    return await self._handle_send_email(arguments, progress_handler)
                else:
                    return MockCallToolResult(content=[MockTextContent("Unknown tool")])

            async def _handle_call_friend(self, arguments, progress_handler=None):
                """Simulate call_friend tool that asks for phone type preference."""
                friend_name = arguments.get("friend_name", "Unknown")

                if progress_handler:
                    await progress_handler(
                        25.0, 100.0, f"Looking up contact info for {friend_name}..."
                    )

                # Simulate elicitation: ask user which phone to use
                self.elicitation_log.append(
                    {
                        "tool": "call_friend",
                        "question": f"Which phone should I use to call {friend_name}?",
                        "options": ["mobile", "home", "work"],
                    }
                )

                # Simulate user choosing mobile
                user_choice = "mobile"
                self.elicitation_log.append(
                    {"tool": "call_friend", "user_response": user_choice}
                )

                if progress_handler:
                    await progress_handler(
                        50.0, 100.0, f"User chose {user_choice} phone"
                    )
                    await progress_handler(
                        75.0, 100.0, f"Dialing {friend_name}'s {user_choice} number..."
                    )
                    await progress_handler(100.0, 100.0, "Call connected")

                return MockCallToolResult(
                    content=[
                        MockTextContent(
                            f"Successfully called {friend_name} on {user_choice} "
                            f"phone. Call duration: 5 minutes."
                        )
                    ]
                )

            async def _handle_send_email(self, arguments, progress_handler=None):
                """Simulate send_email tool that asks for email priority."""
                recipient = arguments.get("to", "Unknown")

                if progress_handler:
                    await progress_handler(20.0, 100.0, "Composing email...")

                # Simulate elicitation: ask for email priority
                self.elicitation_log.append(
                    {
                        "tool": "send_email",
                        "question": (
                            f"What priority should this email to {recipient} have?"
                        ),
                        "options": ["low", "normal", "high", "urgent"],
                    }
                )

                # Simulate user choosing high priority
                user_choice = "high"
                self.elicitation_log.append(
                    {"tool": "send_email", "user_response": user_choice}
                )

                if progress_handler:
                    await progress_handler(
                        60.0, 100.0, f"User set priority to {user_choice}"
                    )
                    await progress_handler(80.0, 100.0, "Sending email...")
                    await progress_handler(100.0, 100.0, "Email sent")

                return MockCallToolResult(
                    content=[
                        MockTextContent(
                            f"Email sent to {recipient} with {user_choice} priority"
                        )
                    ]
                )

        # Create mock tools
        tools = [
            MockMcpTool(
                name="call_friend",
                description="Call a friend - will ask which phone number to use",
                input_schema={
                    "type": "object",
                    "properties": {
                        "friend_name": {
                            "type": "string",
                            "description": "Name of friend to call",
                        }
                    },
                    "required": ["friend_name"],
                },
            ),
            MockMcpTool(
                name="send_email",
                description="Send an email - will ask for priority level",
                input_schema={
                    "type": "object",
                    "properties": {
                        "to": {"type": "string", "description": "Email recipient"},
                        "subject": {"type": "string", "description": "Email subject"},
                        "body": {"type": "string", "description": "Email body"},
                    },
                    "required": ["to", "subject", "body"],
                },
            ),
        ]

        elicitation_client = ElicitationMockClient()

        # Convert to LangChain tools
        lc_tools = mcp_to_langchain(tools, client=elicitation_client)

        assert len(lc_tools) == 2

        # Test call_friend tool with elicitation
        call_result = await lc_tools[0].ainvoke({"friend_name": "Alice"})
        assert "Successfully called Alice on mobile phone" in call_result
        assert "Call duration: 5 minutes" in call_result

        # Test send_email tool with elicitation
        email_result = await lc_tools[1].ainvoke(
            {
                "to": "bob@example.com",
                "subject": "Meeting reminder",
                "body": "Don't forget about our meeting tomorrow",
            }
        )
        assert "Email sent to bob@example.com with high priority" in email_result

        # Verify elicitation interactions were captured
        assert len(elicitation_client.elicitation_log) == 4  # 2 questions + 2 responses

        # Check call_friend elicitation
        call_question = elicitation_client.elicitation_log[0]
        assert call_question["tool"] == "call_friend"
        assert "Which phone should I use" in call_question["question"]
        assert "mobile" in call_question["options"]

        call_response = elicitation_client.elicitation_log[1]
        assert call_response["tool"] == "call_friend"
        assert call_response["user_response"] == "mobile"

        # Check send_email elicitation
        email_question = elicitation_client.elicitation_log[2]
        assert email_question["tool"] == "send_email"
        assert "priority" in email_question["question"]
        assert "urgent" in email_question["options"]

        email_response = elicitation_client.elicitation_log[3]
        assert email_response["tool"] == "send_email"
        assert email_response["user_response"] == "high"
