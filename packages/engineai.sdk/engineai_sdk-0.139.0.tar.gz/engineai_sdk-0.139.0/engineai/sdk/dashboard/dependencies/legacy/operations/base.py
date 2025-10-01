"""Specs for widgets operations."""

from abc import abstractmethod
from typing import Any

from engineai.sdk.dashboard.base import AbstractFactory
from engineai.sdk.dashboard.interface import OperationInterface


class BaseOperation(AbstractFactory, OperationInterface):
    """Base class for operations."""

    _ITEM_ID: str | None = None

    @property
    def item_id(self) -> str:
        """Get Item ID."""
        if self._ITEM_ID is None:
            msg = "BaseOperation's item ID not implemented."
            raise NotImplementedError(msg)
        return self._ITEM_ID

    @abstractmethod
    def build_filter(self) -> dict[str, Any]:
        """Method to build filter spec."""

    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "operation": {self.item_id: self.build_filter()},
        }
