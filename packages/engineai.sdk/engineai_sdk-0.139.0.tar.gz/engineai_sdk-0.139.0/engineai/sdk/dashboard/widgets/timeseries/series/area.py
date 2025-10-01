"""Spec for a area series of a Timeseries widget."""

from typing import Any

import pandas as pd

from engineai.sdk.dashboard.links import WidgetField
from engineai.sdk.dashboard.links.typing import GenericLink
from engineai.sdk.dashboard.styling.color import Palette
from engineai.sdk.dashboard.widgets.components.charts.series.entities.country import (
    CountryEntity,
)
from engineai.sdk.dashboard.widgets.components.charts.series.entities.typing import (
    Entities,
)
from engineai.sdk.dashboard.widgets.components.charts.styling import AreaSeriesStyling
from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItems

from .base import TimeseriesBaseSeries


class AreaSeries(TimeseriesBaseSeries):
    """Visualize data as filled areas in Timeseries widget.

    Construct specifications for an area series within a Timeseries
    widget to visualize data as filled areas on the chart.
    """

    _INPUT_KEY = "area"
    _styling_class = AreaSeriesStyling

    def __init__(
        self,
        *,
        data_column: str | WidgetField,
        name: str | GenericLink | None = None,
        styling: Palette | AreaSeriesStyling | None = None,
        entity: Entities | None = None,
        show_in_legend: bool = True,
        required: bool = True,
        visible: bool = True,
        right_axis: bool = False,
        tooltips: TooltipItems | None = None,
    ) -> None:
        """Constructor for AreaSeries.

        Args:
            data_column: name of column in pandas dataframe(s) used for the values of
                this series.
            name: series name shown in legend and tooltip.
            styling: styling spec, by default uses the values from the sequential
                palette.
            entity: entity spec.
            show_in_legend: whether to show series in legend or not.
            required: Flag to make the Series mandatory. If required == True and no
                Data the widget will show an error. If required==False and no Data,
                the widget hides the Series.
            visible: Flag to make the Series visible when chart is loaded.
            right_axis: Flag to make the Series visible on the right axis.
            tooltips: tooltip items to be displayed at Series level.
        """
        super().__init__(
            name=name,
            data_column=data_column,
            show_in_legend=show_in_legend,
            required=required,
            visible=visible,
            styling=(
                AreaSeriesStyling(color_spec=styling)
                if isinstance(styling, Palette)
                else styling
            ),
            entity=entity,
            right_axis=right_axis,
            tooltips=tooltips,
        )

    def validate(self, *, data: pd.DataFrame) -> None:
        """Validate if dataframe that will be used for series contains required columns.

        Args:
            data: pandas dataframe which will be used for table
        """
        super().validate(data=data)

        if self._entity is not None and isinstance(self._entity, CountryEntity):
            self._entity.validate_country_code()

    def _build_extra_inputs(self) -> dict[str, Any]:
        return {
            "transforms": [transform.build() for transform in self._transforms],
        }
