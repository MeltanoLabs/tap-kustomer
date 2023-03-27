"""kustomer tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_kustomer.streams import *
from tap_kustomer.client import kustomerStream

# All streams to be included in the tap
STREAM_TYPES = [
    # access_management
    AuthCustomerSettingsStream,
    AuthRolesStream,
    AuthSettingsStream,
    AuthTokensCurrentStream,
    AuthTokensStream,
    PAuthSettingsStream,
    RoleGroupsStream,
    TeamsStream,
    UsersCurrentStream,
    UsersStream,
    # apps_platform
    AppsAvailableStream,
    AppsStream,
    CardsStream,
    HooksEmailStream,
    HooksFormStream,
    HooksWebStream,
    KviewsStream,
    OutboundWebhooksStream,
    OutboundWebhooksTransactionsStream,
    # core_resources
    AuditLogsStream,
    BrandsDefaultStream,
    BrandsStream,
    CompaniesStream,
    ConversationsStream,
    CustomersStream,
    KlassesStream,
    MessagesStream,
    NotesStream,
    OutboundAccountsStream,
    SatisfactionStream,
    SchedulesDefaultStream,
    SchedulesStream,
    SlasStream,
    SpamSendersStream,
    # knowledge_base
    PV3KbArticlesSearchStream,
    PV3KbArticlesStream,
    PV3KbCategoriesStream,
    V1KbArticlesSearchStream,
    V1KbArticlesStream,
    V1KbCategoriesStream,
    V1KbFormsStream,
    V1KbInternalCategoriesStream,
    V1KbRouteStream,
    V1KbRoutesStream,
    V3KbTagsStream,
    V3KbTemplatesStream,
    V3KbThemesActiveStream,
    V3KbThemesStream,
    # queues_and_routing
    RoutingQueueRulesCriteriaStream,
    RoutingQueueRulesStream,
    RoutingQueuesStream,
    RoutingSettingsStream,
    RoutingStatusesStream,
    RoutingUsersCurrentSettingsStream,
    RoutingWorkItemsStream,
    RoutingWorkSessionsCurrentStream,
    RoutingWorkSessionsCurrentWorkItemsStream,
    RoutingWorkSessionsStream,
    # settings_and_configurations
    ChatSettingsStream,
    CustomersSearchesPinnedStream,
    CustomersSearchesPositionsStream,
    CustomersSearchesSchemaStream,
    CustomersSearchesStream,
    NotificationsLogsSettingsStream,
    NotificationsStream,
    NotificationsUsersCurrentSettingsStream,
    SettingsStream,
    ShortcutsCategoriesStream,
    ShortcutsStream,
    SnippetsStream,
    SnoozesStream,
    UsersCurrentSettingsStream,
    # workflows
    WorkflowsStream,
]


class Tapkustomer(Tap):
    """kustomer tap class."""

    name = "tap-kustomer"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The API KEY to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "prod_point",
            th.IntegerType,
            default=1,
            description="The production point of deployment for your organization instance. 1 (US) or 2 (EU).",
        ),
    ).to_dict()

    def discover_streams(self) -> list[kustomerStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [stream_type(self) for stream_type in STREAM_TYPES]


if __name__ == "__main__":
    Tapkustomer.cli()
