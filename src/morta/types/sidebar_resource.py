# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SidebarResource"]


class SidebarResource(BaseModel):
    can_move: Optional[bool] = FieldInfo(alias="canMove", default=None)
    """
    Whether this user can move the resource between folders: always for hub Owners,
    otherwise only for documents and tables they own
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the document or table was created"""

    default_view_id: Optional[str] = FieldInfo(alias="defaultViewId", default=None)
    """A table's default view; null for documents"""

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)
    """The folder the resource is in; null at the hub's top level"""

    kind: Optional[Literal["document", "table"]] = None
    """document for a document, table for a table"""

    name: Optional[str] = None

    position: Optional[int] = None
    """Order within its folder"""

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)
