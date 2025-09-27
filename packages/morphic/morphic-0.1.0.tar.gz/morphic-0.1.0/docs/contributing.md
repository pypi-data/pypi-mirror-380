# Contributing

Thank you for your interest in contributing to Morphic! This guide will help you get started with contributing to the project.

## Development Setup

### Prerequisites

- Python 3.10.9 or higher
- Git
- A GitHub account

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/morphic.git
   cd morphic
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

5. **Verify the setup** by running tests:
   ```bash
   pytest
   ```

## Development Workflow

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Write or update tests** for your changes

4. **Run the test suite**:
   ```bash
   pytest
   ```

5. **Check code quality**:
   ```bash
   # Format code
   black src/ tests/

   # Lint code
   ruff check src/ tests/

   # Type checking
   mypy src/
   ```

6. **Update documentation** if needed

7. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

8. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a pull request** on GitHub

## Coding Standards

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **Ruff** for linting
- **mypy** for static type checking

Configuration for these tools is in `pyproject.toml`.

### Code Guidelines

1. **Follow PEP 8** style guidelines
2. **Use type hints** for all public APIs
3. **Write comprehensive docstrings** using Google style
4. **Keep functions small** and focused
5. **Use meaningful variable names**
6. **Add comments** for complex logic

### Example Code Style

```python
from typing import Optional, Dict, Any
from morphic import Registry

class ExampleService:
    """An example service demonstrating coding standards.

    This class shows how to structure code according to Morphic's
    coding standards and conventions.

    Args:
        config: Configuration dictionary for the service
        debug: Whether to enable debug logging
    """

    def __init__(self, config: Dict[str, Any], debug: bool = False) -> None:
        self.config = config
        self.debug = debug
        self._initialized = False

    def initialize(self) -> bool:
        """Initialize the service with the provided configuration.

        Returns:
            True if initialization was successful, False otherwise.

        Raises:
            ValueError: If configuration is invalid.
        """
        if not self.config:
            raise ValueError("Configuration cannot be empty")

        self._initialized = True
        return True

    def process_data(self, data: Optional[str] = None) -> Optional[str]:
        """Process the provided data.

        Args:
            data: The data to process. If None, returns None.

        Returns:
            The processed data, or None if input was None.
        """
        if data is None:
            return None

        # Process the data
        processed = data.upper() if self.debug else data.lower()
        return processed
```

## Testing Guidelines

### Writing Tests

1. **Use pytest** as the testing framework
2. **Write tests for all public APIs**
3. **Include both positive and negative test cases**
4. **Use descriptive test names**
5. **Keep tests independent** and isolated
6. **Use fixtures** for common setup

### Test Structure

```python
import pytest
from morphic import Registry

class TestRegistry:
    """Test cases for Registry functionality."""

    def test_register_class_with_decorator(self):
        """Test registering a class using the decorator."""
        class TestClass(Registry):
            pass

        assert Registry.get_subclass("TestClass", raise_error=False) is TestClass

    def test_create_instance_with_factory(self):
        """Test creating instances using the factory method."""
        class TestClass(Registry):
            def __init__(self, value: int):
                self.value = value

        instance = Registry.of("TestClass", value=42)
        assert isinstance(instance, TestClass)
        assert instance.value == 42

    def test_factory_raises_for_unregistered_class(self):
        """Test that factory raises KeyError for unregistered classes."""
        with pytest.raises(KeyError):
            Registry.of("UnregisteredClass")
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=morphic

# Run specific test file
pytest tests/test_registry.py

# Run specific test
pytest tests/test_registry.py::TestRegistry::test_register_class

# Run with verbose output
pytest -v
```

## Documentation

### Docstring Style

We use Google-style docstrings:

```python
def example_function(param1: str, param2: int = 0) -> bool:
    """Example function demonstrating docstring style.

    This function demonstrates how to write proper docstrings
    according to Morphic's documentation standards.

    Args:
        param1: A string parameter with description.
        param2: An optional integer parameter. Defaults to 0.

    Returns:
        True if the operation was successful, False otherwise.

    Raises:
        ValueError: If param1 is empty.
        TypeError: If param2 is not an integer.

    Example:
        >>> result = example_function("hello", 42)
        >>> print(result)
        True
    """
    if not param1:
        raise ValueError("param1 cannot be empty")

    return True
```

### Updating Documentation

1. **API documentation** is generated automatically from docstrings
2. **User guides** are in the `docs/` directory
3. **Update relevant documentation** when adding features
4. **Build documentation locally** to test:
   ```bash
   pip install mkdocs-material "mkdocstrings[python]"
   mkdocs serve
   ```

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass**
2. **Update documentation** if needed
3. **Add/update tests** for your changes
4. **Follow coding standards**
5. **Write a clear commit message**

### Pull Request Guidelines

1. **Use a descriptive title**
2. **Provide a detailed description** of changes
3. **Reference related issues** if applicable
4. **Include screenshots** for UI changes
5. **Keep PRs focused** and atomic

### PR Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated existing tests as needed

## Checklist
- [ ] Code follows the project's coding standards
- [ ] Self-review of the code has been performed
- [ ] Comments have been added to complex code sections
- [ ] Documentation has been updated
- [ ] No new warnings introduced
```

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior**
4. **Actual behavior**
5. **Environment information** (Python version, OS, etc.)
6. **Code example** that demonstrates the issue

### Feature Requests

For feature requests, please include:

1. **Clear description** of the feature
2. **Use case** and motivation
3. **Proposed implementation** (if you have ideas)
4. **Examples** of how it would be used

## Code Review Process

### For Contributors

1. **Be responsive** to feedback
2. **Make requested changes** promptly
3. **Ask questions** if feedback is unclear
4. **Keep discussions professional** and constructive

### Review Criteria

Code reviews will check for:

1. **Correctness** and functionality
2. **Code quality** and style adherence
3. **Test coverage** and quality
4. **Documentation** completeness
5. **Performance** implications
6. **Breaking changes** and compatibility

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Update documentation
5. Create release PR
6. Tag release after merge
7. Publish to PyPI

## Getting Help

### Communication Channels

- **GitHub Issues** for bug reports and feature requests
- **GitHub Discussions** for general questions and discussions
- **Pull Request comments** for code-related discussions

### Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [pytest Documentation](https://pytest.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)

Thank you for contributing to Morphic! Your contributions help make the library better for everyone.