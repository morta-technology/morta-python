# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .create_notification_schema_header_param import CreateNotificationSchemaHeaderParam

__all__ = ["NotificationCreateParams", "Trigger"]


class NotificationCreateParams(TypedDict, total=False):
    description: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    triggers: Required[Iterable[Trigger]]

    webhook_url: Required[Annotated[str, PropertyInfo(alias="webhookUrl")]]

    custom_headers: Annotated[Iterable[CreateNotificationSchemaHeaderParam], PropertyInfo(alias="customHeaders")]

    processes: SequenceNotStr[str]

    tables: SequenceNotStr[str]


class Trigger(TypedDict, total=False):
    resource: Required[str]

    verb: Required[str]
