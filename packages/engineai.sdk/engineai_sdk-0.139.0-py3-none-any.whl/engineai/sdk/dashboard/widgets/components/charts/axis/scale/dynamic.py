"""Spec for dynamic scale for y axis."""

from typing import Any

from engineai.sdk.dashboard.base import AbstractFactory


class AxisScaleDynamic(AbstractFactory):
    """Dynamically set y-axis extremes for optimal spacing.

    Construct specifications for a dynamic scale for the y-axis of a chart.
    By default, it dynamically calculates axis extremes to minimize
    dead space in the chart.
    """

    def __init__(self, *, tick_amount: int = 3) -> None:
        """Constructor for AxisScaleDynamic.

        Args:
            tick_amount: number of ticks beyond min and max.
        """
        super().__init__()
        self.__tick_amount = tick_amount

    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {"tickAmount": self.__tick_amount}
