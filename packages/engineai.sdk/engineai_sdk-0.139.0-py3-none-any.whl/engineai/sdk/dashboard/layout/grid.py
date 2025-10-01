"""Spec for a grid in a dashboard vertical grid layout."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from typing_extensions import Unpack
from typing_extensions import override

from engineai.sdk.dashboard.abstract.layout import AbstractLayoutItem
from engineai.sdk.dashboard.abstract.typing import PrepareParams
from engineai.sdk.dashboard.interface import GridInterface

from .exceptions import ElementHeightNotDefinedError
from .fluid_row.fluid_row import FluidRow
from .row import Row

if TYPE_CHECKING:
    from engineai.sdk.dashboard.abstract.layout import AbstractLayoutItem
    from engineai.sdk.dashboard.abstract.typing import PrepareParams
    from engineai.sdk.dashboard.layout.typings import LayoutItem


class Grid(GridInterface):
    """Organize dashboard content with vertical grid structure.

    The Grid class is component in a dashboard layout,
    allowing users to organize content using a vertical grid structure.
    It provides a way to arrange widgets, rows, and selectable sections.
    """

    INPUT_KEY = "grid"

    def __init__(self, *items: Row | FluidRow | LayoutItem) -> None:
        """Constructor for Grid.

        Args:
            items: items to add to grid. Can be widgets, rows or
                selectable sections (e.g tabs).

        Examples:
            ??? example "Create Grid with widget"
                ```py linenums="1"
                import pandas as pd

                from engineai.sdk.dashboard import dashboard
                from engineai.sdk.dashboard import layout
                from engineai.sdk.dashboard.widgets import select

                data = pd.DataFrame({"id": [1, 2, 3]})

                dashboard.Dashboard(content=layout.Grid(select.Select(data)))
                ```

            ??? example "Create Grid with multiple widgets"
                ```py linenums="1"
                import pandas as pd

                from engineai.sdk.dashboard import dashboard
                from engineai.sdk.dashboard import layout
                from engineai.sdk.dashboard.widgets import select
                from engineai.sdk.dashboard.widgets import toggle

                data = pd.DataFrame({"id": [1, 2, 3]})

                dashboard.Dashboard(
                    content=layout.Grid(
                        select.Select(data),
                        toggle.Toggle(data)
                    )
                )
                ```

            ??? example "Create Grid with Tab Section and Card"
                ```py linenums="1"
                import pandas as pd

                from engineai.sdk.dashboard import dashboard
                from engineai.sdk.dashboard import layout
                from engineai.sdk.dashboard.widgets import select
                from engineai.sdk.dashboard.widgets import toggle

                data = pd.DataFrame({"id": [1, 2, 3]})

                dashboard.Dashboard(
                    content=layout.Grid(
                        layout.TabSection(
                            layout.Tab(label="tab",
                                    content=select.Select(data)
                            )
                        ),
                        layout.Card(
                            header=layout.Header(title="Card"),
                            content=toggle.Toggle(data)
                        )
                    )
                )
                ```
        """
        super().__init__()
        self._rows: list[Row | FluidRow] = [
            item if isinstance(item, (Row, FluidRow)) else Row(item) for item in items
        ]

        self.__height: int | float | None = None

    def prepare(self, **kwargs: Unpack[PrepareParams]) -> None:
        """Prepare grid.

        Args:
            **kwargs (Unpack[PrepareParams]): keyword arguments
        """
        for row in self._rows:
            row.prepare(**kwargs)

    def prepare_heights(self, row_height: int | float | None = None) -> None:
        """Prepare heights."""
        if self.__any_row_has_forced_height():
            self.__prepare_rows_with_forced_height(row_height)
        else:
            self.__prepare_rows_evenly(row_height)
        self.__set_height(row_height)

    def __any_row_has_forced_height(self) -> bool:
        return any(row.force_height for row in self._rows)

    def __prepare_rows_with_forced_height(
        self, row_height: int | float | None = None
    ) -> None:
        self.__prepare_forced_height_rows()
        forced_heights = [row.height for row in self._rows if row.force_height]

        if row_height is not None and len(forced_heights) == len(self._rows):
            for row in self._rows:
                if isinstance(row, Row):
                    row.prepare_heights(column_height=row_height / len(self._rows))
                else:
                    row.prepare_heights()
        else:
            column_height = (
                (row_height - sum(forced_heights))
                / (len(self._rows) - len(forced_heights))
                if row_height
                else None
            )
            for row in [row for row in self._rows if not row.force_height]:
                if isinstance(row, Row):
                    row.prepare_heights(column_height=column_height)
                else:
                    row.prepare_heights()

    def __prepare_forced_height_rows(self) -> None:
        for row in [row for row in self._rows if row.force_height]:
            row.prepare_heights()

    def __prepare_rows_evenly(self, row_height: int | float | None = None) -> None:
        column_height = row_height / len(self._rows) if row_height else None
        for row in self._rows:
            if isinstance(row, Row):
                row.prepare_heights(column_height=column_height)
            else:
                row.prepare_heights()

    def __set_height(self, row_height: int | float | None = None) -> None:
        self.__height = row_height or sum(row.height for row in self._rows)

    @property
    def height(self) -> int | float:
        """Returns grid height."""
        if self.__height is None:
            raise ElementHeightNotDefinedError

        return self.__height

    @property
    def has_custom_heights(self) -> bool:
        """Returns whether grid has custom heights."""
        return any(row.has_custom_heights for row in self._rows if isinstance(row, Row))

    @override
    def items(self) -> list[AbstractLayoutItem]:
        """Returns list of grid items that need to be inserted individually."""
        items: list[AbstractLayoutItem] = []
        for row in self._rows:
            items += row.items()
        return items

    @override
    def build(self) -> dict[str, Any]:
        """Method implemented by all factories to generate Input spec.

        Returns:
            Input object for Dashboard API
        """
        return {
            "rows": [
                {
                    "fluid": row.build() if isinstance(row, FluidRow) else None,
                    "responsive": row.build() if isinstance(row, Row) else None,
                }
                for row in self._rows
            ],
        }
