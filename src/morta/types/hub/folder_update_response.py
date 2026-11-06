# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .hub_folder import HubFolder

__all__ = ["FolderUpdateResponse"]


class FolderUpdateResponse(BaseModel):
    data: Optional[HubFolder] = None

    metadata: Optional[object] = None
