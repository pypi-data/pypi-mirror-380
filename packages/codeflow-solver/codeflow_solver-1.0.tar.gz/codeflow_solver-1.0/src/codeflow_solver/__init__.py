"""
SARIF Set Cover Optimizer - Mathematical Optimization for Vulnerability Remediation

A Python package that applies Integer Linear Programming to find the minimum
number of code fixes needed to eliminate all vulnerabilities from SARIF output.
"""

__version__ = "1.0.0"
__author__ = "Amine Boudraa"
__description__ = "Mathematical optimization for vulnerability remediation using set cover algorithms"

from .cli.main import main
from .solver.set_cover_solver import SarifSetCoverSolver

__all__ = ["main", "SarifSetCoverSolver"]
