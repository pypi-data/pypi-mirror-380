# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2025-10-01

### Added

- **New `--sort-lists` option**: Recursively sorts all lists in YAML files while preserving structure
- **Improved YAML indentation**: Custom `IndentedDumper` class ensures proper 2-space indentation for list items
- **Comprehensive test coverage**: Added tests for list sorting, error handling, and dumper safety (97% coverage)
- **Type-aware list sorting**: Handles mixed-type lists by sorting by type name then value
- **Error handling for incomparable types**: Gracefully handles lists with incomparable elements

### Changed

- **YAML formatting**: List items now properly indented with 2 spaces (standard YAML formatting)
- **Test suite**: Expanded from 4 to 13 tests covering all functionality and edge cases
- **Documentation**: Updated README with new `--sort-lists` option examples

### Fixed

- **YAML indentation**: Fixed issue where list items were flush-left instead of properly indented
- **Test coverage**: Improved from 76% to 97% with comprehensive error path testing

### Technical Details

- Added `sort_lists_in_data()` function for recursive list sorting
- Created `IndentedDumper` class inheriting from `yaml.SafeDumper`
- Enhanced error handling for sorting operations
- Added pragma comments for coverage exclusions

## [0.1.2] - 2025-10-01

### Added

- **Coverage reporting**: Automated test coverage with pytest-cov and GitHub Actions integration
- **CI/CD improvements**: Optimized workflow with uv caching and coverage publishing
- **Pre-commit hooks**: Updated hook configuration with available options documentation

### Changed

- **Version bump**: Updated to reflect new features and improvements

## [0.1.1] - 2025-10-01

### Added

- **GitHub Actions CI/CD**: Multi-Python testing (3.11, 3.12, 3.13) with optimized uv workflows
- **Pre-commit integration**: Complete hook configuration for external usage
- **PyPI publishing**: OIDC trusted publishing setup
- **Development tooling**: Comprehensive pre-commit, linting, and testing setup

### Changed

- **Project structure**: Organized with proper src/ layout and comprehensive configuration
- **Documentation**: Enhanced README with usage examples and development instructions

## [0.1.0] - 2025-10-01

### Added

- **Initial release**: Fast Python CLI tool for formatting and sorting YAML files
- **Core functionality**: YAML formatting with optional key sorting
- **CLI interface**: Typer-based command-line interface with `--sort-keys` and `--indent` options
- **Basic testing**: Initial test suite with pytest
- **Project setup**: uv-based dependency management, ruff linting, and basic CI/CD

### Technical Details

- Built with Python 3.11+, Typer, and PyYAML
- Safe YAML processing with proper error handling
- Modular architecture with separate formatting logic
