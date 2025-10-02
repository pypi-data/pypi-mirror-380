"""Tests for result format and MCP compatibility."""

import pytest
import json
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import Mock

from codeflow_solver.solver.set_cover_solver import SarifSetCoverSolver
from codeflow_solver.utils.data_structures import Vulnerability, FixLocation
from codeflow_solver.utils.severity_mapper import IssueSeverity


class TestResultFormat:
    """Test cases for result format and MCP compatibility."""

    @pytest.fixture
    def test_sarif_file(self):
        """Create a temporary SARIF file for testing."""
        test_data_path = Path(__file__).parent.parent / "data" / "test_data.sarif"
        return str(test_data_path)

    @pytest.fixture
    def solver(self, test_sarif_file):
        """Create a solver instance with test data."""
        return SarifSetCoverSolver(test_sarif_file)

    def test_export_detailed_solution_structure(self, solver, tmp_path):
        """Test that exported solution has the correct structure for MCP consumption."""
        # Set up solver with test data
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Mock the optimization results for testing
        solver.x_optimal_by_type = {
            "java/XSS": [
                FixLocation("Controller.java", 30, 25, {0}),
                FixLocation("UserService.java", 15, 20, {1})
            ],
            "java/PT": [
                FixLocation("FileHandler.java", 12, 25, {2, 4})
            ],
            "javascript/DOMXSS": [
                FixLocation("app.js", 25, 5, {3})
            ]
        }
        
        # Change to temp directory for output
        original_path = solver.sarif_file_path
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        
        # Export the solution
        solver._export_detailed_solution()
        
        # Read the exported JSON
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        # Restore original path
        solver.sarif_file_path = original_path
        
        # Test top-level structure
        assert "analysis_summary" in result
        assert "fixes_by_vulnerability_type" in result
        assert "overall_summary" in result

    def test_analysis_summary_format(self, solver, tmp_path):
        """Test metadata section format for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        metadata = result["analysis_summary"]
        
        # Required fields for MCP
        required_fields = [
            "total_vulnerabilities",
            "vulnerability_types_found",
            "potential_fix_locations",
            "analysis_timestamp",
            "optimization_method"
        ]
        
        for field in required_fields:
            assert field in metadata, f"Missing required metadata field: {field}"
        
        # Validate field types
        assert isinstance(metadata["total_vulnerabilities"], int)
        assert isinstance(metadata["vulnerability_types_found"], int)
        assert isinstance(metadata["potential_fix_locations"], int)
        assert isinstance(metadata["analysis_timestamp"], str)
        assert isinstance(metadata["optimization_method"], str)
        
        # Validate timestamp format (ISO format for MCP compatibility)
        timestamp = metadata["analysis_timestamp"]
        datetime.fromisoformat(timestamp.replace('Z', '+00:00'))  # Should not raise

    def test_fixes_by_vulnerability_type_format(self, solver, tmp_path):
        """Test vulnerability type solutions format for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Mock optimization results
        solver.x_optimal_by_type = {
            "java/XSS": [FixLocation("test.java", 10, 5, {0, 1})]
        }
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        solutions = result["fixes_by_vulnerability_type"]
        assert isinstance(solutions, list)
        
        if solutions:  # If we have solutions
            solution = solutions[0]
            
            # Required fields for each vulnerability type solution
            required_fields = [
                "vulnerability_type",
                "total_vulnerabilities",
                "fixes_needed",
                "reduction_factor",
                "efficiency_percent",
                "fix_locations"
            ]
            
            for field in required_fields:
                assert field in solution, f"Missing required solution field: {field}"
            
            # Validate field types
            assert isinstance(solution["vulnerability_type"], str)
            assert isinstance(solution["total_vulnerabilities"], int)
            assert isinstance(solution["fixes_needed"], int)
            assert isinstance(solution["reduction_factor"], (int, float))
            assert isinstance(solution["efficiency_percent"], (int, float))
            assert isinstance(solution["fix_locations"], list)

    def test_fix_location_format(self, solver, tmp_path):
        """Test individual fix location format for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Mock optimization results with detailed vulnerability info
        solver.x_optimal_by_type = {
            "java/XSS": [FixLocation("test.java", 10, 5, {0})]
        }
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        solutions = result["fixes_by_vulnerability_type"]
        if solutions and solutions[0]["fix_locations"]:
            fix_location = solutions[0]["fix_locations"][0]
            
            # Required fields for each fix location
            required_fields = [
                "rank",
                "fix_location",
                "vulnerabilities_fixed_this_type",
                "total_vulnerabilities_fixed",
                "vulnerability_details"
            ]
            
            for field in required_fields:
                assert field in fix_location, f"Missing required fix location field: {field}"
            
            # Validate fix_location structure
            fix_loc_ni = fix_location["fix_location"]
            assert "file_path" in fix_loc_ni
            assert "line" in fix_loc_ni
            assert "column" in fix_loc_ni
            
            # Validate types
            assert isinstance(fix_location["rank"], int)
            assert isinstance(fix_location["vulnerabilities_fixed_this_type"], int)
            assert isinstance(fix_location["total_vulnerabilities_fixed"], int)
            assert isinstance(fix_location["vulnerability_details"], list)

    def test_vulnerability_details_format(self, solver, tmp_path):
        """Test vulnerability details format for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        solver.x_optimal_by_type = {
            "java/XSS": [FixLocation("test.java", 10, 5, {0})]
        }
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        solutions = result["fixes_by_vulnerability_type"]
        if solutions and solutions[0]["fix_locations"]:
            fix_location = solutions[0]["fix_locations"][0]
            vuln_details = fix_location["vulnerability_details"]
            
            if vuln_details:  # If we have vulnerability details
                vuln_detail = vuln_details[0]
                
                # Required fields for each vulnerability detail
                required_fields = [
                    "vulnerability_id",
                    "file_path",
                    "line",
                    "rule_id",
                    "severity",
                    "message"
                ]
                
                for field in required_fields:
                    assert field in vuln_detail, f"Missing required vulnerability detail field: {field}"
                
                # Validate types
                assert isinstance(vuln_detail["vulnerability_id"], int)
                assert isinstance(vuln_detail["file_path"], str)
                assert isinstance(vuln_detail["line"], int)
                assert isinstance(vuln_detail["rule_id"], str)
                assert isinstance(vuln_detail["severity"], str)
                assert isinstance(vuln_detail["message"], str)
                
                # Validate severity values
                valid_severities = {"high", "medium", "low", "info"}
                assert vuln_detail["severity"] in valid_severities

    def test_overall_summary_format(self, solver, tmp_path):
        """Test overall summary format for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        summary = result["overall_summary"]
        
        # Required fields for overall summary
        required_fields = [
            "total_vulnerabilities",
            "total_fixes_needed",
            "overall_reduction_factor",
            "overall_efficiency_percent",
            "optimization_guarantee"
        ]
        
        for field in required_fields:
            assert field in summary, f"Missing required summary field: {field}"
        
        # Validate types
        assert isinstance(summary["total_vulnerabilities"], int)
        assert isinstance(summary["total_fixes_needed"], int)
        assert isinstance(summary["overall_reduction_factor"], (int, float))
        assert isinstance(summary["overall_efficiency_percent"], (int, float))
        assert isinstance(summary["optimization_guarantee"], str)
        
        # Validate ranges
        assert summary["overall_efficiency_percent"] >= 0
        assert summary["overall_efficiency_percent"] <= 100

    def test_json_serialization_compatibility(self, solver, tmp_path):
        """Test that exported JSON is properly serializable for MCP."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        
        # Test that JSON can be loaded and re-serialized
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        # Should be able to serialize again without errors
        json_str = json.dumps(result, indent=2, ensure_ascii=False)
        assert isinstance(json_str, str)
        assert len(json_str) > 0
        
        # Should be able to parse the serialized string
        reparsed = json.loads(json_str)
        assert reparsed == result

    def test_output_file_naming_convention(self, solver, tmp_path):
        """Test output file naming convention for MCP compatibility."""
        test_sarif_path = tmp_path / "input_file.sarif"
        solver.sarif_file_path = str(test_sarif_path)
        
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}
        
        solver._export_detailed_solution()
        
        # Check expected output file exists
        expected_output = tmp_path / "input_file_optimal_fix_path.json"
        assert expected_output.exists()

    def test_mathematical_notation_consistency(self, solver, tmp_path):
        """Test that mathematical notation is consistent throughout the output."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            content = f.read()
        
        # Check for consistent field names and structure
        expected_fields = ["total_vulnerabilities", "vulnerability_types_found", "potential_fix_locations", "analysis_timestamp", "optimization_method"]
        
        for field in expected_fields:
            assert field in content, f"Expected field {field} not found in output"

    def test_empty_results_handling(self, solver, tmp_path):
        """Test handling of empty optimization results for MCP compatibility."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        solver.x_optimal_by_type = {}  # No solutions
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        # Should still have valid structure even with no results
        assert "analysis_summary" in result
        assert "fixes_by_vulnerability_type" in result
        assert "overall_summary" in result
        
        # Empty results should be handled gracefully
        assert isinstance(result["fixes_by_vulnerability_type"], list)
        assert result["overall_summary"]["total_fixes_needed"] == 0

    def test_large_numbers_handling(self, solver, tmp_path):
        """Test handling of large numbers for MCP compatibility."""
        # This test ensures that large vulnerability counts don't break JSON serialization
        solver.V_all = [Mock() for _ in range(10000)]  # Large number of vulnerabilities
        solver.N_all = [Mock() for _ in range(5000)]   # Large number of fix locations
        
        solver.initializer = Mock()
        solver.initializer.V_by_type = {"test/type": set(range(10000))}
        solver.x_optimal_by_type = {}
        
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        
        # Should not raise any errors with large numbers
        solver._export_detailed_solution()
        
        output_file = str(tmp_path / "test_optimal_fix_path.json")
        with open(output_file, 'r') as f:
            result = json.load(f)
        
        # Large numbers should be preserved
        assert result["analysis_summary"]["total_vulnerabilities"] == 10000
        assert result["analysis_summary"]["potential_fix_locations"] == 5000
