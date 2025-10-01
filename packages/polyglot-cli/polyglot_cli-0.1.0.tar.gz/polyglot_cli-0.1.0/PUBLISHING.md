# Publishing Guide for Polyglot

## Quick Reference

### 3 Ways to Ship Polyglot:

1. **PyPI (Python Package Index)** - Best for Python users
2. **GitHub Releases** - Binary downloads for all platforms
3. **Homebrew** - macOS users (future)

---

## 1. Publishing to PyPI

### First-time setup:
```bash
pip install build twine
```

### Create PyPI account:
- Go to https://pypi.org/account/register/
- Create account
- Enable 2FA
- Create API token at https://pypi.org/manage/account/token/

### Build and publish:
```bash
# Build the package
python -m build

# Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ polyglot-cli

# If all looks good, upload to real PyPI
twine upload dist/*
```

### After publishing:
Users can install with:
```bash
pip install polyglot-cli
```

---

## 2. GitHub Releases (Binaries)

### Build binaries for each platform:

**macOS (Intel):**
```bash
./build_binary.sh
# Creates: dist/polyglot
```

**macOS (Apple Silicon):**
```bash
./build_binary.sh
# Creates: dist/polyglot
```

**Linux:**
```bash
# On Linux machine or Docker
./build_binary.sh
# Creates: dist/polyglot
```

**Windows:**
```bash
# On Windows machine
pip install pyinstaller
pyinstaller --name polyglot --onefile --console polyglot_cli/__main__.py
# Creates: dist/polyglot.exe
```

### Create GitHub release:
```bash
# Tag the release
git tag -a v0.1.0 -m "Initial release"
git push origin v0.1.0

# Go to GitHub → Releases → Create new release
# Upload the binaries:
# - polyglot-macos-intel
# - polyglot-macos-arm64
# - polyglot-linux-x86_64
# - polyglot-windows.exe
```

### Users can download:
```bash
# macOS/Linux
curl -L https://github.com/samar/polyglot-cli/releases/latest/download/polyglot-macos-arm64 -o polyglot
chmod +x polyglot
./polyglot --help
```

---

## 3. Docker (Bonus)

### Create Dockerfile:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -e .
ENTRYPOINT ["polyglot"]
```

### Build and publish:
```bash
docker build -t polyglot-cli .
docker tag polyglot-cli ghcr.io/samar/polyglot-cli:latest
docker push ghcr.io/samar/polyglot-cli:latest
```

### Users can run:
```bash
docker run -e ANTHROPIC_API_KEY ghcr.io/samar/polyglot-cli translate python rust --file example.py
```

---

## Version Bumping

Update version in:
1. `pyproject.toml` - `version = "x.y.z"`
2. `polyglot_cli/__init__.py` - `__version__ = "x.y.z"`

Then rebuild and republish.

---

## Best Distribution Strategy

**For maximum reach:**

1. **PyPI** (easiest for Python devs)
   - `pip install polyglot-cli`

2. **GitHub Releases** (for non-Python users)
   - Download binary, no Python needed

3. **Homebrew Formula** (future - for macOS users)
   - `brew install polyglot-cli`

Most users will use PyPI, but providing binaries means anyone can use it without installing Python!
