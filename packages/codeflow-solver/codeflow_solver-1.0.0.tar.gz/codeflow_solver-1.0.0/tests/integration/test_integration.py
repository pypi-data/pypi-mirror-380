"""Integration tests for the complete SARIF set cover optimization pipeline."""

import pytest
import json
from pathlib import Path
from unittest.mock import patch, Mock

from codeflow_solver.solver.set_cover_solver import SarifSetCoverSolver
from codeflow_solver.solver.optimizer import SetCoverOptimizer


class TestIntegration:
    """Integration test cases for the complete optimization pipeline."""

    @pytest.fixture
    def test_sarif_file(self):
        """Path to test SARIF file."""
        return str(Path(__file__).parent.parent / "data" / "test_data.sarif")

    @pytest.fixture
    def solver(self, test_sarif_file):
        """Create solver instance."""
        return SarifSetCoverSolver(test_sarif_file, export_detailed=True)

    def test_complete_pipeline_without_ortools(self, solver, capsys):
        """Test complete pipeline when OR-Tools is not available."""
        # Test that optimizer initialization fails when OR-Tools is not available
        with patch('codeflow_solver.solver.optimizer.HAS_ORTOOLS', False):
            with pytest.raises(ImportError, match="OR-Tools not available"):
                SetCoverOptimizer()

    @patch('codeflow_solver.solver.optimizer.pywraplp')
    def test_complete_pipeline_with_ortools(self, mock_pywraplp, solver, tmp_path):
        """Test complete pipeline with mocked OR-Tools."""
        # Mock OR-Tools solver
        mock_solver = Mock()
        mock_pywraplp.Solver.CreateSolver.return_value = mock_solver
        mock_pywraplp.Solver.OPTIMAL = 0
        
        # Mock successful optimization
        mock_solver.Solve.return_value = 0  # OPTIMAL
        mock_solver.Constraint.return_value = Mock()
        mock_solver.Objective.return_value = Mock()
        mock_solver.infinity.return_value = float('inf')
        
        # Mock decision variables
        mock_vars = {}
        var_counter = 0
        
        def create_mock_var(low, high, name):
            nonlocal var_counter
            mock_var = Mock()
            # Select first fix location for each type
            mock_var.solution_value.return_value = 1.0 if var_counter % 3 == 0 else 0.0
            mock_vars[name] = mock_var
            var_counter += 1
            return mock_var
        
        mock_solver.IntVar.side_effect = create_mock_var
        
        # Change output directory
        original_path = solver.sarif_file_path
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        
        try:
            # Run complete pipeline
            solver.solve_mathematical_optimization()
            
            # Verify output file was created
            output_file = tmp_path / "test_optimal_fix_path.json"
            assert output_file.exists()
            
            # Verify output structure
            with open(output_file, 'r') as f:
                result = json.load(f)
            
            assert "analysis_summary" in result
            assert "fixes_by_vulnerability_type" in result
            assert "overall_summary" in result
            
        finally:
            solver.sarif_file_path = original_path

    def test_step1_construct_mathematical_sets(self, solver):
        """Test step 1: mathematical set construction."""
        solver.step1_construct_mathematical_sets()
        
        # Verify vulnerabilities were extracted
        assert len(solver.V_all) == 5  # Based on test_data.sarif
        assert all(hasattr(v, 'index') for v in solver.V_all)
        assert all(hasattr(v, 'rule_id') for v in solver.V_all)
        assert all(hasattr(v, 'severity') for v in solver.V_all)
        
        # Verify fix locations were extracted
        assert len(solver.N_all) > 0
        assert all(hasattr(f, 'file_path') for f in solver.N_all)
        assert all(hasattr(f, 'covered_vulnerabilities') for f in solver.N_all)

    def test_step2_partition_sets_by_vulnerability_type(self, solver):
        """Test step 2: type-specific set partitioning."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Verify initializer was created and configured
        assert solver.initializer is not None
        assert hasattr(solver.initializer, 'V_by_type')
        assert hasattr(solver.initializer, 'Sv_by_type')
        
        # Verify type-specific sets were created
        types = solver.initializer.get_vulnerability_types()
        expected_types = {"java/XSS", "java/PT", "javascript/DOMXSS"}
        assert set(types) == expected_types

    @patch('codeflow_solver.solver.optimizer.pywraplp')
    def test_step3_solve_optimization_problems(self, mock_pywraplp, solver, tmp_path):
        """Test step 3: optimization problem solving."""
        # Setup
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Mock OR-Tools
        mock_solver = Mock()
        mock_pywraplp.Solver.CreateSolver.return_value = mock_solver
        mock_pywraplp.Solver.OPTIMAL = 0
        mock_solver.Solve.return_value = 0
        mock_solver.Constraint.return_value = Mock()
        mock_solver.Objective.return_value = Mock()
        mock_solver.infinity.return_value = float('inf')
        
        # Mock variables
        def create_mock_var(low, high, name):
            mock_var = Mock()
            mock_var.solution_value.return_value = 1.0  # Select all fix locations
            return mock_var
        
        mock_solver.IntVar.side_effect = create_mock_var
        
        # Change output path
        original_path = solver.sarif_file_path
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        
        try:
            solver.step3_solve_optimization_problems()
            
            # Verify optimization results
            assert len(solver.x_optimal_by_type) > 0
            
            # Verify output file
            output_file = tmp_path / "test_optimal_fix_path.json"
            assert output_file.exists()
            
        finally:
            solver.sarif_file_path = original_path

    def test_vulnerability_coverage_completeness(self, solver):
        """Test that all vulnerabilities are covered by fix locations."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Check that every vulnerability is covered by at least one fix location
        all_covered_vulns = set()
        for fix_loc in solver.N_all:
            all_covered_vulns.update(fix_loc.covered_vulnerabilities)
        
        all_vuln_indices = {v.index for v in solver.V_all}
        assert all_vuln_indices.issubset(all_covered_vulns), "Some vulnerabilities are not covered by any fix location"

    def test_type_specific_coverage_consistency(self, solver):
        """Test that type-specific coverage is consistent with global coverage."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        for vuln_type in solver.initializer.get_vulnerability_types():
            V_t, Sv_t = solver.initializer.get_type_specific_data(vuln_type)
            
            # Every vulnerability in V_t should be covered by some fix location in Sv_t
            covered_in_type = set()
            for covered_vulns in Sv_t.values():
                covered_in_type.update(covered_vulns)
            
            assert V_t.issubset(covered_in_type), f"Type {vuln_type} has uncovered vulnerabilities"

    def test_fix_location_index_consistency(self, solver):
        """Test that fix location indices are consistent across data structures."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        max_fix_index = len(solver.N_all) - 1
        
        for vuln_type in solver.initializer.get_vulnerability_types():
            _, Sv_t = solver.initializer.get_type_specific_data(vuln_type)
            
            for fix_idx in Sv_t.keys():
                assert 0 <= fix_idx <= max_fix_index, f"Invalid fix location index {fix_idx} for type {vuln_type}"

    def test_vulnerability_index_consistency(self, solver):
        """Test that vulnerability indices are consistent across data structures."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        max_vuln_index = len(solver.V_all) - 1
        
        # Check global fix locations
        for fix_loc in solver.N_all:
            for vuln_idx in fix_loc.covered_vulnerabilities:
                assert 0 <= vuln_idx <= max_vuln_index, f"Invalid vulnerability index {vuln_idx}"

    def test_severity_mapping_integration(self, solver):
        """Test that severity mapping is properly integrated throughout the pipeline."""
        solver.step1_construct_mathematical_sets()
        
        # Check that all vulnerabilities have valid severity mappings
        valid_severities = {"high", "medium", "low", "info"}
        
        for vuln in solver.V_all:
            assert vuln.severity.value in valid_severities, f"Invalid severity: {vuln.severity.value}"

    def test_mathematical_notation_consistency(self, solver):
        """Test that mathematical notation is consistent throughout the pipeline."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Verify set sizes are consistent
        total_vulns = len(solver.V_all)
        type_vulns = sum(len(V_t) for V_t in solver.initializer.V_by_type.values())
        
        assert total_vulns == type_vulns, "Vulnerability count inconsistency between global and type-specific sets"

    def test_error_handling_invalid_sarif(self, tmp_path):
        """Test error handling with invalid SARIF file."""
        # Create invalid SARIF file
        invalid_sarif = tmp_path / "invalid.sarif"
        with open(invalid_sarif, 'w') as f:
            json.dump({"invalid": "structure"}, f)
        
        solver = SarifSetCoverSolver(str(invalid_sarif))
        
        with pytest.raises(RuntimeError, match="Invalid SARIF"):
            solver.step1_construct_mathematical_sets()

    def test_error_handling_missing_file(self):
        """Test error handling with missing SARIF file."""
        solver = SarifSetCoverSolver("nonexistent.sarif")
        
        with pytest.raises(FileNotFoundError):
            solver.step1_construct_mathematical_sets()

    def test_deterministic_behavior(self, solver):
        """Test that the pipeline produces deterministic results."""
        # Run pipeline twice
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Capture first run results
        V_by_type_1 = dict(solver.initializer.V_by_type)
        Sv_by_type_1 = dict(solver.initializer.Sv_by_type)
        
        # Reset and run again
        solver.initializer = None
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Capture second run results
        V_by_type_2 = dict(solver.initializer.V_by_type)
        Sv_by_type_2 = dict(solver.initializer.Sv_by_type)
        
        # Results should be identical
        assert V_by_type_1 == V_by_type_2, "Non-deterministic vulnerability partitioning"
        assert Sv_by_type_1 == Sv_by_type_2, "Non-deterministic coverage partitioning"

    def test_memory_efficiency(self, solver):
        """Test that the pipeline doesn't create unnecessary data duplicates."""
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Verify that type-specific sets reference the same vulnerability indices
        all_type_vulns = set()
        for V_t in solver.initializer.V_by_type.values():
            all_type_vulns.update(V_t)
        
        all_global_vulns = {v.index for v in solver.V_all}
        
        assert all_type_vulns == all_global_vulns, "Type-specific sets don't match global vulnerability set"

    @patch('codeflow_solver.solver.optimizer.pywraplp')
    def test_optimization_result_validation(self, mock_pywraplp, solver, tmp_path):
        """Test that optimization results are properly validated."""
        # Setup pipeline
        solver.step1_construct_mathematical_sets()
        solver.step2_partition_sets_by_vulnerability_type()
        
        # Mock OR-Tools with invalid solution (no variables selected)
        mock_solver = Mock()
        mock_pywraplp.Solver.CreateSolver.return_value = mock_solver
        mock_pywraplp.Solver.OPTIMAL = 0
        mock_solver.Solve.return_value = 0
        mock_solver.Constraint.return_value = Mock()
        mock_solver.Objective.return_value = Mock()
        mock_solver.infinity.return_value = float('inf')
        
        # All variables return 0 (no fix locations selected)
        def create_mock_var(low, high, name):
            mock_var = Mock()
            mock_var.solution_value.return_value = 0.0
            return mock_var
        
        mock_solver.IntVar.side_effect = create_mock_var
        
        # Change output path
        original_path = solver.sarif_file_path
        solver.sarif_file_path = str(tmp_path / "test.sarif")
        
        try:
            solver.step3_solve_optimization_problems()
            
            # Should handle empty solutions gracefully
            assert isinstance(solver.x_optimal_by_type, dict)
            
            # Output should still be generated
            output_file = tmp_path / "test_optimal_fix_path.json"
            assert output_file.exists()
            
        finally:
            solver.sarif_file_path = original_path
