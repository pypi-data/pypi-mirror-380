# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-12-19

### Added
- Initial release of fastmcp-langchain-adaptor
- Core functionality to convert FastMCP tools to LangChain StructuredTools
- Async support for tool execution
- Progress callback forwarding from MCP to LangChain
- Comprehensive error handling and logging
- Type safety with Pydantic model validation
- JSON schema to Pydantic model conversion
- Support for custom progress formatters
- Extensive test suite with mocks
- Security policy and guidelines
- Complete documentation

### Features
- `mcp_to_langchain()` function for tool conversion
- `_create_langchain_tool_from_mcp()` for individual tool conversion
- `_json_schema_to_pydantic()` for schema conversion
- Progress event handling and forwarding
- Support for various MCP response formats (JSON, text, structured content)
- Robust error handling for malformed responses
- Debug logging throughout the codebase

### Security
- Input validation using Pydantic models
- Secure error handling without information leakage
- No hardcoded credentials or secrets
- Safe JSON parsing with fallbacks
