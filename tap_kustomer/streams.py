
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import CustomerSearchStream, KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    "CompaniesStream",
    "ConversationsStream"
    "CustomersStream",
    "KObjectsStream",
    "MessagesStream",
    "NotesStream",
    "ShortcutsStream",
    "SlaStream",
    "SlaVersionStream",
    "TagsStream",
    "TeamsStream",
    "UsersStream"
]

class CompaniesStream(CustomerSearchStream):

    name = "companies"
    updated_at = "company_updated_at"
    query_context = "company"
    schema_filepath = SCHEMAS_DIR / "companies.json"


class ConversationsStream(CustomerSearchStream):
    
    name = "conversations"
    schema_filepath = SCHEMAS_DIR / "conversations.json"
    updated_at = "conversation_updated_at"
    query_context = "conversation"


class CustomersStream(CustomerSearchStream):

    name = "customers"
    schema_filepath = SCHEMAS_DIR / "customers.json"
    updated_at = "customer_updated_at"
    query_context = "customer"


class KObjectsStream(CustomerSearchStream):

    name = "kobjects"
    schema_filepath = SCHEMAS_DIR / "kobjects.json"
    updated_at = "kobject_updated_at"
    query_context = "kobject"

class MessagesStream(CustomerSearchStream):

    name = "messages"
    schema_filepath = SCHEMAS_DIR / "messages.json"
    updated_at = "message_updated_at"
    query_context = "message"

class NotesStream(CustomerSearchStream):

    name = "notes"
    schema_filepath = SCHEMAS_DIR / "notes.json"
    updated_at = "note_updated_at"
    query_context = "note"

class ShortcutsStream(KustomerStream):

    name = "shortcuts"
    path = "shortcuts"
    schema_filepath = SCHEMAS_DIR / "shortcuts.json"


class SlaStream(KustomerStream):
    name = "slas"
    path = "slas"
    schema_filepath = SCHEMAS_DIR / "slas.json"
    replication_key = None

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        return row


class SlaVersionStream(KustomerStream):
    name = "sla_versions"
    path = "slas"
    schema_filepath = SCHEMAS_DIR / "sla_versions.json"
    replication_key = None

    # Need to get the versions
    records_jsonpath = "$[included][*]"

    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params = super().get_url_params(context, next_page_token)
        params["versions"] = "all"

        return params

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        return row

    name = "tags"
    path = "tags"
    schema_filepath = SCHEMAS_DIR / "tags.json"


class TeamsStream(KustomerStream):

    name = "teams"
    path = "teams"
    schema_filepath = SCHEMAS_DIR / "teams.json"


class UsersStream(KustomerStream):

    name = "users"
    path = "users"
    schema_filepath = SCHEMAS_DIR / "users.json"
