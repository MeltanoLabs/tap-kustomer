from tap_kustomer.streams.access_management import (
	AuthRolesStream,
	RoleGroupsStream,
	TeamsStream,
	UsersStream,
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
	CompaniesStream,
	ConversationsStream,
	CustomersStream,
	KlassesStream,
	MessagesStream,
	NotesStream,
	SatisfactionStream,
	SchedulesStream,
	SlasStream,
	SpamSendersStream,
)

from tap_kustomer.streams.knowledge_base import (
	KbArticlesStream,
	KbCategoriesStream,
	KbFormsStream,
	KbInternalCategoriesStream,
	KbRoutesStream,
	KbTagsStream,
	KbTemplatesStream,
	KbThemesStream,
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
)

from tap_kustomer.streams.settings_and_configurations import (
	CustomersSearchesStream,
	CustomersSearchesPinnedStream,
	CustomersSearchesPositionsStream,
	CustomersSearchesSchemaStream,
	NotificationsStream,
	NotificationsLogsSettingsStream,
	SettingsStream,
	ShortcutsStream,
	ShortcutsCategoriesStream,
	SnippetsStream,
	SnoozesStream,
)

from tap_kustomer.streams.workflows import (
	WorkflowsStream,
)

