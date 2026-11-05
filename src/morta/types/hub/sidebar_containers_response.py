# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .hub_folder import HubFolder
from ..sidebar_resource import SidebarResource

__all__ = ["SidebarContainersResponse", "Data"]


class Data(BaseModel):
    hub_folders: Optional[List[HubFolder]] = FieldInfo(alias="hubFolders", default=None)
    """The containers' direct child folders, as in the hub's `hubFolders`"""

    removed: Optional[List[str]] = None
    """Requested folders that don't exist or aren't in your sidebar"""

    sidebar_resources: Optional[List[SidebarResource]] = FieldInfo(alias="sidebarResources", default=None)
    """
    The documents and tables directly in the containers, as in the hub's
    `sidebarResources`
    """


class SidebarContainersResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[object] = None
