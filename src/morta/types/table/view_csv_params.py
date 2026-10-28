# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ViewCsvParams"]


class ViewCsvParams(TypedDict, total=False):
    display_comment_rows: Annotated[int, PropertyInfo(alias="displayCommentRows")]

    filter: Iterable[object]

    process_id: Annotated[str, PropertyInfo(alias="processId")]

    sort: SequenceNotStr[str]
