# Homebrew Distribution Guide

This guide explains how to install `corclient` via Homebrew using the same repository as a custom Tap.

## 🍺 Installation

### For Users

Users can install `corclient` directly from this repository:

```bash
# Add the tap (one-time setup)
brew tap ProjectCORTeam/corcli https://github.com/ProjectCORTeam/corcli.git

# Install corclient
brew install corclient

# Or in one command
brew install ProjectCORTeam/corcli/corclient
```

### Update

```bash
brew update
brew upgrade corclient
```

### Uninstall

```bash
brew uninstall corclient
brew untap ProjectCORTeam/corcli
```

## 🔧 How It Works

This repository serves dual purposes:
1. **Source code repository** - Contains the Python package code
2. **Homebrew Tap** - Contains Homebrew formulae in `HomebrewFormula/`

When users tap this repository, Homebrew looks for formulae in the `HomebrewFormula/` directory.

## 🚀 Automated Updates

The workflow `.github/workflows/homebrew-formula.yaml` automatically:

1. **Triggers when a GitHub Release is published**
2. **Downloads the tarball from PyPI**
3. **Calculates the SHA256 hash**
4. **Updates the Homebrew formula** in `HomebrewFormula/corclient.rb`
5. **Commits and pushes to the repository**

No separate repository needed!

## 📦 Manual Formula Update

If you need to manually update the formula:

```bash
# 1. Get the version and tarball
VERSION="1.0.0"
wget "https://files.pythonhosted.org/packages/source/c/corclient/corclient-${VERSION}.tar.gz"

# 2. Calculate SHA256
SHA256=$(sha256sum corclient-${VERSION}.tar.gz | awk '{print $1}')

# 3. Update HomebrewFormula/corclient.rb
# Replace the url and sha256 values

# 4. Test the formula
brew install --build-from-source ./HomebrewFormula/corclient.rb

# 5. Commit and push
git add HomebrewFormula/corclient.rb
git commit -m "chore: update Homebrew formula to ${VERSION}"
git push
```

## 🧪 Testing

### Local Testing

```bash
# Test installation from local formula
brew install --build-from-source ./HomebrewFormula/corclient.rb

# Verify it works
cor --help

# Run formula audit
brew audit --strict ./HomebrewFormula/corclient.rb

# Test uninstall
brew uninstall corclient
```

### Test the Tap

```bash
# Add your local repo as a tap
brew tap ProjectCORTeam/corcli /Users/carlos/Documents/04-Repositories/COR/corcli-cli

# Install from the tap
brew install corclient

# Test
cor --help

# Clean up
brew uninstall corclient
brew untap ProjectCORTeam/corcli
```

## 📝 Repository Structure

```
corcli/
├── corecli/                          # Python package source
├── HomebrewFormula/                  # Homebrew formulae directory
│   └── corclient.rb                  # Homebrew formula
├── .github/workflows/
│   ├── pypi-release.yaml            # PyPI publication
│   ├── homebrew-formula.yaml        # Auto-update Homebrew formula
│   └── release.yaml                 # Semantic release
├── pyproject.toml                   # Python package config
└── README.md                        # Main documentation
```

## 🔍 Troubleshooting

### Formula Not Found

```bash
# Re-add the tap
brew untap ProjectCORTeam/corcli
brew tap ProjectCORTeam/corcli https://github.com/ProjectCORTeam/corcli.git
```

### Installation Fails

1. Check Python version: `brew info python@3.11`
2. Clear cache: `brew cleanup`
3. Try with verbose output: `brew install corclient --verbose`

### Version Not Updating

```bash
# Force update the tap
brew update
brew upgrade corclient

# Or reinstall
brew reinstall corclient
```

## 📚 Adding the Tap to README

Add this section to your main README.md:

```markdown
### Install via Homebrew

\`\`\`bash
# Add the tap
brew tap ProjectCORTeam/corcli https://github.com/ProjectCORTeam/corcli.git

# Install
brew install corclient
\`\`\`

### Update

\`\`\`bash
brew update
brew upgrade corclient
\`\`\`
```

## 🎯 Advantages of Single Repository

✅ **Simplified maintenance** - One repository to manage
✅ **Synchronized versioning** - Formula updates with releases
✅ **Automatic updates** - Workflow handles everything
✅ **No extra setup** - No separate tap repository needed
✅ **Single source of truth** - Code and distribution in one place

## 🔗 Resources

- [Homebrew Taps](https://docs.brew.sh/Taps)
- [Formula Cookbook](https://docs.brew.sh/Formula-Cookbook)
- [Python Formula Guide](https://docs.brew.sh/Python-for-Formula-Authors)

---

**Note**: The formula directory MUST be named `HomebrewFormula/` (or `Formula/`) for Homebrew to recognize it as a tap.
