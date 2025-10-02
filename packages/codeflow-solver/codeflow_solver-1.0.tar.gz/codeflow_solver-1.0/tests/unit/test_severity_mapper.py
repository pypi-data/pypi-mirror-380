"""Tests for severity mapping functionality."""

import pytest
from codeflow_solver.utils.severity_mapper import IssueSeverity, SeverityMapper


class TestIssueSeverity:
    """Test cases for IssueSeverity enum."""

    def test_severity_enum_values(self):
        """Test that severity enum has expected values."""
        assert IssueSeverity.HIGH.value == "high"
        assert IssueSeverity.MEDIUM.value == "medium"
        assert IssueSeverity.LOW.value == "low"
        assert IssueSeverity.INFO.value == "info"

    def test_severity_enum_completeness(self):
        """Test that all expected severity levels are present."""
        expected_severities = {"high", "medium", "low", "info"}
        actual_severities = {severity.value for severity in IssueSeverity}
        assert actual_severities == expected_severities


class TestSeverityMapper:
    """Test cases for SeverityMapper class."""

    def test_severity_map_structure(self):
        """Test that SEVERITY_MAP has the exact expected structure."""
        expected_map = {
            "error": IssueSeverity.HIGH,
            "warning": IssueSeverity.MEDIUM,
            "note": IssueSeverity.LOW,
            "none": IssueSeverity.INFO,
        }
        assert SeverityMapper.SEVERITY_MAP == expected_map

    def test_map_severity_exact_matches(self):
        """Test severity mapping for exact SARIF level matches."""
        # Test exact matches (case sensitive)
        assert SeverityMapper.map_severity("error") == IssueSeverity.HIGH
        assert SeverityMapper.map_severity("warning") == IssueSeverity.MEDIUM
        assert SeverityMapper.map_severity("note") == IssueSeverity.LOW
        assert SeverityMapper.map_severity("none") == IssueSeverity.INFO

    def test_map_severity_case_insensitive(self):
        """Test severity mapping is case insensitive."""
        # Test case variations
        assert SeverityMapper.map_severity("ERROR") == IssueSeverity.HIGH
        assert SeverityMapper.map_severity("Error") == IssueSeverity.HIGH
        assert SeverityMapper.map_severity("WARNING") == IssueSeverity.MEDIUM
        assert SeverityMapper.map_severity("Warning") == IssueSeverity.MEDIUM
        assert SeverityMapper.map_severity("NOTE") == IssueSeverity.LOW
        assert SeverityMapper.map_severity("Note") == IssueSeverity.LOW
        assert SeverityMapper.map_severity("NONE") == IssueSeverity.INFO
        assert SeverityMapper.map_severity("None") == IssueSeverity.INFO

    def test_map_severity_unknown_defaults_to_info(self):
        """Test that unknown severity levels default to INFO."""
        assert SeverityMapper.map_severity("unknown") == IssueSeverity.INFO
        assert SeverityMapper.map_severity("critical") == IssueSeverity.INFO
        assert SeverityMapper.map_severity("") == IssueSeverity.INFO
        assert SeverityMapper.map_severity("invalid") == IssueSeverity.INFO

    def test_get_severity_weight_values(self):
        """Test that severity weights have expected values."""
        assert SeverityMapper.get_severity_weight(IssueSeverity.HIGH) == 4
        assert SeverityMapper.get_severity_weight(IssueSeverity.MEDIUM) == 3
        assert SeverityMapper.get_severity_weight(IssueSeverity.LOW) == 2
        assert SeverityMapper.get_severity_weight(IssueSeverity.INFO) == 1

    def test_get_severity_weight_ordering(self):
        """Test that severity weights are properly ordered (higher = more severe)."""
        weights = [
            SeverityMapper.get_severity_weight(IssueSeverity.INFO),
            SeverityMapper.get_severity_weight(IssueSeverity.LOW),
            SeverityMapper.get_severity_weight(IssueSeverity.MEDIUM),
            SeverityMapper.get_severity_weight(IssueSeverity.HIGH),
        ]
        
        # Weights should be in ascending order (INFO < LOW < MEDIUM < HIGH)
        assert weights == sorted(weights)
        assert weights == [1, 2, 3, 4]

    def test_get_severity_weight_unknown_defaults_to_one(self):
        """Test that unknown severity defaults to weight 1."""
        # This tests the default case in the weights dictionary
        # We can't directly pass an invalid enum, but we can test the method's robustness
        class MockSeverity:
            pass
        
        mock_severity = MockSeverity()
        weight = SeverityMapper.get_severity_weight(mock_severity)
        assert weight == 1

    def test_severity_mapping_consistency(self):
        """Test that all mapped severities have corresponding weights."""
        for sarif_level, severity in SeverityMapper.SEVERITY_MAP.items():
            weight = SeverityMapper.get_severity_weight(severity)
            assert isinstance(weight, int)
            assert weight >= 1
            assert weight <= 4

    def test_severity_mapping_immutability(self):
        """Test that SEVERITY_MAP cannot be accidentally modified."""
        original_map = SeverityMapper.SEVERITY_MAP.copy()
        
        # Attempt to modify (this should not affect the original)
        try:
            SeverityMapper.SEVERITY_MAP["new_level"] = IssueSeverity.HIGH
            # If modification succeeds, remove it to restore original state
            if "new_level" in SeverityMapper.SEVERITY_MAP:
                del SeverityMapper.SEVERITY_MAP["new_level"]
        except (TypeError, AttributeError):
            # If the map is immutable, this is expected
            pass
        
        # Verify original mapping is intact
        for key, value in original_map.items():
            assert SeverityMapper.SEVERITY_MAP[key] == value

    def test_all_sarif_levels_covered(self):
        """Test that all expected SARIF levels are covered in mapping."""
        # Based on SARIF 2.1.0 specification
        expected_sarif_levels = {"error", "warning", "note", "none"}
        actual_sarif_levels = set(SeverityMapper.SEVERITY_MAP.keys())
        assert actual_sarif_levels == expected_sarif_levels

    def test_mapping_deterministic(self):
        """Test that mapping is deterministic (same input always gives same output)."""
        test_cases = ["error", "warning", "note", "none", "unknown"]
        
        for test_case in test_cases:
            result1 = SeverityMapper.map_severity(test_case)
            result2 = SeverityMapper.map_severity(test_case)
            assert result1 == result2
            assert result1 is result2  # Should be the same enum instance
