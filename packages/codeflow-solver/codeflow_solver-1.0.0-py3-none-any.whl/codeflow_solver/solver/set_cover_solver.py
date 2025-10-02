"""
Main SARIF Set Cover Solver that orchestrates the optimization process.
"""

import datetime
import json
from typing import Dict, List

from ..set_cover.initializer import SetCoverInitializer
from ..utils.data_structures import FixLocation, Vulnerability
from ..utils.sarif_parser import SarifParser
from .optimizer import SetCoverOptimizer


class SarifSetCoverSolver:
    """
    SARIF Vulnerability Fix Optimizer.

    Finds the minimum number of code fixes needed to resolve all vulnerabilities:
    - Analyzes SARIF files to identify vulnerabilities and potential fix locations
    - For each vulnerability type, finds the optimal set of fixes
    - Uses advanced optimization to guarantee the best solution
    """

    def __init__(self, sarif_file_path: str, severity_filter: List[str] = None, rule_filter: List[str] = None, quiet: bool = False, export_detailed: bool = False, minimal_export: bool = False):
        """
        Initialize the SARIF Set Cover Solver.

        Args:
            sarif_file_path: Path to the SARIF file to analyze
            severity_filter: List of severity levels to include (high, medium, low, info)
            rule_filter: List of rule IDs to include
            quiet: If True, suppress all output except file export
            export_detailed: If True, export detailed JSON analysis with vulnerability details
            minimal_export: If True, export minimal JSON with only fix metadata (MCP-friendly)
        """
        self.sarif_file_path = sarif_file_path
        self.severity_filter = severity_filter or []
        self.rule_filter = rule_filter or []
        self.quiet = quiet
        self.export_detailed = export_detailed
        self.minimal_export = minimal_export

        # Data structures
        self.V_all: List[Vulnerability] = []  # All vulnerabilities found
        self.N_all: List[FixLocation] = []  # All potential fix locations

        # Optimal fix solutions
        self.x_optimal_by_type: Dict[str, List[FixLocation]] = {}

        # Initialize components
        self.parser = SarifParser(sarif_file_path)
        self.initializer = None
        self.optimizer = SetCoverOptimizer()

    def step1_construct_mathematical_sets(self) -> None:
        """
        Step 1: Load and analyze the SARIF file.

        Extracts all vulnerabilities and potential fix locations from the SARIF file.
        """
        if not self.quiet:
            print("STEP 1: LOADING AND ANALYZING SARIF FILE")
        print("=" * 60)

        # Parse SARIF file
        all_vulnerabilities, self.N_all = self.parser.parse_sarif_file()
        
        # Apply filters
        self.V_all = self._apply_filters(all_vulnerabilities)

        if not self.quiet:
            print(f"✓ Found {len(self.V_all)} vulnerabilities to fix")
            print(f"✓ Identified {len(self.N_all)} potential fix locations")

    def _apply_filters(self, vulnerabilities: List[Vulnerability]) -> List[Vulnerability]:
        """
        Apply severity and rule ID filters to vulnerabilities.
        
        Args:
            vulnerabilities: List of all vulnerabilities
            
        Returns:
            Filtered list of vulnerabilities
        """
        filtered = vulnerabilities
        
        # Apply severity filter
        if self.severity_filter:
            from ..utils.severity_mapper import IssueSeverity
            allowed_severities = {IssueSeverity(sev) for sev in self.severity_filter}
            filtered = [v for v in filtered if v.severity in allowed_severities]
            if not self.quiet:
                print(f"✓ Applied severity filter: {len(filtered)} vulnerabilities match {self.severity_filter}")
        
        # Apply rule ID filter
        if self.rule_filter:
            filtered = [v for v in filtered if v.rule_id in self.rule_filter]
            if not self.quiet:
                print(f"✓ Applied rule filter: {len(filtered)} vulnerabilities match {self.rule_filter}")
        
        return filtered

    def step2_partition_sets_by_vulnerability_type(self) -> None:
        """
        Step 2: Group vulnerabilities by type for targeted optimization.

        For each vulnerability type:
        - Groups vulnerabilities of the same type together
        - Identifies relevant fix locations for each type
        - Prepares data for efficient optimization
        """
        if not self.quiet:
            print("\nSTEP 2: GROUPING VULNERABILITIES BY TYPE")
        print("=" * 60)

        self.initializer = SetCoverInitializer(self.V_all, self.N_all)
        self.initializer.partition_sets_by_vulnerability_type()

    def step3_solve_optimization_problems(self) -> None:
        """
        Step 3: Find the optimal fixes for each vulnerability type.

        For each vulnerability type:
        - Finds the minimum number of fixes needed
        - Ensures all vulnerabilities are covered
        - Uses advanced optimization for best results
        """
        if not self.quiet:
            print("\nSTEP 3: FINDING OPTIMAL FIXES")
        print("=" * 60)

        self.x_optimal_by_type = self.optimizer.solve_all_set_cover_problems(
            self.initializer.V_by_type, self.initializer.Sv_by_type, self.N_all
        )

        self._report_optimization_results()
        
        # Export based on user preference
        if self.export_detailed:
            self._export_detailed_solution()
        elif self.minimal_export:
            self._export_minimal_solution()

    def _report_optimization_results(self) -> None:
        """Generate comprehensive report of optimization results."""
        if not self.quiet:
            print("\n" + "=" * 80)
            print("OPTIMIZATION RESULTS")
            print("=" * 80)

        total_vulnerabilities = 0
        total_optimal_fixes = 0

        for vuln_type, optimal_solution in self.x_optimal_by_type.items():
            vuln_count = len(self.initializer.V_by_type[vuln_type])
            fix_count = len(optimal_solution)
            reduction_factor = vuln_count / fix_count if fix_count > 0 else 0

            total_vulnerabilities += vuln_count
            total_optimal_fixes += fix_count

            if not self.quiet:
                print(f"\nVulnerability Type: {vuln_type}")
                print(f"  {vuln_count} vulnerabilities found")
                print(f"  {fix_count} fixes needed")
                print(f"  Reduction factor: {reduction_factor:.1f}x")

            if optimal_solution and not self.quiet:
                print("  Top fix locations (highest impact):")
                for rank, location in enumerate(optimal_solution[:3], 1):
                    covered_count = len(
                        location.covered_vulnerabilities.intersection(self.initializer.V_by_type[vuln_type])
                    )
                    print(f"    {rank}. {location} → covers {covered_count} {vuln_type} vulnerabilities")

        overall_reduction = total_vulnerabilities / total_optimal_fixes if total_optimal_fixes > 0 else 0
        savings_percent = (1 - total_optimal_fixes / total_vulnerabilities) * 100 if total_vulnerabilities > 0 else 0

        if not self.quiet:
            print("\nOVERALL SUMMARY:")
            print(f"  Total {total_vulnerabilities} vulnerabilities")
            print(f"  Total {total_optimal_fixes} fixes needed")
            print(f"  Overall reduction factor: {overall_reduction:.1f}x")
            print(f"  Efficiency: {savings_percent:.1f}% effort reduction")

    def _export_detailed_solution(self) -> None:
        """Export complete solution to JSON with detailed analysis."""
        if not self.quiet:
            print("\nExporting detailed solution to JSON...")

        # Build comprehensive solution report
        solution_data = {
            "analysis_summary": {
                "total_vulnerabilities": len(self.V_all),
                "vulnerability_types_found": len(self.initializer.V_by_type),
                "potential_fix_locations": len(self.N_all),
                "analysis_timestamp": datetime.datetime.now().isoformat(),
                "optimization_method": "Advanced Integer Programming",
            },
            "fixes_by_vulnerability_type": [],
        }

        # Sort by vulnerability set size (largest problems first)
        sorted_types = sorted(self.initializer.V_by_type.items(), key=lambda x: len(x[1]), reverse=True)

        total_optimal_locations = 0
        total_vulnerabilities = 0

        for vuln_type, V_t in sorted_types:
            optimal_solution = self.x_optimal_by_type.get(vuln_type, [])
            # |V_t| = size of vulnerability set for this type
            vuln_count = len(V_t)
            # |x_optimal| = number of optimal fix locations needed
            fix_count = len(optimal_solution)

            total_vulnerabilities += vuln_count
            total_optimal_locations += fix_count

            # Sort optimal fix locations by impact (vulnerabilities covered)
            sorted_solution = sorted(
                optimal_solution, key=lambda loc: len(loc.covered_vulnerabilities.intersection(V_t)), reverse=True
            )

            # Build detailed fix location analysis
            optimal_fix_locations = []
            for rank, location in enumerate(sorted_solution):
                covered_vulns_of_type = location.covered_vulnerabilities.intersection(V_t)

                # Get detailed vulnerability information
                vulnerability_details = []
                for vuln_idx in covered_vulns_of_type:
                    if vuln_idx < len(self.V_all):
                        vuln = self.V_all[vuln_idx]
                        vulnerability_details.append(
                            {
                                "vulnerability_id": vuln_idx,
                                "file_path": vuln.file_path,
                                "line": vuln.line,
                                "rule_id": vuln.rule_id,
                                "severity": vuln.severity.value,
                                "message": vuln.message,
                            }
                        )

                # Sort for consistency
                vulnerability_details.sort(key=lambda x: (x["file_path"], x["line"]))

                fix_location_analysis = {
                    "rank": rank + 1,
                    "fix_location": {
                        "file_path": location.file_path,
                        "line": location.line,
                        "column": location.column,
                    },
                    "vulnerabilities_fixed_this_type": len(covered_vulns_of_type),
                    "total_vulnerabilities_fixed": len(location.covered_vulnerabilities),
                    "vulnerability_details": vulnerability_details,
                }

                optimal_fix_locations.append(fix_location_analysis)

            # Build type-specific analysis
            type_analysis = {
                "vulnerability_type": vuln_type,
                "total_vulnerabilities": vuln_count,
                "fixes_needed": fix_count,
                "reduction_factor": round(vuln_count / fix_count, 2) if fix_count > 0 else 0,
                "efficiency_percent": round((1 - fix_count / vuln_count) * 100, 1) if vuln_count > 0 else 0,
                "fix_locations": optimal_fix_locations,
            }

            solution_data["fixes_by_vulnerability_type"].append(type_analysis)

        # Add overall summary
        solution_data["overall_summary"] = {
            "total_vulnerabilities": total_vulnerabilities,
            "total_fixes_needed": total_optimal_locations,
            "overall_reduction_factor": round(total_vulnerabilities / total_optimal_locations, 2)
            if total_optimal_locations > 0
            else 0,
            "overall_efficiency_percent": round((1 - total_optimal_locations / total_vulnerabilities) * 100, 1)
            if total_vulnerabilities > 0
            else 0,
            "optimization_guarantee": "Guaranteed optimal solution using advanced algorithms",
        }

        # Export to file
        # Handle both .sarif and .json extensions
        if self.sarif_file_path.endswith(".sarif"):
            output_filename = self.sarif_file_path.replace(".sarif", "_optimal_fix_path.json")
        elif self.sarif_file_path.endswith(".json"):
            output_filename = self.sarif_file_path.replace(".json", "_optimal_fix_path.json")
        else:
            # Fallback for files without standard extensions
            output_filename = self.sarif_file_path + "_optimal_fix_path.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(solution_data, f, indent=2, ensure_ascii=False)

        if not self.quiet:
            print(f"✓ Detailed solution exported to: {output_filename}")
            print(
                f"✓ Contains optimal fixes for {len(solution_data['fixes_by_vulnerability_type'])} vulnerability types"
            )
            print("✓ Guaranteed optimal solution using advanced optimization")

    def _export_minimal_solution(self) -> None:
        """Export minimal solution with only fix metadata (MCP-friendly)."""
        # Calculate overall statistics
        total_vulnerabilities = len(self.V_all)
        total_optimal_locations = sum(len(fixes) for fixes in self.x_optimal_by_type.values())
        
        # Build minimal solution structure
        minimal_solution = {
            "analysis_metadata": {
                "sarif_file": self.sarif_file_path,
                "analysis_timestamp": datetime.datetime.now().isoformat(),
                "total_vulnerabilities": total_vulnerabilities,
                "total_optimal_fixes": total_optimal_locations,
                "overall_reduction_factor": round(total_vulnerabilities / total_optimal_locations, 2) if total_optimal_locations > 0 else 0,
                "efficiency_percent": round((1 - total_optimal_locations / total_vulnerabilities) * 100, 1) if total_vulnerabilities > 0 else 0
            },
            "optimal_fixes_by_type": []
        }

        # Add minimal fix information for each vulnerability type
        for vuln_type, optimal_fixes in self.x_optimal_by_type.items():
            if not optimal_fixes:
                continue
                
            # Count vulnerabilities of this type
            vuln_count = len([v for v in self.V_all if v.rule_id == vuln_type])
            fix_count = len(optimal_fixes)
            
            # Sort optimal fix locations by impact (same as full export)
            V_t = set(i for i, v in enumerate(self.V_all) if v.rule_id == vuln_type)
            sorted_fixes = sorted(
                optimal_fixes, key=lambda loc: len(loc.covered_vulnerabilities.intersection(V_t)), reverse=True
            )
            
            # Build minimal fix locations (without vulnerability details)
            minimal_fixes = []
            for rank, fix_location in enumerate(sorted_fixes, 1):  # ALL fixes
                covered_vulns_of_type = fix_location.covered_vulnerabilities.intersection(V_t)
                minimal_fix = {
                    "rank": rank,
                    "file_path": fix_location.file_path,
                    "line": fix_location.line,
                    "vulnerabilities_covered": len(covered_vulns_of_type),
                    "location_id": f"{fix_location.file_path}:{fix_location.line}"
                }
                minimal_fixes.append(minimal_fix)
            
            type_summary = {
                "vulnerability_type": vuln_type,
                "total_vulnerabilities": vuln_count,
                "optimal_fixes_needed": fix_count,
                "reduction_factor": round(vuln_count / fix_count, 2) if fix_count > 0 else 0,
                "efficiency_percent": round((1 - fix_count / vuln_count) * 100, 1) if vuln_count > 0 else 0,
                "top_fixes": minimal_fixes
            }
            
            minimal_solution["optimal_fixes_by_type"].append(type_summary)

        # Export minimal solution
        output_filename = self.sarif_file_path.replace(".sarif", "_minimal_fix_path.json")
        if self.sarif_file_path.endswith(".json"):
            output_filename = self.sarif_file_path.replace(".json", "_minimal_fix_path.json")
        else:
            output_filename = self.sarif_file_path + "_minimal_fix_path.json"
            
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(minimal_solution, f, indent=2, ensure_ascii=False)

        # Generate distribution analysis for agent decision-making
        distribution_analysis = self._generate_distribution_analysis(minimal_solution)
        analysis_filename = output_filename.replace("_minimal_fix_path.json", "_distribution_analysis.json")
        with open(analysis_filename, "w", encoding="utf-8") as f:
            json.dump(distribution_analysis, f, indent=2, ensure_ascii=False)

            if not self.quiet:
                print(f"✓ Minimal solution exported to: {output_filename}")
                print(f"✓ Contains {len(minimal_solution['optimal_fixes_by_type'])} vulnerability types with fix metadata only")
                
                # Add impact distribution analysis
                self._analyze_fix_impact_distribution(minimal_solution)
                print(f"✓ Distribution analysis exported to: {analysis_filename}")

    def _generate_distribution_analysis(self, minimal_solution: dict) -> dict:
        """Generate concise distribution analysis for agent decision-making."""
        distribution_analysis = {
            "analysis_metadata": minimal_solution["analysis_metadata"].copy(),
            "impact_distribution": []
        }
        
        for type_data in minimal_solution["optimal_fixes_by_type"]:
            vuln_type = type_data["vulnerability_type"]
            total_vulns = type_data["total_vulnerabilities"]
            fixes = type_data["top_fixes"]
            
            # Create tier-based distribution analysis
            total_fix_count = len(fixes)
            
            # Define meaningful tier boundaries
            tier_boundaries = [
                {"name": "rank_1_to_10", "start": 0, "end": 10},
                {"name": "rank_10_to_50", "start": 10, "end": 50},
                {"name": "rank_50_to_100", "start": 50, "end": 100},
                {"name": "rank_100_to_rest", "start": 100, "end": total_fix_count}
            ]
            
            tier_analysis = []
            cumulative_coverage = 0
            
            for tier in tier_boundaries:
                start_idx = tier["start"]
                end_idx = min(tier["end"], total_fix_count)
                
                if start_idx >= total_fix_count:
                    break
                    
                # Get fixes in this tier
                tier_fixes = fixes[start_idx:end_idx]
                if not tier_fixes:
                    continue
                
                # Calculate tier metrics
                tier_vulns_covered = sum(fix["vulnerabilities_covered"] for fix in tier_fixes)
                tier_coverage_percent = round((tier_vulns_covered / total_vulns) * 100, 1)
                
                # Count 1:1 fixes in this tier
                single_vuln_fixes_in_tier = sum(1 for fix in tier_fixes if fix["vulnerabilities_covered"] == 1)
                
                # Update cumulative coverage
                cumulative_coverage += tier_vulns_covered
                cumulative_percent = round((cumulative_coverage / total_vulns) * 100, 1)
                
                tier_info = {
                    "tier": tier["name"],
                    "rank_range": f"rank {start_idx + 1} to {end_idx}",
                    "fix_count": len(tier_fixes),
                    "vulnerabilities_covered": tier_vulns_covered,
                    "tier_coverage_percent": tier_coverage_percent,
                    "cumulative_coverage_percent": cumulative_percent,
                    "single_vulnerability_fixes": single_vuln_fixes_in_tier,
                    "multi_vulnerability_fixes": len(tier_fixes) - single_vuln_fixes_in_tier
                }
                
                tier_analysis.append(tier_info)
            
            # Find 80% coverage point
            cumulative = 0
            pareto_80_count = 0
            for i, fix in enumerate(fixes):
                cumulative += fix["vulnerabilities_covered"]
                if cumulative >= total_vulns * 0.8:
                    pareto_80_count = i + 1
                    break
            
            # Overall distribution summary
            single_vuln_fixes = sum(1 for fix in fixes if fix["vulnerabilities_covered"] == 1)
            
            type_analysis = {
                "vulnerability_type": vuln_type,
                "total_vulnerabilities": total_vulns,
                "total_fixes_required": len(fixes),
                "tier_distribution": tier_analysis,
                "coverage_80_point": {
                    "fix_count": pareto_80_count,
                    "effort_percent": round((pareto_80_count / len(fixes)) * 100, 1)
                },
                "overall_summary": {
                    "multi_vulnerability_fixes": len(fixes) - single_vuln_fixes,
                    "single_vulnerability_fixes": single_vuln_fixes,
                    "long_tail_ratio": round((single_vuln_fixes / len(fixes)) * 100, 1)
                }
            }
            
            distribution_analysis["impact_distribution"].append(type_analysis)
        
        return distribution_analysis

    def _get_recommendation(self, tier_name: str, coverage_percentage: float, roi: float) -> str:
        """Generate actionable recommendations for each tier."""
        if tier_name == "critical_fixes":
            return f"IMMEDIATE ACTION: These fixes provide {coverage_percentage:.1f}% coverage with maximum ROI ({roi:.1f}x)"
        elif tier_name == "high_impact_fixes":
            return f"SHORT-TERM GOAL: Extend to {coverage_percentage:.1f}% coverage with strong ROI ({roi:.1f}x)"
        elif tier_name == "medium_impact_fixes":
            return f"MEDIUM-TERM PLAN: Achieve {coverage_percentage:.1f}% coverage, moderate ROI ({roi:.1f}x)"
        else:
            return f"DIMINISHING RETURNS: {coverage_percentage:.1f}% coverage but lower ROI ({roi:.1f}x)"

    def _find_optimal_stopping_points(self, fixes: list, total_vulns: int) -> dict:
        """Find mathematically optimal stopping points for resource allocation."""
        cumulative_coverage = 0
        optimal_points = {}
        
        for i, fix in enumerate(fixes, 1):
            cumulative_coverage += fix["vulnerabilities_covered"]
            coverage_pct = (cumulative_coverage / total_vulns) * 100
            
            # 80% coverage point (Pareto principle)
            if coverage_pct >= 80 and "pareto_80_point" not in optimal_points:
                optimal_points["pareto_80_point"] = {
                    "fix_count": i,
                    "coverage_percentage": round(coverage_pct, 1),
                    "recommendation": "80% of vulnerabilities covered - classic Pareto point"
                }
            
            # Efficiency threshold (when ROI drops below 2x)
            roi = coverage_pct / ((i / len(fixes)) * 100) if i > 0 else 0
            if roi < 2.0 and "efficiency_threshold" not in optimal_points:
                optimal_points["efficiency_threshold"] = {
                    "fix_count": i,
                    "coverage_percentage": round(coverage_pct, 1),
                    "roi": round(roi, 2),
                    "recommendation": "ROI drops below 2x - consider cost-benefit analysis"
                }
        
        return optimal_points

    def _analyze_fix_impact_distribution(self, minimal_solution: dict) -> None:
        """Analyze the distribution of vulnerability coverage across top fixes."""
        print("\n" + "=" * 80)
        print("FIX IMPACT DISTRIBUTION ANALYSIS")
        print("=" * 80)
        
        for type_data in minimal_solution["optimal_fixes_by_type"]:
            vuln_type = type_data["vulnerability_type"]
            total_vulns = type_data["total_vulnerabilities"]
            fixes = type_data["top_fixes"]  # This is now ALL fixes, not just top
            
            print(f"\nVulnerability Type: {vuln_type}")
            print(f"Total Vulnerabilities: {total_vulns}")
            print(f"Total Fixes Needed: {len(fixes)}")
            
            # Calculate cumulative coverage for different thresholds
            thresholds = [10, 20, 30, 40, 50, 70, 100, 200, 500]
            cumulative_coverage = 0
            
            print(f"\nCumulative Impact Analysis:")
            print(f"{'Rank Threshold':<15} {'Vulns Covered':<15} {'Cumulative %':<15} {'Remaining':<15}")
            print("-" * 60)
            
            for threshold in thresholds:
                if threshold > len(fixes):
                    break
                    
                # Calculate vulnerabilities covered by top N fixes
                vulns_covered_by_top_n = sum(fix["vulnerabilities_covered"] for fix in fixes[:threshold])
                percentage = (vulns_covered_by_top_n / total_vulns) * 100
                remaining = total_vulns - vulns_covered_by_top_n
                
                print(f"Top {threshold:<11} {vulns_covered_by_top_n:<15} {percentage:<14.1f}% {remaining:<15}")
            
            # Show the long tail analysis
            print(f"\nLong Tail Analysis:")
            
            # Find how many fixes cover only 1 vulnerability
            single_vuln_fixes = sum(1 for fix in fixes if fix["vulnerabilities_covered"] == 1)
            multi_vuln_fixes = len(fixes) - single_vuln_fixes
            
            print(f"Fixes covering multiple vulnerabilities: {multi_vuln_fixes}")
            print(f"Fixes covering single vulnerability (1:1): {single_vuln_fixes}")
            print(f"Ratio of 1:1 fixes: {(single_vuln_fixes/len(fixes))*100:.1f}%")
            
            # Show top impactful fixes
            print(f"\nTop 10 Most Impactful Fixes:")
            for i, fix in enumerate(fixes[:10], 1):
                print(f"  {i:2}. {fix['vulnerabilities_covered']:3} vulns → {fix['file_path']}:{fix['line']}")

    def solve_mathematical_optimization(self) -> None:
        """
        Execute complete optimization pipeline.

        Pipeline:
        1. Load and analyze SARIF file
        2. Group vulnerabilities by type
        3. Find optimal fixes using advanced algorithms
        """
        if not self.quiet:
            print("SARIF VULNERABILITY FIX OPTIMIZER")
        print("=" * 80)
        print("Finding the minimum number of fixes needed to resolve all vulnerabilities")
        print()

        try:
            self.step1_construct_mathematical_sets()
            self.step2_partition_sets_by_vulnerability_type()
            self.step3_solve_optimization_problems()

            print("✓ OPTIMIZATION COMPLETE")


        except Exception as e:
            print(f"ERROR in optimization: {e}")
            raise
