# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2025-09-29

### Changed
- **BREAKING**: Removed custom type definitions (`ToolConfig`, `ToolExecutionMetadata`, `EnhancedToolResult`)
- **BREAKING**: Simplified API to use only LangChain built-in types
- **BREAKING**: Removed complex configuration options in favor of simple, focused API
- Progress events now forwarded directly through LangChain's callback system
- Tool results are standard LangChain tool returns (no custom wrapper types)

### Removed
- `types.py` module with custom type definitions
- `ToolConfig` class and associated configuration options
- `ToolExecutionMetadata` and progress/elicitation tracking in custom types
- `EnhancedToolResult` wrapper class
- `response_format="content_and_artifact"` support (simplified to standard results)

### Added
- Comprehensive documentation explaining the LangChain-native approach
- Migration guide for users upgrading from custom types
- Example scripts demonstrating simplified usage

### Benefits
- Simpler, more intuitive API that follows LangChain patterns
- Reduced complexity and fewer types to learn
- Better integration with existing LangChain workflows
- Natural progress tracking through LangChain callback managers
- Maintained full functionality for progress and elicitation handling

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
