# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderMoveParams", "Item"]


class FolderMoveParams(TypedDict, total=False):
    items: Required[Iterable[Item]]

    index: Optional[int]

    parent_folder_id: Annotated[Optional[str], PropertyInfo(alias="parentFolderId")]


class Item(TypedDict, total=False):
    id: Required[str]

    kind: Required[Literal["folder", "document", "table"]]
