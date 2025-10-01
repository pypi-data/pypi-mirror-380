"""Spec for Text Styling Dot."""

from engineai.sdk.dashboard.styling.color.typing import ColorSpec
from engineai.sdk.dashboard.templated_string import TemplatedStringItem
from engineai.sdk.dashboard.widgets.components.items.styling.base import BaseItemStyling


class TextStylingDot(BaseItemStyling):
    """Spec for Text Dot Styling Class."""

    _INPUT_KEY: str = "dot"

    def __init__(
        self,
        *,
        color_spec: ColorSpec | None = None,
        data_column: TemplatedStringItem | None = None,
    ) -> None:
        """Construct spec for Text Dot Styling.

        Args:
            color_spec (Optional[ColorSpec): specs for color.
            data_column (Optional[TemplatedStringItem]): styling value key.
                Defaults to None.
        """
        super().__init__(
            color_spec=color_spec,
            data_column=data_column,
        )
