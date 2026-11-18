# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AutoFillParam"]


class AutoFillParam(TypedDict, total=False):
    type: Required[
        Literal[
            "created_time",
            "created_by",
            "row_id",
            "autonumber",
            "last_modified_time",
            "last_modified_by",
            "previous_value",
        ]
    ]

    columns: SequenceNotStr[str]

    fill_gaps: Annotated[bool, PropertyInfo(alias="fillGaps")]
