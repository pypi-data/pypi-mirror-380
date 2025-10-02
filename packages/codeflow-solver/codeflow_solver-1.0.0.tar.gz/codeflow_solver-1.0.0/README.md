# CodeFlow Solver

## Overview

A tool that finds the optimal minimum number of code fixes needed to eliminate all vulnerabilities from SARIF scan results. Uses the set cover problem optimization to determine the most efficient fix strategy - guaranteeing the absolute minimum number of code changes required to address all security issues.

**📖 For detailed algorithm explanation, mathematical formulation, and implementation details, see [src/codeflow_solver/docs/MATHEMATICAL_DETAILS.md](src/codeflow_solver/docs/MATHEMATICAL_DETAILS.md)**

## Installation

### From PyPI

```bash
pip install codeflow-solver
```

### From Source

```bash
git clone <repository-url>
cd solver
uv sync
uv pip install -e .
```

## Usage

### CLI Options

```bash
# Basic usage
codeflow-solver vulnerabilities.sarif

# Filtering options
codeflow-solver vulnerabilities.sarif --severity-filter high medium
codeflow-solver vulnerabilities.sarif --rule-filter java/XSS java/PT

# Export options
codeflow-solver vulnerabilities.sarif --export              # Detailed solution with vulnerability details
codeflow-solver vulnerabilities.sarif --minimal-export     # Optimal path with fix locations only

# Quiet mode
codeflow-solver vulnerabilities.sarif --quiet --minimal-export
```

### Using as Package

```python
from codeflow_solver import SarifSetCoverSolver

# Basic usage
optimizer = SarifSetCoverSolver("vulnerabilities.sarif")
optimizer.solve_mathematical_optimization()

# With filtering and export
optimizer = SarifSetCoverSolver(
    "vulnerabilities.sarif",
    severity_filter=["high", "medium"],
    rule_filter=["java/XSS"],
    export_detailed=True
)
optimizer.solve_mathematical_optimization()
```

### CLI After Cloning

```bash
cd solver
uv run python -m codeflow_solver.cli.main vulnerabilities.sarif

# Available options:
# --severity-filter {high,medium,low,info}  Filter by severity
# --rule-filter RULE_ID [RULE_ID ...]      Filter by rule IDs  
# --export                                  Export detailed solution
# --minimal-export                          Export minimal solution
# --quiet                                   Suppress console output
```

## Package Structure

```
src/
└── codeflow_solver/
    ├── __init__.py
    ├── cli/
    │   ├── __init__.py
    │   └── main.py             # CLI entry point
    ├── utils/
    │   ├── __init__.py
    │   ├── sarif_parser.py     # SARIF parsing
    │   ├── severity_mapper.py  # Severity mapping
    │   └── data_structures.py  # Data classes
    ├── solver/
    │   ├── __init__.py
    │   ├── set_cover_solver.py # Main solver implementation
    │   └── optimizer.py        # Optimization algorithms
    ├── set_cover/
    │   ├── __init__.py
    │   └── initializer.py      # Set cover initialization
    └── docs/                   # Documentation
tests/                          # Test files
```

## Tests

```bash
# Run tests
uv run pytest

# Format and lint
uv run ruff format .
uv run ruff check .
uv run mypy .
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request