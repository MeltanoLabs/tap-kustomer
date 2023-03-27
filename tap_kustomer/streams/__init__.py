from tap_kustomer.streams.access_management import (
	AuthCustomerSettingsStream,
	AuthRolesStream,
	AuthSettingsStream,
	AuthTokensStream,
	AuthTokensCurrentStream,
	RoleGroupsStream,
	TeamsStream,
	UsersStream,
	UsersCurrentStream,
)

from tap_kustomer.streams.apps_platform import (
	AppsStream,
	AppsAvailableStream,
	CardsStream,
	HooksEmailStream,
	HooksFormStream,
	HooksWebStream,
	KviewsStream,
	OutboundWebhooksStream,
	OutboundWebhooksTransactionsStream,
)

from tap_kustomer.streams.core_resources import (
	AuditLogsStream,
	BrandsStream,
	BrandsDefaultStream,
	CompaniesStream,
	ConversationsStream,
	CustomersStream,
	KlassesStream,
	MessagesStream,
	NotesStream,
	OutboundAccountsStream,
	SatisfactionStream,
	SchedulesStream,
	SchedulesDefaultStream,
	SlasStream,
	SpamSendersStream,
)

from tap_kustomer.streams.knowledge_base import (
	KbArticlesStream,
	KbArticlesSearchStream,
	KbCategoriesStream,
	KbFormsStream,
	KbInternalCategoriesStream,
	KbRouteStream,
	KbRoutesStream,
	KbTagsStream,
	KbTemplatesStream,
	KbThemesStream,
	KbThemesActiveStream,
)

from tap_kustomer.streams.queues_and_routing import (
	RoutingQueueRulesStream,
	RoutingQueueRulesCriteriaStream,
	RoutingQueuesStream,
	RoutingSettingsStream,
	RoutingStatusesStream,
	RoutingUsersCurrentSettingsStream,
	RoutingWorkItemsStream,
	RoutingWorkSessionsStream,
	RoutingWorkSessionsCurrentStream,
	RoutingWorkSessionsCurrentWorkItemsStream,
)

from tap_kustomer.streams.settings_and_configurations import (
	ChatSettingsStream,
	CustomersSearchesStream,
	CustomersSearchesPinnedStream,
	CustomersSearchesPositionsStream,
	CustomersSearchesSchemaStream,
	NotificationsStream,
	NotificationsLogsSettingsStream,
	NotificationsUsersCurrentSettingsStream,
	SettingsStream,
	ShortcutsStream,
	ShortcutsCategoriesStream,
	SnippetsStream,
	SnoozesStream,
	UsersCurrentSettingsStream,
)

from tap_kustomer.streams.workflows import (
	WorkflowsStream,
)

