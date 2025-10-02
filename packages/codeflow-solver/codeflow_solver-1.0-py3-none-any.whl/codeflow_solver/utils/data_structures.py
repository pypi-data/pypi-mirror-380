"""
Data structures for representing vulnerabilities and fix locations.
"""

from dataclasses import dataclass
from typing import Set

from .severity_mapper import IssueSeverity


@dataclass
class Vulnerability:
    """
    Represents a single vulnerability vⱼ ∈ V

    Mathematical notation: vⱼ where j is the vulnerability index
    Each vulnerability belongs to a specific type (rule_id) and location
    """

    index: int  # j in vⱼ notation
    rule_id: str  # vulnerability type (XSS, SQLi, PT, etc.)
    file_path: str  # location where vulnerability manifests
    line: int  # specific line number
    severity: IssueSeverity = IssueSeverity.INFO  # severity level
    message: str = ""  # vulnerability description

    def __str__(self) -> str:
        return f"{self.rule_id} at {self.file_path}:{self.line}"


@dataclass
class FixLocation:
    """
    Represents a potential fix location nᵢ ∈ N with its coverage set Sᵥ(nᵢ)

    Mathematical notation:
    - nᵢ = fix location i
    - Sᵥ(nᵢ) = set of vulnerabilities covered by fixing at location nᵢ
    """

    file_path: str  # physical location of fix
    line: int  # line number for fix
    column: int  # column number for fix
    covered_vulnerabilities: Set[int]  # Sᵥ(nᵢ) - vulnerabilities this fix covers

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line}:{self.column}"

    def __hash__(self) -> int:
        return hash((self.file_path, self.line, self.column))

    def __eq__(self, other) -> bool:
        if not isinstance(other, FixLocation):
            return False
        return self.file_path == other.file_path and self.line == other.line and self.column == other.column
