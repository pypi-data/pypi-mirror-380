"""Specs for dashboard components that supports WidgetField or RouteLink."""

from __future__ import annotations

from typing import Generic
from typing import TypeVar
from typing import cast
from typing import get_args

from .abstract.selectable_widgets import AbstractSelectWidget
from .interface import RouteInterface as Route
from .interface import WidgetInterface as Widget
from .links import RouteLink
from .links import WidgetField

ComponentType = TypeVar("ComponentType", AbstractSelectWidget, Route)
LinkType = TypeVar("LinkType", WidgetField, RouteLink)
SpecType = TypeVar("SpecType", Widget, Route)


class Selected(Generic[ComponentType, LinkType, SpecType]):
    """Specs for dashboard components that supports WidgetField or RouteLink."""

    def __init__(self, component: ComponentType) -> None:
        """Constructor for selected class.

        Args:
            component (_ComponentType): selected component. It can be either
                an AbstractSelectWidget or a Route.
        """
        self.__component: ComponentType = component
        self.__set_classes()

    @classmethod
    def __set_classes(cls) -> None:
        """Set dependencies class."""
        cls._ComponentType, cls._LinkType, cls._SpecType = get_args(  # type: ignore[attr-defined]
            cls.__orig_bases__[0]  # type: ignore[attr-defined]
        )

    def get(self, field: str) -> LinkType:
        """Get item method."""
        return cast(
            "LinkType",
            self._LinkType(field=field, **{self.__get_key(): self.__component}),  # type: ignore[operator]
        )

    def __getattr__(self, attr: str) -> LinkType:
        return cast(
            "LinkType",
            self._LinkType(field=attr, **{self.__get_key(): self.__component}),  # type: ignore[operator]
        )

    def __get_key(self) -> str:
        return "widget" if self._LinkType is WidgetField else "route"

    # since __getattr__ is overridden, need to override
    # __getstate__ and __setstate__ in order to pickling/unpickling object with success.
    # Refer to: https://stackoverflow.com/a/50888571/1860606
    def __getstate__(self) -> dict[str, SpecType]:
        return self.__dict__

    def __setstate__(self, state: dict[str, SpecType]) -> None:
        self.__dict__.update(state)
