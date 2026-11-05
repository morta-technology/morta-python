# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ViewGetRowsParams"]


class ViewGetRowsParams(TypedDict, total=False):
    row_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="rowIds")]]

    alphabetical_column_sort: Annotated[bool, PropertyInfo(alias="alphabeticalColumnSort")]

    columns: Optional[SequenceNotStr[str]]

    distinct_columns: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="distinctColumns")]

    expand: str

    filter: Optional[Iterable[object]]

    ignore_cached_options: Annotated[bool, PropertyInfo(alias="ignoreCachedOptions")]

    last_created_at: Annotated[Union[str, datetime, None], PropertyInfo(alias="lastCreatedAt", format="iso8601")]

    last_updated_at: Annotated[Union[str, datetime, None], PropertyInfo(alias="lastUpdatedAt", format="iso8601")]

    next_page_token: Annotated[Optional[str], PropertyInfo(alias="nextPageToken")]

    page: int

    process_id: Annotated[Optional[str], PropertyInfo(alias="processId")]

    sort: Optional[Iterable[object]]
