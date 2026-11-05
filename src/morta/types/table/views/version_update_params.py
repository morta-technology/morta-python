# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["VersionUpdateParams"]


class VersionUpdateParams(TypedDict, total=False):
    view_id: Required[str]

    summary: Optional[str]

    thumbnail: str

    title: Optional[str]
