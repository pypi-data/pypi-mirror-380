# Atomic Term Symbol Calculator

A Python package for calculating all possible atomic term symbols from electron configurations. This tool uses quantum mechanical principles to determine microstates and derive term symbols including J-coupling.

## Features

- Calculate total number of microstates for any electron configuration
- Generate all possible term symbols from electron configurations
- Support for s, p, d, and f orbitals
- Handles multiple electron shells and mixed configurations
- Applies Pauli exclusion principle and Hund's rules
- Calculates J quantum numbers using Russell-Saunders coupling
- Flexible input format (space or dot separated orbitals)

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/ccheung93/atomic-term-symbol-calculator.git
cd atomic-term-symbol-calculator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

4. To install with testing dependencies:
```bash
pip install -e .[test]
```

### Requirements

- Python ≥ 3.8
- numpy
- pandas
- fractions (built-in)
- itertools (built-in)
- re (built-in)

## Usage

### As a Python Module

```python
from atomic_term_symbol_calculator.terms import calc_term_symbols, calc_microstates

# Calculate term symbols for carbon (2p2)
terms = calc_term_symbols("2p2")
print(terms)
# Output: ['3P0', '3P1', '3P2', '1D2', '1S0']

# Calculate microstates for p2 configuration
microstates = calc_microstates(6, 2)  # 6 positions, 2 electrons
print(microstates)
# Output: 15

# Mixed orbital configurations
terms = calc_term_symbols("2s1.2p1")
print(terms)
# Output: ['3P0', '3P1', '3P2', '1P1']

# d orbital configurations
terms = calc_term_symbols("3d2")
print(terms)
```

### Command Line Usage

```bash
python -m atomic_term_symbol_calculator.terms
# Enter configuration when prompted: 2p3
```

### Input Format

Electron configurations can be specified in two formats:

1. **Dot separated**: `2s1.2p3.3d2`
2. **Space separated**: `2s1 2p3 3d2`

The occupancy number can be omitted if it's 1:
- `2p1` is equivalent to `2p`
- `3d1` is equivalent to `3d`

### Examples

| Configuration | Description | Example Terms |
|---------------|-------------|---------------|
| `1s1` | Hydrogen | `2S1/2` |
| `2p1` | Boron | `2P1/2`, `2P3/2` |
| `2p2` | Carbon | `3P0`, `3P1`, `3P2`, `1D2`, `1S0` |
| `2p3` | Nitrogen | `4S3/2`, `2D3/2`, `2D5/2`, `2P1/2`, `2P3/2` |
| `3d1` | Sc²⁺ | `2D3/2`, `2D5/2` |
| `3d5` | Mn²⁺ | Multiple terms (high-spin d5) |

## Testing

Run the test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests for a specific file:

```bash
pytest tests/test_terms.py
```

Run tests with coverage:

```bash
pytest --cov=atomic_term_symbol_calculator
```

## Development

### Project Structure

```
atomic-term-symbol-calculator/
├── src/
│   └── atomic_term_symbol_calculator/
│       ├── __init__.py          # Version info
│       └── terms.py             # Main calculation functions
├── tests/
│   └── test_terms.py           # Comprehensive test suite
├── pyproject.toml              # Project configuration
├── README.md                   # This file
└── CLAUDE.md                   # Development guidance
```

### Algorithm Overview

The calculator follows these steps:

1. **Parse Configuration**: Extract orbital types and electron counts
2. **Generate Microstates**: Create all possible electron arrangements
3. **Apply Quantum Rules**: Filter using Pauli exclusion principle
4. **Tabulate States**: Create ML vs MS quantum number table
5. **Extract Terms**: Systematically remove term symbols from table
6. **Calculate J Values**: Apply |L-S| ≤ J ≤ |L+S| coupling rules

### Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## References

- [Term Symbols Notes](https://ccheung93.github.io/notes/term_symbols/)
- Russell-Saunders coupling theory
- Quantum mechanical principles of atomic structure

## Author

Charles Cheung (ccheung@udel.edu)