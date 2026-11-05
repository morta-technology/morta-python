# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .organisation.site import Site

__all__ = ["UserRetrieveSitesResponse"]


class UserRetrieveSitesResponse(BaseModel):
    data: Optional[List[Site]] = None

    metadata: Optional[object] = None
