# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an atomic term symbol calculator that determines all possible atomic term symbols from electron configurations. The package calculates microstates and term symbols using quantum mechanical principles.

## Development Commands

### Testing
```bash
pytest
```

### Package Installation (Development)
```bash
pip install -e .
```

### Installing Test Dependencies
```bash
pip install -e .[test]
```

## Code Architecture

### Core Module Structure
- `src/atomic_term_symbol_calculator/terms.py` - Main calculation logic
  - `calc_microstates()` - Calculates total number of microstates
  - `calc_term_symbols()` - Main function that determines all possible term symbols from electron configuration
- `src/atomic_term_symbol_calculator/__init__.py` - Package version definition
- `tests/test_terms.py` - Unit tests for the calculation functions

### Key Dependencies
- `numpy` - Numerical computations and array operations
- `pandas` - DataFrame operations for microstate tabulation
- `itertools` - Combinatorial calculations for electron configurations
- `fractions` - Handling fractional J quantum numbers

### Algorithm Overview
The term symbol calculation follows these steps:
1. Parse electron configuration (format: "2s.2p3" or "2s 2p3")
2. Generate all possible microstates using combinatorial methods
3. Apply Pauli exclusion principle to filter valid configurations
4. Create a table mapping total orbital (ML) and spin (MS) quantum numbers
5. Extract term symbols by systematically removing microstates from the table
6. Calculate J quantum numbers using |L-S| ≤ J ≤ |L+S| coupling rules

### Input Format
Electron configurations should be formatted with '.' or ' ' separating orbitals (e.g., "2s.2p3" or "2s 2p3").

### Testing Strategy
The project uses pytest with test files in the `tests/` directory. The test configuration in `pyproject.toml` sets the Python path to include `src/` for proper module importing.