# User

Types:

```python
from morta.types import (
    Event,
    SummaryUser,
    User,
    UserToIntegration,
    UserCreateResponse,
    UserRetrieveResponse,
    UserListAchievementsResponse,
    UserListContributionsResponse,
    UserListOwnerHubsResponse,
    UserListPinnedHubsResponse,
    UserListPublicContributionsResponse,
    UserListPublicHubsResponse,
    UserListTemplatesResponse,
    UserRetrieveByPublicIDResponse,
    UserRetrieveMeResponse,
    UserRetrieveSitesResponse,
    UserSearchResponse,
    UserUpdateAccountResponse,
    UserUpdateProfileResponse,
)
```

Methods:

- <code title="post /v1/user">client.user.<a href="./src/morta/resources/user/user.py">create</a>(\*\*<a href="src/morta/types/user_create_params.py">params</a>) -> <a href="./src/morta/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /v1/user/{firebase_id}">client.user.<a href="./src/morta/resources/user/user.py">retrieve</a>(firebase_id) -> <a href="./src/morta/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /v1/user/{firebase_id}/achievements">client.user.<a href="./src/morta/resources/user/user.py">list_achievements</a>(firebase_id) -> <a href="./src/morta/types/user_list_achievements_response.py">UserListAchievementsResponse</a></code>
- <code title="get /v1/user/{firebase_id}/contributions">client.user.<a href="./src/morta/resources/user/user.py">list_contributions</a>(firebase_id) -> <a href="./src/morta/types/user_list_contributions_response.py">UserListContributionsResponse</a></code>
- <code title="get /v1/user/owner-hubs">client.user.<a href="./src/morta/resources/user/user.py">list_owner_hubs</a>() -> <a href="./src/morta/types/user_list_owner_hubs_response.py">UserListOwnerHubsResponse</a></code>
- <code title="get /v1/user/{firebase_id}/pinned-hubs">client.user.<a href="./src/morta/resources/user/user.py">list_pinned_hubs</a>(firebase_id) -> <a href="./src/morta/types/user_list_pinned_hubs_response.py">UserListPinnedHubsResponse</a></code>
- <code title="get /v1/user/{firebase_id}/public-contributions">client.user.<a href="./src/morta/resources/user/user.py">list_public_contributions</a>(firebase_id) -> <a href="./src/morta/types/user_list_public_contributions_response.py">UserListPublicContributionsResponse</a></code>
- <code title="get /v1/user/public-hubs">client.user.<a href="./src/morta/resources/user/user.py">list_public_hubs</a>() -> <a href="./src/morta/types/user_list_public_hubs_response.py">UserListPublicHubsResponse</a></code>
- <code title="get /v1/user/templates">client.user.<a href="./src/morta/resources/user/user.py">list_templates</a>() -> <a href="./src/morta/types/user_list_templates_response.py">UserListTemplatesResponse</a></code>
- <code title="get /v1/user/public/{public_id}">client.user.<a href="./src/morta/resources/user/user.py">retrieve_by_public_id</a>(public_id) -> <a href="./src/morta/types/user_retrieve_by_public_id_response.py">UserRetrieveByPublicIDResponse</a></code>
- <code title="get /v1/user/me">client.user.<a href="./src/morta/resources/user/user.py">retrieve_me</a>() -> <a href="./src/morta/types/user_retrieve_me_response.py">UserRetrieveMeResponse</a></code>
- <code title="get /v1/user/sites">client.user.<a href="./src/morta/resources/user/user.py">retrieve_sites</a>() -> <a href="./src/morta/types/user_retrieve_sites_response.py">UserRetrieveSitesResponse</a></code>
- <code title="get /v1/user/search">client.user.<a href="./src/morta/resources/user/user.py">search</a>(\*\*<a href="src/morta/types/user_search_params.py">params</a>) -> <a href="./src/morta/types/user_search_response.py">UserSearchResponse</a></code>
- <code title="put /v1/user/account">client.user.<a href="./src/morta/resources/user/user.py">update_account</a>(\*\*<a href="src/morta/types/user_update_account_params.py">params</a>) -> <a href="./src/morta/types/user_update_account_response.py">UserUpdateAccountResponse</a></code>
- <code title="put /v1/user">client.user.<a href="./src/morta/resources/user/user.py">update_profile</a>(\*\*<a href="src/morta/types/user_update_profile_params.py">params</a>) -> <a href="./src/morta/types/user_update_profile_response.py">UserUpdateProfileResponse</a></code>

## Apikey

Types:

```python
from morta.types.user import (
    APIKey,
    ApikeyCreateResponse,
    ApikeyUpdateResponse,
    ApikeyDeleteResponse,
)
```

Methods:

- <code title="post /v1/user/apikey">client.user.apikey.<a href="./src/morta/resources/user/apikey.py">create</a>(\*\*<a href="src/morta/types/user/apikey_create_params.py">params</a>) -> <a href="./src/morta/types/user/apikey_create_response.py">ApikeyCreateResponse</a></code>
- <code title="put /v1/user/apikey/{api_key_id}">client.user.apikey.<a href="./src/morta/resources/user/apikey.py">update</a>(api_key_id, \*\*<a href="src/morta/types/user/apikey_update_params.py">params</a>) -> <a href="./src/morta/types/user/apikey_update_response.py">ApikeyUpdateResponse</a></code>
- <code title="delete /v1/user/apikey/{api_key_id}">client.user.apikey.<a href="./src/morta/resources/user/apikey.py">delete</a>(api_key_id) -> <a href="./src/morta/types/user/apikey_delete_response.py">ApikeyDeleteResponse</a></code>

## Hubs

Types:

```python
from morta.types.user import (
    HomeHub,
    HubListResponse,
    HubListFavouritesResponse,
    HubListTagsResponse,
    HubToggleFavouriteResponse,
    HubTogglePinResponse,
)
```

Methods:

- <code title="get /v1/user/hubs">client.user.hubs.<a href="./src/morta/resources/user/hubs.py">list</a>(\*\*<a href="src/morta/types/user/hub_list_params.py">params</a>) -> <a href="./src/morta/types/user/hub_list_response.py">HubListResponse</a></code>
- <code title="get /v1/user/hubs/favourites">client.user.hubs.<a href="./src/morta/resources/user/hubs.py">list_favourites</a>() -> <a href="./src/morta/types/user/hub_list_favourites_response.py">HubListFavouritesResponse</a></code>
- <code title="get /v1/user/hubs/{hub_id}/tags">client.user.hubs.<a href="./src/morta/resources/user/hubs.py">list_tags</a>(hub_id) -> <a href="./src/morta/types/user/hub_list_tags_response.py">HubListTagsResponse</a></code>
- <code title="put /v1/user/hubs/{hub_id}/favourite">client.user.hubs.<a href="./src/morta/resources/user/hubs.py">toggle_favourite</a>(hub_id) -> <a href="./src/morta/types/user/hub_toggle_favourite_response.py">HubToggleFavouriteResponse</a></code>
- <code title="put /v1/user/hubs/{hub_id}/pin">client.user.hubs.<a href="./src/morta/resources/user/hubs.py">toggle_pin</a>(hub_id) -> <a href="./src/morta/types/user/hub_toggle_pin_response.py">HubTogglePinResponse</a></code>

## Tags

Types:

```python
from morta.types.user import Tag, TagDeleteResponse, TagAddResponse, TagBulkApplyResponse
```

Methods:

- <code title="delete /v1/user/{user_id}/tags/{tag_id}">client.user.tags.<a href="./src/morta/resources/user/tags.py">delete</a>(tag_id, \*, user_id) -> <a href="./src/morta/types/user/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="post /v1/user/{user_id}/tags">client.user.tags.<a href="./src/morta/resources/user/tags.py">add</a>(user_id, \*\*<a href="src/morta/types/user/tag_add_params.py">params</a>) -> <a href="./src/morta/types/user/tag_add_response.py">TagAddResponse</a></code>
- <code title="put /v1/user/{user_id}/tags">client.user.tags.<a href="./src/morta/resources/user/tags.py">bulk_apply</a>(user_id, \*\*<a href="src/morta/types/user/tag_bulk_apply_params.py">params</a>) -> <a href="./src/morta/types/user/tag_bulk_apply_response.py">TagBulkApplyResponse</a></code>

## Sessions

Types:

```python
from morta.types.user import SessionListResponse, SessionDeleteResponse
```

Methods:

- <code title="get /v1/user/sessions">client.user.sessions.<a href="./src/morta/resources/user/sessions.py">list</a>() -> <a href="./src/morta/types/user/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /v1/user/sessions/{session_public_id}">client.user.sessions.<a href="./src/morta/resources/user/sessions.py">delete</a>(session_public_id) -> <a href="./src/morta/types/user/session_delete_response.py">SessionDeleteResponse</a></code>

## Notifications

Types:

```python
from morta.types.user import (
    UserNotification,
    NotificationUpdateResponse,
    NotificationListResponse,
    NotificationReadAllResponse,
)
```

Methods:

- <code title="patch /v1/user/notifications/{notification_id}">client.user.notifications.<a href="./src/morta/resources/user/notifications.py">update</a>(notification_id, \*\*<a href="src/morta/types/user/notification_update_params.py">params</a>) -> <a href="./src/morta/types/user/notification_update_response.py">NotificationUpdateResponse</a></code>
- <code title="get /v1/user/notifications">client.user.notifications.<a href="./src/morta/resources/user/notifications.py">list</a>(\*\*<a href="src/morta/types/user/notification_list_params.py">params</a>) -> <a href="./src/morta/types/user/notification_list_response.py">NotificationListResponse</a></code>
- <code title="post /v1/user/notifications/read-all">client.user.notifications.<a href="./src/morta/resources/user/notifications.py">read_all</a>() -> <a href="./src/morta/types/user/notification_read_all_response.py">NotificationReadAllResponse</a></code>

# Hub

Types:

```python
from morta.types import (
    Answer,
    BaseRequestContext,
    HeadingStyle,
    ProjectList,
    SidebarResource,
    SimpleHub,
    SiteSchemaWithOrg,
    UserHub,
    HubCreateResponse,
    HubRetrieveResponse,
    HubUpdateResponse,
    HubDeleteResponse,
    HubChangeUserRoleResponse,
    HubCreateHeadingStylingResponse,
    HubDeleteTopHeadingStylingResponse,
    HubGetDeletedDocumentsResponse,
    HubGetDeletedTablesResponse,
    HubGetDocumentsResponse,
    HubGetDuplicatedChildrenResponse,
    HubGetInvitedMembersResponse,
    HubGetMembersResponse,
    HubGetNotificationsResponse,
    HubGetResourcesResponse,
    HubGetSentNotificationsResponse,
    HubGetTablesResponse,
    HubGetTagsResponse,
    HubGetVariablesResponse,
    HubInviteMultipleUsersResponse,
    HubPermanentlyDeleteResponse,
    HubRemoveUserResponse,
    HubRestoreResponse,
    HubSearchResourcesResponse,
    HubUpdateHeadingStylingResponse,
    HubUploadTemplateResponse,
)
```

Methods:

- <code title="post /v1/hub">client.hub.<a href="./src/morta/resources/hub/hub.py">create</a>(\*\*<a href="src/morta/types/hub_create_params.py">params</a>) -> <a href="./src/morta/types/hub_create_response.py">HubCreateResponse</a></code>
- <code title="get /v1/hub/{hub_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">retrieve</a>(hub_id) -> <a href="./src/morta/types/hub_retrieve_response.py">HubRetrieveResponse</a></code>
- <code title="put /v1/hub/{hub_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">update</a>(hub_id, \*\*<a href="src/morta/types/hub_update_params.py">params</a>) -> <a href="./src/morta/types/hub_update_response.py">HubUpdateResponse</a></code>
- <code title="delete /v1/hub/{hub_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">delete</a>(hub_id) -> <a href="./src/morta/types/hub_delete_response.py">HubDeleteResponse</a></code>
- <code title="put /v1/hub/{hub_id}/change-user-role/{firebase_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">change_user_role</a>(firebase_id, \*, hub_id, \*\*<a href="src/morta/types/hub_change_user_role_params.py">params</a>) -> <a href="./src/morta/types/hub_change_user_role_response.py">HubChangeUserRoleResponse</a></code>
- <code title="post /v1/hub/{hub_id}/add_heading_styling">client.hub.<a href="./src/morta/resources/hub/hub.py">create_heading_styling</a>(hub_id) -> <a href="./src/morta/types/hub_create_heading_styling_response.py">HubCreateHeadingStylingResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/delete_top_style">client.hub.<a href="./src/morta/resources/hub/hub.py">delete_top_heading_styling</a>(hub_id) -> <a href="./src/morta/types/hub_delete_top_heading_styling_response.py">HubDeleteTopHeadingStylingResponse</a></code>
- <code title="post /v1/hub/{hub_id}/duplicate">client.hub.<a href="./src/morta/resources/hub/hub.py">duplicate</a>(hub_id, \*\*<a href="src/morta/types/hub_duplicate_params.py">params</a>) -> None</code>
- <code title="get /v1/hub/{hub_id}/deleted-documents">client.hub.<a href="./src/morta/resources/hub/hub.py">get_deleted_documents</a>(hub_id) -> <a href="./src/morta/types/hub_get_deleted_documents_response.py">HubGetDeletedDocumentsResponse</a></code>
- <code title="get /v1/hub/{hub_id}/deleted-tables">client.hub.<a href="./src/morta/resources/hub/hub.py">get_deleted_tables</a>(hub_id) -> <a href="./src/morta/types/hub_get_deleted_tables_response.py">HubGetDeletedTablesResponse</a></code>
- <code title="get /v1/hub/{hub_id}/documents">client.hub.<a href="./src/morta/resources/hub/hub.py">get_documents</a>(hub_id) -> <a href="./src/morta/types/hub_get_documents_response.py">HubGetDocumentsResponse</a></code>
- <code title="get /v1/hub/{hub_id}/duplicated-children">client.hub.<a href="./src/morta/resources/hub/hub.py">get_duplicated_children</a>(hub_id) -> <a href="./src/morta/types/hub_get_duplicated_children_response.py">HubGetDuplicatedChildrenResponse</a></code>
- <code title="get /v1/hub/{hub_id}/invited-members">client.hub.<a href="./src/morta/resources/hub/hub.py">get_invited_members</a>(hub_id) -> <a href="./src/morta/types/hub_get_invited_members_response.py">HubGetInvitedMembersResponse</a></code>
- <code title="get /v1/hub/{hub_id}/members">client.hub.<a href="./src/morta/resources/hub/hub.py">get_members</a>(hub_id) -> <a href="./src/morta/types/hub_get_members_response.py">HubGetMembersResponse</a></code>
- <code title="get /v1/hub/{hub_id}/notifications">client.hub.<a href="./src/morta/resources/hub/hub.py">get_notifications</a>(hub_id) -> <a href="./src/morta/types/hub_get_notifications_response.py">HubGetNotificationsResponse</a></code>
- <code title="post /v1/hub/{hub_id}/resources">client.hub.<a href="./src/morta/resources/hub/hub.py">get_resources</a>(hub_id, \*\*<a href="src/morta/types/hub_get_resources_params.py">params</a>) -> <a href="./src/morta/types/hub_get_resources_response.py">HubGetResourcesResponse</a></code>
- <code title="get /v1/hub/{hub_id}/sent-notifications">client.hub.<a href="./src/morta/resources/hub/hub.py">get_sent_notifications</a>(hub_id, \*\*<a href="src/morta/types/hub_get_sent_notifications_params.py">params</a>) -> <a href="./src/morta/types/hub_get_sent_notifications_response.py">HubGetSentNotificationsResponse</a></code>
- <code title="get /v1/hub/{hub_id}/tables">client.hub.<a href="./src/morta/resources/hub/hub.py">get_tables</a>(hub_id) -> <a href="./src/morta/types/hub_get_tables_response.py">HubGetTablesResponse</a></code>
- <code title="get /v1/hub/{hub_id}/tags">client.hub.<a href="./src/morta/resources/hub/hub.py">get_tags</a>(hub_id) -> <a href="./src/morta/types/hub_get_tags_response.py">HubGetTagsResponse</a></code>
- <code title="get /v1/hub/{hub_id}/variables">client.hub.<a href="./src/morta/resources/hub/hub.py">get_variables</a>(hub_id) -> <a href="./src/morta/types/hub_get_variables_response.py">HubGetVariablesResponse</a></code>
- <code title="post /v1/hub/{hub_id}/invite-multiple">client.hub.<a href="./src/morta/resources/hub/hub.py">invite_multiple_users</a>(hub_id, \*\*<a href="src/morta/types/hub_invite_multiple_users_params.py">params</a>) -> <a href="./src/morta/types/hub_invite_multiple_users_response.py">HubInviteMultipleUsersResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/permanent">client.hub.<a href="./src/morta/resources/hub/hub.py">permanently_delete</a>(hub_id) -> <a href="./src/morta/types/hub_permanently_delete_response.py">HubPermanentlyDeleteResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/remove-user/{firebase_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">remove_user</a>(firebase_id, \*, hub_id) -> <a href="./src/morta/types/hub_remove_user_response.py">HubRemoveUserResponse</a></code>
- <code title="put /v1/hub/{hub_id}/restore">client.hub.<a href="./src/morta/resources/hub/hub.py">restore</a>(hub_id) -> <a href="./src/morta/types/hub_restore_response.py">HubRestoreResponse</a></code>
- <code title="get /v1/hub/{hub_id}/search-resources">client.hub.<a href="./src/morta/resources/hub/hub.py">search_resources</a>(hub_id, \*\*<a href="src/morta/types/hub_search_resources_params.py">params</a>) -> <a href="./src/morta/types/hub_search_resources_response.py">HubSearchResourcesResponse</a></code>
- <code title="post /v1/hub/{hub_id}/set-column-coloring">client.hub.<a href="./src/morta/resources/hub/hub.py">set_column_coloring</a>(hub_id) -> None</code>
- <code title="post /v1/hub/{hub_id}/set-column-format/{kind}">client.hub.<a href="./src/morta/resources/hub/hub.py">set_column_format</a>(kind, \*, hub_id) -> None</code>
- <code title="post /v1/hub/{hub_id}/style/{style_id}">client.hub.<a href="./src/morta/resources/hub/hub.py">update_heading_styling</a>(style_id, \*, hub_id, \*\*<a href="src/morta/types/hub_update_heading_styling_params.py">params</a>) -> <a href="./src/morta/types/hub_update_heading_styling_response.py">HubUpdateHeadingStylingResponse</a></code>
- <code title="post /v1/hub/{hub_id}/upload-template">client.hub.<a href="./src/morta/resources/hub/hub.py">upload_template</a>(hub_id, \*\*<a href="src/morta/types/hub_upload_template_params.py">params</a>) -> <a href="./src/morta/types/hub_upload_template_response.py">HubUploadTemplateResponse</a></code>

## Invite

Types:

```python
from morta.types.hub import (
    InvitedMember,
    InviteCreateResponse,
    InviteUpdateResponse,
    InviteDeleteResponse,
    InviteResendResponse,
)
```

Methods:

- <code title="post /v1/hub/{hub_id}/invite">client.hub.invite.<a href="./src/morta/resources/hub/invite.py">create</a>(hub_id, \*\*<a href="src/morta/types/hub/invite_create_params.py">params</a>) -> <a href="./src/morta/types/hub/invite_create_response.py">InviteCreateResponse</a></code>
- <code title="put /v1/hub/{hub_id}/invite/{invite_id}">client.hub.invite.<a href="./src/morta/resources/hub/invite.py">update</a>(invite_id, \*, hub_id, \*\*<a href="src/morta/types/hub/invite_update_params.py">params</a>) -> <a href="./src/morta/types/hub/invite_update_response.py">InviteUpdateResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/invite/{invite_id}">client.hub.invite.<a href="./src/morta/resources/hub/invite.py">delete</a>(invite_id, \*, hub_id) -> <a href="./src/morta/types/hub/invite_delete_response.py">InviteDeleteResponse</a></code>
- <code title="post /v1/hub/{hub_id}/invite/{invite_id}">client.hub.invite.<a href="./src/morta/resources/hub/invite.py">resend</a>(invite_id, \*, hub_id) -> <a href="./src/morta/types/hub/invite_resend_response.py">InviteResendResponse</a></code>

## Secrets

Types:

```python
from morta.types.hub import (
    HubSecret,
    SecretCreateResponse,
    SecretUpdateResponse,
    SecretListResponse,
    SecretDeleteResponse,
)
```

Methods:

- <code title="post /v1/hub/{hub_id}/secrets">client.hub.secrets.<a href="./src/morta/resources/hub/secrets.py">create</a>(hub_id, \*\*<a href="src/morta/types/hub/secret_create_params.py">params</a>) -> <a href="./src/morta/types/hub/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="put /v1/hub/{hub_id}/secrets/{secret_id}">client.hub.secrets.<a href="./src/morta/resources/hub/secrets.py">update</a>(secret_id, \*, hub_id, \*\*<a href="src/morta/types/hub/secret_update_params.py">params</a>) -> <a href="./src/morta/types/hub/secret_update_response.py">SecretUpdateResponse</a></code>
- <code title="get /v1/hub/{hub_id}/secrets">client.hub.secrets.<a href="./src/morta/resources/hub/secrets.py">list</a>(hub_id) -> <a href="./src/morta/types/hub/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/secrets/{secret_id}">client.hub.secrets.<a href="./src/morta/resources/hub/secrets.py">delete</a>(secret_id, \*, hub_id) -> <a href="./src/morta/types/hub/secret_delete_response.py">SecretDeleteResponse</a></code>

## Scripts

Types:

```python
from morta.types.hub import ScriptListResponse, ScriptRetrieveCountResponse
```

Methods:

- <code title="get /v1/hub/{hub_id}/scripts">client.hub.scripts.<a href="./src/morta/resources/hub/scripts.py">list</a>(hub_id) -> <a href="./src/morta/types/hub/script_list_response.py">ScriptListResponse</a></code>
- <code title="get /v1/hub/{hub_id}/scripts/count">client.hub.scripts.<a href="./src/morta/resources/hub/scripts.py">retrieve_count</a>(hub_id) -> <a href="./src/morta/types/hub/script_retrieve_count_response.py">ScriptRetrieveCountResponse</a></code>

## Folders

Types:

```python
from morta.types.hub import (
    HubFolder,
    FolderCreateResponse,
    FolderUpdateResponse,
    FolderDeleteResponse,
    FolderMoveResponse,
)
```

Methods:

- <code title="post /v1/hub/{hub_id}/folders">client.hub.folders.<a href="./src/morta/resources/hub/folders.py">create</a>(hub_id, \*\*<a href="src/morta/types/hub/folder_create_params.py">params</a>) -> <a href="./src/morta/types/hub/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="put /v1/hub/{hub_id}/folders/{folder_id}">client.hub.folders.<a href="./src/morta/resources/hub/folders.py">update</a>(folder_id, \*, hub_id, \*\*<a href="src/morta/types/hub/folder_update_params.py">params</a>) -> <a href="./src/morta/types/hub/folder_update_response.py">FolderUpdateResponse</a></code>
- <code title="delete /v1/hub/{hub_id}/folders/{folder_id}">client.hub.folders.<a href="./src/morta/resources/hub/folders.py">delete</a>(folder_id, \*, hub_id) -> <a href="./src/morta/types/hub/folder_delete_response.py">FolderDeleteResponse</a></code>
- <code title="post /v1/hub/{hub_id}/folders/move">client.hub.folders.<a href="./src/morta/resources/hub/folders.py">move</a>(hub_id, \*\*<a href="src/morta/types/hub/folder_move_params.py">params</a>) -> <a href="./src/morta/types/hub/folder_move_response.py">FolderMoveResponse</a></code>

## Relationships

Methods:

- <code title="get /v1/hub/{hub_id}/relationships">client.hub.relationships.<a href="./src/morta/resources/hub/relationships.py">list</a>(hub_id) -> None</code>

## Sidebar

Types:

```python
from morta.types.hub import SidebarContainersResponse
```

Methods:

- <code title="post /v1/hub/{hub_id}/sidebar/containers">client.hub.sidebar.<a href="./src/morta/resources/hub/sidebar.py">containers</a>(hub_id, \*\*<a href="src/morta/types/hub/sidebar_containers_params.py">params</a>) -> <a href="./src/morta/types/hub/sidebar_containers_response.py">SidebarContainersResponse</a></code>

# Table

Types:

```python
from morta.types import (
    Project,
    Table,
    TableColumnWithAggregation,
    TableJoin,
    TableJoinImportedColumns,
    TableJoinImportedColumns1,
    UpdateDocumentTableCells,
    TableCreateResponse,
    TableRetrieveResponse,
    TableUpdateResponse,
    TableDeleteResponse,
    TableCheckUsageResponse,
    TableCreateIndexResponse,
    TableDeleteRowsResponse,
    TableDownloadCsvResponse,
    TableDuplicateResponse,
    TableGetCsvBackupResponse,
    TableGetDuplicatedChildrenResponse,
    TableGetStatisticsResponse,
    TableListColumnsResponse,
    TableListJoinsResponse,
    TableRestoreResponse,
    TableTruncateResponse,
    TableUpdateCellsResponse,
)
```

Methods:

- <code title="post /v1/table">client.table.<a href="./src/morta/resources/table/table.py">create</a>(\*\*<a href="src/morta/types/table_create_params.py">params</a>) -> <a href="./src/morta/types/table_create_response.py">TableCreateResponse</a></code>
- <code title="get /v1/table/{table_id}">client.table.<a href="./src/morta/resources/table/table.py">retrieve</a>(table_id, \*\*<a href="src/morta/types/table_retrieve_params.py">params</a>) -> <a href="./src/morta/types/table_retrieve_response.py">TableRetrieveResponse</a></code>
- <code title="put /v1/table/{table_id}">client.table.<a href="./src/morta/resources/table/table.py">update</a>(table_id, \*\*<a href="src/morta/types/table_update_params.py">params</a>) -> <a href="./src/morta/types/table_update_response.py">TableUpdateResponse</a></code>
- <code title="delete /v1/table/{table_id}">client.table.<a href="./src/morta/resources/table/table.py">delete</a>(table_id) -> <a href="./src/morta/types/table_delete_response.py">TableDeleteResponse</a></code>
- <code title="get /v1/table/{table_id}/used">client.table.<a href="./src/morta/resources/table/table.py">check_usage</a>(table_id) -> <a href="./src/morta/types/table_check_usage_response.py">TableCheckUsageResponse</a></code>
- <code title="post /v1/table/{table_id}/indexes">client.table.<a href="./src/morta/resources/table/table.py">create_index</a>(table_id, \*\*<a href="src/morta/types/table_create_index_params.py">params</a>) -> <a href="./src/morta/types/table_create_index_response.py">TableCreateIndexResponse</a></code>
- <code title="delete /v1/table/{table_id}/rows">client.table.<a href="./src/morta/resources/table/table.py">delete_rows</a>(table_id) -> <a href="./src/morta/types/table_delete_rows_response.py">TableDeleteRowsResponse</a></code>
- <code title="get /v1/table/{table_id}/csv">client.table.<a href="./src/morta/resources/table/table.py">download_csv</a>(table_id, \*\*<a href="src/morta/types/table_download_csv_params.py">params</a>) -> str</code>
- <code title="post /v1/table/{table_id}/duplicate">client.table.<a href="./src/morta/resources/table/table.py">duplicate</a>(table_id, \*\*<a href="src/morta/types/table_duplicate_params.py">params</a>) -> <a href="./src/morta/types/table_duplicate_response.py">TableDuplicateResponse</a></code>
- <code title="get /v1/table/{table_id}/csv-backup">client.table.<a href="./src/morta/resources/table/table.py">get_csv_backup</a>(table_id, \*\*<a href="src/morta/types/table_get_csv_backup_params.py">params</a>) -> <a href="./src/morta/types/table_get_csv_backup_response.py">TableGetCsvBackupResponse</a></code>
- <code title="get /v1/table/{table_id}/duplicated-children">client.table.<a href="./src/morta/resources/table/table.py">get_duplicated_children</a>(table_id) -> <a href="./src/morta/types/table_get_duplicated_children_response.py">TableGetDuplicatedChildrenResponse</a></code>
- <code title="get /v1/table/{table_id}/file">client.table.<a href="./src/morta/resources/table/table.py">get_file</a>(table_id, \*\*<a href="src/morta/types/table_get_file_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/table/{table_id}/stats">client.table.<a href="./src/morta/resources/table/table.py">get_statistics</a>(table_id, \*\*<a href="src/morta/types/table_get_statistics_params.py">params</a>) -> <a href="./src/morta/types/table_get_statistics_response.py">TableGetStatisticsResponse</a></code>
- <code title="get /v1/table/{table_id}/columns">client.table.<a href="./src/morta/resources/table/table.py">list_columns</a>(table_id) -> <a href="./src/morta/types/table_list_columns_response.py">TableListColumnsResponse</a></code>
- <code title="get /v1/table/{table_id}/joins">client.table.<a href="./src/morta/resources/table/table.py">list_joins</a>(table_id) -> <a href="./src/morta/types/table_list_joins_response.py">TableListJoinsResponse</a></code>
- <code title="put /v1/table/{table_id}/restore">client.table.<a href="./src/morta/resources/table/table.py">restore</a>(table_id) -> <a href="./src/morta/types/table_restore_response.py">TableRestoreResponse</a></code>
- <code title="get /v1/table/{table_id}/rows-stream">client.table.<a href="./src/morta/resources/table/table.py">stream_rows</a>(table_id, \*\*<a href="src/morta/types/table_stream_rows_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /v1/table/{table_id}/truncate">client.table.<a href="./src/morta/resources/table/table.py">truncate</a>(table_id) -> <a href="./src/morta/types/table_truncate_response.py">TableTruncateResponse</a></code>
- <code title="put /v1/table/{table_id}/cells">client.table.<a href="./src/morta/resources/table/table.py">update_cells</a>(table_id, \*\*<a href="src/morta/types/table_update_cells_params.py">params</a>) -> <a href="./src/morta/types/table_update_cells_response.py">TableUpdateCellsResponse</a></code>

## Column

Types:

```python
from morta.types.table import (
    SelectOptionsLookup,
    TableColumn,
    TableColumnAlter,
    ColumnCreateResponse,
    ColumnUpdateResponse,
    ColumnDeleteResponse,
    ColumnCheckViewsResponse,
    ColumnGetDistinctValuesResponse,
    ColumnRestoreResponse,
)
```

Methods:

- <code title="post /v1/table/{table_id}/column">client.table.column.<a href="./src/morta/resources/table/column.py">create</a>(table_id, \*\*<a href="src/morta/types/table/column_create_params.py">params</a>) -> <a href="./src/morta/types/table/column_create_response.py">ColumnCreateResponse</a></code>
- <code title="put /v1/table/{table_id}/column/{column_id}">client.table.column.<a href="./src/morta/resources/table/column.py">update</a>(column_id, \*, table_id, \*\*<a href="src/morta/types/table/column_update_params.py">params</a>) -> <a href="./src/morta/types/table/column_update_response.py">ColumnUpdateResponse</a></code>
- <code title="delete /v1/table/{table_id}/column/{column_id}">client.table.column.<a href="./src/morta/resources/table/column.py">delete</a>(column_id, \*, table_id) -> <a href="./src/morta/types/table/column_delete_response.py">ColumnDeleteResponse</a></code>
- <code title="get /v1/table/{table_id}/column/{column_id}/views">client.table.column.<a href="./src/morta/resources/table/column.py">check_views</a>(column_id, \*, table_id) -> <a href="./src/morta/types/table/column_check_views_response.py">ColumnCheckViewsResponse</a></code>
- <code title="get /v1/table/{table_id}/column/{column_id}/distinct">client.table.column.<a href="./src/morta/resources/table/column.py">get_distinct_values</a>(column_id, \*, table_id, \*\*<a href="src/morta/types/table/column_get_distinct_values_params.py">params</a>) -> <a href="./src/morta/types/table/column_get_distinct_values_response.py">ColumnGetDistinctValuesResponse</a></code>
- <code title="put /v1/table/{table_id}/column/{column_id}/restore">client.table.column.<a href="./src/morta/resources/table/column.py">restore</a>(column_id, \*, table_id) -> <a href="./src/morta/types/table/column_restore_response.py">ColumnRestoreResponse</a></code>

## Row

Types:

```python
from morta.types.table import (
    CreateTableRows,
    TableRowAction,
    UpdateTableRows,
    UpsertTableRows,
    RowUpdateResponse,
    RowAddResponse,
    RowGetRowsResponse,
    RowUpsertResponse,
)
```

Methods:

- <code title="put /v1/table/{table_id}/row">client.table.row.<a href="./src/morta/resources/table/row.py">update</a>(table_id, \*\*<a href="src/morta/types/table/row_update_params.py">params</a>) -> <a href="./src/morta/types/table/row_update_response.py">RowUpdateResponse</a></code>
- <code title="post /v1/table/{table_id}/row">client.table.row.<a href="./src/morta/resources/table/row.py">add</a>(table_id, \*\*<a href="src/morta/types/table/row_add_params.py">params</a>) -> <a href="./src/morta/types/table/row_add_response.py">RowAddResponse</a></code>
- <code title="get /v1/table/{table_id}/row">client.table.row.<a href="./src/morta/resources/table/row.py">get_rows</a>(table_id, \*\*<a href="src/morta/types/table/row_get_rows_params.py">params</a>) -> <a href="./src/morta/types/table/row_get_rows_response.py">RowGetRowsResponse</a></code>
- <code title="post /v1/table/{table_id}/row/upsert">client.table.row.<a href="./src/morta/resources/table/row.py">upsert</a>(table_id, \*\*<a href="src/morta/types/table/row_upsert_params.py">params</a>) -> <a href="./src/morta/types/table/row_upsert_response.py">RowUpsertResponse</a></code>

## Join

Types:

```python
from morta.types.table import (
    TableColumnJoin,
    JoinCreateResponse,
    JoinUpdateResponse,
    JoinDeleteResponse,
)
```

Methods:

- <code title="post /v1/table/{table_id}/join">client.table.join.<a href="./src/morta/resources/table/join.py">create</a>(table_id, \*\*<a href="src/morta/types/table/join_create_params.py">params</a>) -> <a href="./src/morta/types/table/join_create_response.py">JoinCreateResponse</a></code>
- <code title="put /v1/table/{table_id}/join/{join_id}">client.table.join.<a href="./src/morta/resources/table/join.py">update</a>(join_id, \*, table_id, \*\*<a href="src/morta/types/table/join_update_params.py">params</a>) -> <a href="./src/morta/types/table/join_update_response.py">JoinUpdateResponse</a></code>
- <code title="delete /v1/table/{table_id}/join/{join_id}">client.table.join.<a href="./src/morta/resources/table/join.py">delete</a>(join_id, \*, table_id) -> <a href="./src/morta/types/table/join_delete_response.py">JoinDeleteResponse</a></code>

## Sync

Types:

```python
from morta.types.table import (
    SyncUpdateResponse,
    SyncDeleteIntegrationResponse,
    SyncGetSyncInfoResponse,
    SyncRetryIntegrationSyncResponse,
    SyncSyncWithIntegrationResponse,
)
```

Methods:

- <code title="post /v1/table/{table_id}/sync/{integration_name}/update">client.table.sync.<a href="./src/morta/resources/table/sync.py">update</a>(integration_name, \*, table_id, \*\*<a href="src/morta/types/table/sync_update_params.py">params</a>) -> <a href="./src/morta/types/table/sync_update_response.py">SyncUpdateResponse</a></code>
- <code title="delete /v1/table/{table_id}/sync/{integration_name}">client.table.sync.<a href="./src/morta/resources/table/sync.py">delete_integration</a>(integration_name, \*, table_id) -> <a href="./src/morta/types/table/sync_delete_integration_response.py">SyncDeleteIntegrationResponse</a></code>
- <code title="get /v1/table/{table_id}/sync/info">client.table.sync.<a href="./src/morta/resources/table/sync.py">get_sync_info</a>(table_id) -> <a href="./src/morta/types/table/sync_get_sync_info_response.py">SyncGetSyncInfoResponse</a></code>
- <code title="get /v1/table/{table_id}/sync/manual">client.table.sync.<a href="./src/morta/resources/table/sync.py">retry_integration_sync</a>(table_id) -> <a href="./src/morta/types/table/sync_retry_integration_sync_response.py">SyncRetryIntegrationSyncResponse</a></code>
- <code title="post /v1/table/{table_id}/sync/{integration_name}">client.table.sync.<a href="./src/morta/resources/table/sync.py">sync_with_integration</a>(integration_name, \*, table_id, \*\*<a href="src/morta/types/table/sync_sync_with_integration_params.py">params</a>) -> <a href="./src/morta/types/table/sync_sync_with_integration_response.py">SyncSyncWithIntegrationResponse</a></code>

## Views

Types:

```python
from morta.types.table import (
    CalendarSettings,
    Chart,
    Colour,
    Filter,
    Group,
    MatrixSettings,
    PreviewTableRow,
    RowLock,
    Sort,
    TableView,
    TableViewConfigurationParentView,
    TransposeSettings,
    ViewCreateResponse,
    ViewRetrieveResponse,
    ViewUpdateResponse,
    ViewListResponse,
    ViewDeleteResponse,
    ViewCsvResponse,
    ViewDeleteCustomViewDraftResponse,
    ViewDownloadCsvResponse,
    ViewDuplicateResponse,
    ViewDuplicateDefaultResponse,
    ViewGetRowsResponse,
    ViewPreviewRowResponse,
    ViewSetDefaultResponse,
    ViewStatsResponse,
    ViewUpdateCellsResponse,
)
```

Methods:

- <code title="post /v1/table/{table_id}/views">client.table.views.<a href="./src/morta/resources/table/views/views.py">create</a>(table_id, \*\*<a href="src/morta/types/table/view_create_params.py">params</a>) -> <a href="./src/morta/types/table/view_create_response.py">ViewCreateResponse</a></code>
- <code title="get /v1/table/views/{view_id}">client.table.views.<a href="./src/morta/resources/table/views/views.py">retrieve</a>(view_id, \*\*<a href="src/morta/types/table/view_retrieve_params.py">params</a>) -> <a href="./src/morta/types/table/view_retrieve_response.py">ViewRetrieveResponse</a></code>
- <code title="put /v1/table/views/{view_id}">client.table.views.<a href="./src/morta/resources/table/views/views.py">update</a>(view_id, \*\*<a href="src/morta/types/table/view_update_params.py">params</a>) -> <a href="./src/morta/types/table/view_update_response.py">ViewUpdateResponse</a></code>
- <code title="get /v1/table/{table_id}/views">client.table.views.<a href="./src/morta/resources/table/views/views.py">list</a>(table_id, \*\*<a href="src/morta/types/table/view_list_params.py">params</a>) -> <a href="./src/morta/types/table/view_list_response.py">ViewListResponse</a></code>
- <code title="delete /v1/table/views/{view_id}">client.table.views.<a href="./src/morta/resources/table/views/views.py">delete</a>(view_id) -> <a href="./src/morta/types/table/view_delete_response.py">ViewDeleteResponse</a></code>
- <code title="post /v1/table/views/{view_id}/csv">client.table.views.<a href="./src/morta/resources/table/views/views.py">csv</a>(view_id, \*\*<a href="src/morta/types/table/view_csv_params.py">params</a>) -> str</code>
- <code title="delete /v1/table/views/{view_id}/custom-view-draft">client.table.views.<a href="./src/morta/resources/table/views/views.py">delete_custom_view_draft</a>(view_id) -> <a href="./src/morta/types/table/view_delete_custom_view_draft_response.py">ViewDeleteCustomViewDraftResponse</a></code>
- <code title="get /v1/table/views/{view_id}/csv">client.table.views.<a href="./src/morta/resources/table/views/views.py">download_csv</a>(view_id, \*\*<a href="src/morta/types/table/view_download_csv_params.py">params</a>) -> str</code>
- <code title="post /v1/table/{table_id}/views/{view_id}/duplicate">client.table.views.<a href="./src/morta/resources/table/views/views.py">duplicate</a>(view_id, \*, table_id) -> <a href="./src/morta/types/table/view_duplicate_response.py">ViewDuplicateResponse</a></code>
- <code title="post /v1/table/{table_id}/views/duplicate-default">client.table.views.<a href="./src/morta/resources/table/views/views.py">duplicate_default</a>(table_id, \*\*<a href="src/morta/types/table/view_duplicate_default_params.py">params</a>) -> <a href="./src/morta/types/table/view_duplicate_default_response.py">ViewDuplicateDefaultResponse</a></code>
- <code title="post /v1/table/views/{view_id}/get-rows">client.table.views.<a href="./src/morta/resources/table/views/views.py">get_rows</a>(view_id, \*\*<a href="src/morta/types/table/view_get_rows_params.py">params</a>) -> <a href="./src/morta/types/table/view_get_rows_response.py">ViewGetRowsResponse</a></code>
- <code title="post /v1/table/views/{view_id}/preview-row">client.table.views.<a href="./src/morta/resources/table/views/views.py">preview_row</a>(view_id, \*\*<a href="src/morta/types/table/view_preview_row_params.py">params</a>) -> <a href="./src/morta/types/table/view_preview_row_response.py">ViewPreviewRowResponse</a></code>
- <code title="post /v1/table/views/{view_id}/default">client.table.views.<a href="./src/morta/resources/table/views/views.py">set_default</a>(view_id) -> <a href="./src/morta/types/table/view_set_default_response.py">ViewSetDefaultResponse</a></code>
- <code title="get /v1/table/views/{view_id}/stats">client.table.views.<a href="./src/morta/resources/table/views/views.py">stats</a>(view_id, \*\*<a href="src/morta/types/table/view_stats_params.py">params</a>) -> <a href="./src/morta/types/table/view_stats_response.py">ViewStatsResponse</a></code>
- <code title="get /v1/table/views/{view_id}/rows-stream">client.table.views.<a href="./src/morta/resources/table/views/views.py">stream_rows</a>(view_id, \*\*<a href="src/morta/types/table/view_stream_rows_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /v1/table/views/{view_id}/cells">client.table.views.<a href="./src/morta/resources/table/views/views.py">update_cells</a>(view_id, \*\*<a href="src/morta/types/table/view_update_cells_params.py">params</a>) -> <a href="./src/morta/types/table/view_update_cells_response.py">ViewUpdateCellsResponse</a></code>

### Rows

Types:

```python
from morta.types.table.views import (
    RowUpdateResponse,
    RowListResponse,
    RowDeleteResponse,
    RowAddResponse,
    RowUpsertResponse,
)
```

Methods:

- <code title="put /v1/table/views/{view_id}/rows">client.table.views.rows.<a href="./src/morta/resources/table/views/rows.py">update</a>(view_id, \*\*<a href="src/morta/types/table/views/row_update_params.py">params</a>) -> <a href="./src/morta/types/table/views/row_update_response.py">RowUpdateResponse</a></code>
- <code title="get /v1/table/views/{view_id}/rows">client.table.views.rows.<a href="./src/morta/resources/table/views/rows.py">list</a>(view_id, \*\*<a href="src/morta/types/table/views/row_list_params.py">params</a>) -> <a href="./src/morta/types/table/views/row_list_response.py">RowListResponse</a></code>
- <code title="delete /v1/table/views/{view_id}/rows">client.table.views.rows.<a href="./src/morta/resources/table/views/rows.py">delete</a>(view_id, \*\*<a href="src/morta/types/table/views/row_delete_params.py">params</a>) -> <a href="./src/morta/types/table/views/row_delete_response.py">RowDeleteResponse</a></code>
- <code title="post /v1/table/views/{view_id}/rows">client.table.views.rows.<a href="./src/morta/resources/table/views/rows.py">add</a>(view_id, \*\*<a href="src/morta/types/table/views/row_add_params.py">params</a>) -> <a href="./src/morta/types/table/views/row_add_response.py">RowAddResponse</a></code>
- <code title="post /v1/table/views/{view_id}/rows/upsert">client.table.views.rows.<a href="./src/morta/resources/table/views/rows.py">upsert</a>(view_id, \*\*<a href="src/morta/types/table/views/row_upsert_params.py">params</a>) -> <a href="./src/morta/types/table/views/row_upsert_response.py">RowUpsertResponse</a></code>

### Columns

Types:

```python
from morta.types.table.views import (
    TableViewColumn,
    UpdateTableViewColumn,
    ColumnUpdateResponse,
    ColumnAddResponse,
    ColumnDistinctResponse,
    ColumnFormulaInfoResponse,
    ColumnValidateFormulaResponse,
)
```

Methods:

- <code title="put /v1/table/views/{view_id}/columns/{column_id}">client.table.views.columns.<a href="./src/morta/resources/table/views/columns.py">update</a>(column_id, \*, view_id, \*\*<a href="src/morta/types/table/views/column_update_params.py">params</a>) -> <a href="./src/morta/types/table/views/column_update_response.py">ColumnUpdateResponse</a></code>
- <code title="post /v1/table/views/{view_id}/columns">client.table.views.columns.<a href="./src/morta/resources/table/views/columns.py">add</a>(view_id, \*\*<a href="src/morta/types/table/views/column_add_params.py">params</a>) -> <a href="./src/morta/types/table/views/column_add_response.py">ColumnAddResponse</a></code>
- <code title="get /v1/table/views/{view_id}/column/{column_id}/distinct">client.table.views.columns.<a href="./src/morta/resources/table/views/columns.py">distinct</a>(column_id, \*, view_id, \*\*<a href="src/morta/types/table/views/column_distinct_params.py">params</a>) -> <a href="./src/morta/types/table/views/column_distinct_response.py">ColumnDistinctResponse</a></code>
- <code title="get /v1/table/views/{view_id}/column/{column_id}/formula-info">client.table.views.columns.<a href="./src/morta/resources/table/views/columns.py">formula_info</a>(column_id, \*, view_id) -> <a href="./src/morta/types/table/views/column_formula_info_response.py">ColumnFormulaInfoResponse</a></code>
- <code title="post /v1/table/views/{view_id}/column/{column_id}/validate-formula">client.table.views.columns.<a href="./src/morta/resources/table/views/columns.py">validate_formula</a>(column_id, \*, view_id, \*\*<a href="src/morta/types/table/views/column_validate_formula_params.py">params</a>) -> <a href="./src/morta/types/table/views/column_validate_formula_response.py">ColumnValidateFormulaResponse</a></code>

### Export

Methods:

- <code title="post /v1/table/views/{view_id}/export">client.table.views.export.<a href="./src/morta/resources/table/views/export.py">create</a>(view_id, \*\*<a href="src/morta/types/table/views/export_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/table/views/{view_id}/export">client.table.views.export.<a href="./src/morta/resources/table/views/export.py">list</a>(view_id, \*\*<a href="src/morta/types/table/views/export_list_params.py">params</a>) -> BinaryAPIResponse</code>

# Document

Types:

```python
from morta.types import (
    Document,
    DocumentSection1,
    Draftjs,
    DuplicatedChildren,
    MortaDocument,
    MortaDocumentSection,
    SimpleDocument,
    DocumentCreateResponse,
    DocumentRetrieveResponse,
    DocumentUpdateResponse,
    DocumentDeleteResponse,
    DocumentCreateMultipleSectionsResponse,
    DocumentCreateSectionsResponse,
    DocumentGetDeletedSectionsResponse,
    DocumentGetDuplicatedChildrenResponse,
    DocumentRestoreResponse,
    DocumentSyncTemplateResponse,
    DocumentUpdateMultipleSectionsResponse,
    DocumentUpdateSectionOrderResponse,
    DocumentUpdateViewsPermissionsResponse,
)
```

Methods:

- <code title="post /v1/document">client.document.<a href="./src/morta/resources/document/document.py">create</a>(\*\*<a href="src/morta/types/document_create_params.py">params</a>) -> <a href="./src/morta/types/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /v1/document/{document_id}">client.document.<a href="./src/morta/resources/document/document.py">retrieve</a>(document_id, \*\*<a href="src/morta/types/document_retrieve_params.py">params</a>) -> <a href="./src/morta/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="put /v1/document/{document_id}">client.document.<a href="./src/morta/resources/document/document.py">update</a>(document_id, \*\*<a href="src/morta/types/document_update_params.py">params</a>) -> <a href="./src/morta/types/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="delete /v1/document/{document_id}">client.document.<a href="./src/morta/resources/document/document.py">delete</a>(document_id) -> <a href="./src/morta/types/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="post /v1/document/{document_id}/multiple-section">client.document.<a href="./src/morta/resources/document/document.py">create_multiple_sections</a>(document_id, \*\*<a href="src/morta/types/document_create_multiple_sections_params.py">params</a>) -> <a href="./src/morta/types/document_create_multiple_sections_response.py">DocumentCreateMultipleSectionsResponse</a></code>
- <code title="post /v1/document/{document_id}/sections">client.document.<a href="./src/morta/resources/document/document.py">create_sections</a>(document_id, \*\*<a href="src/morta/types/document_create_sections_params.py">params</a>) -> <a href="./src/morta/types/document_create_sections_response.py">DocumentCreateSectionsResponse</a></code>
- <code title="post /v1/document/{document_id}/export">client.document.<a href="./src/morta/resources/document/document.py">export</a>(document_id, \*\*<a href="src/morta/types/document_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /v1/document/{document_id}/deletedsections">client.document.<a href="./src/morta/resources/document/document.py">get_deleted_sections</a>(document_id, \*\*<a href="src/morta/types/document_get_deleted_sections_params.py">params</a>) -> <a href="./src/morta/types/document_get_deleted_sections_response.py">DocumentGetDeletedSectionsResponse</a></code>
- <code title="get /v1/document/{document_id}/duplicated-children">client.document.<a href="./src/morta/resources/document/document.py">get_duplicated_children</a>(document_id) -> <a href="./src/morta/types/document_get_duplicated_children_response.py">DocumentGetDuplicatedChildrenResponse</a></code>
- <code title="put /v1/document/{document_id}/restore">client.document.<a href="./src/morta/resources/document/document.py">restore</a>(document_id) -> <a href="./src/morta/types/document_restore_response.py">DocumentRestoreResponse</a></code>
- <code title="get /v1/document/{document_id}/sync-template">client.document.<a href="./src/morta/resources/document/document.py">sync_template</a>(document_id) -> <a href="./src/morta/types/document_sync_template_response.py">DocumentSyncTemplateResponse</a></code>
- <code title="put /v1/document/{document_id}/update-multiple-section">client.document.<a href="./src/morta/resources/document/document.py">update_multiple_sections</a>(document_id, \*\*<a href="src/morta/types/document_update_multiple_sections_params.py">params</a>) -> <a href="./src/morta/types/document_update_multiple_sections_response.py">DocumentUpdateMultipleSectionsResponse</a></code>
- <code title="put /v1/document/{document_id}/changesectionorder">client.document.<a href="./src/morta/resources/document/document.py">update_section_order</a>(document_id, \*\*<a href="src/morta/types/document_update_section_order_params.py">params</a>) -> <a href="./src/morta/types/document_update_section_order_response.py">DocumentUpdateSectionOrderResponse</a></code>
- <code title="put /v1/document/sync-views-permissions">client.document.<a href="./src/morta/resources/document/document.py">update_views_permissions</a>(\*\*<a href="src/morta/types/document_update_views_permissions_params.py">params</a>) -> <a href="./src/morta/types/document_update_views_permissions_response.py">DocumentUpdateViewsPermissionsResponse</a></code>

## Duplicate

Methods:

- <code title="post /v1/document/{document_id}/duplicate">client.document.duplicate.<a href="./src/morta/resources/document/duplicate.py">duplicate</a>(document_id, \*\*<a href="src/morta/types/document/duplicate_duplicate_params.py">params</a>) -> None</code>

## Section

Types:

```python
from morta.types.document import (
    CreateDocumentSection,
    SectionCreateResponse,
    SectionRetrieveResponse,
    SectionUpdateResponse,
    SectionDeleteResponse,
    SectionDuplicateResponse,
    SectionRestoreResponse,
)
```

Methods:

- <code title="post /v1/document/{document_id}/section">client.document.section.<a href="./src/morta/resources/document/section/section.py">create</a>(document_id, \*\*<a href="src/morta/types/document/section_create_params.py">params</a>) -> <a href="./src/morta/types/document/section_create_response.py">SectionCreateResponse</a></code>
- <code title="get /v1/document/{document_id}/section/{document_section_id}">client.document.section.<a href="./src/morta/resources/document/section/section.py">retrieve</a>(document_section_id, \*, document_id, \*\*<a href="src/morta/types/document/section_retrieve_params.py">params</a>) -> <a href="./src/morta/types/document/section_retrieve_response.py">SectionRetrieveResponse</a></code>
- <code title="put /v1/document/{document_id}/section/{document_section_id}">client.document.section.<a href="./src/morta/resources/document/section/section.py">update</a>(document_section_id, \*, document_id, \*\*<a href="src/morta/types/document/section_update_params.py">params</a>) -> <a href="./src/morta/types/document/section_update_response.py">SectionUpdateResponse</a></code>
- <code title="delete /v1/document/{document_id}/section/{document_section_id}">client.document.section.<a href="./src/morta/resources/document/section/section.py">delete</a>(document_section_id, \*, document_id) -> <a href="./src/morta/types/document/section_delete_response.py">SectionDeleteResponse</a></code>
- <code title="post /v1/document/{document_id}/section/{document_section_id}/duplicate">client.document.section.<a href="./src/morta/resources/document/section/section.py">duplicate</a>(document_section_id, \*, document_id) -> <a href="./src/morta/types/document/section_duplicate_response.py">SectionDuplicateResponse</a></code>
- <code title="put /v1/document/{document_id}/section/{document_section_id}/restore">client.document.section.<a href="./src/morta/resources/document/section/section.py">restore</a>(document_section_id, \*, document_id) -> <a href="./src/morta/types/document/section_restore_response.py">SectionRestoreResponse</a></code>

### Submission

Types:

```python
from morta.types.document.section import (
    CreateEmbedSubmission,
    EmbedSubmission,
    UpdateEmbedSubmission,
    SubmissionCreateResponse,
    SubmissionUpdateResponse,
    SubmissionDeleteResponse,
    SubmissionResetResponse,
    SubmissionSubmitResponse,
)
```

Methods:

- <code title="post /v1/document/{document_id}/section/{document_section_id}/submission">client.document.section.submission.<a href="./src/morta/resources/document/section/submission.py">create</a>(document_section_id, \*, document_id, \*\*<a href="src/morta/types/document/section/submission_create_params.py">params</a>) -> <a href="./src/morta/types/document/section/submission_create_response.py">SubmissionCreateResponse</a></code>
- <code title="put /v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}">client.document.section.submission.<a href="./src/morta/resources/document/section/submission.py">update</a>(submission_id, \*, document_id, document_section_id, \*\*<a href="src/morta/types/document/section/submission_update_params.py">params</a>) -> <a href="./src/morta/types/document/section/submission_update_response.py">SubmissionUpdateResponse</a></code>
- <code title="delete /v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}">client.document.section.submission.<a href="./src/morta/resources/document/section/submission.py">delete</a>(submission_id, \*, document_id, document_section_id) -> <a href="./src/morta/types/document/section/submission_delete_response.py">SubmissionDeleteResponse</a></code>
- <code title="put /v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/reset">client.document.section.submission.<a href="./src/morta/resources/document/section/submission.py">reset</a>(submission_id, \*, document_id, document_section_id) -> <a href="./src/morta/types/document/section/submission_reset_response.py">SubmissionResetResponse</a></code>
- <code title="put /v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/submit">client.document.section.submission.<a href="./src/morta/resources/document/section/submission.py">submit</a>(submission_id, \*, document_id, document_section_id) -> <a href="./src/morta/types/document/section/submission_submit_response.py">SubmissionSubmitResponse</a></code>

# Notifications

Types:

```python
from morta.types import (
    Action,
    CreateNotificationSchemaHeader,
    Notification,
    Table1,
    Trigger,
    NotificationCreateResponse,
    NotificationUpdateResponse,
    NotificationDeleteResponse,
    NotificationListEventTypesResponse,
    NotificationListEventsResponse,
)
```

Methods:

- <code title="post /v1/notifications">client.notifications.<a href="./src/morta/resources/notifications.py">create</a>(\*\*<a href="src/morta/types/notification_create_params.py">params</a>) -> <a href="./src/morta/types/notification_create_response.py">NotificationCreateResponse</a></code>
- <code title="put /v1/notifications/{id}">client.notifications.<a href="./src/morta/resources/notifications.py">update</a>(id, \*\*<a href="src/morta/types/notification_update_params.py">params</a>) -> <a href="./src/morta/types/notification_update_response.py">NotificationUpdateResponse</a></code>
- <code title="delete /v1/notifications/{id}">client.notifications.<a href="./src/morta/resources/notifications.py">delete</a>(id) -> <a href="./src/morta/types/notification_delete_response.py">NotificationDeleteResponse</a></code>
- <code title="get /v1/notifications/event-types">client.notifications.<a href="./src/morta/resources/notifications.py">list_event_types</a>() -> <a href="./src/morta/types/notification_list_event_types_response.py">NotificationListEventTypesResponse</a></code>
- <code title="get /v1/notifications/events/{resource_id}">client.notifications.<a href="./src/morta/resources/notifications.py">list_events</a>(resource_id, \*\*<a href="src/morta/types/notification_list_events_params.py">params</a>) -> <a href="./src/morta/types/notification_list_events_response.py">NotificationListEventsResponse</a></code>

# CommentThread

Types:

```python
from morta.types import (
    CommentThread,
    CommentThreadCreateResponse,
    CommentThreadRetrieveResponse,
    CommentThreadListResponse,
    CommentThreadDeleteResponse,
    CommentThreadGetStatsResponse,
    CommentThreadReopenResponse,
    CommentThreadResolveResponse,
)
```

Methods:

- <code title="post /v1/comment_thread">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">create</a>(\*\*<a href="src/morta/types/comment_thread_create_params.py">params</a>) -> <a href="./src/morta/types/comment_thread_create_response.py">CommentThreadCreateResponse</a></code>
- <code title="get /v1/comment_thread/{comment_thread_id}">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">retrieve</a>(comment_thread_id) -> <a href="./src/morta/types/comment_thread_retrieve_response.py">CommentThreadRetrieveResponse</a></code>
- <code title="get /v1/comment_thread">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">list</a>(\*\*<a href="src/morta/types/comment_thread_list_params.py">params</a>) -> <a href="./src/morta/types/comment_thread_list_response.py">CommentThreadListResponse</a></code>
- <code title="delete /v1/comment_thread/{comment_thread_id}">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">delete</a>(comment_thread_id) -> <a href="./src/morta/types/comment_thread_delete_response.py">CommentThreadDeleteResponse</a></code>
- <code title="get /v1/comment_thread/stats">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">get_stats</a>(\*\*<a href="src/morta/types/comment_thread_get_stats_params.py">params</a>) -> <a href="./src/morta/types/comment_thread_get_stats_response.py">CommentThreadGetStatsResponse</a></code>
- <code title="put /v1/comment_thread/{comment_thread_id}/reopen">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">reopen</a>(comment_thread_id) -> <a href="./src/morta/types/comment_thread_reopen_response.py">CommentThreadReopenResponse</a></code>
- <code title="put /v1/comment_thread/{comment_thread_id}/resolve">client.comment_thread.<a href="./src/morta/resources/comment_thread/comment_thread.py">resolve</a>(comment_thread_id) -> <a href="./src/morta/types/comment_thread_resolve_response.py">CommentThreadResolveResponse</a></code>

## Comment

Types:

```python
from morta.types.comment_thread import (
    CommentModel,
    CommentCreateResponse,
    CommentUpdateResponse,
    CommentDeleteResponse,
)
```

Methods:

- <code title="post /v1/comment_thread/{comment_thread_id}/comment">client.comment_thread.comment.<a href="./src/morta/resources/comment_thread/comment.py">create</a>(comment_thread_id, \*\*<a href="src/morta/types/comment_thread/comment_create_params.py">params</a>) -> <a href="./src/morta/types/comment_thread/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="put /v1/comment_thread/{comment_thread_id}/comment/{comment_id}">client.comment_thread.comment.<a href="./src/morta/resources/comment_thread/comment.py">update</a>(comment_id, \*, comment_thread_id, \*\*<a href="src/morta/types/comment_thread/comment_update_params.py">params</a>) -> <a href="./src/morta/types/comment_thread/comment_update_response.py">CommentUpdateResponse</a></code>
- <code title="delete /v1/comment_thread/{comment_thread_id}/comment/{comment_id}">client.comment_thread.comment.<a href="./src/morta/resources/comment_thread/comment.py">delete</a>(comment_id, \*, comment_thread_id) -> <a href="./src/morta/types/comment_thread/comment_delete_response.py">CommentDeleteResponse</a></code>

# Permissions

Types:

```python
from morta.types import (
    AccessPolicy,
    CreatePermissions,
    Table3,
    PermissionCreateResponse,
    PermissionRetrieveResponse,
    PermissionUpdateResponse,
    PermissionCreateAllResponse,
    PermissionRetrieveTagResponse,
)
```

Methods:

- <code title="post /v1/permissions">client.permissions.<a href="./src/morta/resources/permissions.py">create</a>(\*\*<a href="src/morta/types/permission_create_params.py">params</a>) -> <a href="./src/morta/types/permission_create_response.py">PermissionCreateResponse</a></code>
- <code title="get /v1/permissions">client.permissions.<a href="./src/morta/resources/permissions.py">retrieve</a>(\*\*<a href="src/morta/types/permission_retrieve_params.py">params</a>) -> <a href="./src/morta/types/permission_retrieve_response.py">PermissionRetrieveResponse</a></code>
- <code title="put /v1/permissions/{id}">client.permissions.<a href="./src/morta/resources/permissions.py">update</a>(id, \*\*<a href="src/morta/types/permission_update_params.py">params</a>) -> <a href="./src/morta/types/permission_update_response.py">PermissionUpdateResponse</a></code>
- <code title="delete /v1/permissions/{id}">client.permissions.<a href="./src/morta/resources/permissions.py">delete</a>(id) -> None</code>
- <code title="put /v1/permissions/all">client.permissions.<a href="./src/morta/resources/permissions.py">create_all</a>(\*\*<a href="src/morta/types/permission_create_all_params.py">params</a>) -> <a href="./src/morta/types/permission_create_all_response.py">PermissionCreateAllResponse</a></code>
- <code title="get /v1/permissions/request/{hub_id}/{type}/{id}">client.permissions.<a href="./src/morta/resources/permissions.py">request</a>(id, \*, hub_id, type) -> None</code>
- <code title="get /v1/permissions/tag">client.permissions.<a href="./src/morta/resources/permissions.py">retrieve_tag</a>(\*\*<a href="src/morta/types/permission_retrieve_tag_params.py">params</a>) -> <a href="./src/morta/types/permission_retrieve_tag_response.py">PermissionRetrieveTagResponse</a></code>

# Integrations

Types:

```python
from morta.types import PassthroughAPICall, IntegrationCreatePassthroughResponse
```

Methods:

- <code title="post /v1/integrations/passthrough">client.integrations.<a href="./src/morta/resources/integrations/integrations.py">create_passthrough</a>(\*\*<a href="src/morta/types/integration_create_passthrough_params.py">params</a>) -> <a href="./src/morta/types/integration_create_passthrough_response.py">IntegrationCreatePassthroughResponse</a></code>
- <code title="post /v1/integrations/passthrough-download">client.integrations.<a href="./src/morta/resources/integrations/integrations.py">create_passthrough_download</a>(\*\*<a href="src/morta/types/integration_create_passthrough_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/integrations/{integration_name}/save-api-key">client.integrations.<a href="./src/morta/resources/integrations/integrations.py">save_api_key</a>(integration_name) -> None</code>

## Fields

Methods:

- <code title="get /v1/integrations/{provider}/fields/{field_key}/options">client.integrations.fields.<a href="./src/morta/resources/integrations/fields.py">retrieve_options</a>(field_key, \*, provider) -> None</code>

# AI

## Chat

Types:

```python
from morta.types.ai import ChatCreateResponse
```

Methods:

- <code title="post /v1/ai/chat">client.ai.chat.<a href="./src/morta/resources/ai/chat/chat.py">create</a>(\*\*<a href="src/morta/types/ai/chat_create_params.py">params</a>) -> str</code>

### Conversations

Methods:

- <code title="get /v1/ai/chat/conversations/{conversation_id}">client.ai.chat.conversations.<a href="./src/morta/resources/ai/chat/conversations.py">retrieve</a>(conversation_id) -> None</code>
- <code title="get /v1/ai/chat/conversations">client.ai.chat.conversations.<a href="./src/morta/resources/ai/chat/conversations.py">list</a>(\*\*<a href="src/morta/types/ai/chat/conversation_list_params.py">params</a>) -> None</code>

# Organisation

Types:

```python
from morta.types import (
    CreateOrganisationUser,
    Organisation,
    OrganisationRetrieveHubsResponse,
    OrganisationRetrieveSitesResponse,
)
```

Methods:

- <code title="get /v1/organisation/{organisation_public_id}">client.organisation.<a href="./src/morta/resources/organisation/organisation.py">retrieve</a>(organisation_public_id) -> <a href="./src/morta/types/organisation/organisation.py">Organisation</a></code>
- <code title="put /v1/organisation/{organisation_public_id}">client.organisation.<a href="./src/morta/resources/organisation/organisation.py">update</a>(organisation_public_id, \*\*<a href="src/morta/types/organisation_update_params.py">params</a>) -> <a href="./src/morta/types/organisation/organisation.py">Organisation</a></code>
- <code title="get /v1/organisation/{organisation_public_id}/hubs">client.organisation.<a href="./src/morta/resources/organisation/organisation.py">retrieve_hubs</a>(organisation_public_id) -> <a href="./src/morta/types/organisation_retrieve_hubs_response.py">OrganisationRetrieveHubsResponse</a></code>
- <code title="get /v1/organisation/{organisation_public_id}/sites">client.organisation.<a href="./src/morta/resources/organisation/organisation.py">retrieve_sites</a>(organisation_public_id) -> <a href="./src/morta/types/organisation_retrieve_sites_response.py">OrganisationRetrieveSitesResponse</a></code>

## APIKey

Types:

```python
from morta.types.organisation import CreateAPIKey, UpdateAPIKey, APIKeyRetrieveAPIKeyResponse
```

Methods:

- <code title="put /v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}">client.organisation.api_key.<a href="./src/morta/resources/organisation/api_key.py">update</a>(api_key_public_id, \*, organisation_public_id, \*\*<a href="src/morta/types/organisation/api_key_update_params.py">params</a>) -> <a href="./src/morta/types/user/api_key.py">APIKey</a></code>
- <code title="delete /v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}">client.organisation.api_key.<a href="./src/morta/resources/organisation/api_key.py">delete</a>(api_key_public_id, \*, organisation_public_id) -> None</code>
- <code title="post /v1/organisation/{organisation_public_id}/api-key">client.organisation.api_key.<a href="./src/morta/resources/organisation/api_key.py">api_key</a>(organisation_public_id, \*\*<a href="src/morta/types/organisation/api_key_api_key_params.py">params</a>) -> <a href="./src/morta/types/user/api_key.py">APIKey</a></code>
- <code title="get /v1/organisation/{organisation_public_id}/api-key">client.organisation.api_key.<a href="./src/morta/resources/organisation/api_key.py">retrieve_api_key</a>(organisation_public_id) -> <a href="./src/morta/types/organisation/api_key_retrieve_api_key_response.py">APIKeyRetrieveAPIKeyResponse</a></code>

## Site

Types:

```python
from morta.types.organisation import Site, UserToSite
```

Methods:

- <code title="post /v1/organisation/{organisation_public_id}/site">client.organisation.site.<a href="./src/morta/resources/organisation/site.py">create</a>(organisation_public_id, \*\*<a href="src/morta/types/organisation/site_create_params.py">params</a>) -> <a href="./src/morta/types/organisation/site.py">Site</a></code>
- <code title="get /v1/organisation/{organisation_public_id}/site/{site_public_id}">client.organisation.site.<a href="./src/morta/resources/organisation/site.py">retrieve</a>(site_public_id, \*, organisation_public_id) -> <a href="./src/morta/types/organisation/site.py">Site</a></code>
- <code title="put /v1/organisation/{organisation_public_id}/site/{site_public_id}">client.organisation.site.<a href="./src/morta/resources/organisation/site.py">update</a>(site_public_id, \*, organisation_public_id, \*\*<a href="src/morta/types/organisation/site_update_params.py">params</a>) -> <a href="./src/morta/types/organisation/site.py">Site</a></code>
- <code title="delete /v1/organisation/{organisation_public_id}/site/{site_public_id}">client.organisation.site.<a href="./src/morta/resources/organisation/site.py">delete</a>(site_public_id, \*, organisation_public_id) -> None</code>

## Teams

Methods:

- <code title="post /v1/organisation/{organisation_public_id}/teams">client.organisation.teams.<a href="./src/morta/resources/organisation/teams.py">create</a>(organisation_public_id) -> None</code>
- <code title="get /v1/organisation/{organisation_public_id}/teams/{team_public_id}">client.organisation.teams.<a href="./src/morta/resources/organisation/teams.py">retrieve</a>(team_public_id, \*, organisation_public_id) -> None</code>
- <code title="put /v1/organisation/{organisation_public_id}/teams/{team_public_id}">client.organisation.teams.<a href="./src/morta/resources/organisation/teams.py">update</a>(team_public_id, \*, organisation_public_id) -> None</code>
- <code title="get /v1/organisation/{organisation_public_id}/teams">client.organisation.teams.<a href="./src/morta/resources/organisation/teams.py">list</a>(organisation_public_id) -> None</code>
- <code title="delete /v1/organisation/{organisation_public_id}/teams/{team_public_id}">client.organisation.teams.<a href="./src/morta/resources/organisation/teams.py">delete</a>(team_public_id, \*, organisation_public_id) -> None</code>

## User

Methods:

- <code title="delete /v1/organisation/{organisation_public_id}/user/{user_public_id}">client.organisation.user.<a href="./src/morta/resources/organisation/user.py">delete</a>(user_public_id, \*, organisation_public_id) -> None</code>
- <code title="post /v1/organisation/{organisation_public_id}/user/{user_public_id}/allocate-license">client.organisation.user.<a href="./src/morta/resources/organisation/user.py">allocate_license</a>(user_public_id, \*, organisation_public_id) -> None</code>
- <code title="post /v1/organisation/{organisation_public_id}/user/{user_public_id}/remove-license">client.organisation.user.<a href="./src/morta/resources/organisation/user.py">remove_license</a>(user_public_id, \*, organisation_public_id) -> None</code>

# Teams

## Seats

Methods:

- <code title="get /v1/teams/{team_public_id}/seats">client.teams.seats.<a href="./src/morta/resources/teams/seats.py">list</a>(team_public_id) -> None</code>
- <code title="post /v1/teams/{team_public_id}/seats/assign">client.teams.seats.<a href="./src/morta/resources/teams/seats.py">assign</a>(team_public_id) -> None</code>
- <code title="post /v1/teams/{team_public_id}/seats/revoke">client.teams.seats.<a href="./src/morta/resources/teams/seats.py">revoke</a>(team_public_id) -> None</code>
