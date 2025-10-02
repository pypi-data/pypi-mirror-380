"""
OR-Tools optimizer for set cover problems.
"""

from typing import Dict, List, Set

from ..utils.data_structures import FixLocation

# OR-Tools import for mathematical optimization
try:
    from ortools.linear_solver import pywraplp

    HAS_ORTOOLS = True
except ImportError:
    HAS_ORTOOLS = False


class SetCoverOptimizer:
    """
    OR-Tools based optimizer for set cover problems.

    Solves the mathematical formulation:
    Variables: xᵢ ∈ {0,1} for each nᵢ ∈ N_t
    Objective: Minimize Σxᵢ
    Constraints: For each vⱼ ∈ V_t, Σ(xᵢ: vⱼ ∈ Sᵥ_t(nᵢ)) ≥ 1
    """

    def __init__(self):
        """Initialize the optimizer."""
        if not HAS_ORTOOLS:
            raise ImportError("OR-Tools not available. Install with: pip install ortools")

    def solve_single_set_cover_problem(
        self, vuln_type: str, V_t: Set[int], Sv_t: Dict[int, Set[int]], N_all: List[FixLocation]
    ) -> List[FixLocation]:
        """
        Solve set cover problem for a single vulnerability type.

        Mathematical formulation:
        - V_t = vulnerability set for type t
        - N_t = relevant fix locations for type t
        - xᵢ = decision variables (1 if fix at location i, 0 otherwise)
        - Objective: min Σxᵢ
        - Constraints: ∀vⱼ ∈ V_t, Σ(xᵢ: vⱼ ∈ Sᵥ_t(nᵢ)) ≥ 1

        Args:
            vuln_type: Vulnerability type being optimized
            V_t: Set of vulnerability indices for this type
            Sv_t: Coverage mapping {location_index: covered_vulnerabilities}
            N_all: Complete list of fix locations

        Returns:
            List of optimal fix locations for this vulnerability type
        """
        if not V_t or not Sv_t:
            print(f"  No data for {vuln_type}")
            return []

        print(f"  |V_t| = {len(V_t)} vulnerabilities, |N_t| = {len(Sv_t)} fix locations")

        # Create OR-Tools SCIP solver for integer linear programming
        solver = pywraplp.Solver.CreateSolver("SCIP")
        if not solver:
            print(f"  ERROR: SCIP solver unavailable for {vuln_type}")
            return []

        # Decision variables: xᵢ ∈ {0,1} for each fix location nᵢ ∈ N_t
        x = {}  # x[i] represents xᵢ in mathematical notation
        for location_index in Sv_t.keys():
            x[location_index] = solver.IntVar(0, 1, f"x_{location_index}")

        # Coverage constraints: ∀vⱼ ∈ V_t, Σ(xᵢ: vⱼ ∈ Sᵥ_t(nᵢ)) ≥ 1
        print(f"  Creating coverage constraints for {len(V_t)} vulnerabilities...")
        for vuln_j in V_t:
            # Find all fix locations nᵢ that can cover vulnerability vⱼ
            covering_locations = []
            for location_i, Sv_t_ni in Sv_t.items():
                if vuln_j in Sv_t_ni:  # if vⱼ ∈ Sᵥ_t(nᵢ)
                    covering_locations.append(location_i)

            # Create constraint: Σ(xᵢ: vⱼ ∈ Sᵥ_t(nᵢ)) ≥ 1
            if covering_locations:
                constraint = solver.Constraint(1, solver.infinity())
                for location_i in covering_locations:
                    constraint.SetCoefficient(x[location_i], 1)

        # Objective function: Minimize Σxᵢ (minimize number of selected fix locations)
        objective = solver.Objective()
        for location_index in Sv_t.keys():
            objective.SetCoefficient(x[location_index], 1)
        objective.SetMinimization()

        # Solve the optimization problem
        print("  Solving integer linear program...")
        status = solver.Solve()

        # Extract optimal solution
        if status == pywraplp.Solver.OPTIMAL:
            optimal_locations = []
            for location_i, xi_var in x.items():
                if xi_var.solution_value() > 0.5:  # xᵢ = 1 (location selected)
                    optimal_locations.append(N_all[location_i])

            print(f"  ✓ OPTIMAL: {len(optimal_locations)} fix locations needed")
            return optimal_locations
        else:
            print(f"  ✗ No optimal solution found for {vuln_type}")
            return []

    def solve_all_set_cover_problems(
        self, V_by_type: Dict[str, Set[int]], Sv_by_type: Dict[str, Dict[int, Set[int]]], N_all: List[FixLocation]
    ) -> Dict[str, List[FixLocation]]:
        """
        Solve set cover problems for all vulnerability types.

        Args:
            V_by_type: Vulnerability sets by type
            Sv_by_type: Coverage mappings by type
            N_all: Complete list of fix locations

        Returns:
            Dictionary mapping vulnerability type to optimal fix locations
        """
        print("\nSolving set cover optimization problems...")

        x_optimal_by_type = {}

        for vuln_type in V_by_type:
            print(f"\nSolving set cover problem for vulnerability type: {vuln_type}")
            V_t, Sv_t = V_by_type[vuln_type], Sv_by_type[vuln_type]
            optimal_solution = self.solve_single_set_cover_problem(vuln_type, V_t, Sv_t, N_all)
            x_optimal_by_type[vuln_type] = optimal_solution

        return x_optimal_by_type
