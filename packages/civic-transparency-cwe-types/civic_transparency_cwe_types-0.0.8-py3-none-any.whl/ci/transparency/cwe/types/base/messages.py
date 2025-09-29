# src/ci/transparency/cwe/types/base/messages.py
"""Define message collection classes for error, warning, and informational messages.

It provides:
- MessageCollection: a dataclass for collecting and counting error, warning, and info messages.
"""

from dataclasses import dataclass, field
from typing import cast


# Message collections
@dataclass(frozen=True)
class MessageCollection:
    """Collects error, warning, and info messages.

    Attributes
    ----------
    errors : list[str]
        list of error messages.
    warnings : list[str]
        list of warning messages.
    infos : list[str]
        list of informational messages.
    """

    errors: list[str] = cast("list[str]", field(default_factory=list))
    warnings: list[str] = cast("list[str]", field(default_factory=list))
    infos: list[str] = cast("list[str]", field(default_factory=list))

    @property
    def error_count(self) -> int:
        """Return the number of error messages."""
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        """Return the number of warning messages."""
        return len(self.warnings)

    @property
    def info_count(self) -> int:
        """Return the number of informational messages."""
        return len(self.infos)

    @property
    def total_messages(self) -> int:
        """Return the total number of messages (errors, warnings, infos)."""
        return self.error_count + self.warning_count + self.info_count

    @property
    def has_errors(self) -> bool:
        """Return True if there are any error messages, otherwise False."""
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        """Return True if there are any warning messages, otherwise False."""
        return bool(self.warnings)


__all__ = [
    "MessageCollection",
]
