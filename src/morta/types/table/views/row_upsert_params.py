# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..preview_table_row_param import PreviewTableRowParam
from ...base_request_context_param import BaseRequestContextParam

__all__ = ["RowUpsertParams"]


class RowUpsertParams(TypedDict, total=False):
    rows: Required[Iterable[PreviewTableRowParam]]

    upsert_column_name: Required[Annotated[str, PropertyInfo(alias="upsertColumnName")]]

    context: BaseRequestContextParam

    next_row_public_id: Annotated[Optional[str], PropertyInfo(alias="nextRowPublicId")]
