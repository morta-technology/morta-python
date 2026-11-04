# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ExportCreateParams"]


class ExportCreateParams(TypedDict, total=False):
    colour: Iterable[object]

    display_comment_rows: Annotated[int, PropertyInfo(alias="displayCommentRows")]

    filter: Iterable[object]

    format: Literal["csv", "xlsx"]

    hidden: SequenceNotStr[str]

    process_id: Annotated[str, PropertyInfo(alias="processId")]

    sort: SequenceNotStr[str]

    timezone: str
