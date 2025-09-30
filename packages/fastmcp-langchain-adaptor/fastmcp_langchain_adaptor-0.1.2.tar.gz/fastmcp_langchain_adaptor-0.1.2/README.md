# FastMCP LangChain Adaptor

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python package that provides seamless integration between [FastMCP](https://github.com/jlowin/fastmcp) (Model Context Protocol) and [LangChain](https://langchain.com/), allowing you to use MCP tools as LangChain StructuredTools.

## Features

- 🔄 **Seamless Integration**: Convert FastMCP tools to LangChain StructuredTools with a single function call
- 🔄 **Async Support**: Full async/await support for modern Python applications
- 📊 **Progress Callbacks**: Forward MCP progress events to LangChain callbacks
- 🛡️ **Error Handling**: Comprehensive error handling with detailed logging
- 🔍 **Type Safety**: Full type hints and Pydantic model validation
- 📝 **Extensive Logging**: Debug-friendly logging for troubleshooting

## Installation

```bash
pip install fastmcp-langchain-adaptor
```

Or using uv (recommended):

```bash
uv add fastmcp-langchain-adaptor
```

### Development Installation

```bash
git clone https://github.com/username/fastmcp-langchain-adaptor.git
cd fastmcp-langchain-adaptor
uv sync --dev
uv run pre-commit install
```

## Quick Start

```python
import asyncio
from fastmcp import Client
from fastmcp_langchain_adaptor import mcp_to_langchain
from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI

async def main():
    # Create FastMCP client
    client = Client("http://localhost:8000")

    # Get MCP tools and convert to LangChain tools
    mcp_tools = await client.list_tools()
    lc_tools = mcp_to_langchain(mcp_tools, client=client)

    # Use with LangChain
    llm = ChatOpenAI(temperature=0)
    agent = create_openai_functions_agent(llm, lc_tools, prompt)

    # Execute with agent
    result = await agent.ainvoke({"input": "Use the MCP tool to help me"})
    print(result)

asyncio.run(main())
```

## Advanced Usage

### Custom Progress Formatting

```python
def custom_progress_formatter(event: dict) -> str:
    progress = event.get("progress", 0)
    total = event.get("total", 100)
    message = event.get("message", "")
    return f"Progress: {progress}/{total} - {message}"

lc_tools = mcp_to_langchain(
    mcp_tools,
    client=client,
    progress_formatter=custom_progress_formatter
)
```

### Elicitation (User Input During Tool Execution)

FastMCP supports elicitation, which allows tools to request additional information from users during execution. This is particularly useful for tools that need to make decisions based on user preferences or require confirmation for sensitive operations.

```python
from fastmcp import Client
from fastmcp.client.elicitation import ElicitResult

# Set up elicitation handler
async def elicitation_handler(
    message: str,
    response_type: type,
    params,
    context
):
    """Handle elicitation requests from MCP tools."""
    print(f"Tool is asking: {message}")

    # Example: call_friend tool asking which phone to use
    if "phone" in message.lower():
        # In a real app, you'd show a UI dialog or prompt
        user_choice = input("Which phone? (mobile/home/work): ")
        return {"phone_type": user_choice}

    # Example: delete_files tool asking for confirmation
    elif "delete" in message.lower():
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == 'yes':
            return ElicitResult(action="accept", content={})
        else:
            return ElicitResult(action="reject", content={})

    # Default response
    return ElicitResult(action="accept", content={})

# Create client with elicitation handler
client = Client("http://localhost:8000", elicitation_handler=elicitation_handler)

# Convert tools - elicitation will work transparently
lc_tools = mcp_to_langchain(mcp_tools, client=client)

# When you invoke tools, they may trigger elicitation
result = await lc_tools[0].ainvoke({"friend_name": "Alice"})
# This might pause and ask: "Which phone should I use to call Alice?"
# User responds, tool continues execution
print(result)  # "Successfully called Alice on mobile phone"
```

**Common Elicitation Scenarios:**
- **Phone calls**: Asking which number to use (mobile/home/work)
- **File operations**: Confirming dangerous operations (delete, overwrite)
- **Configuration**: Requesting user preferences (theme, settings)
- **Data input**: Collecting structured information (forms, profiles)
- **Multi-step workflows**: Making decisions at each step
```

### Error Handling

```python
import logging

# Enable debug logging
logging.getLogger('fastmcp_langchain_adaptor').setLevel(logging.DEBUG)

try:
    lc_tools = mcp_to_langchain(mcp_tools, client=client)
except Exception as e:
    logger.error(f"Failed to convert MCP tools: {e}")
```

## API Reference

### `mcp_to_langchain`

Convert a list of FastMCP tool descriptors into LangChain StructuredTools.

**Parameters:**
- `tools` (List[McpTool]): The descriptors returned by `await client.list_tools()`
- `client` (Client): The FastMCP client you created
- `progress_formatter` (Optional[Callable]): Optional function to format progress events

**Returns:**
- `List[StructuredTool]`: List of LangChain StructuredTools

## Requirements

- Python 3.11+
- fastmcp >= 2.12.4
- langchain >= 0.3.27

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Clone your fork
3. Install development dependencies:
   ```bash
   uv sync --dev
   uv run pre-commit install
   ```
4. Run tests:
   ```bash
   uv run pytest
   ```
5. Run linting and formatting:
   ```bash
   uv run black . && uv run ruff check . --fix
   ```

## Security

This package follows security best practices:

- Input validation using Pydantic models
- Comprehensive error handling without exposing sensitive information
- No hardcoded secrets or credentials
- Secure defaults for all configurations

If you discover a security vulnerability, please email security@example.com instead of opening a public issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Support

- 📖 Documentation: [docs.example.com](https://docs.example.com)
- 🐛 Issues: [GitHub Issues](https://github.com/username/fastmcp-langchain-adaptor/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/username/fastmcp-langchain-adaptor/discussions)
