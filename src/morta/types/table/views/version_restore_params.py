# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VersionRestoreParams"]


class VersionRestoreParams(TypedDict, total=False):
    view_id: Required[str]

    delete_newer: Annotated[bool, PropertyInfo(alias="deleteNewer")]
