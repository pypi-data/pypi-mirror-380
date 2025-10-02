# Release Notes - Version 0.1.4

## Overview

Version 0.1.4 completes the package rename with **clean, consistent module structure** throughout.

## BREAKING CHANGES

### Clean Import Structure
- **Old imports**: `from atomic_term_symbol_calculator.terms import calc_term_symbols`
- **New imports**: `from term_symbols.terms import calc_term_symbols`

### Complete Consistency
- **Package name**: `term-symbols` (install with pip)
- **Command name**: `term-symbols` (CLI command)
- **Module name**: `term_symbols` (Python imports)

## Installation

```bash
# Install the package
pip install term-symbols
```

## Usage

```bash
# Command line interface
term-symbols
# Enter: 2p2

# Python usage with clean imports
python -c "from term_symbols.terms import calc_term_symbols; print(calc_term_symbols('2p2'))"
# Output: ['1D2', '3P0', '3P1', '3P2', '1S0']
```

## What Changed

### Module Structure
- Renamed source directory: `src/atomic_term_symbol_calculator/` → `src/term_symbols/`
- Updated all internal imports and references
- Updated test suite to use new module structure
- Updated all documentation and examples

### Functionality
- **No functional changes** - all calculations work exactly the same
- **All 30 tests pass** - comprehensive coverage maintained
- **Same performance** - d5 fix from 0.1.2 still works perfectly

## Technical Details

- Updated `pyproject.toml` paths and entry points
- Rebuilt package with new module structure
- All examples and documentation updated
- Clean, professional package structure

## Files Changed

- `src/term_symbols/__init__.py` - Version bump to 0.1.4
- `src/atomic_term_symbol_calculator/` → `src/term_symbols/` - Complete directory rename
- `tests/test_terms.py` - Updated all imports
- `README.md` - Updated all examples
- `CHANGELOG.md` - Added 0.1.4 section
- `pyproject.toml` - Updated paths and entry points

## Build Verification

✅ Package builds successfully  
✅ All 30 tests pass  
✅ Twine check passes  
✅ Clean imports work  
✅ CLI command works  
✅ Ready for PyPI upload  

## Ready to Publish

```bash
twine upload dist/*
```

This version provides the clean, professional package structure users expect with consistent naming throughout.

---

**Full changelog**: [CHANGELOG.md](CHANGELOG.md)