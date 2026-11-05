# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel
from .custom_view_version_with_html import CustomViewVersionWithHTML

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    data: Optional[CustomViewVersionWithHTML] = None

    metadata: Optional[Dict[str, object]] = None
