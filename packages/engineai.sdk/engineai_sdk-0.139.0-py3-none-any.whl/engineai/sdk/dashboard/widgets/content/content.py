"""Spec for Content widget."""

from __future__ import annotations

from typing import Any

from engineai.sdk.dashboard.data.manager.manager import DataType
from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.widgets.base import Widget
from engineai.sdk.dashboard.widgets.base import WidgetTitleType
from engineai.sdk.dashboard.widgets.utils import build_data

from ...links import WidgetField
from .exceptions import ContentNoItemsError
from .item import ContentItem
from .item import build_content_item


class Content(Widget):
    """Spec for Content widget."""

    _WIDGET_API_TYPE = "content"
    _DEPENDENCY_ID = "__CONTENT_DATA_DEPENDENCY__"

    def __init__(
        self,
        *,
        data: DataType | dict[str, Any],
        widget_id: str | None = None,
        title: WidgetTitleType | None = None,
    ) -> None:
        """Construct spec for Content widget.

        Args:
            widget_id: unique widget id in a dashboard.
            title: title of widget can be either a
                string (fixed value) or determined by a value from another widget
                using a WidgetField.
            data: data source for the widget.
        """
        super().__init__(widget_id=widget_id, data=data)
        self.__items: list[ContentItem] = []
        self.__title = title
        self.__as_dict = (
            data.as_dict
            if isinstance(data, DataType) and not isinstance(data, WidgetField)
            else True
        )

    def validate(self, data: dict[str, Any], **_: Any) -> None:
        """Validates Content Widget specs and its inner components.

        Args:
            data (Dict[str, Any]): Dictionary where the data is present.
        """
        for item in self.__items:
            item.validate(data=data)

    def add_items(self, *items: ContentItem) -> Content:
        """Add a new ContentItem to the list of items to show on Content Widget.

        Args:
            items (ContentItem): Content Items to add to the Content Widget.

        Returns:
            Content: reference to this Content Widget to facilitate inline manipulation.

        """
        self.__items.extend(items)
        return self

    def _build_widget_input(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        if len(self.__items) == 0:
            raise ContentNoItemsError(
                widget_id=self.widget_id,
            )
        return {
            "title": (
                build_templated_strings(items=self.__title) if self.__title else None
            ),
            "contentItems": [build_content_item(item=item) for item in self.__items],
            "data": build_data(
                path=self.dependency_id,
                json_data=self._json_data,
                as_dict=self.__as_dict,
            ),
        }
