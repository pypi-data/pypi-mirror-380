"""Spec for Tile Widget Area Chart Item."""

from collections.abc import Mapping
from typing import Any

from engineai.sdk.dashboard.formatting.number import NumberFormatting
from engineai.sdk.dashboard.styling.color.palette import Palette
from engineai.sdk.dashboard.templated_string import DataField
from engineai.sdk.dashboard.templated_string import InternalDataField
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.widgets.components.items.styling import AreaChartItemStyling
from engineai.sdk.dashboard.widgets.components.items.tooltip.tooltip import ChartTooltip

from .base import BaseTileChartItem


class AreaChartItem(BaseTileChartItem):
    """Spec for Tile Area Chart Item."""

    _API_CHART_TYPE = "area"

    def __init__(
        self,
        *,
        data_column: TemplatedStringItem,
        reference_line: int | float | DataField | None = None,
        styling: Palette | AreaChartItemStyling | None = None,
        formatting: NumberFormatting | None = None,
        label: TemplatedStringItem | DataField | None = None,
        tooltip: ChartTooltip | None = None,
        required: bool = True,
    ) -> None:
        """Construct spec for the TileAreaChartItem class.

        Args:
            reference_line: spec for a fixed reference line.
            styling: styling spec for item charts.
            data_column: key in data that will have the values used by the item.
            formatting: formatting spec.
            label: str that will label the item values.
            tooltip: specs for tooltip.
            required: Flag to make Number item mandatory. If required is True
                and no Data the widget will show an error. If
                required is False and no Data, the item is not shown.
        """
        super().__init__(
            styling=(
                AreaChartItemStyling(color_spec=styling)
                if isinstance(styling, Palette)
                else (
                    AreaChartItemStyling(color_spec=Palette.AQUA_GREEN)
                    if styling is None
                    else styling
                )
            ),
            data_column=data_column,
            formatting=formatting,
            label=label,
            required=required,
        )
        self.__set_reference_line(reference_line=reference_line)
        self.__tooltip = tooltip

    def __set_reference_line(
        self, reference_line: int | float | DataField | None
    ) -> None:
        if reference_line is None:
            self.__reference_line = None
        elif isinstance(reference_line, (DataField)):
            self.__reference_line = InternalDataField(reference_line)
        else:
            self.__reference_line = InternalDataField(str(reference_line))

    def _build_extra_chart_inputs(self) -> Mapping[str, Any]:
        """Build extra inputs for the chart."""
        return {
            "referenceLine": (
                self.__reference_line.build() if self.__reference_line else None
            ),
            "tooltip": self.__tooltip.build() if self.__tooltip else None,
        }

    def validate(self, data: dict[str, Any]) -> None:
        """Validates Tile Item.

        Args:
            widget_id (str): id of Tile Widget.
            data (Dict[str, Any]): Dict where the data is present.
        """
        super().validate(data)
        if self.__reference_line:
            self.__reference_line.validate(data=data)
        if self.__tooltip:
            self.__tooltip.validate(data=data)
