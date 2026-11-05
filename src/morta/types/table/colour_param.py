# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ColourParam"]


class ColourParam(TypedDict, total=False):
    apply_to_entire_row: Required[Annotated[bool, PropertyInfo(alias="applyToEntireRow")]]

    background_colour: Required[Annotated[str, PropertyInfo(alias="backgroundColour")]]

    column_name: Required[Annotated[str, PropertyInfo(alias="columnName")]]

    filter_type: Required[
        Annotated[
            Literal[
                "eq",
                "lt",
                "gt",
                "lte",
                "gte",
                "neq",
                "contains",
                "in",
                "row_id",
                "is",
                "is_not",
                "one_of",
                "not_one_of",
                "is_null",
                "is_not_null",
                "not_contains",
                "starts_with",
                "ends_with",
                "is_valid",
                "is_not_valid",
                "all_values",
            ],
            PropertyInfo(alias="filterType"),
        ]
    ]

    font_bold: Required[Annotated[bool, PropertyInfo(alias="fontBold")]]

    font_colour: Required[Annotated[str, PropertyInfo(alias="fontColour")]]

    font_italic: Required[Annotated[bool, PropertyInfo(alias="fontItalic")]]

    font_underline: Required[Annotated[bool, PropertyInfo(alias="fontUnderline")]]

    column_id: Annotated[str, PropertyInfo(alias="columnId")]

    multiple_values: Annotated[Iterable[Optional[object]], PropertyInfo(alias="multipleValues")]

    value: object
