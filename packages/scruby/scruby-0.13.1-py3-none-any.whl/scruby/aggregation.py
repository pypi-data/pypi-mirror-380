"""Aggregation classes."""

from __future__ import annotations

__all__ = (
    "Average",
    "Max",
    "Min",
    "Sum",
)

from typing import Any


class Average:
    """Aggregation class for calculating the average value."""

    def __init__(self) -> None:  # noqa: D107
        self.value = 0.0
        self.counter = 0.0

    def set(self, number: int | float) -> None:
        """Add value."""
        self.value += float(number)
        self.counter += 1.0

    def get(self) -> float:
        """Get arithmetic average value."""
        return self.value / self.counter


class Max:
    """Aggregation class for calculating the maximum value."""

    def __init__(self) -> None:  # noqa: D107
        self.value: Any = 0

    def set(self, number: int | float) -> None:
        """Add value."""
        if number > self.value:
            self.value = number

    def get(self) -> Any:
        """Get maximum value."""
        return self.value


class Min:
    """Aggregation class for calculating the minimum value."""

    def __init__(self) -> None:  # noqa: D107
        self.value: Any = 0

    def set(self, number: int | float) -> None:
        """Add value."""
        if self.value == 0 or number < self.value:
            self.value = number

    def get(self) -> Any:
        """Get minimum value."""
        return self.value


class Sum:
    """Aggregation class for calculating sum of values."""

    def __init__(self) -> None:  # noqa: D107
        self.value: Any = 0

    def set(self, number: int | float) -> None:
        """Add value."""
        self.value += number

    def get(self) -> Any:
        """Get sum of values."""
        return self.value
