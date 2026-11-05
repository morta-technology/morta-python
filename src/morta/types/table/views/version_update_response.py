# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel
from .custom_view_version import CustomViewVersion

__all__ = ["VersionUpdateResponse"]


class VersionUpdateResponse(BaseModel):
    data: Optional[CustomViewVersion] = None

    metadata: Optional[Dict[str, object]] = None
