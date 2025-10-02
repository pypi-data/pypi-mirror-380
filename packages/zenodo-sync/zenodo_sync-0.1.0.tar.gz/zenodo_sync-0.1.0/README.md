# zenodo-sync

[![PyPI version](https://badge.fury.io/py/zenodo-sync.svg)](https://badge.fury.io/py/zenodo-sync)
[![Python Support](https://img.shields.io/pypi/pyversions/zenodo-sync.svg)](https://pypi.org/project/zenodo-sync/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight CLI and Python library to synchronise local research data, results and analysis artifacts with [Zenodo](https://zenodo.org/). Designed for reproducible science and seamless data publishing workflows.

## Status

🚧 **Active Development** - This repository is currently in active development. The core functionality is being implemented and the API may change.

The package is available on PyPI as a placeholder to reserve the name. Full functionality will be available in upcoming releases.

## Features (Planned)

- 📤 **Upload & Publish**: Upload metadata, READMEs, and digital assets from local filesystem to Zenodo
- 📥 **Download**: Download published datasets to local filesystem for reproducible research
- 🔄 **Sync**: Bidirectional synchronization between local directories and Zenodo records
- 🔐 **Authentication**: Secure API token-based authentication with Zenodo
- 🧪 **Sandbox Support**: Test your workflows safely with Zenodo's sandbox environment
- 🎯 **Semantic Versioning**: Built-in support for semantic versioning of your research outputs
- 🐍 **Python API**: Comprehensive Python API for integration into existing workflows
- ⌨️ **CLI Interface**: Easy-to-use command-line interface for quick operations

## Installation

### From PyPI (Recommended)

```bash
pip install zenodo-sync
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/causaliq/zenodo-sync.git
cd zenodo-sync

# Set up development environment (Windows)
scripts\setup-dev.bat

# Set up development environment (Unix/Linux/macOS)
chmod +x scripts/setup-dev.sh
./scripts/setup-dev.sh

# Or manually:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev,test]"
```

## Quick Start

### 1. Get Your Zenodo API Token

1. Visit [Zenodo](https://zenodo.org/) (or [Zenodo Sandbox](https://sandbox.zenodo.org/) for testing)
2. Go to Account Settings → Applications → Personal access tokens
3. Create a new token with appropriate scopes

### 2. Configure Authentication

```bash
# Set environment variable
export ZENODO_TOKEN="your-api-token-here"

# Or create a .env file
cp .env.example .env
# Edit .env and add your token
```

### 3. Use the CLI

```bash
# Upload a file (to sandbox by default)
zenodo-sync upload my-dataset.csv

# Download files from a record
zenodo-sync download 12345 ./downloads/

# Sync a directory with Zenodo
zenodo-sync sync ./my-research-project/
```

### 4. Use the Python API

```python
from zenodo_sync import ZenodoSync

# Initialize (uses sandbox by default for safety)
sync = ZenodoSync(token="your-token", sandbox=True)

# Upload a file
result = sync.upload_file("my-dataset.csv")

# Download files
files = sync.download_file("12345", "./downloads/")

# Sync directory
result = sync.sync_directory("./my-project/")
```

## Configuration

You can configure zenodo-sync using:

1. **Environment variables**:
   - `ZENODO_TOKEN`: Your Zenodo API token
   - `ZENODO_SANDBOX`: Use sandbox (default: true)

2. **Configuration file** (`.env`):
   ```env
   ZENODO_TOKEN=your_token_here
   ZENODO_SANDBOX=true
   ```

3. **Command-line arguments**:
   ```bash
   zenodo-sync --token your-token --production upload file.txt
   ```

## Development

### Requirements

- Python 3.9 or higher
- pip (latest version recommended)

### Development Setup

```bash
# Clone and setup
git clone https://github.com/causaliq/zenodo-sync.git
cd zenodo-sync

# Quick setup using task runner
python tasks.py setup

# Or manual setup
pip install -e ".[dev,test]"
pre-commit install
```

### Running Tests

```bash
# Run all tests with coverage
python tasks.py test

# Quick tests (no coverage)
python tasks.py test-quick

# Or directly with pytest
pytest -v
```

### Code Quality

```bash
# Run all checks (lint, type-check, test)
python tasks.py check

# Format code
python tasks.py format

# Run linting only
python tasks.py lint

# Type checking
python tasks.py type-check
```

### Building and Publishing

```bash
# Build package
python tasks.py build

# Using the build script (Windows)
scripts\build-and-publish.bat

# Manual build and upload
python -m build
twine upload --repository testpypi dist/*  # Test PyPI
twine upload dist/*  # Production PyPI
```

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`python tasks.py check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes and version history.

## Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/causaliq/zenodo-sync/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/causaliq/zenodo-sync/discussions)
- 📚 **Documentation**: [GitHub README](https://github.com/causaliq/zenodo-sync#readme)

## Acknowledgments

- Built for the research community
- Powered by the [Zenodo](https://zenodo.org/) platform
- Inspired by the need for reproducible science

---

**Supported Python Versions**: 3.9, 3.10, 3.11, 3.12  
**Default Python Version**: 3.11
