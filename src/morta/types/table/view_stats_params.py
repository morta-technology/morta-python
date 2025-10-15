# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ViewStatsParams"]


class ViewStatsParams(TypedDict, total=False):
    filter: str
    """Filters to apply to the statistical data retrieval."""

    process_id: str
    """Optional UUID of a process to filter the data."""

    sum_avg_max_min_count: Annotated[SequenceNotStr[str], PropertyInfo(alias="sum, avg, max, min, count")]
    """Specify columns to perform sum, average, max, min, or count operations."""
