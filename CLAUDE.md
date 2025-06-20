# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"descuentos" is a Python command-line program that calculates discounts applied to a base amount. The program takes two parameters: the base amount and the discount percentage, returning the final amount after applying the discount.

## Development Setup

This is a Python 3 project with no external dependencies beyond the standard library.

### Running Tests
```bash
python3 -m unittest test_descuentos.py -v
```

### Running the Program
```bash
python3 descuentos.py <importe> <descuento>
# Example: python3 descuentos.py 100 15
```

## Architecture

- `descuentos.py`: Main program with the `calcular_descuento()` function and command-line interface
- `test_descuentos.py`: Comprehensive unit tests covering normal cases, edge cases, and error handling

### Key Functions
- `calcular_descuento(importe, descuento)`: Core calculation function with input validation
- `main()`: Command-line interface handler with error handling

## Validation Rules
- Base amount (importe) must be non-negative
- Discount percentage must be between 0 and 100 inclusive
- Both parameters must be numeric values

## Documentation
Both Python files are fully documented with comprehensive docstrings following Python standards:

### descuentos.py Documentation
- Module-level docstring with program overview, usage examples, and metadata
- Function-level docstrings with detailed parameter descriptions, return values, exceptions, and examples
- Complete documentation of the command-line interface and error handling

### test_descuentos.py Documentation  
- Module-level docstring explaining the test suite architecture and reporting system
- Class-level docstrings for TestResult and TestDescuentos classes
- Method-level docstrings for all test cases explaining what each test validates
- Documentation of the automated report generation system

### Accessing Documentation
Use Python's built-in help system to view documentation:
```bash
python3 -c "import descuentos; help(descuentos)"
python3 -c "import descuentos; help(descuentos.calcular_descuento)"
```