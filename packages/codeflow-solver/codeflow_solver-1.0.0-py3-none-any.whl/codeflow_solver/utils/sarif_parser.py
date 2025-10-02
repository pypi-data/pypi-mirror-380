"""
SARIF file parsing utilities for extracting vulnerabilities and fix locations.
"""

import json
from collections import defaultdict
from typing import Dict, List, Tuple

from .data_structures import FixLocation, Vulnerability
from .severity_mapper import SeverityMapper


class SarifParser:
    """Parser for SARIF files to extract vulnerability and fix location data."""

    def __init__(self, sarif_file_path: str):
        """
        Initialize SARIF parser.

        Args:
            sarif_file_path: Path to the SARIF file to parse
        """
        self.sarif_file_path = sarif_file_path
        self.sarif_data = None
        self.results = []

    def load_sarif_data(self) -> None:
        """Load and validate SARIF file structure."""
        print(f"Loading SARIF data from: {self.sarif_file_path}")

        with open(self.sarif_file_path, "r", encoding="utf-8") as f:
            self.sarif_data = json.load(f)

        # Validate SARIF structure
        if not self.sarif_data.get("runs", []):
            raise RuntimeError("Invalid SARIF: No runs found")

        self.results = self.sarif_data["runs"][0].get("results", [])
        if not self.results:
            raise RuntimeError("Invalid SARIF: No results found")

    def extract_vulnerabilities(self) -> List[Vulnerability]:
        """
        Extract vulnerability set V = {v₁, v₂, ..., vₙ} from SARIF results.

        Each vⱼ ∈ V represents a security vulnerability with:
        - Unique index j
        - Type (rule_id)
        - Location (file, line)
        - Severity level

        Returns:
            List of Vulnerability objects representing set V
        """
        print("Extracting vulnerability set V from SARIF results...")

        vulnerabilities = []

        for j, result in enumerate(self.results):
            rule_id = result.get("ruleId", "unknown")
            message = result.get("message", {}).get("text", "")

            # Extract severity level
            level = result.get("level", "none")
            severity = SeverityMapper.map_severity(level)

            # Extract vulnerability location
            locations = result.get("locations", [])
            if locations:
                phys_loc = locations[0].get("physicalLocation", {})
                artifact = phys_loc.get("artifactLocation", {})
                region = phys_loc.get("region", {})

                file_path = artifact.get("uri", "unknown")
                line = region.get("startLine", 0)
            else:
                file_path = "unknown"
                line = 0

            # Create vulnerability vⱼ
            vulnerability_vj = Vulnerability(
                index=j,  # j in vⱼ notation
                rule_id=rule_id,  # vulnerability type
                file_path=file_path,
                line=line,
                severity=severity,
                message=message,
            )

            vulnerabilities.append(vulnerability_vj)

        return vulnerabilities

    def extract_fix_locations(self, vulnerabilities: List[Vulnerability]) -> List[FixLocation]:
        """
        Extract fix location set N = {n₁, n₂, ..., nₘ} with coverage sets Sᵥ(nᵢ).

        For each potential fix location nᵢ ∈ N:
        - Determine Sᵥ(nᵢ) = set of vulnerabilities covered by fixing at nᵢ
        - Coverage determined by SARIF code flow analysis

        Args:
            vulnerabilities: List of vulnerabilities to determine coverage for

        Returns:
            List of FixLocation objects representing set N
        """
        print("Extracting fix location set N and computing coverage sets Sᵥ(nᵢ)...")

        # Track coverage: location_key -> set of vulnerability indices
        # This builds Sᵥ(nᵢ) for each potential fix location nᵢ
        location_coverage_map = defaultdict(set)

        for vuln_j, result in enumerate(self.results):
            code_flows = result.get("codeFlows", [])

            # If no code flows, vulnerability can only be fixed at its primary location
            if not code_flows:
                vuln = vulnerabilities[vuln_j]
                location_key = (vuln.file_path, vuln.line, 0)
                location_coverage_map[location_key].add(vuln_j)
                continue

            # Extract all locations from code flows
            # Each location in the flow is a potential fix point for this vulnerability
            for flow in code_flows:
                for thread_flow in flow.get("threadFlows", []):
                    for location_data in thread_flow.get("locations", []):
                        location = location_data.get("location", {})
                        phys_loc = location.get("physicalLocation", {})
                        artifact = phys_loc.get("artifactLocation", {})
                        region = phys_loc.get("region", {})

                        file_path = artifact.get("uri", "unknown")
                        line = region.get("startLine", 0)
                        column = region.get("startColumn", 0)

                        if file_path != "unknown" and line > 0:
                            location_key = (file_path, line, column)
                            # Add vulnerability vuln_j to Sᵥ(nᵢ) for this location nᵢ
                            location_coverage_map[location_key].add(vuln_j)

        # Convert to FixLocation objects representing elements of N
        fix_locations = []
        for (file_path, line, column), covered_vulns in location_coverage_map.items():
            fix_location_ni = FixLocation(
                file_path=file_path,
                line=line,
                column=column,
                covered_vulnerabilities=covered_vulns,  # This is Sᵥ(nᵢ)
            )
            fix_locations.append(fix_location_ni)

        return fix_locations

    def parse_sarif_file(self) -> Tuple[List[Vulnerability], List[FixLocation]]:
        """
        Parse SARIF file and extract both vulnerabilities and fix locations.

        Returns:
            Tuple of (vulnerabilities, fix_locations) representing sets V and N
        """
        self.load_sarif_data()
        vulnerabilities = self.extract_vulnerabilities()
        fix_locations = self.extract_fix_locations(vulnerabilities)

        print(f"✓ Parsed SARIF file: {len(vulnerabilities)} vulnerabilities, {len(fix_locations)} fix locations")
        return vulnerabilities, fix_locations

    def get_vulnerability_types(self, vulnerabilities: List[Vulnerability]) -> Dict[str, int]:
        """
        Get count of vulnerabilities by type.

        Args:
            vulnerabilities: List of vulnerabilities to analyze

        Returns:
            Dictionary mapping vulnerability type to count
        """
        type_counts = defaultdict(int)
        for vuln in vulnerabilities:
            type_counts[vuln.rule_id] += 1
        return dict(type_counts)
