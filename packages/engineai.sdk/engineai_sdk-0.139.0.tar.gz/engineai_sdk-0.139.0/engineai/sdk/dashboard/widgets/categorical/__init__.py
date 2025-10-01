"""Specs for categorical widgets."""

from engineai.sdk.dashboard.enum import LegendPosition
from engineai.sdk.dashboard.widgets.components.charts.axis.label import AxisLabel
from engineai.sdk.dashboard.widgets.components.charts.band.band import AxisBand
from engineai.sdk.dashboard.widgets.components.charts.line.line import AxisLine
from engineai.sdk.dashboard.widgets.components.charts.tooltip import CategoryTooltipItem
from engineai.sdk.dashboard.widgets.components.charts.tooltip import DatetimeTooltipItem
from engineai.sdk.dashboard.widgets.components.charts.tooltip import NumberTooltipItem
from engineai.sdk.dashboard.widgets.components.charts.tooltip import TextTooltipItem

from .axis.category import CategoryAxis
from .axis.value import ValueAxis
from .categorical import Categorical
from .enum import ChartDirection
from .series.area import AreaSeries
from .series.area_range import AreaRangeSeries
from .series.bubble import BubbleSeries
from .series.column import ColumnSeries
from .series.error_bar import ErrorBarSeries
from .series.line import LineSeries
from .series.point import PointSeries
from .series.scatter import ScatterSeries

__all__ = [
    "AreaRangeSeries",
    "AreaSeries",
    "AxisBand",
    "AxisLabel",
    # .lines/bands
    "AxisLine",
    "BubbleSeries",
    # .categorical
    "Categorical",
    # .axis
    "CategoryAxis",
    # .tooltip
    "CategoryTooltipItem",
    # .chart
    "ChartDirection",
    "ColumnSeries",
    "DatetimeTooltipItem",
    "ErrorBarSeries",
    # .legend
    "LegendPosition",
    # .series
    "LineSeries",
    "NumberTooltipItem",
    "PointSeries",
    "ScatterSeries",
    "TextTooltipItem",
    "ValueAxis",
]
