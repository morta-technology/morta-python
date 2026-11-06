# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExportListParams"]


class ExportListParams(TypedDict, total=False):
    colour: str
    """
    URL encoded JSON colour rule to use instead of the view's saved rules (xlsx
    only). Repeat for more rules.
    """

    filter: str
    """URL encoded JSON filter, as for the CSV download. Repeat for more filters."""

    format: Literal["csv", "xlsx"]
    """The file format."""

    hidden: str
    """The UUID of a column to leave out. Repeat for more columns."""

    process_id: str
    """
    The UUID of the document the view is exported from, for document variable
    filters.
    """

    sort: str
    """Sort as `ColumnName:asc` or `ColumnName:desc`. Repeat for more sorts."""

    timezone: str
    """
    IANA time zone, such as Europe/London, that Excel shows dates and times in (xlsx
    only). Defaults to UTC.
    """
