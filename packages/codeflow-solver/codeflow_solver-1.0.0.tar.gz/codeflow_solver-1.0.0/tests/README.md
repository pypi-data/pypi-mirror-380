# Testing Guide

## Overview

This directory contains comprehensive tests for the SAST Set Cover Optimizer. The test suite ensures the mathematical optimization algorithms work correctly and that the package integrates properly with different environments.

## Test Structure

```
tests/
├── unit/                           # Unit tests for individual modules
│   ├── test_basic.py              # Package structure and imports
│   ├── test_sarif_parser.py       # SARIF file parsing logic
│   ├── test_severity_mapper.py    # Severity level mapping
│   ├── test_optimizer.py          # OR-Tools optimization algorithms
│   └── test_set_cover_initializer.py # Mathematical set initialization
├── integration/                    # Integration and end-to-end tests
│   ├── test_integration.py        # Complete pipeline testing
│   └── test_result_format.py      # JSON export format validation
├── data/                          # Test data files
│   ├── test_data.sarif            # Sample SARIF file with 5 vulnerabilities
│   └── test_data_mathematical_optimal_solution.json # Expected optimization results
└── __init__.py
```

## Running Tests

### All Tests
```bash
uv run pytest
```

### By Category
```bash
# Unit tests only
uv run pytest tests/unit/

# Integration tests only  
uv run pytest tests/integration/

# Specific module
uv run pytest tests/unit/test_optimizer.py
```

### With Different Output Levels
```bash
# Verbose output
uv run pytest -v

# Quiet mode
uv run pytest -q

# Show test coverage
uv run pytest --cov=src/prodsec_sast_set_cover_solver
```

### Alternative Methods
```bash
# Using standard pytest (if uv not available)
pytest

# Using Python module
python -m pytest
```

## What Gets Tested

### Unit Tests (tests/unit/)

**test_basic.py** - Package integrity
- Import functionality and module availability
- Version information and metadata
- Package structure validation
- CLI entry point verification

**test_sarif_parser.py** - SARIF file processing
- SARIF file loading and validation
- Vulnerability extraction from scan results
- Fix location identification from code flows
- Error handling for malformed files

**test_severity_mapper.py** - Security severity handling
- Severity level enumeration and mapping
- Case-insensitive severity matching
- Weight calculation for prioritization
- Unknown severity default handling

**test_optimizer.py** - Mathematical optimization
- OR-Tools solver initialization and configuration
- Set cover problem constraint creation
- Objective function minimization logic
- Solution extraction and validation
- Error handling when OR-Tools unavailable

**test_set_cover_initializer.py** - Problem setup
- Vulnerability grouping by type
- Coverage set computation for fix locations
- Type-specific mathematical set creation
- Data structure consistency validation

### Integration Tests (tests/integration/)

**test_integration.py** - End-to-end pipeline
- Complete optimization workflow from SARIF to results
- Multi-step process validation (parsing → grouping → optimization)
- Error handling across the entire pipeline
- Memory efficiency and deterministic behavior
- Cross-module integration verification

**test_result_format.py** - Export functionality
- JSON export structure validation
- Detailed and minimal export format testing
- Large dataset handling capabilities
- Mathematical notation consistency
- File naming conventions

### Test Data (tests/data/)

**test_data.sarif** - Sample vulnerability data
- Contains 5 vulnerabilities across 3 types (XSS, Path Traversal, DOM XSS)
- Includes code flow information for fix location identification
- Represents realistic SAST scan output structure

**test_data_mathematical_optimal_solution.json** - Expected results
- Known optimal solution for the test SARIF data
- Used to verify optimization algorithm correctness

## Test Requirements

### Dependencies
- pytest (testing framework)
- pytest-cov (coverage reporting)
- pytest-asyncio (async test support)
- OR-Tools (for optimization algorithm testing)

### Test Data Requirements
- Valid SARIF files with vulnerability and code flow information
- Expected optimization results for validation
- Sufficient test coverage across vulnerability types

## Performance Expectations

- **Unit tests**: Complete in under 1 second
- **Integration tests**: Complete in under 30 seconds
- **Full test suite**: Complete in under 1 minute
- **Coverage target**: 95%+ code coverage

## Troubleshooting

### Common Issues

**Import errors**: Ensure package is installed in development mode
```bash
uv pip install -e .
```

**OR-Tools not found**: Install optimization dependency
```bash
uv pip install ortools
```

**Test data missing**: Verify data files exist in tests/data/
```bash
ls tests/data/
```

### Running Specific Test Categories
```bash
# Test only SARIF parsing
uv run pytest tests/unit/test_sarif_parser.py

# Test only optimization algorithms
uv run pytest tests/unit/test_optimizer.py

# Test complete pipeline
uv run pytest tests/integration/test_integration.py
``` 