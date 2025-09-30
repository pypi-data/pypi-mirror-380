# GitHub Copilot Instructions for FastMCP LangChain Adaptor

## Python Package Manager

**Always use `uv` for Python package management and task execution.**

### Key Commands:
- Use `uv sync` instead of `pip install`
- Use `uv sync --dev` for development dependencies
- Use `uv run <command>` for running Python tools and scripts
- Use `uv add <package>` to add dependencies
- Use `uv remove <package>` to remove dependencies
- Use `uv build` to build the package
- Use `uv publish` to publish to PyPI

### Development Workflow:

#### Installation and Setup:
```bash
uv sync --dev
uv run pre-commit install
```

#### Testing:
```bash
uv run pytest                    # Run tests
uv run pytest --cov=...        # Run with coverage
uv run pytest tests/specific.py # Run specific test file
```

#### Code Quality:
```bash
uv run black .                  # Format code
uv run ruff check .            # Lint code
uv run ruff check . --fix      # Auto-fix lint issues
uv run isort .                 # Sort imports
uv run mypy fastmcp_langchain_adaptor/  # Type checking
```

#### Security:
```bash
uv run bandit -r fastmcp_langchain_adaptor/  # Security linting
uv run safety check                          # Vulnerability check
```

#### Pre-commit:
```bash
uv run pre-commit run --all-files  # Run all pre-commit hooks
```

#### Documentation:
```bash
uv run mkdocs build  # Build docs
uv run mkdocs serve  # Serve docs locally
```

#### Package Management:
```bash
uv build              # Build package
uv publish           # Publish to PyPI
uv run twine check dist/*  # Validate package
```

## Code Style Guidelines

### Imports:
- Always use absolute imports within the package
- Use `from __future__ import annotations` for type hints
- Group imports: standard library, third-party, local imports

### Type Hints:
- Use type hints for all public functions and methods
- Use `Optional[T]` for optional parameters
- Use `Union[A, B]` sparingly, prefer Union types with `|` when Python 3.10+
- Use `Any` sparingly and document why it's needed

### Error Handling:
- Use specific exception types
- Always log errors with context
- Don't expose internal details in user-facing error messages
- Use `logger.exception()` for unexpected errors

### Testing:
- Use descriptive test names: `test_should_convert_mcp_tools_when_valid_input_provided`
- Group related tests in classes
- Use fixtures for shared test data
- Test both success and error paths
- Mock external dependencies

### Documentation:
- Use Google-style docstrings
- Include examples in docstrings for complex functions
- Document all parameters and return values
- Add type information in docstrings when helpful

### Async Code:
- Prefer `async`/`await` over callbacks
- Use `asyncio.gather()` for concurrent operations
- Handle `CancelledError` appropriately
- Use context managers (`async with`) for resources

### Security:
- Never log sensitive information
- Validate all inputs
- Use parameterized queries/statements
- Handle authentication/authorization properly
- Use secure defaults

### Performance:
- Use generators for large data sets
- Cache expensive computations when appropriate
- Profile code for performance bottlenecks
- Use appropriate data structures

## Project Structure

```
fastmcp_langchain_adaptor/
├── __init__.py              # Public API exports
├── tools.py                 # Main conversion logic
tests/
├── __init__.py
├── conftest.py             # Test fixtures
├── test_tools.py           # Unit tests
└── test_integration.py     # Integration tests
scripts/
└── validate_package.py     # Package validation
```

## Common Patterns

### Function Structure:
```python
async def function_name(
    required_param: Type,
    *,
    optional_param: Optional[Type] = None,
) -> ReturnType:
    """
    Brief description.
    
    Args:
        required_param: Description.
        optional_param: Description.
    
    Returns:
        Description of return value.
    
    Raises:
        SpecificError: When this happens.
    """
    # Input validation
    if not required_param:
        raise ValueError("required_param cannot be empty")
    
    # Main logic with error handling
    try:
        # Implementation
        pass
    except SomeSpecificError as e:
        logger.error(f"Context about error: {e}")
        raise
```

### Testing Pattern:
```python
class TestFeature:
    """Tests for Feature functionality."""

    def test_should_succeed_when_valid_input(self, fixture):
        """Test successful operation with valid input."""
        # Arrange
        input_data = create_test_data()
        
        # Act
        result = function_under_test(input_data)
        
        # Assert
        assert result.expected_property == expected_value

    def test_should_raise_error_when_invalid_input(self):
        """Test error handling with invalid input."""
        with pytest.raises(ExpectedError, match="expected error message"):
            function_under_test(invalid_input)
```

## Commit Messages

Use Conventional Commits:
- `feat: add new MCP tool conversion feature`
- `fix: handle malformed JSON responses gracefully`  
- `docs: update README with uv instructions`
- `test: add comprehensive error handling tests`
- `refactor: improve type safety in schema conversion`
- `chore: update dependencies to latest versions`

## When Suggesting Code Changes

1. **Always use `uv` commands** in documentation, scripts, and examples
2. **Include comprehensive error handling** with proper logging
3. **Add type hints** to all function signatures
4. **Write corresponding tests** for new functionality
5. **Update documentation** when changing public APIs
6. **Follow the existing code style** and patterns
7. **Consider security implications** of any changes
8. **Use async/await** for I/O operations
9. **Validate inputs** at function boundaries
10. **Log important events** for debugging and monitoring
