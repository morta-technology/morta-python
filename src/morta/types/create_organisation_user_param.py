# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .base_request_context_param import BaseRequestContextParam

__all__ = ["CreateOrganisationUserParam"]


class CreateOrganisationUserParam(TypedDict, total=False):
    email: Required[str]

    role: Required[Literal["admin"]]

    context: BaseRequestContextParam
