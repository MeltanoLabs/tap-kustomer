from __future__ import annotations
from typing import Optional, Any

from pathlib import Path

from tap_kustomer.client import CustomerSearchStream, KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    # Parent streams
    "CompaniesStream",
    "ConversationsStream",
    "CustomersStream",
    "KObjectsStream",
    "MessagesStream",
    "NotesStream",
    "ShortcutsStream",
    "TagsStream",
    "TeamsStream",
    "UsersStream",
    # Child streams
    "AttachmentsChildStream",
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

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "id": record["id"],
        }


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


class TagsStream(KustomerStream):


class TagsStream(KustomerStream):
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


# Child streams


class AttachmentsChildStream(KustomerStream):
    name = "attachments"
    path = "conversations/{id}/attachments"
    schema_filepath = SCHEMAS_DIR / "attachments.json"
    replication_key = None

    parent_stream_type = ConversationsStream

    # Assume attachments don't have `updated_at` incremented when attachments are changed
    ignore_parent_replication_keys = True

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        return row
