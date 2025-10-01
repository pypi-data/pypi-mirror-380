# Publishing to PyPI Guide

## ✅ Pre-Publication Checklist Complete

All PyPI best practices have been implemented:

- [x] LICENSE file (MIT)
- [x] Comprehensive README.md
- [x] Python version: 3.8+ (wide compatibility)
- [x] Author email added
- [x] Enhanced classifiers (Python versions, OS independent, audiences)
- [x] Additional project URLs (Bug Tracker, Changelog)
- [x] YAML config files included in package
- [x] Entry point configured
- [x] Tests passing (40/40)
- [x] CHANGELOG.md created

## 📦 Publishing Steps

### 1. Install Publishing Tools (Optional)

Using `uvx` (recommended - no installation needed):
```bash
# No installation required! uvx runs tools on-demand
# Skip to step 2
```

OR traditional approach:
```bash
pip install twine
```

> **Note**: This guide uses `uvx twine` commands which automatically download and run twine without permanent installation. This is cleaner and more consistent with the uv workflow.

### 2. Clean Previous Builds

```bash
rm -rf dist/
```

### 3. Build Package

```bash
# Using uv (recommended)
uv build

# Or using build module
python -m build
```

This creates:
- `dist/entrophier-0.1.0.tar.gz` (source distribution)
- `dist/entrophier-0.1.0-py3-none-any.whl` (wheel)

### 4. Validate Package

```bash
# Using uvx (recommended)
uvx twine check dist/*

# OR traditional
twine check dist/*
```

Expected output: `Checking dist/... PASSED`

### 5. Test in Clean Environment

```bash
# Create test environment
python -m venv test-env
source test-env/bin/activate  # Windows: test-env\Scripts\activate

# Install from wheel
pip install dist/entrophier-0.1.0-py3-none-any.whl

# Test CLI
entrophier --help

# Test library
python -c "
from entrophier import redact_sensitive_data, load_config
load_config()
result = redact_sensitive_data('test-abc123')
print(f'Redacted: {result}')
assert '*' in result
print('✓ Package works!')
"

# Cleanup
deactivate
rm -rf test-env
```

### 6. Upload to TestPyPI (Recommended First)

```bash
# Create account at https://test.pypi.org/ first

# Upload to TestPyPI (using uvx - recommended)
uvx twine upload --repository testpypi dist/*

# OR traditional approach
twine upload --repository testpypi dist/*

# You'll be prompted for:
# Username: __token__
# Password: <your TestPyPI API token>
```

### 7. Test Install from TestPyPI

```bash
# Create fresh environment
python -m venv testpypi-env
source testpypi-env/bin/activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ entrophier

# Test it
entrophier --help

# Cleanup
deactivate
rm -rf testpypi-env
```

### 8. Upload to Production PyPI

Once TestPyPI installation works:

```bash
# Create account at https://pypi.org/ first
# Generate API token at https://pypi.org/manage/account/token/

# Upload to PyPI (using uvx - recommended)
uvx twine upload dist/*

# OR traditional approach
twine upload dist/*

# You'll be prompted for:
# Username: __token__
# Password: <your PyPI API token>
```

### 9. Verify on PyPI

Visit: https://pypi.org/project/entrophier/

### 10. Test Production Install

```bash
pip install entrophier
entrophier --help
```

### 11. Tag the Release

```bash
git tag v0.1.0
git push origin v0.1.0
```

### 12. Create GitHub Release

1. Go to: https://github.com/rjury-sumo/python-entrophier/releases/new
2. Choose tag: v0.1.0
3. Title: "v0.1.0 - Initial Release"
4. Copy content from CHANGELOG.md
5. Attach build artifacts (optional):
   - `dist/entrophier-0.1.0.tar.gz`
   - `dist/entrophier-0.1.0-py3-none-any.whl`

## 🔐 Using API Tokens (Recommended)

### Create PyPI API Token

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: "entrophier-upload"
4. Scope: "Entire account" or "Project: entrophier"
5. Copy the token (starts with `pypi-`)

### Configure .pypirc (Optional)

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = <your-pypi-token>

[testpypi]
username = __token__
password = <your-testpypi-token>
```

Then upload without prompts:
```bash
# Using uvx (recommended)
uvx twine upload --repository testpypi dist/*
uvx twine upload dist/*

# OR traditional
twine upload --repository testpypi dist/*
twine upload dist/*
```

## 🚨 Common Issues

### Issue: "File already exists"
**Solution**: Increment version in `pyproject.toml` - PyPI doesn't allow re-uploading same version

### Issue: "Invalid classifier"
**Solution**: Check classifiers at https://pypi.org/classifiers/

### Issue: "Description failed to render"
**Solution**: Validate README: `twine check dist/*`

### Issue: Import fails after install
**Solution**: Ensure YAML files are in wheel: `unzip -l dist/*.whl`

## 📝 Post-Publication

### Update Installation Instructions

Update README.md:
```bash
# Now available on PyPI!
pip install entrophier
```

### Announce Release

- GitHub Discussions
- Python security mailing lists
- Project blog/changelog

### Monitor

- PyPI download stats: https://pypistats.org/packages/entrophier
- GitHub issues: https://github.com/rjury-sumo/python-entrophier/issues

## 🔄 Future Releases

### Version Bumping

```bash
# Update version in pyproject.toml
# Update CHANGELOG.md with new version
# Commit changes
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to 0.2.0"

# Tag and push
git tag v0.2.0
git push origin main v0.2.0

# Build and upload
rm -rf dist/
uv build
twine check dist/*
twine upload dist/*
```

## 📚 References

- [PyPI Publishing Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [TestPyPI](https://test.pypi.org/)
- [PyPI Help](https://pypi.org/help/)
