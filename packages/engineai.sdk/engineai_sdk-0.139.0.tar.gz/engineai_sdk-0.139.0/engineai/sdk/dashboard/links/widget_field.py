"""Specs for WidgetField."""

from collections.abc import Iterator
from typing import Any
from typing import cast

import pandas as pd
from typing_extensions import override

from engineai.sdk.dashboard.abstract.selectable_widgets import AbstractSelectWidget
from engineai.sdk.dashboard.base import AbstractLink
from engineai.sdk.dashboard.dependencies import WidgetSelectDependency


class WidgetField(AbstractLink):
    """Establish a link to a selectable widget.

    Used in indirect dependencies and text fields that are linked to a other widgets.
    """

    def __init__(self, *, widget: AbstractSelectWidget, field: str) -> None:
        """Construct link to a selectable widget.

        Args:
            widget (SelectableWidget): selectable widget to establish link
            field (str): field from selectable widget
        """
        self.__widget = widget
        self.__field = field
        self.__dependency = cast(WidgetSelectDependency, widget.select_dependency())  # type: ignore

    @property
    def item_id(self) -> str:
        """Returns Item Id."""
        return f"WF_{self.__widget.widget_id}_{self.__field}"

    def __iter__(self) -> Iterator[tuple[str, str]]:
        yield "widget_id", self.__widget.widget_id
        yield "field", self.__field

    def __hash__(self) -> int:
        return hash(tuple(self))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and tuple(self) == tuple(other)

    def validate(self, storage: Any, data: pd.DataFrame, data_column_name: str) -> None:
        """Validates if field used in link is exposed by widget.

        For instance if field is an id of one of the columns in a table

        Args:
            storage (Any): storage spec.
            data (DataFrame): pandas DataFrame where the data is present.
            data_column_name (str): name of the column where the data is present.
        """

    @property
    @override
    def link_component(self) -> Any:
        """Returns selectable widget.

        Returns:
            SelectableWidget: selectable widget
        """
        return self.__widget

    @property
    def field(self) -> str:
        """Returns id of field to be used from selectable widget.

        Returns:
            str: field id from selectable widget
        """
        return self.__field

    @property
    @override
    def dependency(self) -> WidgetSelectDependency:
        """Return Dependency."""
        return self.__dependency

    def set_dependency(self, dependency_id: str, widget_id: str, path: str) -> None:
        """Set dependency for WidgetField."""
        self.__dependency = WidgetSelectDependency(
            dependency_id=dependency_id, widget_id=widget_id, path=path
        )

    @override
    def _generate_templated_string(self, *, selection: int = 0) -> str:
        """Generates template string to be used in dependency.

        Args:
            selection (int): which element from selectable widget is returned.
                Defaults to 0 (first selection)

        Returns:
            str: store id for dependency
        """
        return f"{{{{{self.__widget.widget_id}.{selection}.{self.__field}}}}}"
