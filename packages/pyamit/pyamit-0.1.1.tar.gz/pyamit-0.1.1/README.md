# 🔧 pyamit

> A Python CLI tool for formatting and sorting YAML files, perfect for pre-commit hooks

`pyamit` (Pyyamlprecommit) is a fast, reliable tool that formats YAML files with consistent indentation and optional key sorting. Built with Typer and PyYAML, it's designed to integrate seamlessly with pre-commit for automated YAML formatting in your projects.

## ✨ Features

- 🚀 **Fast formatting** - Quick YAML processing with PyYAML
- 🔢 **Key sorting** - Optional alphabetical key sorting
- 📏 **Custom indentation** - Configurable indent levels (default: 2 spaces)
- 🪝 **Pre-commit ready** - Easy integration with pre-commit hooks
- 🧪 **Well tested** - Comprehensive test suite with pytest
- 🎨 **Auto-formatted** - Code linted and formatted with Ruff

## 📦 Installation

### Using uv (recommended)

```bash
uv install
```

### Using pip

```bash
pip install .
```

### For development

```bash
git clone <repository-url>
cd pyamit
uv install --dev
```

## 🚀 Usage

### Basic formatting

```bash
pyamit file1.yaml file2.yaml
```

### Sort keys alphabetically

```bash
pyamit --sort-keys file1.yaml file2.yaml
```

### Custom indentation

```bash
pyamit --indent 4 file1.yaml file2.yaml
```

### Combine options

```bash
pyamit --sort-keys --indent 4 file1.yaml file2.yaml
```

### Get help

```bash
pyamit --help
```

## 🪝 Pre-commit Integration

Once installed via pip/uv, you can integrate pyamit into your pre-commit hooks.

### For your projects

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/mounirmesselmeni/pyamit
    rev: v0.1.1 # Use the latest version
    hooks:
      - id: pyamit

  # Or use with custom arguments
  - repo: https://github.com/mounirmesselmeni/pyamit
    rev: v0.1.1
    hooks:
      - id: pyamit
        args: [--sort-keys, --indent=4]
```

### Alternative: Local installation

If you prefer to install locally:

```yaml
repos:
  - repo: local
    hooks:
      - id: pyamit
        name: Format YAML files
        entry: pyamit
        language: system
        files: \.yaml$
        args: [--sort-keys]
```

### For this project

The included pre-commit config ensures code quality:

```bash
pre-commit install
pre-commit run --all-files
```

## 🛠️ Development

### Run tests

```bash
uv run pytest
```

### Lint and format code

```bash
uv run ruff check . --fix
uv run ruff format .
```

### Use pre-commit hooks

```bash
pre-commit install
pre-commit run --all-files
```

### CI/CD

This project uses GitHub Actions for continuous integration and deployment with optimized uv workflows:

- **Multi-Python Testing**: Tests across Python 3.11, 3.12, and 3.13
- **Coverage Reporting**: Automated test coverage reporting (93%+) with coverage publishing
- **Pre-commit Hooks**: Automated linting and formatting with cached hooks
- **uv Caching**: Dependency and virtual environment caching for faster builds
- **Publishing**: Automatic PyPI publishing on releases using OIDC trusted publishing
- **Cache Optimization**: uv cache pruning for efficient CI resource usage

## 📋 Requirements

- Python 3.11+
- uv (for development)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
