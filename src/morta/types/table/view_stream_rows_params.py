# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ViewStreamRowsParams"]


class ViewStreamRowsParams(TypedDict, total=False):
    filter: str
    """Filters to apply to the streaming data."""

    format: Literal["rows", "columnar"]
    """Wire format of the stream.

    `rows` (default) sends each row as an array; `columnar` sends each batch as
    column blobs (16-byte binary ids, little-endian float64 sort orders, typed
    dictionary indices).
    """

    page: int
    """Page number for pagination"""

    process_id: str
    """Optional UUID of a process to filter the data."""

    size: int
    """Number of items per page for pagination"""

    sort: str
    """Sorting parameters for the streaming data."""
