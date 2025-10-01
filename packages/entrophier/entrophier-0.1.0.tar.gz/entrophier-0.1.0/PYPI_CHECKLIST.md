# PyPI Publication Checklist

Use this checklist when publishing to PyPI.

## ✅ Pre-Publication (Complete)

- [x] LICENSE file exists (MIT)
- [x] README.md comprehensive
- [x] Python version: >=3.8 (wide compatibility)
- [x] Author email added
- [x] Classifiers complete (Python versions, audiences, topics)
- [x] Project URLs added (Bug Tracker, Changelog)
- [x] Keywords optimized
- [x] YAML config files included in package
- [x] Entry point configured (entrophier CLI)
- [x] Tests passing (40/40)
- [x] CHANGELOG.md created
- [x] Package builds successfully

## 📝 Before Publishing

- [ ] Review and update author email if needed (currently: noreply@example.com)
- [ ] Update version number in pyproject.toml if needed
- [ ] Update CHANGELOG.md with any last-minute changes
- [ ] Commit all changes to git
- [ ] Clean dist directory: `rm -rf dist/`

## 🔨 Build & Test

- [ ] Build package: `uv build`
- [ ] Verify build: `ls -lh dist/`
- [ ] Check package: `uvx twine check dist/*` (should PASS)
- [ ] Test in clean environment (see PUBLISHING.md)

> **Note**: Using `uvx` instead of `pip install twine` - no installation needed!

## 🧪 TestPyPI (Recommended First)

- [ ] Create TestPyPI account: https://test.pypi.org/
- [ ] Generate API token: https://test.pypi.org/manage/account/token/
- [ ] Upload: `uvx twine upload --repository testpypi dist/*`
- [ ] Test install: `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ entrophier`
- [ ] Verify CLI: `entrophier --help`
- [ ] Verify library: `python -c "from entrophier import redact_sensitive_data, load_config; load_config(); print('OK')"`

## 🚀 Production PyPI

- [ ] Create PyPI account: https://pypi.org/
- [ ] Generate API token: https://pypi.org/manage/account/token/
- [ ] Upload: `uvx twine upload dist/*`
- [ ] Verify on PyPI: https://pypi.org/project/entrophier/
- [ ] Test install: `pip install entrophier`
- [ ] Verify it works

## 🏷️ Git Release

- [ ] Tag release: `git tag v0.1.0`
- [ ] Push tag: `git push origin v0.1.0`
- [ ] Create GitHub release at: https://github.com/rjury-sumo/python-entrophier/releases/new
- [ ] Attach dist files (optional)

## 📢 Post-Publication

- [ ] Update README installation instructions (remove "not yet on PyPI" note)
- [ ] Test fresh installation: `pip install entrophier`
- [ ] Announce on GitHub Discussions
- [ ] Monitor PyPI stats: https://pypistats.org/packages/entrophier
- [ ] Watch for issues: https://github.com/rjury-sumo/python-entrophier/issues

## ✏️ Notes

**Version**: 0.1.0
**Date**: _______________
**Published by**: _______________
**PyPI URL**: https://pypi.org/project/entrophier/

## 📚 Documentation

- Full guide: [PUBLISHING.md](PUBLISHING.md)
- Readiness analysis: [PYPI_READINESS.md](PYPI_READINESS.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)
