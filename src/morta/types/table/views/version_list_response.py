# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from .custom_view_version import CustomViewVersion

__all__ = ["VersionListResponse"]


class VersionListResponse(BaseModel):
    data: Optional[List[CustomViewVersion]] = None

    metadata: Optional[Dict[str, object]] = None
