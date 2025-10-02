"""Tests for SARIF parser functionality."""

import pytest
import tempfile
import json
from pathlib import Path

from codeflow_solver.utils.sarif_parser import SarifParser
from codeflow_solver.utils.severity_mapper import IssueSeverity


class TestSarifParser:
    """Test cases for SARIF file parsing."""

    @pytest.fixture
    def test_sarif_file(self):
        """Create a temporary SARIF file for testing."""
        test_data_path = Path(__file__).parent.parent / "data" / "test_data.sarif"
        return str(test_data_path)

    @pytest.fixture
    def parser(self, test_sarif_file):
        """Create a SarifParser instance with test data."""
        return SarifParser(test_sarif_file)

    def test_parser_initialization(self, test_sarif_file):
        """Test that parser initializes correctly."""
        parser = SarifParser(test_sarif_file)
        assert parser.sarif_file_path == test_sarif_file
        assert parser.sarif_data is None
        assert parser.results == []

    def test_load_sarif_data(self, parser):
        """Test loading SARIF data from file."""
        parser.load_sarif_data()
        
        assert parser.sarif_data is not None
        assert "runs" in parser.sarif_data
        assert len(parser.sarif_data["runs"]) > 0
        assert parser.results is not None
        assert len(parser.results) == 5  # Based on our test data

    def test_load_sarif_data_invalid_file(self):
        """Test loading invalid SARIF file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"invalid": "structure"}, f)
            f.flush()
            
            parser = SarifParser(f.name)
            with pytest.raises(RuntimeError, match="Invalid SARIF: No runs found"):
                parser.load_sarif_data()

    def test_load_sarif_data_no_results(self):
        """Test loading SARIF file with no results."""
        sarif_data = {
            "runs": [{"tool": {"driver": {"name": "test"}}, "results": []}]
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(sarif_data, f)
            f.flush()
            
            parser = SarifParser(f.name)
            with pytest.raises(RuntimeError, match="Invalid SARIF: No results found"):
                parser.load_sarif_data()

    def test_extract_vulnerabilities(self, parser):
        """Test extracting vulnerabilities from SARIF data."""
        parser.load_sarif_data()  # Need to load data first
        vulnerabilities = parser.extract_vulnerabilities()
        
        assert len(vulnerabilities) == 5
        
        # Check first vulnerability (XSS)
        vuln1 = vulnerabilities[0]
        assert vuln1.index == 0
        assert vuln1.rule_id == "java/XSS"
        assert vuln1.file_path == "src/main/java/com/example/Controller.java"
        assert vuln1.line == 45
        assert vuln1.severity == IssueSeverity.HIGH  # error -> HIGH
        assert "Cross-Site Scripting" in vuln1.message

        # Check second vulnerability (another XSS)
        vuln2 = vulnerabilities[1]
        assert vuln2.index == 1
        assert vuln2.rule_id == "java/XSS"
        assert vuln2.file_path == "src/main/java/com/example/UserService.java"
        assert vuln2.line == 22
        assert vuln2.severity == IssueSeverity.HIGH

        # Check third vulnerability (Path Traversal - warning)
        vuln3 = vulnerabilities[2]
        assert vuln3.index == 2
        assert vuln3.rule_id == "java/PT"
        assert vuln3.file_path == "src/main/java/com/example/FileHandler.java"
        assert vuln3.line == 18
        assert vuln3.severity == IssueSeverity.MEDIUM  # warning -> MEDIUM

        # Check fourth vulnerability (DOM XSS - note)
        vuln4 = vulnerabilities[3]
        assert vuln4.index == 3
        assert vuln4.rule_id == "javascript/DOMXSS"
        assert vuln4.file_path == "src/main/webapp/js/app.js"
        assert vuln4.line == 25
        assert vuln4.severity == IssueSeverity.LOW  # note -> LOW

    def test_extract_fix_locations(self, parser):
        """Test extracting fix locations from SARIF data."""
        parser.load_sarif_data()  # Need to load data first
        vulnerabilities = parser.extract_vulnerabilities()
        fix_locations = parser.extract_fix_locations(vulnerabilities)
        
        # Should have multiple fix locations based on code flows
        assert len(fix_locations) > 0
        
        # Check that fix locations have proper structure
        for fix_loc in fix_locations:
            assert fix_loc.file_path != ""
            assert fix_loc.line > 0
            assert isinstance(fix_loc.covered_vulnerabilities, set)
            assert len(fix_loc.covered_vulnerabilities) > 0

        # Verify that vulnerabilities with code flows have multiple fix locations
        controller_fixes = [
            loc for loc in fix_locations 
            if "Controller.java" in loc.file_path
        ]
        assert len(controller_fixes) >= 3  # Should have 3 locations from code flow

    def test_extract_fix_locations_no_code_flows(self, parser):
        """Test extracting fix locations for vulnerabilities without code flows."""
        parser.load_sarif_data()  # Need to load data first
        vulnerabilities = parser.extract_vulnerabilities()
        fix_locations = parser.extract_fix_locations(vulnerabilities)
        
        # The DOM XSS vulnerability has no code flows, so should be fixed at primary location
        dom_xss_fixes = [
            loc for loc in fix_locations 
            if "app.js" in loc.file_path and 3 in loc.covered_vulnerabilities
        ]
        assert len(dom_xss_fixes) >= 1

    def test_parse_sarif_file(self, parser):
        """Test the complete SARIF parsing process."""
        vulnerabilities, fix_locations = parser.parse_sarif_file()
        
        assert len(vulnerabilities) == 5
        assert len(fix_locations) > 0
        
        # Verify that all vulnerabilities are covered by at least one fix location
        covered_vulnerabilities = set()
        for fix_loc in fix_locations:
            covered_vulnerabilities.update(fix_loc.covered_vulnerabilities)
        
        for vuln in vulnerabilities:
            assert vuln.index in covered_vulnerabilities

    def test_get_vulnerability_types(self, parser):
        """Test getting vulnerability type counts."""
        parser.load_sarif_data()  # Need to load data first
        vulnerabilities = parser.extract_vulnerabilities()
        type_counts = parser.get_vulnerability_types(vulnerabilities)
        
        expected_counts = {
            "java/XSS": 2,
            "java/PT": 2,
            "javascript/DOMXSS": 1
        }
        
        assert type_counts == expected_counts

    def test_severity_mapping_coverage(self, parser):
        """Test that all severity levels are properly mapped."""
        parser.load_sarif_data()  # Need to load data first
        vulnerabilities = parser.extract_vulnerabilities()
        
        # Check that we have all severity levels represented
        severities = {vuln.severity for vuln in vulnerabilities}
        assert IssueSeverity.HIGH in severities  # error
        assert IssueSeverity.MEDIUM in severities  # warning  
        assert IssueSeverity.LOW in severities  # note

    def test_file_not_found(self):
        """Test handling of non-existent SARIF file."""
        parser = SarifParser("non_existent_file.sarif")
        with pytest.raises(FileNotFoundError):
            parser.load_sarif_data()

    def test_malformed_json(self):
        """Test handling of malformed JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("{ invalid json content")
            f.flush()
            
            parser = SarifParser(f.name)
            with pytest.raises(json.JSONDecodeError):
                parser.load_sarif_data()

    def test_vulnerability_without_location(self):
        """Test handling of vulnerabilities without location information."""
        sarif_data = {
            "runs": [{
                "tool": {"driver": {"name": "test"}},
                "results": [{
                    "ruleId": "test/rule",
                    "level": "error",
                    "message": {"text": "Test vulnerability"},
                    "locations": []  # No locations
                }]
            }]
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(sarif_data, f)
            f.flush()
            
            parser = SarifParser(f.name)
            parser.load_sarif_data()  # Need to load data first
            vulnerabilities = parser.extract_vulnerabilities()
            
            assert len(vulnerabilities) == 1
            assert vulnerabilities[0].file_path == "unknown"
            assert vulnerabilities[0].line == 0
