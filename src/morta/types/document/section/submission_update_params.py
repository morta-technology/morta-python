# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...base_request_context_param import BaseRequestContextParam

__all__ = ["SubmissionUpdateParams"]


class SubmissionUpdateParams(TypedDict, total=False):
    document_id: Required[str]

    document_section_id: Required[str]

    context: BaseRequestContextParam

    enable_submission: Annotated[Optional[bool], PropertyInfo(alias="enableSubmission")]

    reset_after_submission: Annotated[Optional[bool], PropertyInfo(alias="resetAfterSubmission")]
