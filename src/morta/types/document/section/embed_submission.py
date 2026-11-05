# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...summary_user import SummaryUser

__all__ = ["EmbedSubmission", "SubmittedBy"]

SubmittedBy: TypeAlias = Union[SummaryUser, Optional[object]]


class EmbedSubmission(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    enable_submission: Optional[bool] = FieldInfo(alias="enableSubmission", default=None)

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    reset_after_submission: Optional[bool] = FieldInfo(alias="resetAfterSubmission", default=None)

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)

    submitted_by: Optional[SubmittedBy] = FieldInfo(alias="submittedBy", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
