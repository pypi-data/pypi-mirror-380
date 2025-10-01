"""Spec for Toggle Widget."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

import pandas as pd
from typing_extensions import override

from engineai.sdk.dashboard.templated_string import build_templated_strings
from engineai.sdk.dashboard.widgets.base import SelectableWidget
from engineai.sdk.dashboard.widgets.utils import build_data

from .exceptions import ToggleValidateValueError

if TYPE_CHECKING:
    from engineai.sdk.dashboard.data.manager.manager import DataType
    from engineai.sdk.dashboard.data.manager.manager import StaticDataType
    from engineai.sdk.dashboard.links import WidgetField


class Toggle(SelectableWidget):
    """Enables selection from list, toggling between entries/settings.

    Enables users to select from a list of entries, providing a mechanism to
    toggle between different selections or settings.
    """

    _DEPENDENCY_ID = "__TOGGLE_DATA_DEPENDENCY__"
    _WIDGET_API_TYPE = "toggle"
    _DEFAULT_HEIGHT = 0.5
    _FORCE_HEIGHT = True
    _FLUID_ROW_COMPATIBLE = True

    def __init__(
        self,
        data: DataType | pd.DataFrame,
        *,
        id_column: str = "id",
        label: str | WidgetField = "",
        label_column: str | None = None,
        widget_id: str | None = None,
        default_selection: str | None = None,
    ) -> None:
        """Constructor for Toggle widget.

        Args:
            id_column: Column name in pandas DataFrame used as entries ids.
            data: data source for the widget.
            label: toggle widget label.
            label_column: Column name in pandas DataFrame used for the
                widget labeling.
            widget_id: unique widget id in a dashboard.
            default_selection: pre selected entities on initial state.

        Examples:
            ??? example "Create a minimal toggle widget"
                ```py linenums="1"
                import pandas as pd
                from engineai.sdk.dashboard.dashboard import Dashboard
                from engineai.sdk.dashboard.widgets import toggle
                df = pd.DataFrame(
                    {
                        "id": ["1", "2", "3"],
                    }
                )
                Dashboard(content=toggle.Toggle(df))
                ```

            ??? example "Change the label for each entry"
                ```py linenums="1"
                import pandas as pd
                from engineai.sdk.dashboard.dashboard import Dashboard
                from engineai.sdk.dashboard.widgets import toggle
                df = pd.DataFrame(
                    {
                        "id": ["1", "2", "3"],
                        "label": ["First", "Second", "Third"],
                    }
                )
                Dashboard(content=toggle.Toggle(df, label_column="label")
                ```

        """
        super().__init__(widget_id=widget_id, data=data)
        self.__label = label
        self.__label_column = label_column if label_column is not None else id_column
        self.__id_column = id_column
        self.__default_selection = default_selection

    def _build_label(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Input object for Dashboard API
        """
        return {
            "text": build_templated_strings(items=self.__label),
        }

    def _build_option(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Input object for Dashboard API
        """
        return {
            "labelKey": build_templated_strings(items=self.__label_column),
            "idKey": build_templated_strings(items=self.__id_column),
        }

    @override
    def validate(self, data: StaticDataType, **_: Any) -> None:
        """Validates widget spec.

        Args:
            data (DataFrame): pandas DataFrame or dict where
                the data is present.
        """
        if not isinstance(data, pd.DataFrame):
            return
        if self.__label_column not in data.columns:
            raise ToggleValidateValueError(
                argument="label_column",
                value=self.__label_column,
            )
        if self.__id_column not in data.columns:
            raise ToggleValidateValueError(
                argument="id_column",
                value=self.__id_column,
            )

    @override
    def _build_widget_input(self) -> dict[str, Any]:
        """Builds spec for dashboard API.

        Returns:
            Input object for Dashboard API
        """
        return {
            "label": self._build_label(),
            "data": build_data(path=self.dependency_id, json_data=self._json_data),
            "option": self._build_option(),
            "initialState": {
                "selected": build_templated_strings(items=self.__default_selection),
            },
        }
