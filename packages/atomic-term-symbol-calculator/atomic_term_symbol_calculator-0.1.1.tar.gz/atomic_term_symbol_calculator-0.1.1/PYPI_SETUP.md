# PyPI Setup and Publishing Guide

## Overview

Your project is now configured for PyPI distribution! Here's what I've set up and how to publish.

## Files Created/Modified

### 1. `pyproject.toml` Updates
- Changed package name to `atomic-term-symbol-calculator` (hyphens for PyPI)
- Removed built-in modules from dependencies (`itertools`, `re`, `fractions`)
- Removed "Private :: Do Not Upload" classifier
- Added proper PyPI classifiers for chemistry/physics packages
- Added keywords for better discoverability
- Added command-line entry point: `atomic-term-calculator`
- Added proper license field

### 2. `MANIFEST.in` (New)
- Specifies which files to include in the distribution
- Ensures README, LICENSE, and other important files are packaged

### 3. `terms.py` Updates
- Added proper `main()` function for command-line interface
- Better error handling for CLI usage

## Publishing to PyPI

### Step 1: Create PyPI Account
1. Go to [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. Create an account
3. Verify your email

### Step 2: Create API Token
1. Go to [https://pypi.org/manage/account/](https://pypi.org/manage/account/)
2. Scroll to "API tokens" section
3. Click "Add API token"
4. Name it (e.g., "atomic-term-calculator")
5. Scope: "Entire account" (or specific project after first upload)
6. **Save the token** - you won't see it again!

### Step 3: Configure Authentication
```bash
# Option 1: Use .pypirc file (recommended)
cat > ~/.pypirc << EOF
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = pypi-your-token-here
EOF

# Option 2: Set environment variable
export TWINE_PASSWORD=pypi-your-token-here
export TWINE_USERNAME=__token__
```

### Step 4: Build and Upload

```bash
# Clean previous builds
rm -rf dist/

# Build the package
python -m build

# Check the package (optional but recommended)
twine check dist/*

# Upload to PyPI
twine upload dist/*
```

### Step 5: Test Installation

```bash
# In a new environment
pip install atomic-term-symbol-calculator

# Test the command-line tool
atomic-term-calculator

# Test the Python module
python -c "from atomic_term_symbol_calculator.terms import calc_term_symbols; print(calc_term_symbols('2p2'))"
```

## Publishing to Test PyPI First (Recommended)

Before publishing to the real PyPI, test with Test PyPI:

### Step 1: Register on Test PyPI
1. Go to [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
2. Create account and get API token

### Step 2: Upload to Test PyPI
```bash
# Upload to test PyPI
twine upload --repository testpypi dist/*

# Test installation from test PyPI
pip install --index-url https://test.pypi.org/simple/ atomic-term-symbol-calculator
```

## Version Management

Your version is managed in `src/atomic_term_symbol_calculator/__init__.py`. To release a new version:

1. Update the version in `__init__.py`:
   ```python
   __version__ = "0.1.2"
   ```

2. Rebuild and upload:
   ```bash
   rm -rf dist/
   python -m build
   twine upload dist/*
   ```

## Package Features After Installation

Users will be able to:

1. **Install via pip:**
   ```bash
   pip install atomic-term-symbol-calculator
   ```

2. **Use command-line interface:**
   ```bash
   atomic-term-calculator
   ```

3. **Import in Python:**
   ```python
   from atomic_term_symbol_calculator.terms import calc_term_symbols, calc_microstates
   ```

## Important Notes

- **Package name on PyPI**: `atomic-term-symbol-calculator` (with hyphens)
- **Import name**: `atomic_term_symbol_calculator` (with underscores)
- **CLI command**: `atomic-term-calculator`
- Make sure your LICENSE file exists and matches the "MIT" license specified
- The package is classified as "Beta" - change to "Production/Stable" when ready

## Troubleshooting

1. **Name already taken**: If the package name is taken, modify the `name` field in `pyproject.toml`
2. **Upload fails**: Check your API token and that you're using `__token__` as username
3. **Missing files**: Check `MANIFEST.in` includes all needed files
4. **Import errors**: Ensure all dependencies are listed correctly in `pyproject.toml`

Your package is now ready for PyPI! 🚀