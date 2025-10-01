# 📦 Navam Package Management Guide

Complete guide for building, testing, and publishing the Navam package to PyPI using `uv` for optimal performance.

## 🔧 Prerequisites

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install required build and publish tools
uv add --dev build twine check-manifest pyroma

# Optional: Install keyring for secure credential storage
uv add --dev keyring
```

## 🏗️ Step 1: Build the Package

```bash
# Clean any previous builds
rm -rf dist/ build/ src/*.egg-info/

# Build source distribution and wheel using uv
uv run python -m build

# Verify build artifacts
ls dist/
# Expected output: navam-1.0.0-py3-none-any.whl and navam-1.0.0.tar.gz

# Check file sizes (should be reasonable)
du -h dist/*
```

## 🧪 Step 2: Test in Fresh Virtual Environment

### Method A: Quick Test with uv
```bash
# Create a completely isolated test environment
uv venv test_navam_env --python 3.11
source test_navam_env/bin/activate  # On Windows: test_navam_env\Scripts\activate

# Install from local wheel
uv pip install dist/navam-1.0.0-py3-none-any.whl

# Test basic CLI functionality
navam --help
navam --version

# Test MCP server connections
navam test-connection

# Test tool listing
navam list-tools

# Test a simple analysis (if you have API keys configured)
# navam analyze AAPL

# Test CLI commands without external APIs
echo "Testing CLI interface..."
navam --help | grep -q "Navam" && echo "✅ CLI working"

# Cleanup
deactivate
rm -rf test_navam_env
```

### Method B: Comprehensive Test with Dependencies
```bash
# Create test environment with all optional dependencies
uv venv comprehensive_test_env --python 3.11
source comprehensive_test_env/bin/activate

# Install with all extras
uv pip install "dist/navam-1.0.0-py3-none-any.whl[dev,mcp,all]"

# Test core functionality
navam --help
navam test-connection
navam list-tools

# Test MCP server functionality (if .mcp.json exists)
if [ -f ".mcp.json" ]; then
    echo "Testing MCP servers..."
    uv run python -m src.stock_mcp.server --help
    uv run python -m src.company_mcp.server --help
    uv run python -m src.news_mcp.server --help
fi

# Test chat interface (requires ANTHROPIC_API_KEY)
# export ANTHROPIC_API_KEY="your_key_here"
# echo "/help" | timeout 10 navam chat || echo "Chat test completed"

# Cleanup
deactivate
rm -rf comprehensive_test_env
```

## 🔍 Step 3: Package Quality Checks

```bash
# Check package structure and metadata
uv run python -m build --check

# Validate README will render correctly on PyPI
uv run python -m twine check dist/*

# Check manifest completeness
uv run check-manifest

# Check package quality rating
uv run pyroma .

# Optional: Check for security vulnerabilities
uv run pip-audit

# Verify all required files are included
echo "Checking package contents..."
tar -tzf dist/navam-1.0.0.tar.gz | head -20
```

## 🚀 Step 4: Publish to PyPI

### 4a. Test on PyPI Test Repository First (Strongly Recommended)

```bash
# Upload to TestPyPI first for validation
uv run python -m twine upload --repository testpypi dist/*
# Enter TestPyPI credentials when prompted

# Test installation from TestPyPI
uv venv testpypi_install_env
source testpypi_install_env/bin/activate

# Install from TestPyPI (with fallback to main PyPI for dependencies)
uv pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    navam

# Quick verification
navam --version
navam --help

# Cleanup test environment
deactivate
rm -rf testpypi_install_env

echo "✅ TestPyPI upload successful!"
echo "🔗 Check: https://test.pypi.org/project/navam/"
```

### 4b. Publish to Production PyPI

```bash
# Final upload to production PyPI
uv run python -m twine upload dist/*
# Enter PyPI credentials when prompted

echo "🎉 Package published to PyPI!"
echo "🔗 View at: https://pypi.org/project/navam/"
echo "📦 Install with: pip install navam"
```

## 🔐 Authentication Setup

### Option 1: API Tokens (Recommended)

Create API tokens at:
- PyPI: https://pypi.org/manage/account/token/
- TestPyPI: https://test.pypi.org/manage/account/token/

```bash
# Create .pypirc file in your home directory
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_PRODUCTION_API_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_API_TOKEN_HERE
EOF

# Set secure permissions
chmod 600 ~/.pypirc
```

### Option 2: Environment Variables

```bash
# Set for current session
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR_API_TOKEN_HERE

# Or add to your shell profile for persistence
echo 'export TWINE_USERNAME=__token__' >> ~/.zshrc
echo 'export TWINE_PASSWORD=pypi-YOUR_API_TOKEN_HERE' >> ~/.zshrc
```

### Option 3: Keyring (Most Secure)

```bash
# Store credentials securely
uv run python -m keyring set https://upload.pypi.org/legacy/ __token__
# Enter your API token when prompted

uv run python -m keyring set https://test.pypi.org/legacy/ __token__
# Enter your TestPyPI token when prompted
```

## 📋 Complete Automated Workflow

Save this as `scripts/publish.sh`:

```bash
#!/bin/bash
set -e

echo "🔧 Navam Package Build & Publish Workflow"
echo "=========================================="

# Configuration
PACKAGE_NAME="navam"
PYTHON_VERSION="3.11"

echo "🧹 Step 1: Cleaning previous builds..."
rm -rf dist/ build/ src/*.egg-info/

echo "🏗️ Step 2: Building package with uv..."
uv run python -m build

echo "📊 Step 3: Package info..."
ls -lh dist/
echo "Package size: $(du -sh dist/ | cut -f1)"

echo "🔍 Step 4: Quality checks..."
uv run python -m twine check dist/* || {
    echo "❌ Package quality check failed!"
    exit 1
}

echo "✅ Quality checks passed!"

echo "🧪 Step 5: Testing in isolated environment..."
uv venv test_env --python $PYTHON_VERSION
source test_env/bin/activate

uv pip install "dist/${PACKAGE_NAME}-*.whl"

# Run basic tests
$PACKAGE_NAME --version || {
    echo "❌ Package installation test failed!"
    deactivate
    rm -rf test_env
    exit 1
}

$PACKAGE_NAME test-connection
echo "✅ Package tests passed!"

deactivate
rm -rf test_env

echo "📤 Step 6: Uploading to TestPyPI..."
uv run python -m twine upload --repository testpypi dist/*

echo "🎯 Step 7: Testing TestPyPI installation..."
uv venv testpypi_env
source testpypi_env/bin/activate

uv pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    $PACKAGE_NAME

$PACKAGE_NAME --version
echo "✅ TestPyPI installation successful!"

deactivate
rm -rf testpypi_env

echo ""
echo "🚀 Ready for production PyPI!"
echo "Run the following command to publish:"
echo "    uv run python -m twine upload dist/*"
echo ""
echo "📋 Post-publish checklist:"
echo "  🔗 Check: https://pypi.org/project/$PACKAGE_NAME/"
echo "  📦 Test: pip install $PACKAGE_NAME"
echo "  📚 Update documentation if needed"
echo "  🏷️ Create GitHub release tag"
```

Make it executable:
```bash
chmod +x scripts/publish.sh
```

## 🎯 Quick Reference Commands

```bash
# Full build and test cycle
rm -rf dist/ && uv run python -m build && uv run python -m twine check dist/*

# Test install from wheel
uv venv test && source test/bin/activate && uv pip install dist/navam-*.whl

# Upload to TestPyPI
uv run python -m twine upload --repository testpypi dist/*

# Upload to production PyPI
uv run python -m twine upload dist/*

# Install published package
pip install navam

# Install with all extras
pip install "navam[all]"
```

## ⚠️ Pre-Publish Checklist

Before publishing each release:

- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md` with new features/fixes
- [ ] Run full test suite: `uv run python -m pytest`
- [ ] Check code quality: `uv run ruff check .`
- [ ] Format code: `uv run black .`
- [ ] Type check: `uv run mypy .`
- [ ] Build and test package locally
- [ ] Test on TestPyPI first
- [ ] Verify README renders correctly on TestPyPI
- [ ] Update documentation if needed

## 🔧 Troubleshooting

### Build Issues
```bash
# Update build tools
uv add --dev --upgrade build setuptools wheel

# Check for missing files
uv run check-manifest

# Verbose build for debugging
uv run python -m build --verbose
```

### Upload Issues
```bash
# Update twine
uv add --dev --upgrade twine

# Test authentication
uv run python -m twine check dist/*

# Upload with verbose output
uv run python -m twine upload --verbose --repository testpypi dist/*
```

### Installation Issues
```bash
# Check dependencies
uv pip check

# Install with verbose output
uv pip install -v dist/navam-*.whl

# Check for conflicts
uv pip list --outdated
```

### Version Conflicts
```bash
# Check current version
grep "version" pyproject.toml

# Ensure version is unique on PyPI
curl -s https://pypi.org/pypi/navam/json | jq '.releases | keys'
```

## 📈 Post-Publish Steps

After successful publication:

1. **Verify PyPI page**: https://pypi.org/project/navam/
2. **Test installation**: `pip install navam`
3. **Create GitHub release** with same version tag
4. **Update documentation** links if needed
5. **Announce on social media** or relevant channels
6. **Monitor download stats** on PyPI
7. **Watch for user issues** on GitHub

## 🎉 Success Indicators

Your package is successfully published when:

- ✅ Package appears on PyPI: https://pypi.org/project/navam/
- ✅ `pip install navam` works from any environment
- ✅ `navam --help` shows expected output
- ✅ All command-line tools function correctly
- ✅ MCP servers can be imported and run
- ✅ README displays properly on PyPI page

---

**Happy Publishing! 🚀**

*This workflow is optimized for `uv` to provide the fastest and most reliable package management experience.*