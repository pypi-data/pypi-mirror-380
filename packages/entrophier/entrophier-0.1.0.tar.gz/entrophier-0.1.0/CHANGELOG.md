# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-01

### Added
- **Module-based architecture**: Converted from standalone script to proper Python package
  - `src/entrophier/` package structure with clean separation of concerns
  - `__init__.py` - Public API exports
  - `__main__.py` - Module entry point for `python -m entrophier`
  - `cli.py` - Command-line interface
  - `config.py` - Configuration management
  - `core.py` - Core redaction logic
- **Modern Python tooling**:
  - uv for fast dependency management and development
  - Python 3.13 support
  - hatchling build system
  - Proper pyproject.toml configuration
- **Comprehensive pytest test suite**:
  - 40 unit tests covering all functionality
  - Test classes for entropy calculation, pattern detection, redaction methods
  - 67% overall code coverage (91% on core module)
  - Tests for AWS paths, file paths, timestamps, IP addresses, containers
- **CLI enhancements**:
  - Installable `entrophier` command-line tool
  - `--config-dir` option for custom configuration directories
  - Multiple output modes and parameter overrides
- **Configuration system**:
  - Config files bundled with package in `src/entrophier/`
  - Support for custom config directories
  - Validates all required configuration on startup
- **Documentation**:
  - Comprehensive README with installation, usage, and examples
  - Test documentation in `tests/README.md`
  - Development workflow documentation

### Fixed
- **IPv4 address redaction**: Fixed YAML multiline formatting that prevented IPv4 addresses from being properly redacted
  - Changed from `|` (literal block) to quoted string format in `redaction_patterns.yaml`
  - IPv4 addresses like `192.168.1.100` now correctly redacted in all contexts

### Changed
- **Package name**: Changed from `python-entrophier` to `entrophier`
- **Import path**: Use `from entrophier import ...` instead of `from entropy import ...`
- **Command usage**: Use `entrophier` command instead of `python3 entropy.py`
- **Config location**: Configuration files now bundled in package at `src/entrophier/` (can be overridden)
- **Test execution**: Use `uv run pytest` instead of `python3 test_entropy.py`

### Technical Details
- **Dependencies**:
  - Runtime: `pyyaml>=6.0.0`
  - Development: `pytest>=8.0.0`, `pytest-cov>=4.0.0`
- **Python version**: Requires Python 3.13+
- **Build system**: Uses hatchling for wheel and source distribution builds

### Distribution
- Package can be built with `uv build`
- Creates both wheel (`.whl`) and source distribution (`.tar.gz`)
- Ready for PyPI publication (currently local install only)

## [Unreleased]

### Planned
- PyPI package publication
- Additional pattern types for cloud providers (GCP, Azure)
- Performance optimizations for large files
- CI/CD pipeline setup

---

## Migration from Standalone Script

If migrating from the original standalone `entropy.py` script:

### Import Changes
```python
# Old
from entropy import redact_sensitive_data, load_config

# New
from entrophier import redact_sensitive_data, load_config
```

### Command-Line Changes
```bash
# Old
python3 entropy.py input.txt

# New
entrophier input.txt
# or
python -m entrophier input.txt
```

### Configuration
- Config files previously in same directory as script
- Now bundled with package at `src/entrophier/`
- Use `--config-dir` flag or `load_config(config_dir="/path")` for custom configs

[0.1.0]: https://github.com/rjury-sumo/python-entrophier/releases/tag/v0.1.0
