# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TableColumnAlterParam"]


class TableColumnAlterParam(TypedDict, total=False):
    date_conversion_format: Annotated[
        Literal[
            "DD/MM/YYYY",
            "MM/DD/YYYY",
            "YYYY-MM-DD",
            "DD-Mon-YY",
            "DD/MM/YYYY HH:mm:ss",
            "DD/MM/YYYY HH:mm",
            "MM/DD/YYYY HH:mm:ss",
            "MM/DD/YYYY HH:mm",
            "YYYY-MM-DDTHH:mm:ss",
            "YYYY-MM-DDTHH:mm",
            "YYYY-MM-DD HH:mm:ss",
            "YYYY-MM-DD HH:mm",
            "DD-Mon-YY HH:mm:ss",
            "DD-Mon-YY HH:mm",
        ],
        PropertyInfo(alias="dateConversionFormat"),
    ]

    run_script_on_all_cells: Annotated[bool, PropertyInfo(alias="runScriptOnAllCells")]
