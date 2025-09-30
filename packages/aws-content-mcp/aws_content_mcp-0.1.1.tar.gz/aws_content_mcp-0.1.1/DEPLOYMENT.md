# Deployment and Publishing Guide

This guide covers how to build, test, and publish the AWS Content MCP Server to PyPI for public use.

## Prerequisites

1. **Python 3.8+** installed
2. **Build tools** installed:
   ```bash
   pip install build twine
   ```
3. **PyPI account** created at https://pypi.org
4. **API token** generated from PyPI account settings

## Development Setup

### 1. Clone and Setup Environment

```bash
git clone https://github.com/yourusername/aws-content-mcp.git
cd aws-content-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=aws_content_mcp

# Run specific test file
pytest tests/test_server.py -v
```

### 3. Code Quality Checks

```bash
# Format code
black src/
isort src/

# Type checking
mypy src/

# Lint code
flake8 src/
```

## Building the Package

### 1. Update Version

Update version in `pyproject.toml`:

```toml
[project]
name = "aws-content-mcp"
version = "0.1.1"  # Increment version
```

### 2. Build Distribution

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build package
python -m build
```

This creates:
- `dist/aws_content_mcp-0.1.1-py3-none-any.whl` (wheel)
- `dist/aws-content-mcp-0.1.1.tar.gz` (source distribution)

### 3. Verify Build

```bash
# Check package contents
tar -tzf dist/aws-content-mcp-0.1.1.tar.gz

# Test installation from wheel
pip install dist/aws_content_mcp-0.1.1-py3-none-any.whl
```

## Testing Before Publishing

### 1. Test Local Installation

```bash
# Install from local build
pip install dist/aws_content_mcp-0.1.1-py3-none-any.whl

# Test the command
aws-content-mcp --help

# Test as MCP server (in another terminal)
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}' | aws-content-mcp
```

### 2. Test with uvx

```bash
# Test uvx installation from local wheel
uvx --from ./dist/aws_content_mcp-0.1.1-py3-none-any.whl aws-content-mcp
```

### 3. Integration Testing

Create a test MCP configuration:

```json
{
  "mcpServers": {
    "aws-content-test": {
      "command": "python",
      "args": ["-m", "aws_content_mcp.server"],
      "cwd": "/path/to/aws-content-mcp"
    }
  }
}
```

## Publishing to PyPI

### 1. Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ aws-content-mcp
```

### 2. Publish to PyPI

```bash
# Upload to PyPI
python -m twine upload dist/*

# Enter your PyPI credentials or use API token
```

### 3. Verify Publication

```bash
# Install from PyPI
pip install aws-content-mcp

# Test uvx installation
uvx aws-content-mcp
```

## Post-Publication

### 1. Create GitHub Release

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v0.1.1`
4. Release title: `AWS Content MCP Server v0.1.1`
5. Describe changes and improvements
6. Attach the built wheel and source distribution

### 2. Update Documentation

Update README.md with:
- Installation instructions
- New features
- Breaking changes
- Usage examples

### 3. Announce Release

Consider announcing on:
- GitHub Discussions
- Python community forums
- AWS community channels
- Social media

## Continuous Integration (GitHub Actions)

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"
    
    - name: Run tests
      run: |
        pytest --cov=aws_content_mcp
    
    - name: Lint
      run: |
        black --check src/
        isort --check-only src/
        mypy src/

  publish:
    needs: test
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags/')
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: "3.11"
    
    - name: Install build dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

## Version Management

### Semantic Versioning

Follow semantic versioning (semver):
- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.1.0): New features, backward compatible
- **PATCH** (0.0.1): Bug fixes, backward compatible

### Release Process

1. **Development**: Work on `develop` branch
2. **Feature branches**: Create for new features
3. **Release preparation**: 
   - Update version in `pyproject.toml`
   - Update CHANGELOG.md
   - Create release branch
4. **Testing**: Thorough testing on release branch
5. **Merge**: Merge to `main` and tag release
6. **Publish**: Automated via GitHub Actions

## Monitoring and Maintenance

### 1. Monitor PyPI Downloads

- Check download statistics on PyPI
- Monitor for issues reported by users
- Track GitHub issues and discussions

### 2. Dependency Updates

Regularly update dependencies:

```bash
# Check for outdated packages
pip list --outdated

# Update dependencies in pyproject.toml
# Test thoroughly after updates
```

### 3. Security Updates

- Monitor security advisories
- Update vulnerable dependencies promptly
- Consider using tools like `safety`:

```bash
pip install safety
safety check
```

## Troubleshooting

### Common Issues

1. **Import errors**: Check package structure and `__init__.py` files
2. **Missing dependencies**: Verify `pyproject.toml` dependencies
3. **Version conflicts**: Use virtual environments
4. **Build failures**: Check Python version compatibility

### Debug Commands

```bash
# Check package metadata
python -m pip show aws-content-mcp

# Verify entry points
python -c "import pkg_resources; print(list(pkg_resources.iter_entry_points('console_scripts')))"

# Test import
python -c "from aws_content_mcp import server; print('Import successful')"
```

## Best Practices

1. **Always test locally** before publishing
2. **Use TestPyPI** for testing releases
3. **Keep dependencies minimal** and up-to-date
4. **Document breaking changes** clearly
5. **Provide migration guides** for major updates
6. **Respond to user issues** promptly
7. **Maintain backward compatibility** when possible

This deployment guide ensures your AWS Content MCP Server can be reliably built, tested, and published for public use via PyPI and uvx.