# CLAI Publishing Guide

This guide will help you publish CLAI to PyPI so others can install it with `pip install clai`.

## Prerequisites

1. **PyPI Account**: Create accounts on both:
   - [Test PyPI](https://test.pypi.org/) (for testing)
   - [PyPI](https://pypi.org/) (for production)

2. **API Tokens**: Generate API tokens for both accounts:
   - Go to Account Settings → API tokens
   - Create a token with "Entire account" scope
   - Save these tokens securely

## Step-by-Step Publishing Process

### 1. Prepare Your Package

Make sure you've updated the following files with your information:

- `setup.py`: Update author, email, and GitHub URL ✅ (Updated to AndreyZ)
- `pyproject.toml`: Update author, email, and repository URLs ✅ (Updated to AndreyZ)
- `clai/__init__.py`: Update author and email ✅ (Updated to AndreyZ)
- `README.md`: Update GitHub URLs and author information ✅ (Updated to AndreyZ)

### 2. Test Locally

```bash
# Install in development mode
python dev_setup.py

# Test the CLI
clai --help
clai --config  # Set up your Gemini API key
clai list files in current directory
```

### 3. Run Tests

```bash
python test_clai.py
```

### 4. Publish to Test PyPI (Recommended First)

```bash
# Run the publishing script
python publish.py

# Choose option 1 (Test PyPI)
# Enter your Test PyPI credentials when prompted
```

### 5. Test Installation from Test PyPI

```bash
# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ clai

# Test it works
clai --help
```

### 6. Publish to Production PyPI

```bash
# Run the publishing script again
python publish.py

# Choose option 2 (PyPI)
# Enter your PyPI credentials when prompted
```

### 7. Verify Installation

```bash
# Install from PyPI
pip install clai

# Test it works
clai --help
```

## Manual Publishing (Alternative)

If you prefer to do it manually:

```bash
# Install build tools
pip install build twine

# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Check the package
twine check dist/*

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*
```

## Configuration for Automated Publishing

For automated publishing (CI/CD), you can use API tokens:

```bash
# Set environment variables
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your_pypi_token

# Upload without interactive prompts
twine upload dist/*
```

## Version Management

To release a new version:

1. Update version in `setup.py`, `pyproject.toml`, and `clai/__init__.py`
2. Update `CHANGELOG.md` (if you have one)
3. Commit changes and tag the release:
   ```bash
   git add .
   git commit -m "Release v0.1.1"
   git tag v0.1.1
   git push origin main --tags
   ```
4. Follow the publishing process above

## Troubleshooting

### Common Issues

1. **"Package already exists"**: You can't overwrite a version on PyPI. Increment the version number.

2. **"Invalid credentials"**: Make sure you're using the correct username/password or API token.

3. **"Package name already taken"**: Choose a different package name in `setup.py` and `pyproject.toml`.

4. **Missing files**: Make sure `MANIFEST.in` includes all necessary files.

### Getting Help

- [PyPI Help](https://pypi.org/help/)
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)

## Security Notes

- Never commit API keys or tokens to version control
- Use API tokens instead of passwords when possible
- Consider using keyring for credential storage
- Review your package contents before publishing

## Success! 🎉

Once published, users can install your tool with:

```bash
pip install clai
```

And use it immediately:

```bash
clai --config  # Set up Gemini API key
clai list all files in current directory
```
