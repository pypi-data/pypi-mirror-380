"""Specs for header for a tooltip."""

from typing import Any

import pandas as pd

from engineai.sdk.dashboard.links.abstract import AbstractFactoryLinkItemsHandler
from engineai.sdk.dashboard.templated_string import DataField
from engineai.sdk.dashboard.templated_string import InternalDataField
from engineai.sdk.dashboard.widgets.components.charts.tooltip.base import (
    TooltipItemFormatter,
)

from .format_build import build_items


class HeaderTooltip(AbstractFactoryLinkItemsHandler):
    """Specs for Header Tooltip."""

    def __init__(
        self,
        title: str | DataField,
        formatting: TooltipItemFormatter,
    ) -> None:
        """Construct for Header Tooltip class.

        Args:
            title (Union[str, DataField]): header title spec.
            formatting (TooltipItemFormatter): header tooltip formatting.
        """
        super().__init__()
        self.__title = InternalDataField(title)
        self.__format = formatting

    def validate(
        self,
        data: pd.DataFrame | dict[str, Any],
        item_id_key: str | None = None,
    ) -> None:
        """Validate tooltip header data dependencies.

        Args:
            data (Union[pd.DataFrame, Dict[str, Any]]): pandas DataFrame or dict where
                the data is present.
            item_id_key: Optional[str]: key in data (if using data as dict) used to
                identify the data that feeds this item.
        """
        self.__title.validate(data=data, item_id_key=item_id_key)

    def build(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Any: Input object for Dashboard API
        """
        return {
            "title": self.__title.build(),
            "format": build_items(self.__format) if self.__format else None,
        }
