# Contributing to Sector8 SDK

Thank you for your interest in contributing to the Sector8 SDK! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- pip or conda for package management

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sector8/sector8-sdk.git
   cd sector8-sdk
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

## Development Guidelines

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **ruff** for linting

Run these tools before committing:

```bash
black src/ tests/
isort src/ tests/
mypy src/
ruff check src/ tests/
```

### Testing

We use pytest for testing. Run tests with:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=sector8

# Run specific test file
pytest tests/test_client.py

# Run with verbose output
pytest -v
```

### Type Hints

All new code should include type hints. We use mypy for type checking:

```bash
mypy src/
```

### Documentation

- Update docstrings for any new functions or classes
- Follow Google-style docstrings
- Include type information in docstrings

Example:
```python
def process_data(data: List[str], config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Process the input data according to configuration.
    
    Args:
        data: List of strings to process
        config: Optional configuration dictionary
        
    Returns:
        Dictionary containing processed results
        
    Raises:
        ValueError: If data is empty
    """
```

## Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Run tests and quality checks:**
   ```bash
   pytest
   mypy src/
   black --check src/ tests/
   ruff check src/ tests/
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** with a clear description of your changes

### Commit Message Format

We follow conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for test changes
- `chore:` for maintenance tasks

## Issue Reporting

When reporting issues, please include:

- Python version
- Operating system
- SDK version
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs

## Security

If you discover a security vulnerability, please report it privately to security@sector8.com.

## License

By contributing to Sector8 SDK, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, please:

1. Check the existing documentation
2. Search existing issues
3. Create a new issue with the "question" label

Thank you for contributing to Sector8 SDK! 