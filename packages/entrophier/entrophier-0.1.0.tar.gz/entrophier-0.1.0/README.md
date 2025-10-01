# High-Entropy String Redaction Tool

A configurable Python tool for detecting and redacting sensitive data in text using entropy analysis and pattern matching. Designed for processing log files, user input, and any text containing potentially sensitive information like timestamps, UUIDs, account IDs, IP addresses, and AWS hostnames.

## 🚀 Quick Start

### Installation

```bash
# Development installation with uv (recommended)
git clone https://github.com/rjury-sumo/python-entrophier.git
cd python-entrophier
uv sync

# Or install locally with uv
uv pip install .

# Or install with pip
pip install .

# Note: Package not yet published to PyPI
```

### Command-Line Usage

```bash
# Process a file (redacted output only)
entrophier input.txt

# Comparative mode (see original vs redacted)
entrophier -c input.txt

# Comparative mode with condensed asterisks
entrophier -c test_strings.txt --condense-asterisks

# Process stdin
cat logfile.txt | entrophier

# Save to file
entrophier -c -o output.txt input.txt
```

## 📋 Features

### Core Capabilities
- **Shannon Entropy Analysis**: Identifies high-randomness strings using information theory
- **Pattern-Based Detection**: Recognizes structured data like timestamps, IPs, and AWS hostnames
- **Word Preservation**: Protects common English words and technical terms from redaction
- **Selective Redaction**: AWS hostname patterns preserve domain parts while redacting sensitive IDs
- **Two Redaction Methods**: Token-level (default, more reliable) and sliding window (more granular)

### Supported Pattern Types
- **Datetime/Timestamps**: ISO 8601, human-readable dates, epoch timestamps
- **IP Addresses**: IPv4, IPv6, with contextual detection
- **AWS Resources**: EC2 hostnames, RDS endpoints, CloudFront distributions, API Gateway
- **UUIDs and Hex Sequences**: Full and partial UUID detection
- **Account IDs and Random Strings**: Long numeric and alphanumeric sequences

## ⚙️ Configuration

The tool requires three YAML configuration files:

### `common_words.yaml`
Contains word lists and patterns to preserve during redaction:
```yaml
common_words:
  - admin, alert, application, auth, backup, cache
  - database, debug, deployment, development, device
  # ... extensive list of technical and common terms

word_patterns:
  prefixes: [pre, post, anti, auto, co, de, dis, ...]
  suffixes: [able, ible, al, ed, er, est, ful, ic, ...]
```

### `entropy_settings.yaml`
Controls detection behavior and thresholds:
```yaml
entropy_detection:
  default_threshold: 2.5        # Higher = less sensitive
  word_pattern_bonus: 0.5       # Extra threshold for word-like patterns
  min_length: 4                 # Minimum string length to consider
  window_size: 6                # Sliding window size

output_formatting:
  # Note: condense_asterisks is now a command-line option only

pattern_detection:
  detect_timestamps: true       # Enable timestamp detection
  detect_ip_addresses: true     # Enable IP address detection
  detect_aws_hostnames: true    # Enable AWS hostname detection
```

### `redaction_patterns.yaml`
Defines regex patterns for structured data detection:
```yaml
datetime_patterns:
  human_readable_datetime: |
    (Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\w+\s+\d{4}
  date_yyyy_mm_dd: '\d{4}/\d{2}/\d{2}'
  # ... more datetime patterns

aws_selective_patterns:
  ec2_public_ipv4_dns:
    pattern: 'ec2-(\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3})(\..*\.amazonaws\.com)'
    replacement: 'ec2-*\2'
  # ... selective redaction patterns
```

## 🛠️ Command-Line Options

```bash
entrophier [options] [input_file]

Options:
  -c, --comparative           Show original and redacted (default: redacted only)
  -o OUTPUT, --output OUTPUT  Output file path (default: stdout)
  --method {token,sliding}    Redaction method (default: token)
  --threshold THRESHOLD       Override entropy threshold
  --min-length MIN_LENGTH     Override minimum length
  --condense-asterisks        Condense consecutive asterisks to single *
  --config-dir CONFIG_DIR     Directory containing configuration files

Positional:
  input_file                  Input file path (use "-" or omit for stdin)
```

## 📚 Library Usage

```python
from entrophier import redact_sensitive_data, load_config

# Load configuration (required - uses default config files from module directory)
load_config()

# Basic usage (recommended)
result = redact_sensitive_data("model-scheduler-667689996-jd4g7")
# Output: "model-scheduler-*********-*****"

# Use custom config directory
load_config(config_dir="/path/to/config")

# Alternative methods
from entrophier import redact_high_entropy_tokens, redact_high_entropy_strings

# Token-level approach (more reliable)
result = redact_high_entropy_tokens("text")

# Sliding window approach (more granular)
result = redact_high_entropy_strings("text")
```

## 🎯 Examples

### Input/Output Examples

```bash
# AWS CloudTrail path
Original: s3://aws-cloudtrail-logs-123456789012-us-east-1/CloudTrail/...
Redacted: s3://aws-cloudtrail-logs-************-us-east-1/CloudTrail/...

# EC2 hostname (selective redaction)
Original: ec2-198-51-100-1.compute-1.amazonaws.com
Redacted: ec2-*.compute-1.amazonaws.com

# Human-readable datetime
Original: Wed Sep 24 11:17:52 NZST 2025
Redacted: Wed Sep 24 ******** NZST 2025

# UUID
Original: uuid-550e8400-e29b-41d4-a716-446655440000
Redacted: uuid-********-****-****-****-************

# Mixed content preserving common words
Original: database-connection-string-server-production-guid-550e8400
Redacted: database-connection-string-server-production-guid-********

# With --condense-asterisks flag
Original: user-session-abc123def456-another-xyz789abc123
Redacted: user-session-*-another-*

# Without --condense-asterisks flag (default)
Original: user-session-abc123def456-another-xyz789abc123
Redacted: user-session-************-another-************
```

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/rjury-sumo/python-entrophier.git
cd python-entrophier

# Install with uv (creates .venv automatically)
uv sync

# Verify installation
uv run python -c "from entrophier import redact_sensitive_data, load_config; load_config(); print('✓ Setup complete')"
```

### Development Workflow

```bash
# Run tests during development
uv run pytest

# Run tests with coverage
uv run pytest --cov=entrophier --cov-report=term-missing

# Run CLI in development mode
uv run entrophier input.txt

# Build package
uv build

# Run specific module
uv run python -m entrophier input.txt
```

### Project Dependencies

- **Runtime**: `pyyaml>=6.0.0`
- **Development**: `pytest>=8.0.0`, `pytest-cov>=4.0.0`
- **Python**: 3.8+ (compatible with Python 3.8 through 3.13)
- **Build**: hatchling (specified in pyproject.toml)

## 🧪 Testing

Run the comprehensive pytest test suite (40 tests):

```bash
# Run all tests
uv run pytest

# With verbose output
uv run pytest -v

# With coverage report
uv run pytest --cov=entrophier

# Run specific test class
uv run pytest tests/test_entropy.py::TestEntropyCalculation -v
```

The test suite includes:
- Entropy calculation and segment detection
- Word preservation and pattern matching
- AWS S3 CloudTrail and CloudWatch paths
- Container and Docker paths (Kubernetes, Docker)
- Windows and Linux file paths
- Database connection strings
- IP addresses (IPv4/IPv6) and network identifiers
- Various timestamp and datetime formats
- Edge cases and boundary conditions

See [tests/README.md](tests/README.md) for detailed test documentation.

## 🔧 How It Works

### Entropy Analysis
The tool uses Shannon entropy to measure randomness in character distributions:
- **High entropy** (>2.5 bits): Random-looking strings like `abc123def456`
- **Low entropy** (<2.0 bits): Structured text like common words
- **Pattern boosting**: Adds entropy score for mixed case, alphanumeric combinations

### Two-Phase Detection
1. **Pattern-based detection**: Identifies structured data using regex patterns
2. **Entropy-based analysis**: Catches random strings missed by patterns

### Word Preservation
- Extensive dictionary of common English and technical terms
- Pattern matching for word prefixes/suffixes
- Contextual analysis to avoid redacting legitimate words

## 📁 Project Structure

```
python-entrophier/
├── src/
│   └── entrophier/
│       ├── __init__.py          # Public API exports
│       ├── __main__.py          # Module entry point
│       ├── cli.py               # Command-line interface
│       ├── config.py            # Configuration loading
│       ├── core.py              # Core redaction logic
│       ├── common_words.yaml    # Word lists and patterns
│       ├── entropy_settings.yaml # Detection and output settings
│       └── redaction_patterns.yaml # Regex patterns for structured data
├── tests/
│   └── test_entropy.py          # Comprehensive test suite
├── pyproject.toml               # Project metadata and dependencies
├── README.md                    # This documentation
└── .python-version              # Python version (3.13)
```

## ⚠️ Configuration Requirements

The package will exit with an error if any required configuration files or settings are missing. This ensures consistent behavior and prevents fallback to hardcoded values.

**Default Configuration**: Config files are bundled with the package in `src/entrophier/`. For custom configurations, use the `--config-dir` CLI option or `load_config(config_dir="/path/to/config")` in Python.

Required sections in YAML files:
- `common_words.yaml`: `common_words`, `word_patterns`
- `entropy_settings.yaml`: `entropy_detection`, `pattern_detection`
- `redaction_patterns.yaml`: Pattern sections as needed

## 🎛️ Customization

### Adding Custom Patterns
Add to `redaction_patterns.yaml`:
```yaml
custom_patterns:
  my_identifier: 'pattern-\d{6}-[a-z]{4}'
```

### Adjusting Sensitivity
Modify `entropy_settings.yaml`:
```yaml
entropy_detection:
  default_threshold: 3.0    # Less sensitive (higher threshold)
  min_length: 6            # Only redact longer strings
```

### Adding Words to Preserve
Add to `common_words.yaml`:
```yaml
common_words:
  - mycompany
  - customterm
  - projectname
```

## 📦 Building and Distribution

### Build Package

```bash
# Build wheel and source distribution
uv build

# Output files in dist/:
# - entrophier-0.1.0-py3-none-any.whl
# - entrophier-0.1.0.tar.gz
```

### Install Built Package

```bash
# Install wheel locally
uv pip install dist/entrophier-0.1.0-py3-none-any.whl

# Or install from source distribution
uv pip install dist/entrophier-0.1.0.tar.gz
```

## 📚 Additional Documentation

- **[Test Documentation](tests/README.md)**: Comprehensive test suite details
- **[Changelog](CHANGELOG.md)**: Version history and release notes

## 🤝 Contributing

This is a defensive security tool. Contributions should focus on:
- Improving detection accuracy
- Adding new pattern types
- Enhancing performance
- Expanding test coverage

## 📄 License

MIT License - See LICENSE file for details

## 🔒 Security Note

This tool provides enterprise-grade sensitive data redaction with full configurability and no hardcoded assumptions about your data formats. However, always verify redaction results for your specific use case before using in production.