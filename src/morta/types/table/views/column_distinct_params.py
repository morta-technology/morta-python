# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ColumnDistinctParams"]


class ColumnDistinctParams(TypedDict, total=False):
    view_id: Required[str]

    filter: str
    """Filters to apply to the data retrieval."""

    group_columns: SequenceNotStr[str]
    """Optional columns to group the distinct values."""
