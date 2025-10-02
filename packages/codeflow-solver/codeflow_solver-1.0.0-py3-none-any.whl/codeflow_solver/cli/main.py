"""
Command-line interface for the SARIF Set Cover Optimizer.
"""

import argparse
import json
import os
import sys
from pathlib import Path

from ..solver.set_cover_solver import SarifSetCoverSolver


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the command-line argument parser.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="sarif-set-cover-optimizer",
        description="SARIF Set Cover Mathematical Optimizer - Apply Integer Linear Programming to find the minimum number of code fixes needed to eliminate all vulnerabilities.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s vulnerabilities.sarif
  %(prog)s --input report.sarif --verbose
  %(prog)s /path/to/sarif/file.sarif --quiet

This tool applies Integer Linear Programming to find the minimum
number of code fixes needed to eliminate all vulnerabilities from
SARIF (Static Analysis Results Interchange Format) output.

The optimization process:
1. Extracts vulnerabilities and potential fix locations from SARIF
2. Groups vulnerabilities by type for separate optimization
3. Solves set cover problems using OR-Tools for guaranteed optimal solutions
4. Exports detailed mathematical analysis and fix recommendations
        """,
    )

    # Input file argument
    parser.add_argument("sarif_file", nargs="?", help="Path to the SARIF file to analyze")

    # Alternative input specification
    parser.add_argument(
        "-i",
        "--input",
        dest="sarif_file_alt",
        help="Path to the SARIF file to analyze (alternative to positional argument)",
    )

    # Output options
    parser.add_argument("-o", "--output", help="Output directory for results (default: same directory as input file)")

    # Verbosity options
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output with detailed progress information"
    )
    verbosity_group.add_argument("-q", "--quiet", action="store_true", help="Suppress all output except errors")

    # Analysis options
    parser.add_argument(
        "--severity-filter",
        choices=["high", "medium", "low", "info"],
        nargs="+",
        help="Filter vulnerabilities by severity level (can specify multiple)",
    )

    parser.add_argument(
        "--rule-filter", nargs="+", help="Filter vulnerabilities by rule ID (can specify multiple rule IDs)"
    )

    # Export options
    export_group = parser.add_mutually_exclusive_group()
    export_group.add_argument("--export", action="store_true", help="Export detailed mathematical solution to JSON file with full vulnerability details")
    export_group.add_argument("--minimal-export", action="store_true", help="Export minimal solution to JSON file with only fix metadata (MCP-friendly)")

    # Version information
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    return parser


def validate_arguments(args: argparse.Namespace) -> str:
    """
    Validate command-line arguments and return the SARIF file path.

    Args:
        args: Parsed command-line arguments

    Returns:
        Validated SARIF file path

    Raises:
        SystemExit: If validation fails
    """
    # Determine SARIF file path
    sarif_file = args.sarif_file or args.sarif_file_alt

    if not sarif_file:
        print("Error: No SARIF file specified.", file=sys.stderr)
        print("Use --help for usage information.", file=sys.stderr)
        sys.exit(1)

    # Validate file exists and is readable
    sarif_path = Path(sarif_file)
    if not sarif_path.exists():
        print(f"Error: SARIF file not found: {sarif_file}", file=sys.stderr)
        sys.exit(1)

    if not sarif_path.is_file():
        print(f"Error: Path is not a file: {sarif_file}", file=sys.stderr)
        sys.exit(1)

    if not os.access(sarif_path, os.R_OK):
        print(f"Error: Cannot read SARIF file: {sarif_file}", file=sys.stderr)
        sys.exit(1)

    # Validate file extension (optional warning)
    if not sarif_file.lower().endswith((".sarif", ".json")):
        print(f"Warning: File does not have .sarif or .json extension: {sarif_file}", file=sys.stderr)

    return str(sarif_path.absolute())


def setup_output_verbosity(args: argparse.Namespace) -> None:
    """
    Configure output verbosity based on command-line arguments.

    Args:
        args: Parsed command-line arguments
    """
    if args.quiet:
        # Redirect stdout to devnull, keep stderr for errors
        sys.stdout = open(os.devnull, "w")
    elif args.verbose:
        # Verbose mode is handled by the solver itself
        print("Verbose mode enabled - detailed progress information will be shown")


def run_optimization(sarif_file_path: str, args: argparse.Namespace) -> None:
    """
    Run the SARIF set cover optimization process.

    Args:
        sarif_file_path: Path to the SARIF file to analyze
        args: Parsed command-line arguments
    """
    try:
        # Initialize the solver with filters
        solver = SarifSetCoverSolver(
            sarif_file_path,
            severity_filter=args.severity_filter,
            rule_filter=args.rule_filter,
            quiet=args.quiet,
            export_detailed=args.export,
            minimal_export=args.minimal_export
        )

        # Run the optimization
        solver.solve_mathematical_optimization()

        # Output handled by solver based on quiet/export flags
        pass

    except ImportError as e:
        if "ortools" in str(e).lower():
            print("Error: OR-Tools is required but not installed.", file=sys.stderr)
            print("Install it with: pip install ortools", file=sys.stderr)
            sys.exit(1)
        else:
            raise

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in SARIF file: {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Error during optimization: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


def main() -> None:
    """
    Main entry point for the SARIF Set Cover Optimizer CLI.
    """
    # Parse command-line arguments
    parser = create_parser()
    args = parser.parse_args()

    # Validate arguments and get SARIF file path
    sarif_file_path = validate_arguments(args)

    # Setup output verbosity
    setup_output_verbosity(args)

    # Run the optimization
    run_optimization(sarif_file_path, args)


if __name__ == "__main__":
    main()
