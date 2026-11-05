# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RowLockParam"]


class RowLockParam(TypedDict, total=False):
    apply_to_entire_row: Required[Annotated[bool, PropertyInfo(alias="applyToEntireRow")]]

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

    column_id: Annotated[str, PropertyInfo(alias="columnId")]

    multiple_values: Annotated[Iterable[Optional[object]], PropertyInfo(alias="multipleValues")]

    public_id: Annotated[str, PropertyInfo(alias="publicId")]

    value: object
