# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel
from .embed_submission import EmbedSubmission

__all__ = ["SubmissionCreateResponse"]


class SubmissionCreateResponse(BaseModel):
    data: Optional[EmbedSubmission] = None

    metadata: Optional[Dict[str, object]] = None
