# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ....._models import BaseModel

__all__ = ["SelectOptionRetrieveCheckResponse"]


class SelectOptionRetrieveCheckResponse(BaseModel):
    data: Union[List[str], Dict[str, List[str]], None] = None

    metadata: Optional[Dict[str, object]] = None
