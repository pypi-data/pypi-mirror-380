# ASTODOJO: Intelligent TODO Scanner for Python Codebases

[![Tests](https://img.shields.io/badge/tests-34%20passed-brightgreen)](https://github.com/seanmcdonald/astodojo)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

ASTODOJO is an intelligent TODO scanner that goes beyond simple grep searches. Using Python's AST (Abstract Syntax Tree) parsing, it understands your code structure and provides contextual information about TODO items, function names, and class hierarchies.

**✨ NEW: Automatic GitHub Authentication Setup** - When you try GitHub features without authentication, ASTODOJO automatically opens your browser to guide you through token creation!

**🎯 Perfect for AI Coding Assistants** - Designed with machine-readable outputs and agent-friendly workflows. Includes `ASTODOJO-AGENT-HELPER.md` for AI agent guidance.

## 🎯 Features

- **AST-Powered Scanning**: Uses Python's AST to understand code structure and context
- **Rich Taxonomy**: Supports multiple tag types (TODO, BLAME, DEV-CRUFT, PAY-ATTENTION, BUG)
- **Multiple Output Formats**: Tree view (colored), JSON, and summary reports
- **Smart Filtering**: Configurable exclude patterns and intelligent defaults
- **GitHub Integration**: Sync TODO items to GitHub issues with controlled batching
- **🔐 Automatic Auth Setup**: Opens browser automatically when GitHub authentication is needed
- **Caching**: Efficient scanning with local caching to avoid redundant work
- **Configuration**: Project-specific settings via `.astodojorc` files

## 🚀 Quick Start

### Installation

#### From PyPI (Recommended)
```bash
pip install astodojo
```

#### From Source (Development)
```bash
# Clone the repository
git clone https://github.com/seanmcdonald/astodojo.git
cd astodojo

# Install in development mode
pip install -e .
```

#### Verify Installation
```bash
astodojo --version
astodojo --help

# AI agents: Check the agent helper guide
cat $(python -c "import astodojo; import os; print(os.path.join(os.path.dirname(astodojo.__file__), 'ASTODOJO-AGENT-HELPER.md'))")
```

### Basic Usage

#### Scanning Files and Directories

```bash
# Scan current directory recursively
astodojo scan

# Scan a specific file
astodojo scan my_file.py

# Scan a specific directory
astodojo scan src/

# Scan with custom exclude patterns
astodojo scan --exclude "**/tests/**" --exclude "**/*.test.py" --exclude "**/venv/**"
```

#### Output Formats

```bash
# Tree view (default, human-readable)
astodojo scan

# JSON format (machine-readable)
astodojo scan --format json

# Summary report
astodojo scan --format report

# Save output to file
astodojo scan --format json > todos.json
```

#### Practical Examples

```bash
# Quick overview of current codebase
astodojo scan --format report

# Find all BLAME tags that need human review
astodojo scan | grep "\[BLAME\]"

# Check a specific module for TODOs
astodojo scan my_module.py

# Get machine-readable output for scripts
astodojo scan --format json | jq '.[] | select(.tag == "BLAME")'
```

### Tag Types

ASTODOJO recognizes these special comment tags:

```python
# TODO: Implement this feature
# BLAME: This code needs human review
# DEV-CRUFT: Remove this temporary code
# PAY-ATTENTION: Critical implementation detail
# BUG: This causes a runtime error
```

Tags work in both regular comments and docstrings:

```python
def my_function():
    """
    This function does something important.

    TODO: Add proper error handling here
    BLAME: Review the security implications
    """
    pass
```

## 🎨 Output Formats

### Tree View (Default)
```
📋 ASTODOJO Scan Results
├── 📄 src/main.py
│   ├── [TODO] Implement user authentication (line 15)
│   │   in function login_user
│   └── [BLAME] Security vulnerability here (line 42)
│       in class AuthHandler in function validate_token
└── 📄 src/utils.py
    └── [DEV-CRUFT] Remove debug logging (line 23)
```

### JSON Format
```bash
astodojo scan --format json
```

```json
[
  {
    "file_path": "src/main.py",
    "line_number": 15,
    "tag": "TODO",
    "content": "Implement user authentication",
    "parent_function": "login_user",
    "parent_class": null
  }
]
```

### Report Format
```bash
astodojo scan --format report
```

```
📊 ASTODOJO Report
========================================

📈 Summary:
- Total TODO items: 5
- Files with TODOs: 3

🏷️  By Tag Type:
  TODO: 3
  BLAME: 1
  DEV-CRUFT: 1

📁 Files with most TODOs:
  src/main.py: 2
  src/utils.py: 2
  tests/test_auth.py: 1
```

## ⚙️ Configuration

### Project Configuration

Initialize ASTODOJO in your project:

```bash
astodojo init
```

This creates a `.astodojorc` configuration file:

```yaml
# Default output format
output_format: tree

# Exclude patterns (glob syntax)
exclude_patterns:
  - "**/__pycache__/**"
  - "**/*.pyc"
  - "**/.git/**"
  - "**/.pytest_cache/**"
  - "**/.tox/**"
  - "**/venv/**"
  - "**/env/**"
  - "**/node_modules/**"
  - "**/dist/**"
  - "**/build/**"

# Custom colors for tag types
colors:
  TODO: blue
  BLAME: red
  DEV-CRUFT: yellow
  PAY-ATTENTION: purple
  BUG: red

# GitHub integration (optional)
github_token: your_token_here
github_repo: owner/repo
```

### Environment Variables

```bash
# GitHub integration
export GITHUB_TOKEN=your_github_token
export GITHUB_REPOSITORY=owner/repo
```

## 🔗 GitHub Integration

ASTODOJO can sync TODO items to GitHub issues, with special handling for `BLAME` tags that require human review.

### 🔐 Automatic Authentication Setup

**NEW**: ASTODOJO now guides you through GitHub authentication automatically!

When you run GitHub commands without authentication, ASTODOJO will:

1. **Automatically open your browser** to GitHub's token creation page
2. **Show step-by-step instructions** for creating a Personal Access Token
3. **Guide you through configuration** with environment variables or config files

Simply run `astodojo github-report` and follow the prompts!

### Manual Setup (Alternative)

If you prefer to set up authentication manually:

1. Create a GitHub Personal Access Token with `repo` scope at: https://github.com/settings/tokens
2. Set environment variables or configure in `.astodojorc`:

```bash
export GITHUB_TOKEN=ghp_your_token_here
export GITHUB_REPOSITORY=yourusername/yourrepo
```

### Generate Sync Report

```bash
# Check what needs to be synced
astodojo github-report

# Check specific directory
astodojo github-report src/
```

This shows what needs to be synced:

```
📊 ASTODOJO GitHub Sync Report
========================================
📋 Current TODOs: 5
🆕 New TODOs: 2
🔄 Changed TODOs: 0
🚨 TODOs needing issues: 1
📋 Existing GitHub issues: 3

🔧 Recommended Actions:
  • Create issue for BLAME in src/auth.py:42
    "Security vulnerability in token validation"
```

### Sync to GitHub

```bash
# Sync BLAME tags (requires human review)
astodojo github-sync --tag BLAME

# Sync TODO items from specific directory
astodojo github-sync src/ --tag TODO

# Sync limited number of items at once
astodojo github-sync --tag BLAME --count 1

# Dry run first (shows what would be synced)
astodojo github-report
```

### GitHub Workflow Examples

```bash
# Before code review: Check for BLAME tags
astodojo scan --format report | grep BLAME

# Create issues for code that needs human review
astodojo github-sync --tag BLAME --count 3

# Regular maintenance: Sync remaining TODOs
astodojo github-sync --tag TODO --count 5

# Check sync status
astodojo github-report
```

### How It Works

- **Caching**: Local cache (`.astodojo/cache.json`) stores scan results and GitHub issues
- **Controlled Sync**: Only syncs items one at a time to respect rate limits
- **Smart Mapping**: Matches TODO items to existing issues based on file path and content
- **Rich Issues**: Created issues include links back to source code and contextual information

## 🏗️ Architecture

### Core Components

- **`astodojo.core`**: AST-based scanner and TODO extraction
- **`astodojo.config`**: Configuration management
- **`astodojo.cli`**: Command-line interface
- **`astodojo.github`**: GitHub API integration, caching, and authentication setup

### Design Philosophy

1. **Agent-Friendly**: Designed for AI coding assistants with machine-readable outputs
2. **Safe Defaults**: Conservative exclude patterns and controlled GitHub operations
3. **Composable**: Modular design allows extending functionality
4. **Fast**: AST parsing is efficient, caching prevents redundant work

## 🧪 Development

### Prerequisites

- Python 3.8+
- Git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/astodojo.git
cd astodojo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest pytest-cov build twine
```

### Running Tests

```bash
# Run the complete autopilot test suite (recommended)
python3 run_autopilot.py

# Run individual test suites
pytest tests/                    # Unit tests
pytest tests/test_core.py       # Core functionality tests
pytest tests/test_github.py     # GitHub integration tests

# Run with coverage
pytest --cov=astodojo --cov-report=html
open htmlcov/index.html  # View coverage report

# Run specific test
pytest tests/test_core.py::TestASTODOJO::test_scan_file_with_todo_comments -v
```

### Code Quality

```bash
# Format code
black astodojo/ tests/ test/

# Lint code
flake8 astodojo/ tests/ test/

# Type checking
mypy astodojo/
```

### Building and Publishing

```bash
# Build package
python -m build

# Test on TestPyPI first
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*

# See HOW-TO-PUBLISH-PACKAGE.md for detailed instructions
```

## 📋 Tag Taxonomy Reference

| Tag | Purpose | Color | GitHub Sync |
|-----|---------|-------|-------------|
| `TODO` | General task to be done | Blue | Optional |
| `BLAME` | Requires human review | Red | Automatic |
| `DEV-CRUFT` | Temporary code to remove | Yellow | Optional |
| `PAY-ATTENTION` | Critical implementation detail | Purple | Optional |
| `BUG` | Confirmed bug | Red | Optional |

## 🤝 Contributing

We welcome contributions! ASTODOJO is designed to be a community-driven tool for improving code quality and developer workflows.

### Ways to Contribute

- **🐛 Bug Reports**: Found a bug? [Open an issue](https://github.com/yourusername/astodojo/issues)
- **💡 Feature Requests**: Have an idea? [Start a discussion](https://github.com/yourusername/astodojo/discussions)
- **📝 Documentation**: Help improve docs, examples, or tutorials
- **🧪 Testing**: Add tests for new features or edge cases
- **🔧 Code**: Submit pull requests for bug fixes or new features

### Development Workflow

1. **Fork and Clone**
   ```bash
   git clone https://github.com/yourusername/astodojo.git
   cd astodojo
   ```

2. **Set up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed
   - Run the full test suite: `python3 run_autopilot.py`

5. **Submit a Pull Request**
   - Ensure all tests pass
   - Update CHANGELOG.md if applicable
   - Provide a clear description of changes

### Guidelines

- **Tests**: All new features must include comprehensive tests
- **Documentation**: Update README.md and docstrings for API changes
- **Compatibility**: Maintain Python 3.8+ compatibility
- **Performance**: Consider performance implications for large codebases
- **Security**: Be mindful of security when handling tokens or sensitive data

### Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

### Getting Help

- **📖 Documentation**: Check this README and HOW-TO-PUBLISH-PACKAGE.md
- **💬 Discussions**: Use [GitHub Discussions](https://github.com/yourusername/astodojo/discussions) for questions
- **🐛 Issues**: Report bugs or request features via [GitHub Issues](https://github.com/yourusername/astodojo/issues)

## 📊 Project Status

### ✅ Current Version: 0.1.0

**All planned features implemented and tested:**
- ✅ AST-powered scanning with context awareness
- ✅ Rich tag taxonomy (TODO, BLAME, DEV-CRUFT, PAY-ATTENTION, BUG)
- ✅ Multiple output formats (tree, json, report)
- ✅ Smart filtering and configuration
- ✅ GitHub integration with automatic authentication
- ✅ Comprehensive test suite (34 automated tests)
- ✅ Python package ready for PyPI publication

### 🔮 Roadmap

- **v0.2.0**: Enhanced GitHub integration, webhook support
- **v0.3.0**: IDE integrations, VS Code extension
- **v1.0.0**: Stable API, enterprise features

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/seanmcdonald/astodojo.git
cd astodojo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
./venv/bin/python -m pytest tests/ -v

# Test installation
./test_astodojo_install.sh
```

### Releasing

To release a new version:

```bash
# Use the automated release script
./release_to_pypi.sh

# Or follow the manual process in RELEASE.md
```

See [RELEASE.md](RELEASE.md) for detailed release instructions.

> **Note:** GitHub Actions CI/CD workflows are currently disabled while we conduct further testing before enabling automated publishing. Use the manual release process documented above.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

**ASTODOJO** was born from the need for more intelligent code analysis tools that understand context and structure, not just text patterns. Special thanks to:

- **Python AST**: For making code structure analysis possible
- **Rich Library**: For beautiful terminal output
- **The Python Community**: For inspiring this tool
- **AI Coding Assistants**: For the vision of agent-friendly development tools

Built with the goal of making code review and maintenance more efficient for both humans and AI assistants. This project demonstrates how modern development tools can bridge the gap between traditional coding practices and AI-assisted workflows.
