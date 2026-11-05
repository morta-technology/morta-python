# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...base_request_context_param import BaseRequestContextParam

__all__ = ["RowDeleteParams"]


class RowDeleteParams(TypedDict, total=False):
    row_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="rowIds")]]

    context: BaseRequestContextParam
