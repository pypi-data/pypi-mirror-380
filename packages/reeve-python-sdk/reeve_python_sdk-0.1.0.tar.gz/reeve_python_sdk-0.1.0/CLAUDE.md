# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python SDK for the **Reeve API** - a facial recognition service for person identification and verification. The project is scaffolded with PyScaffold 4.6 and uses a src-layout structure with the main package code in `src/reeve_python_sdk/`.

### Reeve API Features

The SDK provides access to the following Reeve API capabilities:

- **Authentication**: Token-based authentication (Bearer JWT)
- **Person Management**: Create, list, edit, and delete persons
- **Face Management**: Add, list, and delete face images for persons
- **Face Recognition**: Identify unknown faces against enrolled persons
- **Face Verification**:
  - Verify a face against a specific person
  - Compare two faces to determine if they match

API specification is available in `docs/swagger.json`.

## Development Commands

### Testing
```bash
# Run all tests with coverage
pytest

# Run tests with tox (recommended for comprehensive testing)
tox

# Run specific test
pytest tests/test_skeleton.py::test_fib

# Run tests with verbose output and specific markers
pytest -v -k test_name
```

### Building
```bash
# Build the package
tox -e build

# Clean build artifacts
tox -e clean
```

### Documentation
```bash
# Build documentation
tox -e docs

# View documentation locally
python3 -m http.server --directory 'docs/_build/html'
# Then navigate to http://localhost:8000
```

### Installation
```bash
# Install in editable mode for development
pip install -e .

# Install with test dependencies
pip install -e .[testing]
```

## Project Structure

- **src/reeve_python_sdk/**: Main package directory (src-layout pattern)
  - `__init__.py`: Package initialization with version handling via setuptools_scm
  - `skeleton.py`: Template file with example fibonacci function and CLI entry point
- **tests/**: Test directory
  - `conftest.py`: Pytest configuration and fixtures
  - `test_skeleton.py`: Example tests for the skeleton module
- **docs/**: Sphinx documentation
- **setup.cfg**: Main configuration file for package metadata, dependencies, and tool settings
- **pyproject.toml**: Build system configuration using setuptools_scm
- **tox.ini**: Test automation configuration

## Architecture Notes

### SDK Structure
The SDK is built with an async-first architecture using aiohttp:

- **client.py**: Base async HTTP client with authentication and error handling
- **exceptions.py**: Custom exception hierarchy for different error types
- **models.py**: Data models (Person, APIResponse) with serialization
- **auth.py**: Authentication module for token management
- **person.py**: Person CRUD operations
- **face.py**: Face management, recognition, and verification
- **subject.py**: Direct face-to-face comparison
- **__init__.py**: Main ReeveClient that combines all modules

### Usage Pattern
All operations are async and use context managers:
```python
async with ReeveClient(api_url="...", api_key="...") as client:
    person = await client.person.add(firstname="John", lastname="Doe")
    faces = await client.face.list(person_id=person["id"])
```

### Version Management
The project uses `setuptools_scm` for automatic version management based on git tags. Version scheme is set to "no-guess-dev" which means development versions are derived from git history.

### Testing Configuration
- Uses pytest-asyncio for async test support
- aioresponses for mocking HTTP calls
- pytest is configured in `setup.cfg` under `[tool:pytest]`
- Coverage reporting is enabled by default (`--cov reeve_python_sdk --cov-report term-missing`)
- Test paths are configured to `tests/` directory

### Code Style
- flake8 configuration in `setup.cfg` with max line length of 88 (Black-compatible)
- Extends ignore for E203, W503 (Black edge cases)

### Dependencies
- **aiohttp**: Async HTTP client for API calls
- **aiofiles**: Async file operations
- **python-dateutil**: DateTime parsing for API responses
- **pytest-asyncio**: Async testing support
- **aioresponses**: HTTP mocking for tests

## Important Conventions

- Never commit changes without running tests first
- Use tox for running tests to ensure consistency across environments
- Documentation uses reStructuredText format
