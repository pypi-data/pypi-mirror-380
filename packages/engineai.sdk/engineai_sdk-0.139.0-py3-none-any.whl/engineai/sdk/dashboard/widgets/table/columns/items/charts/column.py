"""Specification for Column Chart columns in Table widget."""

from typing import Any

import pandas as pd

from engineai.sdk.dashboard.formatting import NumberFormatting
from engineai.sdk.dashboard.links import WidgetField
from engineai.sdk.dashboard.links.typing import GenericLink
from engineai.sdk.dashboard.styling import color
from engineai.sdk.dashboard.styling.color import Palette
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.widgets.components.items.tooltip.tooltip import ChartTooltip
from engineai.sdk.dashboard.widgets.table.columns.styling.column import (
    ColumnChartStyling,
)

from .base import ChartColumn
from .base import ReferenceLineType


class ColumnChartColumn(ChartColumn):
    """Define table widget column: Column sparkline chart with data.

    Define a column in the table widget that displays a column
    sparkline chart, including options for data, formatting, styling,
    and more.
    """

    _ITEM_ID_TYPE: str = "COLUMN_CHART"

    def __init__(
        self,
        *,
        data_column: str | WidgetField,
        data_key: str | WidgetField,
        label: str | GenericLink | None = None,
        formatting: NumberFormatting | None = None,
        styling: Palette | ColumnChartStyling | None = None,
        display_first_value: bool = True,
        display_last_value: bool = True,
        reference_line: ReferenceLineType | None = None,
        hiding_priority: int = 0,
        tooltip_text: list[TemplatedStringItem] | None = None,
        min_width: int | None = None,
        sortable: bool = True,
        optional: bool = False,
        tooltip: ChartTooltip | None = None,
    ) -> None:
        """Constructor for ColumnChartColumn.

        Args:
            data_column: name of column in pandas dataframe(s) used for this widget.
            data_key: key in object that contains the value for the line chart.
            label: label to be displayed for this column.
            formatting: formatting spec.
            styling: styling spec for column chart.
            display_first_value: display first value before chart.
            display_last_value: display last value after chart.
            reference_line: reference line that will be added to the chart created.
            hiding_priority: columns with lower hiding_priority are hidden first
                if not all data can be shown.
            tooltip_text: info text to explain column. Each element of list is
                displayed as a separate paragraph.
            min_width: min width of the column in pixels.
            sortable: determines if column can be sorted.
            optional: flag to make the column optional if there is no Data for that
                columns.
            tooltip: specs for tooltip.

        Examples:
            ??? example "Create a Table widget with ColumnChartColumn"
                ```py linenums="1"
                import pandas as pd
                from engineai.sdk.dashboard.dashboard import Dashboard
                from engineai.sdk.dashboard.widgets import table
                data = pd.DataFrame(
                    {
                        "chart": [{"value": [1, 2, 3]}, {"value": [5, 10, 1]}],
                    },
                )
                Dashboard(
                    content=table.Table(
                        data=data,
                        columns=[
                            table.ColumnChartColumn(
                                data_column="chart",
                                data_key="value",
                            ),
                        ],
                    )
                )
                ```
        """
        super().__init__(
            data_column=data_column,
            label=label,
            hiding_priority=hiding_priority,
            tooltip_text=tooltip_text,
            min_width=min_width,
            data_key=data_key,
            reference_line=reference_line,
            styling=(
                styling
                if styling
                else ColumnChartStyling(color_spec=color.Palette.MINT_GREEN)
            ),
            optional=optional,
        )
        self.__formatting = formatting if formatting else NumberFormatting()
        self.__display_first_value = display_first_value
        self.__display_last_value = display_last_value
        self.__sortable = sortable
        self.__tooltip = tooltip

    def _build_column(self) -> dict[str, Any]:
        return {
            "columnChartColumn": {
                "formatting": self.__formatting.build(),
                "styling": self._build_styling(),
                "displayFirstValue": self.__display_first_value,
                "displayLastValue": self.__display_last_value,
                "referenceLine": (
                    self.reference_line.build() if self.reference_line else None
                ),
                "valueKey": build_templated_strings(items=self.data_key),
                "sortable": self.__sortable,
                "optional": self._optional,
                "tooltip": self.__tooltip.build() if self.__tooltip else None,
            }
        }

    def _custom_validation(self, *, data: pd.DataFrame) -> None:
        super()._custom_validation(data=data)
        if self.__tooltip:
            self.__tooltip.validate(data=data)
