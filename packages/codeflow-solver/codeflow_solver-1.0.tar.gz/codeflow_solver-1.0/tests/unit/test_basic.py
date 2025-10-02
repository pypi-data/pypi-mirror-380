"""Basic tests for the SARIF Set Cover Optimizer package."""

import pytest
from pathlib import Path
from codeflow_solver import SarifSetCoverSolver


class TestBasicFunctionality:
    """Basic functionality tests for the package."""

    def test_package_imports(self):
        """Test that the package imports correctly."""
        from codeflow_solver import main, SarifSetCoverSolver
        assert main is not None
        assert SarifSetCoverSolver is not None

    def test_all_modules_importable(self):
        """Test that all modules can be imported without errors."""
        # Utils modules
        from codeflow_solver.utils import sarif_parser, severity_mapper, data_structures
        assert sarif_parser is not None
        assert severity_mapper is not None
        assert data_structures is not None
        
        # Set cover modules
        from codeflow_solver.set_cover import initializer
        assert initializer is not None
        
        # Solver modules
        from codeflow_solver.solver import optimizer, set_cover_solver
        assert optimizer is not None
        assert set_cover_solver is not None
        
        # CLI modules
        from codeflow_solver.cli import main
        assert main is not None

    def test_solver_initialization(self):
        """Test that the solver can be initialized."""
        solver = SarifSetCoverSolver("dummy_file.sarif")
        assert solver.sarif_file_path == "dummy_file.sarif"
        assert solver.V_all == []
        assert solver.N_all == []
        assert solver.x_optimal_by_type == {}

    def test_version_info(self):
        """Test that version information is available."""
        import codeflow_solver
        assert hasattr(codeflow_solver, "__version__")
        assert codeflow_solver.__version__ == "1.0.0"
        assert hasattr(codeflow_solver, "__author__")
        assert hasattr(codeflow_solver, "__description__")

    def test_data_structures_available(self):
        """Test that data structures are properly defined."""
        from codeflow_solver.utils.data_structures import Vulnerability, FixLocation
        from codeflow_solver.utils.severity_mapper import IssueSeverity
        
        # Test Vulnerability creation
        vuln = Vulnerability(
            index=0,
            rule_id="test/rule",
            file_path="test.java",
            line=10,
            severity=IssueSeverity.HIGH,
            message="Test vulnerability"
        )
        assert vuln.index == 0
        assert vuln.rule_id == "test/rule"
        assert vuln.severity == IssueSeverity.HIGH
        
        # Test FixLocation creation
        fix_loc = FixLocation(
            file_path="test.java",
            line=5,
            column=10,
            covered_vulnerabilities={0, 1}
        )
        assert fix_loc.file_path == "test.java"
        assert fix_loc.line == 5
        assert fix_loc.covered_vulnerabilities == {0, 1}

    def test_severity_mapper_available(self):
        """Test that severity mapper is properly configured."""
        from codeflow_solver.utils.severity_mapper import SeverityMapper, IssueSeverity
        
        # Test mapping functionality
        assert SeverityMapper.map_severity("error") == IssueSeverity.HIGH
        assert SeverityMapper.map_severity("warning") == IssueSeverity.MEDIUM
        assert SeverityMapper.map_severity("note") == IssueSeverity.LOW
        assert SeverityMapper.map_severity("none") == IssueSeverity.INFO

    def test_package_structure_integrity(self):
        """Test that package structure is intact."""
        # Test that __all__ exports are available
        from codeflow_solver import __all__
        assert "main" in __all__
        assert "SarifSetCoverSolver" in __all__
        
        # Test that submodule __all__ exports work
        from codeflow_solver.utils import __all__ as utils_all
        expected_utils = ["SarifParser", "IssueSeverity", "SeverityMapper", "Vulnerability", "FixLocation"]
        for item in expected_utils:
            assert item in utils_all

    def test_cli_entry_points(self):
        """Test that CLI entry points are properly configured."""
        from codeflow_solver.cli.main import main, create_parser
        
        # Test parser creation
        parser = create_parser()
        assert parser is not None
        assert parser.prog == "sarif-set-cover-optimizer"
        
        # Test main function exists
        assert callable(main)

    def test_test_data_availability(self):
        """Test that test data files are available."""
        test_data_path = Path(__file__).parent.parent / "data" / "test_data.sarif"
        assert test_data_path.exists(), "Test SARIF file should be available for tests"
        
        # Verify it's valid JSON
        import json
        with open(test_data_path, 'r') as f:
            data = json.load(f)
        
        assert "runs" in data
        assert len(data["runs"]) > 0
        assert "results" in data["runs"][0]
