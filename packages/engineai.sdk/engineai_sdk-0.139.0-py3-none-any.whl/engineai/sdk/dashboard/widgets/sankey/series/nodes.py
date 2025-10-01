"""Spec for Sankey nodes."""

from typing import Any
from typing import Generic
from typing import TypeVar

import pandas as pd

from engineai.sdk.dashboard.data.manager.manager import DataType
from engineai.sdk.dashboard.data.manager.manager import DependencyManager
from engineai.sdk.dashboard.styling.color import Palette
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.widgets.components.charts.tooltip.item import (
    build_tooltip_item,
)
from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItems
from engineai.sdk.dashboard.widgets.sankey.exceptions import (
    SankeyItemsValidateNoDataColumnError,
)
from engineai.sdk.dashboard.widgets.utils import build_data
from engineai.sdk.dashboard.widgets.utils import get_tooltips

from .styling.nodes import NodesStyling

T = TypeVar("T", pd.DataFrame, dict[str, pd.DataFrame])


class BaseNodes(Generic[T], DependencyManager):
    """Spec for Sankey nodes."""

    _DEPENDENCY_ID = "__SANKEY_NODES_DEPENDENCY__"
    _ID_COUNTER = 0

    def __init__(
        self,
        data: DataType | T,
        *,
        id_column: TemplatedStringItem = "id",
        label_column: TemplatedStringItem | None = None,
        styling: Palette | NodesStyling | None = None,
        tooltips: TooltipItems | None = None,
    ) -> None:
        """Construct spec for nodes in Sankey widget.

        Args:
            id_column: name of column in pandas dataframe with
                id of each node.
            label_column: name of column in pandas
                dataframe with label for each node.
            data: data for
                the widget. Can be a pandas dataframe, a dictionary or Storage object
                if the data is to be retrieved from a storage.
            styling: styling spec.
            tooltips: list of tooltip items.
        """
        self.__data_id = self.__generate_id()
        super().__init__(data=data)
        self._tooltip_items = get_tooltips(tooltips)
        self.__id_column = id_column
        self.__label_column = label_column or id_column
        self.__styling = (
            NodesStyling(color_spec=styling)
            if isinstance(styling, Palette)
            else styling
            if styling
            else NodesStyling()
        )
        self.__is_playback = False

    @property
    def data_id(self) -> str:
        """Get data id."""
        return self.__data_id

    @property
    def is_playback(self) -> bool:
        """Getter for the is_playback property."""
        return self.__is_playback

    @is_playback.setter
    def is_playback(self, value: bool) -> None:
        """Setter for the is_playback property."""
        self.__is_playback = value

    def __generate_id(self) -> str:
        self._increment_id_counter()
        return f"nodes_data_{self._ID_COUNTER}"

    @classmethod
    def _increment_id_counter(cls) -> None:
        cls._ID_COUNTER = cls._ID_COUNTER + 1

    def validate(self, data: T, **_: object) -> None:  # type: ignore
        """Validates Sankey Series Nodes widget spec.

        Args:
            data: Data related to Nodes

        Raises:
            SankeyItemsValidateNoDataColumnError: If id_column is not found
                in Data Columns
            SankeyItemsValidateNoDataColumnError: If label_column is not found
                in Data Columns
        """
        iterable = iter([data]) if isinstance(data, pd.DataFrame) else data.values()
        for value in iterable:
            if (
                isinstance(self.__id_column, str)
                and isinstance(value, pd.DataFrame)
                and self.__id_column not in value.columns
            ):
                raise SankeyItemsValidateNoDataColumnError(
                    missing_column_name="Id column",
                    missing_column=self.__id_column,
                    item_name="Nodes",
                )

            if (
                isinstance(self.__label_column, str)
                and isinstance(value, pd.DataFrame)
                and self.__label_column not in value.columns
            ):
                raise SankeyItemsValidateNoDataColumnError(
                    missing_column_name="Label column",
                    missing_column=self.__label_column,
                    item_name="Nodes",
                )

            self.__styling.validate(data=value)

    @property
    def tooltip_items(self) -> Any:
        """Returns the tooltip items."""
        return self._tooltip_items

    def build_tooltips(
        self,
    ) -> dict[str, Any] | None:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return (
            {
                "idKey": self.__id_column,
                "items": [build_tooltip_item(item=item) for item in self.tooltip_items],
                "data": build_data(path=self.dependency_id, json_data=self._json_data),
            }
            if len(self.tooltip_items) > 0
            else None
        )

    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "idKey": build_templated_strings(items=self.__id_column),
            "labelKey": build_templated_strings(items=self.__label_column),
            "styling": self.__styling.build(),
            "data": build_data(
                path=self.dependency_id,
                json_data=self._json_data,
                as_dict=self.__is_playback,
            ),
        }
