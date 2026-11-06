# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .table_row_action_param import TableRowActionParam
from ..base_request_context_param import BaseRequestContextParam

__all__ = ["RowAddParams"]


class RowAddParams(TypedDict, total=False):
    rows: Required[Iterable[TableRowActionParam]]

    context: BaseRequestContextParam

    next_row_public_id: Annotated[Optional[str], PropertyInfo(alias="nextRowPublicId")]
