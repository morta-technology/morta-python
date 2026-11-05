# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserUpdateAccountParams"]


class UserUpdateAccountParams(TypedDict, total=False):
    allow_support_access_expires_at: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="allowSupportAccessExpiresAt", format="iso8601")
    ]

    old_password: Annotated[str, PropertyInfo(alias="oldPassword")]

    opt_out_ai_email: Annotated[Optional[bool], PropertyInfo(alias="optOutAiEmail")]

    opt_out_assignment_email: Annotated[Optional[bool], PropertyInfo(alias="optOutAssignmentEmail")]

    opt_out_community_email: Annotated[bool, PropertyInfo(alias="optOutCommunityEmail")]

    opt_out_deprecation_email: Annotated[Optional[bool], PropertyInfo(alias="optOutDeprecationEmail")]

    opt_out_duplication_email: Annotated[Optional[bool], PropertyInfo(alias="optOutDuplicationEmail")]

    opt_out_hub_email: Annotated[Optional[bool], PropertyInfo(alias="optOutHubEmail")]

    opt_out_marketing_email: Annotated[bool, PropertyInfo(alias="optOutMarketingEmail")]

    opt_out_mention_email: Annotated[Optional[bool], PropertyInfo(alias="optOutMentionEmail")]

    opt_out_sync_email: Annotated[Optional[bool], PropertyInfo(alias="optOutSyncEmail")]

    opt_out_welcome_email: Annotated[Optional[bool], PropertyInfo(alias="optOutWelcomeEmail")]

    password: str

    password_confirm: Annotated[str, PropertyInfo(alias="passwordConfirm")]

    theme: Literal["light", "dark", "system"]

    two_factor_code: Annotated[Optional[str], PropertyInfo(alias="twoFactorCode")]
