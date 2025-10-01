"""Spec for the layout Header component."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from typing_extensions import override

from engineai.sdk.dashboard.base import AbstractFactory
from engineai.sdk.dashboard.base import DependencyInterface
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings

if TYPE_CHECKING:
    from .chip import BaseChip


class BaseHeader(AbstractFactory):
    """Spec for the layout Header component.

    This component is used in Card and CollapsibleSection components.
    """

    def __init__(
        self,
        *chips: BaseChip,
        title: TemplatedStringItem | None = None,
    ) -> None:
        """Construct Header in layout.

        Args:
            chips: chips to be added to the header.
            title: Component title.
        """
        super().__init__()
        self.__title = title
        self.__chips = chips

    def has_title(self) -> bool:
        """Method to validate if header has title."""
        return self.__title is not None

    @property
    def dependencies(
        self,
    ) -> list[DependencyInterface]:
        """Method to generate the dependencies list from the elements of the class."""
        dependencies_list = []
        for chip in self.__chips:
            dependencies_list.extend(chip.dependencies)

        if self.__title is not None and not isinstance(self.__title, str):
            if isinstance(self.__title, list):
                dependencies_list.extend([title.dependency for title in self.__title])
            else:
                dependencies_list.extend([self.__title.dependency])
        return list(set(dependencies_list))

    @override
    def build(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Input object for Dashboard API
        """
        return {
            "title": build_templated_strings(items=self.__title),
            "context": [chip.build() for chip in self.__chips],
        }
