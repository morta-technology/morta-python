# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .api_key import APIKey
from ..._models import BaseModel
from ..user_to_integration import UserToIntegration
from ..organisation.organisation import Organisation

__all__ = ["User"]


class User(BaseModel):
    admin_organisations: Optional[List[Organisation]] = FieldInfo(alias="adminOrganisations", default=None)

    allow_support_access: Optional[bool] = FieldInfo(alias="allowSupportAccess", default=None)

    allow_support_access_expires_at: Optional[datetime] = FieldInfo(alias="allowSupportAccessExpiresAt", default=None)

    api_keys: Optional[List[APIKey]] = FieldInfo(alias="apiKeys", default=None)

    bio: Optional[str] = None

    construction_software: Optional[List[str]] = FieldInfo(alias="constructionSoftware", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    firebase_user_id: Optional[str] = FieldInfo(alias="firebaseUserId", default=None)

    integrations: Optional[List[UserToIntegration]] = None

    is_on_free_trial: Optional[bool] = FieldInfo(alias="isOnFreeTrial", default=None)

    is_service_account: Optional[bool] = FieldInfo(alias="isServiceAccount", default=None)

    is_team_manager: Optional[object] = FieldInfo(alias="isTeamManager", default=None)

    kind: Optional[str] = None

    linkedin: Optional[str] = None

    location: Optional[str] = None

    managed_teams: Optional[object] = FieldInfo(alias="managedTeams", default=None)

    name: Optional[str] = None

    opt_out_ai_email: Optional[bool] = FieldInfo(alias="optOutAiEmail", default=None)

    opt_out_deprecation_email: Optional[bool] = FieldInfo(alias="optOutDeprecationEmail", default=None)

    opt_out_duplication_email: Optional[bool] = FieldInfo(alias="optOutDuplicationEmail", default=None)

    opt_out_hub_email: Optional[bool] = FieldInfo(alias="optOutHubEmail", default=None)

    opt_out_mention_email: Optional[bool] = FieldInfo(alias="optOutMentionEmail", default=None)

    opt_out_sync_email: Optional[bool] = FieldInfo(alias="optOutSyncEmail", default=None)

    opt_out_welcome_email: Optional[bool] = FieldInfo(alias="optOutWelcomeEmail", default=None)

    organisation: Optional[str] = None

    phone: Optional[str] = None

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    projects_worked_on: Optional[List[str]] = FieldInfo(alias="projectsWorkedOn", default=None)

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    specialisms: Optional[List[str]] = None

    subscription_level: Optional[int] = FieldInfo(alias="subscriptionLevel", default=None)

    tags: Optional[object] = None

    team: Optional[object] = None

    twitter: Optional[str] = None

    university: Optional[str] = None

    university_degree: Optional[str] = FieldInfo(alias="universityDegree", default=None)

    user_level_subscription: Optional[int] = FieldInfo(alias="userLevelSubscription", default=None)

    website: Optional[str] = None
