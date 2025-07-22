# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["ResponseDeleteResponse"]


class ResponseDeleteResponse(BaseModel):
    data: Optional["MortaDocumentSection"] = None

    metadata: Optional[Dict[str, object]] = None


from ...morta_document_section import MortaDocumentSection
