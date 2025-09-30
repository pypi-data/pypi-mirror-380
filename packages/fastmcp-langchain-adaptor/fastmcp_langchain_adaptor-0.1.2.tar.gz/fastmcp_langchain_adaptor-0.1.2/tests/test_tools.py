"""
Tests for the main tools module of fastmcp-langchain-adaptor.
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from langchain_core.tools import StructuredTool

from fastmcp_langchain_adaptor.tools import (
    _create_langchain_tool_from_mcp,
    mcp_to_langchain,
)
from tests.conftest import MockCallToolResult, MockMcpTool, MockTextContent


class TestCreateLangChainTool:
    """Tests for creating LangChain tools from MCP tools."""

    @pytest.mark.asyncio
    async def test_basic_tool_creation(self, mock_client):
        """Test basic tool creation."""
        mcp_tool = MockMcpTool(
            name="test_tool",
            description="Test description",
            input_schema={
                "type": "object",
                "properties": {"message": {"type": "string"}},
                "required": ["message"],
            },
        )

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        assert isinstance(lc_tool, StructuredTool)
        assert lc_tool.name == "test_tool"
        assert lc_tool.description == "Test description"

    @pytest.mark.asyncio
    async def test_tool_invocation_with_json_response(self, mock_client):
        """Test tool invocation with JSON response."""
        mcp_tool = MockMcpTool(name="json_tool", description="JSON tool")

        # Set up mock result
        mock_result = MockCallToolResult(
            content=[MockTextContent('{"result": "success", "data": "test"}')]
        )
        mock_client.set_tool_result("json_tool", mock_result)

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"message": "test"})
        expected = {"result": "success", "data": "test"}
        assert result == expected

    @pytest.mark.asyncio
    async def test_tool_invocation_with_text_response(self, mock_client):
        """Test tool invocation with text response."""
        mcp_tool = MockMcpTool(name="text_tool", description="Text tool")

        # Set up mock result
        mock_result = MockCallToolResult(
            content=[MockTextContent("Simple text response")]
        )
        mock_client.set_tool_result("text_tool", mock_result)

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({})
        assert result == "Simple text response"

    @pytest.mark.asyncio
    async def test_tool_invocation_with_progress_handler(self, mock_client):
        """Test tool invocation with progress handler."""
        mcp_tool = MockMcpTool(name="progress_tool", description="Progress tool")

        # Mock run manager
        mock_run_manager = MagicMock()

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        # Call the coroutine directly with run_manager
        await lc_tool.coroutine(run_manager=mock_run_manager)

        # Should have called on_text at least once for progress
        assert mock_run_manager.on_text.called

    @pytest.mark.asyncio
    async def test_tool_with_empty_schema(self, mock_client):
        """Test tool with empty input schema."""
        mcp_tool = MockMcpTool(
            name="empty_schema_tool",
            description="Tool with empty schema",
            input_schema=None,
        )

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        # Should be able to invoke without arguments
        result = await lc_tool.ainvoke({})
        assert result is not None

    @pytest.mark.asyncio
    async def test_tool_error_handling(self, mock_client):
        """Test tool error handling."""
        mcp_tool = MockMcpTool(name="error_tool", description="Error tool")

        # Mock client to raise exception
        async def mock_call_tool(*args, **kwargs):
            raise Exception("Test error")

        mock_client.call_tool = mock_call_tool

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        with pytest.raises(Exception, match="Test error"):
            await lc_tool.ainvoke({})


class TestMcpToLangChain:
    """Tests for the main mcp_to_langchain function."""

    def test_empty_tools_list(self, mock_client):
        """Test with empty tools list."""
        result = mcp_to_langchain([], client=mock_client)
        assert result == []

    def test_multiple_tools_conversion(self, sample_mcp_tools, mock_client):
        """Test converting multiple tools."""
        result = mcp_to_langchain(sample_mcp_tools, client=mock_client)

        assert len(result) == len(sample_mcp_tools)
        assert all(isinstance(tool, StructuredTool) for tool in result)

        # Check tool names
        tool_names = [tool.name for tool in result]
        expected_names = [tool.name for tool in sample_mcp_tools]
        assert tool_names == expected_names

    def test_tool_conversion_with_progress_formatter(
        self, sample_mcp_tools, mock_client
    ):
        """Test tool conversion with progress formatter."""

        def custom_formatter(event: dict[str, Any]) -> str:
            return f"Custom: {event.get('message', 'No message')}"

        result = mcp_to_langchain(
            sample_mcp_tools, client=mock_client, progress_formatter=custom_formatter
        )

        assert len(result) == len(sample_mcp_tools)

    @patch("fastmcp_langchain_adaptor.tools.logger")
    def test_tool_conversion_error_handling(self, mock_logger, mock_client):
        """Test error handling during tool conversion."""

        # Create a malformed tool that will cause conversion to fail
        class BadMcpTool:
            @property
            def name(self):
                raise ValueError("Cannot get name")

        bad_tool = BadMcpTool()
        tools = [bad_tool]

        result = mcp_to_langchain(tools, client=mock_client)

        # Should return empty list and log error
        assert result == []
        mock_logger.error.assert_called()


class TestProgressHandling:
    """Tests for progress event handling."""

    @pytest.mark.asyncio
    async def test_progress_handler_with_dict_arg(self, mock_client):
        """Test progress handler with dictionary argument."""
        mcp_tool = MockMcpTool(name="progress_test", description="Progress test")

        mock_run_manager = MagicMock()

        async def custom_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                # Simulate progress event with correct MCP signature
                await progress_handler(50.0, 100.0, "Processing...")
            return MockCallToolResult(content=[MockTextContent("Done")])

        mock_client.call_tool = custom_call_tool

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        # Call the coroutine directly with run_manager
        await lc_tool.coroutine(run_manager=mock_run_manager)

        # Check that progress was forwarded
        mock_run_manager.on_text.assert_called()
        call_args = mock_run_manager.on_text.call_args[0][0]
        assert "50.0/100.0" in call_args and "Processing..." in call_args

    @pytest.mark.asyncio
    async def test_progress_handler_with_multiple_args(self, mock_client):
        """Test progress handler with multiple arguments."""
        mcp_tool = MockMcpTool(name="progress_test", description="Progress test")

        mock_run_manager = MagicMock()

        async def custom_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                # Simulate progress event with correct MCP signature
                await progress_handler(75.0, 100.0, "Almost done")
            return MockCallToolResult(content=[MockTextContent("Done")])

        mock_client.call_tool = custom_call_tool

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        # Call the coroutine directly with run_manager
        await lc_tool.coroutine(run_manager=mock_run_manager)

        # Check that progress was forwarded
        mock_run_manager.on_text.assert_called()
        call_args = mock_run_manager.on_text.call_args[0][0]
        assert "75.0/100.0" in call_args and "Almost done" in call_args


class TestEdgeCases:
    """Tests for edge cases and error conditions."""

    @pytest.mark.asyncio
    async def test_malformed_json_response(self, mock_client):
        """Test handling of malformed JSON response."""
        mcp_tool = MockMcpTool(name="malformed_json", description="Malformed JSON tool")

        mock_result = MockCallToolResult(
            content=[MockTextContent('{"incomplete": json')]
        )
        mock_client.set_tool_result("malformed_json", mock_result)

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({})
        # Should return the raw text instead of trying to parse as JSON
        assert result == '{"incomplete": json'

    @pytest.mark.asyncio
    async def test_empty_response_with_progress_data(self, mock_client):
        """Test handling empty response but with progress data."""
        mcp_tool = MockMcpTool(
            name="empty_with_progress", description="Empty with progress"
        )

        # Set up empty official response
        mock_result = MockCallToolResult(content=[MockTextContent('{"response":""}')])
        mock_client.set_tool_result("empty_with_progress", mock_result)

        # Mock progress handler that captures data

        async def custom_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                # Simulate progress with actual data in message field
                await progress_handler(1.0, 1.0, "This is the real data from progress")
            return mock_result

        mock_client.call_tool = custom_call_tool

        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({})
        # The simplified code returns the parsed JSON content directly
        assert result == {"response": ""}

    def test_tool_without_name_attribute(self, mock_client):
        """Test handling tool without name attribute."""

        class NamelessToolMock:
            def __init__(self):
                self.description = "Tool without name"
                self.inputSchema = {"type": "object", "properties": {}}

        nameless_tool = NamelessToolMock()

        lc_tool = _create_langchain_tool_from_mcp(
            tool=nameless_tool, client=mock_client
        )

        # Should use default name
        assert lc_tool.name == "mcp_tool"

    def test_tool_without_description(self, mock_client):
        """Test handling tool without description."""

        class NoDescToolMock:
            def __init__(self):
                self.name = "no_desc_tool"
                self.inputSchema = {"type": "object", "properties": {}}

        no_desc_tool = NoDescToolMock()

        lc_tool = _create_langchain_tool_from_mcp(tool=no_desc_tool, client=mock_client)

        # Should create default description
        assert "MCP tool 'no_desc_tool'" in lc_tool.description


class TestEdgeCaseCoverage:
    """Additional tests to improve code coverage."""

    @pytest.mark.asyncio
    async def test_progress_handler_exception(self, mock_client):
        """Test progress handler when run_manager.on_text raises exception."""
        mcp_tool = MockMcpTool(name="error_progress", description="Error progress")

        # Mock run manager that raises exception
        mock_run_manager = MagicMock()
        mock_run_manager.on_text.side_effect = Exception("Mock error")

        async def custom_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                # This should trigger the exception handling in progress handler
                await progress_handler(50.0, 100.0, "Progress update")
            return MockCallToolResult(content=[MockTextContent("Done")])

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        # Should not raise exception despite run_manager error
        result = await lc_tool.coroutine(run_manager=mock_run_manager)
        assert result == "Done"

    @pytest.mark.asyncio
    async def test_tool_with_structured_content(self, mock_client):
        """Test tool result with structured_content attribute."""
        mcp_tool = MockMcpTool(name="structured_tool", description="Structured tool")

        class MockResultWithStructured:
            def __init__(self):
                self.data = None
                self.structured_content = {"key": "structured_value"}
                self.content = []

        async def custom_call_tool(name, arguments, progress_handler=None):
            return MockResultWithStructured()

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.coroutine()
        assert result == {"key": "structured_value"}

    @pytest.mark.asyncio
    async def test_tool_with_data_attribute(self, mock_client):
        """Test tool result with data attribute."""
        mcp_tool = MockMcpTool(name="data_tool", description="Data tool")

        class MockResultWithData:
            def __init__(self):
                self.data = {"key": "data_value"}

        async def custom_call_tool(name, arguments, progress_handler=None):
            return MockResultWithData()

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.coroutine()
        assert result == {"key": "data_value"}

    @pytest.mark.asyncio
    async def test_tool_with_complex_content_list(self, mock_client):
        """Test tool result with multiple items in content list."""
        mcp_tool = MockMcpTool(name="multi_content", description="Multi content")

        mock_result = MockCallToolResult(
            content=[MockTextContent("First item"), MockTextContent("Second item")]
        )

        async def custom_call_tool(name, arguments, progress_handler=None):
            return mock_result

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.coroutine()
        # Should return the full content list when multiple items
        assert len(result) == 2

    @pytest.mark.asyncio
    async def test_tool_with_dict_content_item(self, mock_client):
        """Test tool result with dictionary content item."""
        mcp_tool = MockMcpTool(name="dict_content", description="Dict content")

        # Mock result with dict content
        mock_content = [{"text": "extracted_text", "data": "some_data"}]
        mock_result = MockCallToolResult(content=mock_content)

        async def custom_call_tool(name, arguments, progress_handler=None):
            return mock_result

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.coroutine()
        assert result == mock_content  # The simplified code returns content directly

    @pytest.mark.asyncio
    async def test_progress_handler_with_none_total(self, mock_client):
        """Test progress handler with None total value."""
        mcp_tool = MockMcpTool(name="none_total", description="None total")

        mock_run_manager = MagicMock()

        async def custom_call_tool(name, arguments, progress_handler=None):
            if progress_handler:
                # Call with None total
                await progress_handler(50.0, None, "Progress without total")
            return MockCallToolResult(content=[MockTextContent("Done")])

        mock_client.call_tool = custom_call_tool
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        await lc_tool.coroutine(run_manager=mock_run_manager)

        # Should have formatted progress without total
        mock_run_manager.on_text.assert_called()
        call_args = mock_run_manager.on_text.call_args[0][0]
        assert "50.0 –" in call_args and "Progress without total" in call_args


class TestElicitationHandling:
    """Tests for MCP elicitation handling during tool execution."""

    @pytest.mark.asyncio
    async def test_tool_with_elicitation_request(self, mock_client):
        """Test tool that requires user input via elicitation during execution."""
        mcp_tool = MockMcpTool(
            name="call_friend",
            description="Call a friend - will ask for phone type preference",
        )

        # Track elicitation interactions
        elicitation_log = []

        async def mock_call_tool_with_elicitation(
            name, arguments, progress_handler=None
        ):
            # Simulate tool execution that requires elicitation
            elicitation_log.append("Tool started: calling friend")

            # Mock elicitation - tool asks which phone to use
            elicitation_response = {"phone_type": "mobile"}  # Simulated user response
            elicitation_log.append(f"User chose: {elicitation_response['phone_type']}")

            # Tool continues with user's choice
            if progress_handler:
                await progress_handler(
                    50.0,
                    100.0,
                    f"Calling {elicitation_response['phone_type']} phone...",
                )
                await progress_handler(100.0, 100.0, "Call completed")

            return MockCallToolResult(
                content=[
                    MockTextContent(
                        f"Successfully called friend on "
                        f"{elicitation_response['phone_type']} phone"
                    )
                ]
            )

        mock_client.call_tool = mock_call_tool_with_elicitation
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"friend_name": "Alice"})

        assert "Successfully called friend on mobile phone" in result
        assert len(elicitation_log) == 2
        assert "Tool started" in elicitation_log[0]
        assert "User chose: mobile" in elicitation_log[1]

    @pytest.mark.asyncio
    async def test_elicitation_with_progress_updates(self, mock_client):
        """Test elicitation combined with progress updates."""
        mcp_tool = MockMcpTool(
            name="configure_service",
            description="Configure a service with user preferences",
        )

        mock_run_manager = MagicMock()
        progress_messages = []

        def capture_progress(text, **kwargs):
            progress_messages.append(text)

        mock_run_manager.on_text.side_effect = capture_progress

        async def mock_call_tool_with_elicitation_and_progress(
            name, arguments, progress_handler=None
        ):
            if progress_handler:
                await progress_handler(10.0, 100.0, "Starting configuration...")
                await progress_handler(25.0, 100.0, "Asking for user preferences...")

                # Simulate elicitation pause - in real scenario, FastMCP handles this
                await progress_handler(50.0, 100.0, "User selected advanced mode")
                await progress_handler(75.0, 100.0, "Applying configuration...")
                await progress_handler(100.0, 100.0, "Configuration complete")

            return MockCallToolResult(
                content=[MockTextContent("Service configured successfully")]
            )

        mock_client.call_tool = mock_call_tool_with_elicitation_and_progress
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.coroutine(run_manager=mock_run_manager)

        assert result == "Service configured successfully"
        assert len(progress_messages) == 5
        assert "Starting configuration" in progress_messages[0]
        assert "Asking for user preferences" in progress_messages[1]
        assert "User selected advanced mode" in progress_messages[2]
        assert "Configuration complete" in progress_messages[4]

    @pytest.mark.asyncio
    async def test_elicitation_rejection_handling(self, mock_client):
        """Test handling when user rejects elicitation request."""
        mcp_tool = MockMcpTool(
            name="delete_files", description="Delete files - will ask for confirmation"
        )

        async def mock_call_tool_with_rejection(name, arguments, progress_handler=None):
            # Simulate elicitation rejection
            if progress_handler:
                await progress_handler(
                    25.0, 100.0, "Requesting deletion confirmation..."
                )
                await progress_handler(50.0, 100.0, "User declined deletion request")

            return MockCallToolResult(
                content=[MockTextContent("Operation cancelled by user")]
            )

        mock_client.call_tool = mock_call_tool_with_rejection
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"files": ["file1.txt", "file2.txt"]})

        assert "Operation cancelled by user" in result

    @pytest.mark.asyncio
    async def test_multiple_elicitation_rounds(self, mock_client):
        """Test tool with multiple elicitation rounds."""
        mcp_tool = MockMcpTool(
            name="book_travel", description="Book travel - may ask multiple questions"
        )

        elicitation_sequence = []

        async def mock_call_tool_with_multiple_elicitations(
            name, arguments, progress_handler=None
        ):
            if progress_handler:
                await progress_handler(20.0, 100.0, "Searching flights...")

                # First elicitation: flight preference
                elicitation_sequence.append("Asked for flight preference")
                await progress_handler(40.0, 100.0, "User chose economy class")

                # Second elicitation: seat preference
                elicitation_sequence.append("Asked for seat preference")
                await progress_handler(60.0, 100.0, "User chose window seat")

                # Third elicitation: meal preference
                elicitation_sequence.append("Asked for meal preference")
                await progress_handler(80.0, 100.0, "User chose vegetarian meal")

                await progress_handler(100.0, 100.0, "Booking confirmed")

            return MockCallToolResult(
                content=[
                    MockTextContent(
                        "Flight booked: Economy, Window seat, Vegetarian meal"
                    )
                ]
            )

        mock_client.call_tool = mock_call_tool_with_multiple_elicitations
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"destination": "Paris", "date": "2024-12-25"})

        assert "Flight booked: Economy, Window seat, Vegetarian meal" in result
        assert len(elicitation_sequence) == 3
        assert "flight preference" in elicitation_sequence[0]
        assert "seat preference" in elicitation_sequence[1]
        assert "meal preference" in elicitation_sequence[2]

    @pytest.mark.asyncio
    async def test_elicitation_with_structured_response(self, mock_client):
        """Test elicitation that expects structured response data."""
        mcp_tool = MockMcpTool(
            name="create_profile",
            description="Create user profile - will ask for structured data",
        )

        async def mock_call_tool_with_structured_elicitation(
            name, arguments, progress_handler=None
        ):
            # Simulate structured elicitation response
            user_profile = {
                "name": "John Doe",
                "age": 30,
                "preferences": {
                    "theme": "dark",
                    "language": "en",
                    "notifications": True,
                },
            }

            if progress_handler:
                await progress_handler(
                    25.0, 100.0, "Requesting user profile information..."
                )
                await progress_handler(
                    50.0, 100.0, f"Received profile for {user_profile['name']}"
                )
                await progress_handler(75.0, 100.0, "Validating profile data...")
                await progress_handler(100.0, 100.0, "Profile created successfully")

            return MockCallToolResult(
                content=[
                    MockTextContent(
                        f"Profile created for {user_profile['name']} "
                        f"with preferences: {user_profile['preferences']}"
                    )
                ]
            )

        mock_client.call_tool = mock_call_tool_with_structured_elicitation
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({})

        assert "Profile created for John Doe" in result
        assert "dark" in result  # theme preference
        assert "notifications" in result

    @pytest.mark.asyncio
    async def test_elicitation_timeout_handling(self, mock_client):
        """Test handling of elicitation timeout scenarios."""
        mcp_tool = MockMcpTool(
            name="interactive_tool",
            description="Tool that may timeout waiting for user input",
        )

        async def mock_call_tool_with_timeout(name, arguments, progress_handler=None):
            if progress_handler:
                await progress_handler(25.0, 100.0, "Waiting for user input...")
                await progress_handler(50.0, 100.0, "Still waiting...")
                await progress_handler(75.0, 100.0, "Timeout approaching...")
                await progress_handler(100.0, 100.0, "Timeout - using default values")

            return MockCallToolResult(
                content=[
                    MockTextContent(
                        "Operation completed with default settings due to timeout"
                    )
                ]
            )

        mock_client.call_tool = mock_call_tool_with_timeout
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"action": "configure"})

        assert "completed with default settings due to timeout" in result

    @pytest.mark.asyncio
    async def test_elicitation_error_recovery(self, mock_client):
        """Test error recovery during elicitation."""
        mcp_tool = MockMcpTool(
            name="validation_tool",
            description="Tool that handles validation errors during elicitation",
        )

        async def mock_call_tool_with_validation_error(
            name, arguments, progress_handler=None
        ):
            if progress_handler:
                await progress_handler(20.0, 100.0, "Requesting input...")
                await progress_handler(40.0, 100.0, "Invalid input received")
                await progress_handler(60.0, 100.0, "Requesting corrected input...")
                await progress_handler(80.0, 100.0, "Valid input received")
                await progress_handler(100.0, 100.0, "Processing completed")

            return MockCallToolResult(
                content=[MockTextContent("Input validated and processed successfully")]
            )

        mock_client.call_tool = mock_call_tool_with_validation_error
        lc_tool = _create_langchain_tool_from_mcp(tool=mcp_tool, client=mock_client)

        result = await lc_tool.ainvoke({"data": "invalid_format"})

        assert "validated and processed successfully" in result
