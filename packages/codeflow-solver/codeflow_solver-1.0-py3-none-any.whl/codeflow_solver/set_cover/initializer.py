"""
Set cover initialization module for preparing mathematical sets and variables.
"""

from collections import defaultdict
from typing import Dict, List, Set

from ..utils.data_structures import FixLocation, Vulnerability


class SetCoverInitializer:
    """
    Initializes mathematical sets and variables for set cover optimization.

    Prepares type-specific vulnerability and fix location sets for optimization:
    - V_by_type[t] = subset of V containing only vulnerabilities of type t
    - Sv_by_type[t][i] = Sᵥ(nᵢ) for vulnerability type t
    """

    def __init__(self, vulnerabilities: List[Vulnerability], fix_locations: List[FixLocation]):
        """
        Initialize set cover data structures.

        Args:
            vulnerabilities: Complete vulnerability set V
            fix_locations: Complete fix location set N
        """
        self.V_all = vulnerabilities
        self.N_all = fix_locations

        # Type-specific mathematical sets
        self.V_by_type: Dict[str, Set[int]] = {}
        self.Sv_by_type: Dict[str, Dict[int, Set[int]]] = {}

    def partition_sets_by_vulnerability_type(self) -> None:
        """
        Partition mathematical sets by vulnerability type.

        For each vulnerability type t:
        - V_t ⊆ V = subset of vulnerabilities of type t
        - N_t ⊆ N = subset of fix locations relevant to type t
        - Sᵥ_t(nᵢ) = coverage set restricted to vulnerabilities of type t
        """
        print("\nPartitioning sets by vulnerability type...")

        self._detect_vulnerability_types()
        self._create_V_subsets_by_type()
        self._create_Sv_coverage_by_type()

        print("✓ Created type-specific mathematical sets for optimization")

    def _detect_vulnerability_types(self) -> None:
        """Detect all vulnerability types T = {t₁, t₂, ..., tₖ}."""
        print("Detecting vulnerability types T = {t₁, t₂, ..., tₖ}...")

        type_counts = defaultdict(int)
        for vuln in self.V_all:
            type_counts[vuln.rule_id] += 1

        print(f"Found |T| = {len(type_counts)} vulnerability types:")
        for rule_id, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {rule_id}: {count} vulnerabilities")

    def _create_V_subsets_by_type(self) -> None:
        """
        Create V_t ⊆ V for each vulnerability type t.

        V_t = {vⱼ ∈ V : vⱼ has type t}
        """
        print("Creating vulnerability subsets V_t for each type t...")

        for vuln in self.V_all:
            vuln_type = vuln.rule_id
            if vuln_type not in self.V_by_type:
                self.V_by_type[vuln_type] = set()

            self.V_by_type[vuln_type].add(vuln.index)

        print(f"Created {len(self.V_by_type)} vulnerability subsets:")
        for vuln_type, V_subset in self.V_by_type.items():
            print(f"  |V_{vuln_type}| = {len(V_subset)} vulnerabilities")

    def _create_Sv_coverage_by_type(self) -> None:
        """
        Create type-specific coverage sets Sᵥ_t(nᵢ) for each vulnerability type t.

        For each type t and fix location nᵢ:
        Sᵥ_t(nᵢ) = Sᵥ(nᵢ) ∩ V_t = vulnerabilities of type t covered by nᵢ
        """
        print("Computing type-specific coverage sets Sᵥ_t(nᵢ)...")

        for vuln_type in self.V_by_type:
            self.Sv_by_type[vuln_type] = {}
            V_subset = self.V_by_type[vuln_type]

            # For each fix location nᵢ, compute Sᵥ_t(nᵢ) = Sᵥ(nᵢ) ∩ V_t
            for i, fix_location_ni in enumerate(self.N_all):
                # Intersect coverage with vulnerabilities of this type
                Sv_t_ni = fix_location_ni.covered_vulnerabilities.intersection(V_subset)

                # Only include fix locations that cover vulnerabilities of this type
                if Sv_t_ni:
                    self.Sv_by_type[vuln_type][i] = Sv_t_ni

        print(f"Created coverage sets for {len(self.Sv_by_type)} vulnerability types:")
        for vuln_type, coverage_dict in self.Sv_by_type.items():
            print(f"  |N_{vuln_type}| = {len(coverage_dict)} relevant fix locations")

    def get_vulnerability_types(self) -> List[str]:
        """
        Get list of all vulnerability types.

        Returns:
            List of vulnerability type strings
        """
        return list(self.V_by_type.keys())

    def get_type_specific_data(self, vuln_type: str) -> tuple:
        """
        Get type-specific vulnerability and coverage data.

        Args:
            vuln_type: Vulnerability type to get data for

        Returns:
            Tuple of (V_t, Sv_t) where:
            - V_t is the set of vulnerability indices for this type
            - Sv_t is the coverage mapping for this type
        """
        V_t = self.V_by_type.get(vuln_type, set())
        Sv_t = self.Sv_by_type.get(vuln_type, {})
        return V_t, Sv_t

    def get_statistics(self) -> Dict[str, int]:
        """
        Get statistics about the initialized sets.

        Returns:
            Dictionary with statistics about vulnerabilities and fix locations
        """
        return {
            "total_vulnerabilities": len(self.V_all),
            "total_fix_locations": len(self.N_all),
            "vulnerability_types": len(self.V_by_type),
            "max_vulnerabilities_per_type": max(len(v) for v in self.V_by_type.values()) if self.V_by_type else 0,
            "min_vulnerabilities_per_type": min(len(v) for v in self.V_by_type.values()) if self.V_by_type else 0,
        }
