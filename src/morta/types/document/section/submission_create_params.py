# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...base_request_context_param import BaseRequestContextParam

__all__ = ["SubmissionCreateParams"]


class SubmissionCreateParams(TypedDict, total=False):
    document_id: Required[str]

    context: BaseRequestContextParam

    enable_submission: Annotated[bool, PropertyInfo(alias="enableSubmission")]

    reset_after_submission: Annotated[bool, PropertyInfo(alias="resetAfterSubmission")]
