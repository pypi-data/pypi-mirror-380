"""
Severity mapping utilities for SARIF vulnerability classification.
"""

from enum import Enum
from typing import Dict


class IssueSeverity(Enum):
    """Enumeration of issue severity levels."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class SeverityMapper:
    """Maps SARIF severity levels to standardized issue severity."""

    # Mapping from SARIF severity to IssueSeverity
    SEVERITY_MAP: Dict[str, IssueSeverity] = {
        "error": IssueSeverity.HIGH,
        "warning": IssueSeverity.MEDIUM,
        "note": IssueSeverity.LOW,
        "none": IssueSeverity.INFO,
    }

    @classmethod
    def map_severity(cls, sarif_level: str) -> IssueSeverity:
        """
        Map SARIF severity level to IssueSeverity.

        Args:
            sarif_level: SARIF severity level string

        Returns:
            Corresponding IssueSeverity enum value
        """
        return cls.SEVERITY_MAP.get(sarif_level.lower(), IssueSeverity.INFO)

    @classmethod
    def get_severity_weight(cls, severity: IssueSeverity) -> int:
        """
        Get numerical weight for severity level (higher = more severe).

        Args:
            severity: IssueSeverity enum value

        Returns:
            Numerical weight for the severity level
        """
        weights = {
            IssueSeverity.HIGH: 4,
            IssueSeverity.MEDIUM: 3,
            IssueSeverity.LOW: 2,
            IssueSeverity.INFO: 1,
        }
        return weights.get(severity, 1)
