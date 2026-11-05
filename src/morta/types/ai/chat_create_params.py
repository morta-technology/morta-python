# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    message: Required[str]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    document_context_id: Annotated[str, PropertyInfo(alias="documentContextId")]

    resume: bool
    """
    Carry on after the user accepted every change proposed in the conversation's
    last reply. Requires conversationId, and is only allowed when that reply asked
    to continue and every one of its changes was accepted and applied.
    """

    table_view_context_id: Annotated[str, PropertyInfo(alias="tableViewContextId")]
