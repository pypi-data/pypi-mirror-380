"""Spec to build tooltip items supported by different charts."""

from typing import Any

from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItem

from .category import CategoryTooltipItem
from .datetime import DatetimeTooltipItem
from .number import NumberTooltipItem
from .text import TextTooltipItem


def build_tooltip_item(item: TooltipItem) -> dict[str, Any]:
    """Builds spec for dashboard API.

    Args:
        item (TooltipItem): item spec

    Returns:
        Input object for Dashboard API
    """
    return {_get_input_key(item): item.build()}


def _get_input_key(item: TooltipItem) -> str:
    if isinstance(item, NumberTooltipItem):
        return "number"
    if isinstance(item, TextTooltipItem):
        return "text"
    if isinstance(item, DatetimeTooltipItem):
        return "dateTime"
    if isinstance(item, CategoryTooltipItem):
        return "categorical"
    # if isinstance(item, CountryTooltipItem):
    return "country"
