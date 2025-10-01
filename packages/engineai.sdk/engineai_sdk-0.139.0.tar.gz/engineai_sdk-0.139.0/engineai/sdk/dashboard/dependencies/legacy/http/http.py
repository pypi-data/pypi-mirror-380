"""Spec for defining data from a http request."""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from engineai.sdk.dashboard.dependencies.legacy.operations.base import BaseOperation
from engineai.sdk.dashboard.interface import LegacyHttpInterface
from engineai.sdk.dashboard.links.abstract import AbstractFactoryLinkItemsHandler
from engineai.sdk.dashboard.templated_string import TemplatedStringItem

from .dependency import LegacyHttpDependency
from .header import LegacyHttpHeader


class LegacyHttp(AbstractFactoryLinkItemsHandler, LegacyHttpInterface):
    """Spec for defining data from a http request."""

    def __init__(
        self,
        *,
        path: TemplatedStringItem,
        host: str,
        headers: Optional[Dict[str, str]] = None,
        operations: Optional[List[BaseOperation]] = None,
        as_dict: bool = False,
    ) -> None:
        """Constructor for Http class.

        Args:
            path: path to the data.
            host: host of the data.
            headers: headers for the request.
            operations: operations to be performed on the data.
            as_dict: flag to return data as dictionary.
        """
        super().__init__()
        self.__path = path
        self.__dependency = LegacyHttpDependency(
            path=self.__path,
            host=host,
            headers=(
                [
                    LegacyHttpHeader(key=key, value=value)
                    for key, value in headers.items()
                ]
                if headers is not None
                else None
            ),
            operations=operations,
        )
        self.as_dict = as_dict

    @property
    def base_path(self) -> str:
        """Return the base path."""
        return "http"

    @property
    def separator(self) -> str:
        """Return the separator."""
        return "/"

    @property
    def dependency(self) -> LegacyHttpDependency:
        """Property to get the dependency object."""
        return self.__dependency

    def build(self) -> Dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return self.__dependency.build()
