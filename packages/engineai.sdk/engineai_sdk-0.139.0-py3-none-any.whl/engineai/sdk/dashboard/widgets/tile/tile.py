"""Spec for Tile Widget."""

from typing import Any
from typing import get_args

from engineai.sdk.dashboard.data.manager.manager import DataType
from engineai.sdk.dashboard.widgets.base import Widget

from ..utils import build_data
from .content.items.chart.base import BaseTileChartItem
from .content.items.typings import LineChartItem
from .content.items.typings import NumberItem
from .content.items.typings import TextItem
from .content.items.typings import TileContentItem
from .enum import Orientation
from .header.header import Header


class Tile(Widget):
    """Spec for Tile Widget."""

    _DEPENDENCY_ID = "__TILE_DATA_DEPENDENCY__"
    _WIDGET_API_TYPE = "tile"
    _DEFAULT_HEIGHT = 0.84
    _FLUID_ROW_COMPATIBLE = True

    def __init__(
        self,
        data: DataType | dict[str, Any],
        *,
        items: list[TileContentItem | str] | None = None,
        widget_id: str | None = None,
        header: Header | None = None,
        show_separator: bool = True,
        orientation: Orientation = Orientation.HORIZONTAL,
        height: int | float | None = None,
    ) -> None:
        """Construct spec for the Tile Widget.

        Args:
            items: list of items to be displayed in the tile widget.
            widget_id: unique widget id in a dashboard.
            data: data to be used by widget. Accepts Storages as well as raw data.
            header: spec for the header in Tile widget.
            show_separator: flag to show or hide separator.
            orientation: orientation of items in tile widget content.
            height: height value for the widget.
                Defaults to 0.84 (84px).

        Note:
            If `data` is a Http connector dependency,
            make sure that the return from the http request is a dictionary.

        Examples:
            ??? example "Create a minimal Tile widget"
                ```py linenums="1"
                    from engineai.sdk.dashboard.dashboard import Dashboard
                    from engineai.sdk.dashboard.widgets import tile

                    data = {
                        "number": 10,
                        "text": "Hello World",
                        "line_chart": [1, 2, 3, 4, 5],
                        }

                    tile_widget = tile.Tile(data=data)

                    Dashboard(content=tile_widget)
                ```
        """
        super().__init__(
            widget_id=widget_id,
            data=data,
        )
        self.__header = header
        self.__show_separator = show_separator
        self.__orientation = orientation
        self.__items: list[TileContentItem] = self.__set_items(data=data, items=items)
        self.__height = height or self._DEFAULT_HEIGHT
        self.__as_dict = data.as_dict if isinstance(data, get_args(DataType)) else True

    def __set_items(
        self,
        data: DataType | dict[str, Any],
        items: list[TileContentItem | str] | None,
    ) -> list[TileContentItem]:
        if isinstance(data, DataType):
            if items is None or len(items) == 0:
                msg = (
                    "Items cannot be empty when data is a "
                    "DataSource or a Http instance."
                )
                raise ValueError(msg)
        elif items is None or len(items) == 0:
            return self.__generate_data(data)

        return [
            TextItem(data_column=item) if isinstance(item, str) else item
            for item in items
        ]

    def __generate_data(self, data: dict[str, Any]) -> list[TileContentItem]:
        result: list[TileContentItem] = []
        for key, value in data.items():
            if isinstance(value, int | float):
                result.append(
                    NumberItem(
                        data_column=key,
                    )
                )
            elif isinstance(value, str):
                result.append(
                    TextItem(
                        data_column=key,
                    )
                )

            elif isinstance(value, list) and all(
                isinstance(i, int | float) for i in value
            ):
                result.append(
                    LineChartItem(
                        data_column=key,
                    )
                )
        return result

    @property
    def full_height(self) -> float | int:
        """Returns full height required widget.

        Returns:
            Union[float, int]: full height required by item
        """
        return self.__height

    @property
    def height(self) -> float | int:
        """Returns tile widget height."""
        return self.__height

    def _prepare(self, **_: object) -> None:
        """Prepares widget spec."""
        for item in self.__items:
            if isinstance(item, BaseTileChartItem):
                item.prepare()

    def _validate_header(
        self,
        *,
        data: dict[str, Any],
    ) -> None:
        if self.__header is not None:
            self.__header.validate(data=data, required=False)

    def _validate_items(
        self,
        *,
        data: dict[str, Any],
    ) -> None:
        for item in self.__items:
            item.validate(data=data)

    def validate(self, data: dict[str, Any], **_: Any) -> None:
        """Validates widget spec.

        Args:
            data (Dict[str, Any]): Dict where
                the data is present.
        """
        self._validate_header(data=data)
        self._validate_items(data=data)

    def _build_content(self) -> dict[str, Any]:
        return {
            "items": [item.build_item() for item in self.__items],
            "layout": self._build_content_layout(),
        }

    def _build_content_layout(self) -> dict[str, Any]:
        return {
            "showSeparator": self.__show_separator,
            "orientation": self.__orientation.value,
        }

    def _build_widget_input(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Input object for Dashboard API
        """
        return {
            "data": build_data(
                path=self.dependency_id,
                json_data=self._json_data,
                as_dict=self.__as_dict,
            ),
            "header": (
                self.__header.build() if self.__header is not None else self.__header
            ),
            "content": self._build_content(),
        }
