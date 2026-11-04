# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .organisation.site import Site

__all__ = ["OrganisationRetrieveSitesResponse"]

OrganisationRetrieveSitesResponse: TypeAlias = List[Site]
