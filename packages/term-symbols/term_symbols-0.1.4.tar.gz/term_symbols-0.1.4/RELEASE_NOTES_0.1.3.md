# Release Notes - Version 0.1.3

## Overview

Version 0.1.3 features a **package rename** for easier installation, plus improved documentation and user experience.

## What's New

### 🏷️ **Package Rename**
- **New package name**: `term-symbols` (much shorter and easier to type!)
- **New command**: `term-symbols` instead of `atomic-term-calculator`
- **Clean imports**: Python imports now `from term_symbols.terms import ...` (consistent naming!)

### 📚 Comprehensive Documentation
- **Added CHANGELOG.md**: Complete version history following Keep a Changelog format
- **Enhanced README.md**: Added Quick Start section for immediate usage
- **Better Installation Guide**: PyPI installation prominently featured

### 🚀 Improved User Onboarding
- **Quick Start Section**: Shows installation and usage in first few lines of README
- **Copy-Paste Examples**: Ready-to-use commands for immediate testing
- **Clear Installation Path**: `pip install term-symbols`

### 📦 Package Improvements
- **MANIFEST.in Updates**: Ensures CHANGELOG.md is included in distributions
- **Documentation Structure**: Better organized information hierarchy

## Installation

```bash
# New package name (much shorter!)
pip install term-symbols
```

## Quick Test

```bash
# Test the command line
term-symbols
# Enter: 2p2

# Test Python import (clean new imports!)
python -c "from term_symbols.terms import calc_term_symbols; print(calc_term_symbols('2p2'))"
# Expected output: ['1D2', '3P0', '3P1', '3P2', '1S0']
```

## No Breaking Changes

All existing code continues to work exactly as before. This is purely a documentation and user experience improvement.

## Files Changed

- `src/atomic_term_symbol_calculator/__init__.py` - Version bump to 0.1.3
- `CHANGELOG.md` - Added (new file with complete version history)
- `README.md` - Enhanced with Quick Start section
- `MANIFEST.in` - Updated to include CHANGELOG.md

## Build Verification

✅ Package builds successfully  
✅ All 30 tests pass  
✅ Twine check passes  
✅ Ready for PyPI upload  

## Next Steps

Ready to publish to PyPI with:

```bash
twine upload dist/*
```

## Future Roadmap

- Performance optimizations for large configurations
- Ground state identification
- Additional output formats (JSON, CSV)
- Enhanced documentation with chemistry examples

---

**Full changelog**: [CHANGELOG.md](CHANGELOG.md)