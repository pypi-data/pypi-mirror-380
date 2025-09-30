# Contributing to FastMCP LangChain Adaptor

Thank you for your interest in contributing to FastMCP LangChain Adaptor! We welcome contributions from the community.

## Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastmcp-langchain-adaptor.git
   cd fastmcp-langchain-adaptor
   ```

3. Install the package in development mode with all dependencies:
   ```bash
   uv sync --dev
   ```

4. Install pre-commit hooks:
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

### Running Tests

Run the full test suite:
```bash
uv run pytest
```

Run tests with coverage:
```bash
uv run pytest --cov=fastmcp_langchain_adaptor --cov-report=html
```

Run specific test files:
```bash
uv run pytest tests/test_tools.py -v
```

### Code Quality

We use several tools to maintain code quality:

**Format code with Black:**
```bash
uv run black .
```

**Lint with Ruff:**
```bash
uv run ruff check .
uv run ruff check . --fix  # Auto-fix issues
```

**Type checking with MyPy:**
```bash
uv run mypy fastmcp_langchain_adaptor/
```

**Security scanning with Bandit:**
```bash
uv run bandit -r fastmcp_langchain_adaptor/
```

**Check for known vulnerabilities:**
```bash
uv run safety check
```

### Pre-commit Hooks

We use pre-commit to run checks automatically:
```bash
uv run pre-commit run --all-files
```

## Code Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python style guide
- Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Maximum line length: 88 characters (Black's default)
- Use type hints for all public APIs
- Add comprehensive logging for debugging

### Example Function Documentation:
```python
def mcp_to_langchain(
    tools: List[McpTool],
    *,
    client: Client,
    progress_formatter: Optional[Callable[[Dict[str, Any]], str]] = None,
) -> List[StructuredTool]:
    """
    Convert a list of FastMCP tool descriptors into LangChain StructuredTools.

    Args:
        tools: The descriptors returned by `await client.list_tools()`.
        client: The FastMCP client you created (already configured with elicitation/progress).
        progress_formatter: Optional function to format progress events before sending to LC callbacks.

    Returns:
        List of LangChain StructuredTools.

    Raises:
        ValueError: If tools list is malformed.
        ConnectionError: If client cannot connect to MCP server.
    """
```

## Testing Guidelines

- Write tests for all new functionality
- Aim for >90% code coverage
- Use descriptive test names
- Group related tests in classes
- Use fixtures for common test data
- Test both success and error cases
- Use mocks for external dependencies

### Test Structure:
```python
class TestFeatureName:
    """Tests for FeatureName functionality."""

    def test_success_case(self, mock_dependency):
        """Test the main success scenario."""
        # Arrange
        # Act
        # Assert

    def test_error_case(self, mock_dependency):
        """Test error handling."""
        # Test exception scenarios
```

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Write code following our style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Run all checks locally:**
   ```bash
   uv run pytest
   uv run black .
   uv run ruff check .
   uv run mypy fastmcp_langchain_adaptor/
   uv run pre-commit run --all-files
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **PR Requirements:**
   - Clear description of changes
   - Link to related issues
   - All checks must pass
   - Code review approval required

## Commit Message Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `chore:` Maintenance tasks

Examples:
```
feat: add support for custom progress formatters
fix: handle malformed JSON responses gracefully
docs: update README with new examples
test: add comprehensive edge case tests
```

## Reporting Issues

When reporting issues:

1. Use GitHub Issues
2. Include Python version, package version
3. Provide minimal reproduction case
4. Include relevant error messages/stack traces
5. Describe expected vs actual behavior

## Security

- Never commit secrets or credentials
- Report security vulnerabilities privately to security@[domain].com
- Follow our security policy in SECURITY.md

## Questions?

- Check existing issues and discussions
- Ask questions in GitHub Discussions
- Join our community chat (if available)

Thank you for contributing! 🚀
