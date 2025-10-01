"""Specs for Tab and TabSection."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from typing_extensions import override

from engineai.sdk.dashboard.layout.typings import LayoutItem
from engineai.sdk.dashboard.links.widget_field import WidgetField
from engineai.sdk.dashboard.styling.icons import Icons
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.utils import is_valid_url

from .base import SelectableItem
from .base import SelectableSection

if TYPE_CHECKING:
    from engineai.sdk.dashboard.layout.typings import LayoutItem
    from engineai.sdk.dashboard.links.widget_field import WidgetField


class Tab(SelectableItem):
    """Represents an individual tab within a TabSection."""

    INPUT_KEY = "tab"

    def __init__(
        self,
        *,
        label: TemplatedStringItem,
        content: LayoutItem,
        icon: Icons | WidgetField | str | None = None,
        default_selected: bool = False,
    ) -> None:
        """Constructor for Tab.

        Args:
            label: label to be displayed in tab.
            content: item to be added in tab.
            icon: tab icon.
            default_selected: set tab as default selected.
        """
        super().__init__(
            label=label, content=content, default_selected=default_selected
        )
        self.validate_icon(icon)
        self.__icon = icon

    def validate_icon(self, icon: Icons | WidgetField | str | None) -> None:
        """Check if the icon is valid."""
        if icon is not None and isinstance(icon, str):
            is_valid_url(icon)

    @override
    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec."""
        return {
            "label": build_templated_strings(items=self.label),
            "item": {self.item.INPUT_KEY: self.item.build()},
            "icon": (
                build_templated_strings(
                    items=(
                        self.__icon.value
                        if isinstance(self.__icon, Icons)
                        else self.__icon
                    )
                )
                if self.__icon is not None
                else None
            ),
            "preSelected": self.default_selected,
        }


class TabSection(SelectableSection):
    """Organize dashboard content within tabs.

    The TabSection class is a crucial part of a dashboard
    layout, allowing users to organize content within tabs.

    """

    INPUT_KEY = "tabSection"

    def __init__(
        self,
        *tabs: Tab,
    ) -> None:
        """Constructor for TabSection.

        Args:
            tabs: tabs to be added to tab section.

        Examples:
            ??? example "Create a TabSection with different tabs"
                ```py linenums="1"
                import pandas as pd
                from engineai.sdk.dashboard.dashboard import Dashboard
                from engineai.sdk.dashboard.widgets import maps
                from engineai.sdk.dashboard.layout import TabSection
                from engineai.sdk.dashboard.layout import Tab
                from engineai.sdk.dashboard.layout import Grid
                from engineai.sdk.dashboard.layout import Row

                data = pd.DataFrame(
                   data=[{"region": "PT", "value": 10}, {"region": "GB", "value": 100}]
                )

                tab_1 = Tab(label="One Widget", content=maps.Geo(data=data))
                tab_2 = Tab(
                    label="Multiple Widgets",
                    content=[maps.Geo(data=data), maps.Geo(data=data)]
                )
                tab_3 = Tab(
                    label="Multiple Widgets - Different Layout",
                    content=Grid(Row(maps.Geo(data=data), maps.Geo(data=data)))
                )

                Dashboard(content=TabSection(tab_1, tab_2, tab_3))
                ```
        """
        super().__init__()
        self._add_items(*tabs)

    @override
    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "options": [tab.build() for tab in self._items],
        }
