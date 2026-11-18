# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .simple_hub import SimpleHub
from .hub.hub_folder import HubFolder
from .sidebar_resource import SidebarResource

__all__ = ["HubRetrieveResponse", "Data"]


class Data(BaseModel):
    hub_folders: Optional[List[HubFolder]] = FieldInfo(alias="hubFolders", default=None)
    """The hub's folder tree as a flat list, in sidebar order.

    Hub Owners see every folder; everyone else sees only folders that contain (at
    any depth) a document or table they can access.
    """

    project_details: Optional[SimpleHub] = FieldInfo(alias="projectDetails", default=None)

    role: Optional[str] = None
    """User's role in the hub"""

    sidebar_resources: Optional[List[SidebarResource]] = FieldInfo(alias="sidebarResources", default=None)
    """The live documents and tables this user can access, with the folder each is in"""


class HubRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[object] = None
