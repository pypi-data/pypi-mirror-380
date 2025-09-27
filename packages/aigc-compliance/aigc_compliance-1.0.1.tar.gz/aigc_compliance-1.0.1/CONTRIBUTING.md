# Contributing to AIGC Compliance Python SDK

Thank you for your interest in contributing to the AIGC Compliance Python SDK! This document provides guidelines for contributing to this project.

## 🚀 Quick Start for Contributors

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Git

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/aigc-compliance/python-sdk.git
   cd python-sdk
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Development Dependencies**
   ```bash
   pip install -e .
   pip install pytest pytest-cov black flake8 mypy
   ```

4. **Run Tests**
   ```bash
   pytest tests/ -v --cov=aigc_compliance
   ```

## 🧪 Testing

### Running Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=aigc_compliance --cov-report=html

# Specific test file
pytest tests/test_client.py -v

# Integration tests (requires API key)
AIGC_API_KEY=your_test_key pytest tests/test_integration.py
```

### Writing Tests
- Place tests in the `tests/` directory
- Follow the pattern: `test_*.py`
- Mock external API calls using `pytest-mock`
- Aim for >90% code coverage

Example test:
```python
import pytest
from unittest.mock import Mock, patch
from aigc_compliance import ComplianceClient
from aigc_compliance.exceptions import ComplianceAuthenticationError

def test_client_initialization():
    client = ComplianceClient("test_key")
    assert client.api_key == "test_key"

@patch('aigc_compliance.client.requests.post')
def test_comply_success(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {"compliant": True}
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    
    client = ComplianceClient("test_key")
    result = client.comply("test.jpg")
    
    assert result["compliant"] is True
```

## 🎨 Code Style

### Python Style Guide
We follow PEP 8 with these specifics:

```bash
# Format code
black .

# Check style
flake8 aigc_compliance/ tests/

# Type checking
mypy aigc_compliance/
```

### Code Standards
- **Line Length**: 88 characters (Black default)
- **Imports**: Use `isort` for import sorting
- **Docstrings**: Google style docstrings
- **Type Hints**: Required for all public functions
- **Naming**: Snake_case for functions/variables, PascalCase for classes

Example:
```python
from typing import Optional, Dict, Any
import requests

def comply(
    self, 
    file_path: str, 
    region: str = "EU",
    watermark_position: Optional[str] = None
) -> Dict[str, Any]:
    """Process image for AI detection and compliance watermarking.
    
    Args:
        file_path: Path to the image file to process.
        region: Compliance region ("EU" or "CN").
        watermark_position: Position for watermark placement.
        
    Returns:
        Dictionary containing compliance results.
        
    Raises:
        ComplianceAuthenticationError: If API key is invalid.
        ComplianceQuotaExceededError: If quota is exceeded.
    """
```

## 🐛 Bug Reports

### Before Submitting
1. Check existing issues
2. Update to the latest version
3. Test with minimal reproduction case

### Bug Report Template
```markdown
**Describe the Bug**
A clear description of what the bug is.

**Reproduction Steps**
1. Initialize client with '...'
2. Call method '...'
3. See error

**Expected Behavior**
What you expected to happen.

**Environment**
- Python version: [e.g., 3.9.0]
- SDK version: [e.g., 1.0.1]
- OS: [e.g., Ubuntu 20.04]

**Code Sample**
```python
from aigc_compliance import ComplianceClient
client = ComplianceClient("your_key")
# Minimal code that reproduces the issue
```
```

## 🚀 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
Clear description of the feature you'd like to see.

**Use Case**
Explain why this feature would be useful.

**Proposed Implementation**
If you have ideas about how to implement this.

**API Design**
```python
# How you envision the API looking
client.new_method(param1="value1")
```
```

## 📝 Pull Requests

### PR Checklist
- [ ] Tests pass (`pytest`)
- [ ] Code formatted (`black .`)
- [ ] Linting passes (`flake8`)
- [ ] Type checking passes (`mypy`)
- [ ] Documentation updated
- [ ] Changelog entry added
- [ ] Tests added for new functionality

### PR Process
1. **Fork** the repository
2. **Create branch**: `git checkout -b feature/your-feature-name`
3. **Make changes** with tests
4. **Run quality checks**:
   ```bash
   black .
   flake8 .
   mypy aigc_compliance/
   pytest
   ```
5. **Commit** with clear messages
6. **Push** and create PR

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add batch processing support
fix: handle network timeout errors properly
docs: update API reference for new parameters
test: add integration tests for EU region
refactor: simplify error handling logic
```

## 🏗️ Project Structure

```
python-sdk/
├── aigc_compliance/          # Main package
│   ├── __init__.py          # Package exports
│   ├── client.py            # Main client class
│   ├── exceptions.py        # Custom exceptions
│   └── models.py            # Data models
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_client.py       # Client tests
│   ├── test_exceptions.py   # Exception tests
│   └── test_integration.py  # Integration tests
├── docs/                    # Documentation
├── examples/                # Usage examples
├── pyproject.toml          # Package configuration
├── README.md               # Main documentation
├── CHANGELOG.md            # Version history
└── CONTRIBUTING.md         # This file
```

## 🔄 Release Process

### Version Management
We use [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)  
- **PATCH**: Bug fixes

### Release Checklist
1. Update `CHANGELOG.md`
2. Bump version in `pyproject.toml`
3. Run full test suite
4. Create release PR
5. Tag release: `git tag v1.2.3`
6. Publish to PyPI
7. Update GitHub release notes

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

### Getting Help
- 📖 **Documentation**: Check README and API docs first
- 🐛 **Issues**: Search existing issues before creating new ones
- 💬 **Discussions**: Use GitHub Discussions for questions
- 📧 **Contact**: support@aigc-compliance.com for urgent matters

## 🏆 Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub contributors page
- Release notes for significant contributions
- Annual contributor spotlight

### Contributor Levels
- 🥉 **Bronze**: 1+ merged PR
- 🥈 **Silver**: 5+ merged PRs or major feature
- 🥇 **Gold**: 10+ merged PRs or significant contributions
- 💎 **Diamond**: Core maintainer status

## 📊 Metrics & Goals

### Quality Metrics
- Test coverage: >90%
- Documentation coverage: 100% of public APIs
- Performance: <2s for typical API calls
- Reliability: 99.9% uptime for API integration

### Contribution Goals
- Response time to issues: <48 hours
- PR review time: <7 days
- Release frequency: Monthly minor releases
- Security updates: <24 hours for critical issues

---

Thank you for contributing to AIGC Compliance Python SDK! 🚀

**Questions?** Open a [GitHub Discussion](https://github.com/aigc-compliance/python-sdk/discussions) or contact [support@aigc-compliance.com](mailto:support@aigc-compliance.com).