# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .project_list import ProjectList
from .heading_style import HeadingStyle
from .site_schema_with_org import SiteSchemaWithOrg

__all__ = [
    "OrganisationRetrieveHubsResponse",
    "OrganisationRetrieveHubsResponseItem",
    "OrganisationRetrieveHubsResponseItemSite",
]

OrganisationRetrieveHubsResponseItemSite: TypeAlias = Union[SiteSchemaWithOrg, Optional[object]]


class OrganisationRetrieveHubsResponseItem(BaseModel):
    allow_document_export: Optional[bool] = FieldInfo(alias="allowDocumentExport", default=None)

    allow_table_export: Optional[bool] = FieldInfo(alias="allowTableExport", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    default_banner: Optional[str] = FieldInfo(alias="defaultBanner", default=None)

    default_date_format: Optional[str] = FieldInfo(alias="defaultDateFormat", default=None)

    default_datetime_format: Optional[str] = FieldInfo(alias="defaultDatetimeFormat", default=None)

    default_header_background_color: Optional[str] = FieldInfo(alias="defaultHeaderBackgroundColor", default=None)

    default_header_text_color: Optional[str] = FieldInfo(alias="defaultHeaderTextColor", default=None)

    default_process_id: Optional[str] = FieldInfo(alias="defaultProcessId", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    domains_access: Optional[List[str]] = FieldInfo(alias="domainsAccess", default=None)

    font_colour: Optional[str] = FieldInfo(alias="fontColour", default=None)

    heading_styles: Optional[List[HeadingStyle]] = FieldInfo(alias="headingStyles", default=None)

    hide_process_created: Optional[bool] = FieldInfo(alias="hideProcessCreated", default=None)

    image: Optional[str] = None

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)

    logo: Optional[str] = None

    mfa_required: Optional[bool] = FieldInfo(alias="mfaRequired", default=None)

    name: Optional[str] = None

    primary_colour: Optional[str] = FieldInfo(alias="primaryColour", default=None)

    process_title_alignment: Optional[str] = FieldInfo(alias="processTitleAlignment", default=None)

    process_title_bold: Optional[bool] = FieldInfo(alias="processTitleBold", default=None)

    process_title_colour: Optional[str] = FieldInfo(alias="processTitleColour", default=None)

    process_title_font_size: Optional[float] = FieldInfo(alias="processTitleFontSize", default=None)

    process_title_italic: Optional[bool] = FieldInfo(alias="processTitleItalic", default=None)

    process_title_underline: Optional[bool] = FieldInfo(alias="processTitleUnderline", default=None)

    project_list: Optional[List[ProjectList]] = FieldInfo(alias="projectList", default=None)

    public: Optional[bool] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    site: Optional[OrganisationRetrieveHubsResponseItemSite] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    word_table_style: Optional[str] = FieldInfo(alias="wordTableStyle", default=None)

    word_table_styles: Optional[List[str]] = FieldInfo(alias="wordTableStyles", default=None)

    word_template: Optional[str] = FieldInfo(alias="wordTemplate", default=None)


OrganisationRetrieveHubsResponse: TypeAlias = List[OrganisationRetrieveHubsResponseItem]
