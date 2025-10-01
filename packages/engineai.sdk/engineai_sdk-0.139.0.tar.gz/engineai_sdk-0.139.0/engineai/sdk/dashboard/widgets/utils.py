"""Utils related to Widgets classes."""

from __future__ import annotations

from typing import Any
from typing import get_args

import orjson
import pandas as pd

from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItem
from engineai.sdk.dashboard.widgets.components.charts.typing import TooltipItems

COUNTRY_CODES = {
    "FO",
    "US",
    "JP",
    "IN",
    "FR",
    "CN",
    "PT",
    "BR",
    "PH",
    "MX",
    "ES",
    "GB",
    "GR",
    "DK",
    "GL",
    "PR",
    "CA",
    "NL",
    "JM",
    "OM",
    "TR",
    "BD",
    "NO",
    "BH",
    "FI",
    "ID",
    "SE",
    "MY",
    "PA",
    "CL",
    "TH",
    "EE",
    "TW",
    "IT",
    "SG",
    "CY",
    "LK",
    "RU",
    "VA",
    "SM",
    "KZ",
    "AZ",
    "TJ",
    "LS",
    "UZ",
    "MA",
    "CO",
    "TL",
    "TZ",
    "AR",
    "SA",
    "PK",
    "YE",
    "AE",
    "KE",
    "PE",
    "DO",
    "HT",
    "PG",
    "AO",
    "KH",
    "VN",
    "MZ",
    "CR",
    "BJ",
    "NG",
    "IR",
    "SV",
    "SL",
    "GW",
    "HR",
    "BZ",
    "ZA",
    "CF",
    "SD",
    "CD",
    "KW",
    "DE",
    "BE",
    "IE",
    "KP",
    "KR",
    "GY",
    "HN",
    "MM",
    "GA",
    "GQ",
    "NI",
    "LV",
    "UG",
    "MW",
    "AM",
    "SX",
    "TM",
    "ZM",
    "NC",
    "MR",
    "DZ",
    "LT",
    "ET",
    "ER",
    "GH",
    "SI",
    "GT",
    "BA",
    "JO",
    "SY",
    "MC",
    "AL",
    "UY",
    "MN",
    "RW",
    "SO",
    "BO",
    "CM",
    "CG",
    "EH",
    "RS",
    "ME",
    "TG",
    "LA",
    "AF",
    "UA",
    "SK",
    "BG",
    "QA",
    "LI",
    "AT",
    "SZ",
    "HU",
    "RO",
    "NE",
    "LU",
    "AD",
    "CI",
    "LR",
    "BN",
    "IQ",
    "GE",
    "GM",
    "CH",
    "TD",
    "KV",
    "LB",
    "DJ",
    "BI",
    "SR",
    "IL",
    "ML",
    "SN",
    "GN",
    "ZW",
    "PL",
    "MK",
    "PY",
    "BY",
    "CZ",
    "BF",
    "NA",
    "LY",
    "TN",
    "BT",
    "MD",
    "SS",
    "BW",
    "BS",
    "NZ",
    "CU",
    "EC",
    "AU",
    "VE",
    "MG",
    "IS",
    "EG",
    "KG",
    "NP",
}


def build_data(
    *, path: str, json_data: Any = None, as_dict: bool = False
) -> dict[str, Any]:
    """Build Data Input."""
    if json_data is not None:
        result_json = (
            orjson.loads(json_data.to_json(orient="records"))
            if isinstance(json_data, pd.DataFrame)
            else json_data
        )
        return {
            "json": (
                result_json
                if not as_dict
                else result_json[0]
                if as_dict and len(result_json) > 0
                else {}
            ),
        }
    return {
        "dependency": {"path": f"{path}.0" if as_dict else path},
    }


def get_tooltips(tooltips: TooltipItems | None) -> Any:
    """Get tooltips."""
    return (
        tooltips
        if isinstance(tooltips, list)
        else [tooltips]
        if isinstance(tooltips, get_args(TooltipItem))
        else []
    )
