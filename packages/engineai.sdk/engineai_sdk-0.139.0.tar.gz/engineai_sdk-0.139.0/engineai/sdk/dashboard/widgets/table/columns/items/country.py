"""Specification for Country Column in Table widget."""

from __future__ import annotations

import enum
from typing import TYPE_CHECKING
from typing import Any

from typing_extensions import override

from engineai.sdk.dashboard.formatting import TextFormatting
from engineai.sdk.dashboard.widgets.table.columns.styling.country_flag import (
    CountryFlagStyling,
)
from engineai.sdk.dashboard.widgets.table.columns.styling.utils import (
    build_styling_input,
)
from engineai.sdk.dashboard.widgets.table.enums import HorizontalAlignment

from .base import Column

if TYPE_CHECKING:
    import pandas as pd

    from engineai.sdk.dashboard.links import WidgetField
    from engineai.sdk.dashboard.links.typing import GenericLink
    from engineai.sdk.dashboard.templated_string import TemplatedStringItem


class FlagPositions(enum.Enum):
    """Country Column Flag Position Options.

    Attributes:
        LEFT: Flag at the left of the country name.
        RIGHT: Flag at the right of the country name.
        HIDDEN: Flag is hidden.
    """

    LEFT = True
    RIGHT = False
    HIDDEN = None


class CountryColumn(Column):
    """Define table widget column: Country information with data source.

    Define a column in the table widget that displays country information,
    including options for data source, label, formatting, and alignment.
    """

    _ITEM_ID_TYPE: str = "COUNTRY"

    def __init__(
        self,
        *,
        data_column: str | WidgetField,
        label: str | GenericLink | None = None,
        formatting: TextFormatting | None = None,
        flag_position: FlagPositions = FlagPositions.LEFT,
        align: HorizontalAlignment = HorizontalAlignment.LEFT,
        hiding_priority: int = 0,
        tooltip_text: list[TemplatedStringItem] | None = None,
        min_width: int | None = None,
        sortable: bool = False,
        optional: bool = False,
    ) -> None:
        """Constructor for Country Column.

        Args:
            data_column: name of column in pandas dataframe(s) used for this widget.
                Data in this column should be ISO 3166-1 alpha-2 country codes.
            label: label to be displayed for this column.
            flag_position: position of country flag.
            formatting: text formatting spec.
            align: column alignment.
            hiding_priority: columns with lower hiding_priority are hidden first
                if not all data can be shown.
            tooltip_text: info text to explain column. Each element of list is
                displayed as a separate paragraph.
            min_width: min width of the column in pixels.
            sortable: determines if column can be sorted.
            optional: flag to make the column optional if there is no Data for that
                columns.

        Examples:
            ??? example "Create a Table widget with Country Column"
                ```py linenums="1"
                import pandas as pd
                from engineai.sdk.dashboard.dashboard import Dashboard
                from engineai.sdk.dashboard.widgets import table
                data = pd.DataFrame(
                    {
                        "country_code": ["US", "CA", "MX"],
                    },
                )
                Dashboard(
                    content=table.Table(
                        data=data,
                        columns=[
                            table.CountryColumn(
                                data_column="country_code",
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
            optional=optional,
        )
        self.__align = align
        self.__styling = (
            None
            if flag_position == FlagPositions.HIDDEN
            else CountryFlagStyling(data_column=data_column, left=flag_position.value)
        )
        self.__sortable = sortable
        self.__formatting = formatting if formatting else TextFormatting()

    @override
    def _custom_validation(self, *, data: pd.DataFrame) -> None:
        pass

    def _build_styling(self) -> dict[str, Any] | None:
        return (
            None
            if self.__styling is None
            else build_styling_input(
                data_column=self.data_column, styling=self.__styling
            )
        )

    @override
    def _build_column(self) -> dict[str, Any]:
        return {
            "countryColumn": {
                "sortable": self.__sortable,
                "formatting": self.__formatting.build(),
                "align": self.__align.value,
                "styling": self._build_styling(),
                "optional": self._optional,
            }
        }
