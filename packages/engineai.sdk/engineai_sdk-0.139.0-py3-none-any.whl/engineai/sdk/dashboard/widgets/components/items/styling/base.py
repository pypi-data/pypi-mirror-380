"""Spec for Base Item Styling class."""

import warnings
from typing import Any
from typing import cast

import pandas as pd

from engineai.sdk.dashboard.links.abstract import AbstractFactoryLinkItemsHandler
from engineai.sdk.dashboard.links.typing import GenericLink
from engineai.sdk.dashboard.styling.color import Palette
from engineai.sdk.dashboard.styling.color import Single
from engineai.sdk.dashboard.styling.color.spec import build_color_spec
from engineai.sdk.dashboard.styling.color.typing import ColorSpec
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.templated_string import build_templated_strings

from .exceptions import ItemStylingValidationError


class BaseItemStyling(AbstractFactoryLinkItemsHandler):
    """Spec for Number Styling Base class."""

    _INPUT_KEY: str | None = None

    def __init__(
        self,
        *,
        color_spec: ColorSpec | None = None,
        data_column: TemplatedStringItem | None = None,
    ) -> None:
        """Construct for BaseItemStyling class.

        Args:
            color_spec (Optional[ColorSpec]): specs for color.
            data_column (Optional[TemplatedStringItem]): styling value key.
        """
        super().__init__()

        self.__data_column = data_column
        self.__color_spec = color_spec or Palette.AQUA_GREEN

        self.__verify_column_is_not_used()

    @property
    def input_key(self) -> str:
        """Input key for the item."""
        if self._INPUT_KEY is None:
            msg = "Subclass must implement this property."
            raise NotImplementedError(msg)
        return self._INPUT_KEY

    def prepare(
        self, data_column: str | TemplatedStringItem | GenericLink | None
    ) -> None:
        """Prepare data column."""
        if self.__data_column is None:
            self.__data_column = data_column

    def __verify_column_is_not_used(self) -> None:
        if (
            self.__color_spec is not None
            and self.__data_column is not None
            and isinstance(self.__color_spec, Single | Palette | str)
        ):
            warnings.warn(
                f"class variable with value = {self.__data_column} is not used if "
                f"`color_spec` is Single, str or Palette.",
                UserWarning,
            )

    def _build_extra_inputs(self) -> dict[str, Any]:
        return {}

    @property
    def column(
        self,
    ) -> TemplatedStringItem | None:
        """Return Data Column."""
        return self.__data_column

    @column.setter
    def column(
        self,
        column: TemplatedStringItem,
    ) -> None:
        self.__data_column = column

    def __contains_key(self, data: pd.DataFrame | dict[str, Any]) -> bool:
        if isinstance(data, pd.DataFrame):
            return self.__data_column in cast("pd.DataFrame", data).columns
        return self.__data_column in cast("dict[str, Any]", data)

    def validate(
        self,
        *,
        data: pd.DataFrame | dict[str, Any],
        column_name: str,
    ) -> None:
        """Validate if dataframe that will be used for column contains required columns.

        Args:
            data (Union[DataFrame, Dict[str, Any]]): pandas dataframe or Dict which
                will be used for Number.
            column_name (str): column name in data.

        """
        if self.__data_column is None or isinstance(
            self.__color_spec, Single | Palette | str
        ):
            return

        if not self.__contains_key(data=data):
            raise ItemStylingValidationError(
                class_name=self.__class__.__name__,
                column_value=str(self.__data_column),
                column_name=column_name,
            )

    def build_styling(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {self.input_key: self.build()}

    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "colorSpec": (
                build_color_spec(spec=self.__color_spec)
                if self.__color_spec
                else self.__color_spec
            ),
            "valueKey": build_templated_strings(items=self.__data_column),
            **self._build_extra_inputs(),
        }
