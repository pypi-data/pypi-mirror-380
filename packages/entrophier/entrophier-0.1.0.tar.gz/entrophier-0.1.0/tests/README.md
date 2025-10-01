# Test Suite Documentation

This directory contains the comprehensive test suite for the entrophier package.

## Running Tests

### Basic Test Run
```bash
# Run all tests
uv run pytest tests/

# Run with verbose output
uv run pytest tests/ -v

# Run specific test class
uv run pytest tests/test_entropy.py::TestEntropyCalculation -v
```

### Coverage Reports
```bash
# Run with coverage
uv run pytest tests/ --cov=entrophier

# Generate detailed coverage report
uv run pytest tests/ --cov=entrophier --cov-report=term-missing

# Generate HTML coverage report
uv run pytest tests/ --cov=entrophier --cov-report=html
```

## Test Structure

The test suite is organized into the following test classes:

### TestEntropyCalculation (4 tests)
Tests for Shannon entropy calculation:
- Empty string handling
- Single character handling
- Uniform distribution entropy
- Random vs structured string entropy comparison

### TestHighEntropySegmentDetection (5 tests)
Tests for high entropy segment detection:
- Short string filtering
- Common word preservation
- UUID detection
- Random hex string detection
- Numeric ID detection

### TestWordPreservation (3 tests)
Tests for preserving common words and technical terms:
- Common words preservation
- Technical terms preservation
- File structure words preservation

### TestTokenLevelRedaction (4 tests)
Tests for token-level redaction approach:
- Random token redaction
- UUID redaction
- API key redaction
- Asterisk condensation

### TestAWSPathRedaction (2 tests)
Tests for AWS S3 path redaction:
- CloudTrail path redaction
- Lambda deployment path redaction

### TestAWSHostnameRedaction (3 tests)
Tests for AWS hostname selective redaction:
- EC2 hostname redaction (preserves domain)
- RDS hostname redaction
- CloudFront hostname redaction

### TestFilePathRedaction (2 tests)
Tests for file path redaction:
- Windows path redaction
- Linux path redaction

### TestTimestampRedaction (3 tests)
Tests for timestamp and datetime redaction:
- ISO timestamp redaction
- Epoch timestamp redaction
- Human-readable datetime redaction

### TestIPAddressRedaction (2 tests)
Tests for IP address redaction:
- IPv4 address redaction
- IPv6 address redaction

### TestDockerKubernetesRedaction (2 tests)
Tests for container infrastructure:
- Docker image path redaction
- Kubernetes pod name redaction

### TestSlidingWindowApproach (2 tests)
Tests for sliding window redaction approach:
- Basic sliding window redaction
- Word preservation in sliding window

### TestDefaultRedactionFunction (2 tests)
Tests for the default convenience function:
- Basic redaction
- Redaction with custom options

### TestEdgeCases (5 tests)
Tests for edge cases and boundary conditions:
- Empty string handling
- Only common words (no redaction)
- Only random strings (full redaction)
- Year preservation
- Custom entropy threshold

### TestConfigurationLoading (1 test)
Tests for configuration system:
- Configuration loading validation

## Test Coverage

Current test coverage (as of last run):

```
Name                         Stmts   Miss  Cover
--------------------------------------------------
src/entrophier/__init__.py       4      0   100%
src/entrophier/__main__.py       3      3     0%   (CLI entry point, tested manually)
src/entrophier/cli.py           67     67     0%   (CLI tested manually)
src/entrophier/config.py        96     26    73%
src/entrophier/core.py         171     16    91%  ← Core logic well-covered
--------------------------------------------------
TOTAL                          341    112    67%
```

**Note**: CLI and __main__ are tested manually as they involve argument parsing and I/O.

## Test Fixtures

### setup_config
- **Scope**: Module-level
- **Purpose**: Loads configuration once for all tests
- **Usage**: Automatically injected into all test methods

## Writing New Tests

When adding new tests:

1. Choose the appropriate test class or create a new one
2. Use the `setup_config` fixture to ensure configuration is loaded
3. Follow the naming convention: `test_<functionality>_<specific_case>`
4. Add docstrings explaining what the test validates
5. Use clear assertions with helpful messages

Example:
```python
class TestNewFeature:
    """Test new feature description."""

    def test_new_feature_basic(self, setup_config):
        """Test basic functionality of new feature."""
        text = "example input"
        result = new_function(text)
        assert expected in result
        assert unexpected not in result
```

## Continuous Integration

These tests are designed to run in CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run tests
  run: |
    uv sync
    uv run pytest tests/ --cov=entrophier
```

## Test Data

Test cases cover:
- **AWS Resources**: CloudTrail, S3, Lambda, EC2, RDS, CloudFront
- **File Paths**: Windows, Linux, network shares
- **Containers**: Docker images, Kubernetes pods
- **Identifiers**: UUIDs, API keys, session tokens, account IDs
- **Timestamps**: ISO 8601, epoch, human-readable
- **Network**: IPv4, IPv6, hostnames
- **Random Strings**: Hex, alphanumeric, Base64-like

## Performance

Tests run in ~0.1 seconds total with all 40 tests passing.

## Debugging Failed Tests

If tests fail:

1. Run with verbose output: `uv run pytest tests/ -v`
2. Run specific failing test: `uv run pytest tests/test_entropy.py::TestClass::test_method -vv`
3. Use `--tb=short` or `--tb=long` for different traceback formats
4. Check if config files are present and valid
5. Verify Python version is 3.13+

## Related Documentation

- [Main README](../README.md) - Package documentation
