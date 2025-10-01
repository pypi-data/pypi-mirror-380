"""Spec for a numeric series of a Map widget."""

from typing import Any

import pandas as pd

from engineai.sdk.dashboard.formatting import NumberFormatting
from engineai.sdk.dashboard.styling import color
from engineai.sdk.dashboard.styling.color import Palette
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.widgets.components.charts.tooltip.item import (
    build_tooltip_item,
)
from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItems
from engineai.sdk.dashboard.widgets.maps.exceptions import MapColumnDataNotFoundError
from engineai.sdk.dashboard.widgets.maps.series.styling import SeriesStyling
from engineai.sdk.dashboard.widgets.utils import build_data
from engineai.sdk.dashboard.widgets.utils import get_tooltips


class NumericSeries:
    """Spec for a numeric series of a Map widget."""

    def __init__(
        self,
        *,
        data_column: TemplatedStringItem = "value",
        name: TemplatedStringItem | None = None,
        formatting: NumberFormatting | None = None,
        styling: Palette | SeriesStyling | None = None,
        required: bool = True,
        tooltips: TooltipItems | None = None,
    ) -> None:
        """Constructor for NumericSeries.

        Args:
            data_column: data column to match field in DataStore.
            name: series name (shown in legend and tooltip).
            formatting: formatting spec for value.
            styling: styling spec.
            required: Flag to make the Series mandatory. If required == True and no
                Data the widget will show an error. If required==False and no Data,
                the widget hides the Series.
            tooltips: tooltip items to be displayed at Series level.
        """
        super().__init__()
        self.__name = name or "Series"
        self.__formatting = formatting if formatting else NumberFormatting()
        self.__styling = (
            SeriesStyling(color_spec=styling)
            if isinstance(styling, Palette)
            else styling
        )
        self.__tooltip_items = get_tooltips(tooltips)
        self.__required = required
        self.__data_column = data_column
        self.__dependency_id: str = ""
        self.__region_column: str = ""
        self._json_data: Any = None
        self.__is_playback = False

    @property
    def data_column(self) -> TemplatedStringItem:
        """Returns the data column."""
        return self.__data_column

    @property
    def is_playback(self) -> bool:
        """Getter for the is_playback property."""
        return self.__is_playback

    @is_playback.setter
    def is_playback(self, value: bool) -> None:
        """Setter for the is_playback property."""
        self.__is_playback = value

    def validate(self, data: pd.DataFrame) -> None:
        """Validates widget spec.

        Args:
            data: pandas DataFrame where
                the data is present.

        Raises:
            TooltipItemColumnNotFoundError: if column(s) of tooltip(s) were not found
            MapColumnDataNotFoundError: if column(s) supposed to contain data were not
                found.
            DataFieldNotFoundError: if column passed as DataField not found in data.
        """
        if self.__data_column not in data.columns:
            raise MapColumnDataNotFoundError(column_data=self.__data_column)

        self.__formatting.validate(data=data)

        if self.__styling:
            self.__styling.validate(data=data)

        if self.__tooltip_items:
            for tooltips in self.__tooltip_items:
                tooltips.validate(data=data)

    def prepare(
        self, index: int, region_column: str, dependency_id: str, json_data: Any = None
    ) -> None:
        """Prepares widget spec."""
        self.__region_column = region_column
        self.__dependency_id = dependency_id
        self._json_data = json_data
        if self.__styling is None:
            self.__styling = SeriesStyling(
                color_spec=color.Single(
                    color=color.palette.qualitative_palette(index=index)
                )
            )

    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "valueKey": build_templated_strings(items=self.__data_column),
            "regionKey": build_templated_strings(items=self.__region_column),
            "name": build_templated_strings(items=self.__name),
            "formatting": self.__formatting.build(),
            "styling": self.__styling.build() if self.__styling else None,
            "tooltipItems": [
                build_tooltip_item(item=item) for item in self.__tooltip_items
            ],
            "data": build_data(
                path=self.__dependency_id,
                json_data=self._json_data,
                as_dict=self.__is_playback,
            ),
            "required": self.__required,
        }
