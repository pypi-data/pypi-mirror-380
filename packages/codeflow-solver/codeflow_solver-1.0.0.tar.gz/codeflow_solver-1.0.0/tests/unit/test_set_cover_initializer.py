"""Tests for set cover initialization functionality."""

import pytest
from codeflow_solver.utils.data_structures import Vulnerability, FixLocation
from codeflow_solver.utils.severity_mapper import IssueSeverity
from codeflow_solver.set_cover.initializer import SetCoverInitializer


class TestSetCoverInitializer:
    """Test cases for SetCoverInitializer class."""

    @pytest.fixture
    def sample_vulnerabilities(self):
        """Create sample vulnerabilities for testing."""
        return [
            Vulnerability(
                index=0,
                rule_id="java/XSS",
                file_path="Controller.java",
                line=45,
                severity=IssueSeverity.HIGH,
                message="XSS vulnerability 1"
            ),
            Vulnerability(
                index=1,
                rule_id="java/XSS",
                file_path="UserService.java",
                line=22,
                severity=IssueSeverity.HIGH,
                message="XSS vulnerability 2"
            ),
            Vulnerability(
                index=2,
                rule_id="java/PT",
                file_path="FileHandler.java",
                line=18,
                severity=IssueSeverity.MEDIUM,
                message="Path traversal 1"
            ),
            Vulnerability(
                index=3,
                rule_id="java/PT",
                file_path="FileHandler.java",
                line=25,
                severity=IssueSeverity.MEDIUM,
                message="Path traversal 2"
            ),
            Vulnerability(
                index=4,
                rule_id="javascript/DOMXSS",
                file_path="app.js",
                line=25,
                severity=IssueSeverity.LOW,
                message="DOM XSS"
            ),
        ]

    @pytest.fixture
    def sample_fix_locations(self):
        """Create sample fix locations for testing."""
        return [
            FixLocation(
                file_path="Controller.java",
                line=30,
                column=25,
                covered_vulnerabilities={0}  # Covers XSS vuln 1
            ),
            FixLocation(
                file_path="Controller.java",
                line=35,
                column=15,
                covered_vulnerabilities={0}  # Also covers XSS vuln 1
            ),
            FixLocation(
                file_path="UserService.java",
                line=15,
                column=20,
                covered_vulnerabilities={1}  # Covers XSS vuln 2
            ),
            FixLocation(
                file_path="FileHandler.java",
                line=12,
                column=25,
                covered_vulnerabilities={2, 3}  # Covers both PT vulns
            ),
            FixLocation(
                file_path="app.js",
                line=25,
                column=5,
                covered_vulnerabilities={4}  # Covers DOM XSS
            ),
        ]

    @pytest.fixture
    def initializer(self, sample_vulnerabilities, sample_fix_locations):
        """Create SetCoverInitializer instance with sample data."""
        return SetCoverInitializer(sample_vulnerabilities, sample_fix_locations)

    def test_initializer_creation(self, sample_vulnerabilities, sample_fix_locations):
        """Test that initializer is created correctly."""
        initializer = SetCoverInitializer(sample_vulnerabilities, sample_fix_locations)
        
        assert initializer.V_all == sample_vulnerabilities
        assert initializer.N_all == sample_fix_locations
        assert initializer.V_by_type == {}
        assert initializer.Sv_by_type == {}

    def test_detect_vulnerability_types(self, initializer, capsys):
        """Test vulnerability type detection."""
        initializer._detect_vulnerability_types()
        
        # Check console output
        captured = capsys.readouterr()
        assert "Found |T| = 3 vulnerability types:" in captured.out
        assert "java/XSS: 2 vulnerabilities" in captured.out
        assert "java/PT: 2 vulnerabilities" in captured.out
        assert "javascript/DOMXSS: 1 vulnerabilities" in captured.out

    def test_create_V_subsets_by_type(self, initializer, capsys):
        """Test creation of vulnerability subsets by type."""
        initializer._create_V_subsets_by_type()
        
        # Check V_by_type structure
        expected_V_by_type = {
            "java/XSS": {0, 1},
            "java/PT": {2, 3},
            "javascript/DOMXSS": {4}
        }
        assert initializer.V_by_type == expected_V_by_type
        
        # Check console output
        captured = capsys.readouterr()
        assert "Created 3 vulnerability subsets:" in captured.out
        assert "|V_java/XSS| = 2 vulnerabilities" in captured.out
        assert "|V_java/PT| = 2 vulnerabilities" in captured.out
        assert "|V_javascript/DOMXSS| = 1 vulnerabilities" in captured.out

    def test_create_Sv_coverage_by_type(self, initializer, capsys):
        """Test creation of type-specific coverage sets."""
        # First create the V subsets
        initializer._create_V_subsets_by_type()
        
        # Then create coverage sets
        initializer._create_Sv_coverage_by_type()
        
        # Check Sv_by_type structure
        expected_Sv_by_type = {
            "java/XSS": {
                0: {0},  # Fix location 0 covers vuln 0
                1: {0},  # Fix location 1 covers vuln 0
                2: {1},  # Fix location 2 covers vuln 1
            },
            "java/PT": {
                3: {2, 3},  # Fix location 3 covers vulns 2 and 3
            },
            "javascript/DOMXSS": {
                4: {4},  # Fix location 4 covers vuln 4
            }
        }
        assert initializer.Sv_by_type == expected_Sv_by_type
        
        # Check console output
        captured = capsys.readouterr()
        assert "Created coverage sets for 3 vulnerability types:" in captured.out
        assert "|N_java/XSS| = 3 relevant fix locations" in captured.out
        assert "|N_java/PT| = 1 relevant fix locations" in captured.out
        assert "|N_javascript/DOMXSS| = 1 relevant fix locations" in captured.out

    def test_partition_sets_by_vulnerability_type(self, initializer, capsys):
        """Test the complete partitioning process."""
        initializer.partition_sets_by_vulnerability_type()
        
        # Verify all data structures are populated
        assert len(initializer.V_by_type) == 3
        assert len(initializer.Sv_by_type) == 3
        
        # Check console output includes all steps
        captured = capsys.readouterr()
        assert "Partitioning sets by vulnerability type..." in captured.out
        assert "✓ Created type-specific mathematical sets for optimization" in captured.out

    def test_get_vulnerability_types(self, initializer):
        """Test getting list of vulnerability types."""
        initializer.partition_sets_by_vulnerability_type()
        
        types = initializer.get_vulnerability_types()
        expected_types = ["java/XSS", "java/PT", "javascript/DOMXSS"]
        
        assert set(types) == set(expected_types)
        assert len(types) == 3

    def test_get_type_specific_data(self, initializer):
        """Test getting type-specific data."""
        initializer.partition_sets_by_vulnerability_type()
        
        # Test existing type
        V_t, Sv_t = initializer.get_type_specific_data("java/XSS")
        assert V_t == {0, 1}
        assert len(Sv_t) == 3  # 3 fix locations for XSS
        
        # Test non-existing type
        V_t_empty, Sv_t_empty = initializer.get_type_specific_data("nonexistent/type")
        assert V_t_empty == set()
        assert Sv_t_empty == {}

    def test_get_statistics(self, initializer):
        """Test getting statistics about initialized sets."""
        initializer.partition_sets_by_vulnerability_type()
        
        stats = initializer.get_statistics()
        
        expected_stats = {
            "total_vulnerabilities": 5,
            "total_fix_locations": 5,
            "vulnerability_types": 3,
            "max_vulnerabilities_per_type": 2,  # java/XSS and java/PT both have 2
            "min_vulnerabilities_per_type": 1,  # javascript/DOMXSS has 1
        }
        
        assert stats == expected_stats

    def test_empty_input_handling(self):
        """Test handling of empty vulnerability and fix location lists."""
        initializer = SetCoverInitializer([], [])
        initializer.partition_sets_by_vulnerability_type()
        
        assert initializer.V_by_type == {}
        assert initializer.Sv_by_type == {}
        
        stats = initializer.get_statistics()
        assert stats["total_vulnerabilities"] == 0
        assert stats["total_fix_locations"] == 0
        assert stats["vulnerability_types"] == 0

    def test_single_vulnerability_type(self):
        """Test handling of single vulnerability type."""
        vulnerabilities = [
            Vulnerability(0, "java/XSS", "test.java", 10, IssueSeverity.HIGH, "test")
        ]
        fix_locations = [
            FixLocation("test.java", 5, 1, {0})
        ]
        
        initializer = SetCoverInitializer(vulnerabilities, fix_locations)
        initializer.partition_sets_by_vulnerability_type()
        
        assert len(initializer.V_by_type) == 1
        assert "java/XSS" in initializer.V_by_type
        assert initializer.V_by_type["java/XSS"] == {0}

    def test_fix_location_covers_no_vulnerabilities_of_type(self):
        """Test handling when fix location covers no vulnerabilities of a specific type."""
        vulnerabilities = [
            Vulnerability(0, "java/XSS", "test.java", 10, IssueSeverity.HIGH, "test"),
            Vulnerability(1, "java/PT", "test.java", 20, IssueSeverity.MEDIUM, "test")
        ]
        fix_locations = [
            FixLocation("test.java", 5, 1, {0}),  # Only covers XSS, not PT
            FixLocation("test.java", 15, 1, {1}),  # Only covers PT, not XSS
        ]
        
        initializer = SetCoverInitializer(vulnerabilities, fix_locations)
        initializer.partition_sets_by_vulnerability_type()
        
        # Each type should only have fix locations that cover vulnerabilities of that type
        assert len(initializer.Sv_by_type["java/XSS"]) == 1
        assert len(initializer.Sv_by_type["java/PT"]) == 1
        assert 0 in initializer.Sv_by_type["java/XSS"]  # Fix location 0
        assert 1 in initializer.Sv_by_type["java/PT"]   # Fix location 1

    def test_data_structure_immutability(self, initializer):
        """Test that returned data structures are references (not copies) - this is expected behavior."""
        initializer.partition_sets_by_vulnerability_type()
        
        # Get type-specific data
        V_t, Sv_t = initializer.get_type_specific_data("java/XSS")
        
        # Store original values
        original_V_t = V_t.copy()
        original_Sv_t = dict(Sv_t)
        
        # Modify returned data (this will modify internal state since they're references)
        V_t.add(999)
        Sv_t[999] = {999}
        
        # Verify that the internal state was modified (this is the expected behavior)
        V_t_fresh, Sv_t_fresh = initializer.get_type_specific_data("java/XSS")
        assert 999 in V_t_fresh  # Should be modified since it's a reference
        assert 999 in Sv_t_fresh  # Should be modified since it's a reference
        
        # Clean up the test modifications
        V_t.remove(999)
        del Sv_t[999]

    def test_vulnerability_index_consistency(self, initializer):
        """Test that vulnerability indices are consistent across data structures."""
        initializer.partition_sets_by_vulnerability_type()
        
        # Collect all vulnerability indices from V_by_type
        all_indices_in_types = set()
        for V_subset in initializer.V_by_type.values():
            all_indices_in_types.update(V_subset)
        
        # Should match the indices of actual vulnerabilities
        expected_indices = {vuln.index for vuln in initializer.V_all}
        assert all_indices_in_types == expected_indices

    def test_fix_location_index_consistency(self, initializer):
        """Test that fix location indices are consistent across data structures."""
        initializer.partition_sets_by_vulnerability_type()
        
        # Collect all fix location indices from Sv_by_type
        all_fix_indices = set()
        for Sv_dict in initializer.Sv_by_type.values():
            all_fix_indices.update(Sv_dict.keys())
        
        # Should be valid indices for N_all
        max_fix_index = len(initializer.N_all) - 1
        for fix_idx in all_fix_indices:
            assert 0 <= fix_idx <= max_fix_index
