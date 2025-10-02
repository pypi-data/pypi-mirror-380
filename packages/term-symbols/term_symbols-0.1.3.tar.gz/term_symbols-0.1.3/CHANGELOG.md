# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2024-10-01

### Added
- **Comprehensive CHANGELOG.md**: Added detailed version history and release notes following Keep a Changelog format
- **Enhanced README.md**: Added Quick Start section with immediate pip installation and usage examples
- **PyPI Installation Instructions**: Clear pip install commands prominently featured
- **MANIFEST.in Updates**: Ensured CHANGELOG.md is included in package distributions

### Changed
- **Package Name**: Renamed from `atomic-term-symbol-calculator` to `term-symbols` for easier installation
- **Command-Line Interface**: Changed from `atomic-term-calculator` to `term-symbols` command
- **Improved Documentation Structure**: Reorganized README with Quick Start at the top
- **Better User Onboarding**: Installation and usage instructions are now more prominent and user-friendly
- **Version History Tracking**: Established systematic changelog maintenance for future releases

### Documentation
- Added migration guide for version upgrades
- Included planned features for future releases
- Added contributing guidelines for changelog updates
- Enhanced project structure documentation

## [0.1.2] - 2024-10-01

### Fixed
- **Critical Bug**: Fixed KeyError -6 when calculating term symbols for d5 and other complex configurations
- Fixed ML (magnetic quantum number) range calculation that was too restrictive for high angular momentum configurations
- Corrected DataFrame indexing to handle the full range of possible ML values

### Added
- Comprehensive test suite expansion from 17 to 30 tests
- **f Orbital Support**: Added extensive tests for f1, f2, f3, and f7 configurations
- **Complex Configuration Tests**: Added tests for d4, d5, d6, d7, d8, d9 configurations
- **Electron-Hole Duality Tests**: Verification that d1≡d9, d2≡d8, and f1≡f13
- **Mixed Orbital Tests**: Support for configurations like "3d1.4f1"
- Tests for large magnetic range configurations that previously failed

### Changed
- Improved ML range calculation: `ml_max = sum(abs(ml_val) for ml_val in ml)` instead of `2*max(ml)+1`
- Enhanced error handling in command-line interface
- Better documentation of quantum mechanical principles in code comments

### Technical Details
- **Root Cause**: The previous ML range calculation `2*max(ml)+1` created DataFrames with insufficient index ranges
- **Solution**: New calculation accounts for the sum of all possible magnetic quantum number contributions
- **Impact**: d5 configurations now correctly return 29 term symbols including the expected 6S5/2 ground state
- **f7 Support**: Complex f7 configurations now work correctly, returning 98 term symbols including 8S7/2

## [0.1.1] - 2024-07-21

### Added
- Initial PyPI release
- Core functionality for calculating atomic term symbols
- Support for s, p, and d orbital configurations
- Command-line interface via `atomic-term-calculator`
- Python module interface for programmatic use
- Basic test suite with 17 tests

### Features
- Calculate microstates for electron configurations
- Generate all possible term symbols with J-coupling
- Support for multiple input formats (space or dot separated)
- Russell-Saunders coupling calculations
- Pauli exclusion principle enforcement

### Dependencies
- numpy for numerical operations
- pandas for microstate tabulation
- Built-in Python modules (itertools, fractions, re)

## [0.1.0] - 2024-07-21

### Added
- Initial development version
- Core algorithm implementation
- Basic electron configuration parsing
- Term symbol generation logic

---

## Unreleased

### Planned Features
- Performance optimizations for large configurations
- Ground state identification and energy ordering
- Additional output formats (JSON, CSV)
- Enhanced documentation

### Known Issues
- f7 and higher configurations can be computationally intensive (this is expected due to quantum mechanical complexity)
- Very large mixed configurations may require significant computation time

---

## Version History Summary

| Version | Date | Key Changes |
|---------|------|-------------|
| 0.1.3 | 2024-10-01 | **Package renamed to `term-symbols`**, added changelog, enhanced README with Quick Start |
| 0.1.2 | 2024-10-01 | **Critical d5 fix**, expanded f orbital support, 30 comprehensive tests |
| 0.1.1 | 2024-07-21 | Initial PyPI release with core functionality |
| 0.1.0 | 2024-07-21 | Development version |

## Migration Guide

### Upgrading to 0.1.3
- **Package renamed**: Now install with `pip install term-symbols` instead of `atomic-term-symbol-calculator`
- **Command changed**: Use `term-symbols` instead of `atomic-term-calculator`
- **Import unchanged**: Python imports remain the same (`from atomic_term_symbol_calculator.terms import ...`)
- Enhanced documentation and changelog added
- All existing functionality preserved

### Upgrading from 0.1.1 to 0.1.2
- No breaking changes
- All existing code will continue to work
- d5 and complex configurations that previously crashed now work correctly
- Update with: `pip install --upgrade atomic-term-symbol-calculator`

## Contributing

When contributing, please:
1. Update this changelog with your changes
2. Follow the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
3. Add appropriate tests for new functionality
4. Ensure all tests pass before submitting