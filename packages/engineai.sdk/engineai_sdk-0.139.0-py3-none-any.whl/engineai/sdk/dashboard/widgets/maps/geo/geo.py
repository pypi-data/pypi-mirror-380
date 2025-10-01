"""Spec for Map Geo widget."""

from engineai.sdk.dashboard.data.manager.manager import DataType
from engineai.sdk.dashboard.data.manager.manager import StaticDataType
from engineai.sdk.dashboard.widgets.base import WidgetTitleType
from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItems
from engineai.sdk.dashboard.widgets.maps.color_axis import ColorAxis
from engineai.sdk.dashboard.widgets.maps.enums import LegendPosition
from engineai.sdk.dashboard.widgets.maps.enums import Region
from engineai.sdk.dashboard.widgets.maps.series.series import MapSeries

from .base import BaseMapGeo
from .styling.styling import MapStyling


class Geo(BaseMapGeo):
    """Widget for tailored geographic data visualization.

    Allows the construction of a widget specifically tailored
    for geographical data visualization.
    """

    def __init__(
        self,
        data: DataType | StaticDataType,
        *,
        series: MapSeries | None = None,
        region_column: str = "region",
        color_axis: ColorAxis | None = None,
        widget_id: str | None = None,
        title: WidgetTitleType | None = None,
        legend_position: LegendPosition = LegendPosition.BOTTOM,
        styling: MapStyling | None = None,
        region: Region = Region.WORLD,
        tooltips: TooltipItems | None = None,
    ) -> None:
        """Constructor for Map Geo widget.

        Args:
            data: data source for the widget.
            series: Series to be added to y axis.
            region_column: key to match region code in DS.
            widget_id: unique widget id in a dashboard.
            color_axis: color axis spec.
            title: title of widget can be either a string (fixed value) or determined
                by a value from another widget using a WidgetField.
            legend_position: location of position relative to data, maps.
            styling: styling for the map.
            region: sets the region os the Map.
            tooltips: tooltip items to be displayed at Chart level.
        """
        super().__init__(
            data=data,
            series=series,
            region_column=region_column,
            widget_id=widget_id,
            title=title,
            legend_position=legend_position,
            color_axis=color_axis,
            styling=styling,
            region=region,
            tooltips=tooltips,
        )
