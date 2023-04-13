
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
    "TagsStream",
    "TeamsStream",
    "UsersStream"
]

class CompaniesStream(CustomerSearchStream):
    """
    TODO
    """
    name = "companies"
    updated_at = "company_updated_at"
    query_context = "company"
    schema_filepath = SCHEMAS_DIR / "companies.json"


class ConversationsStream(CustomerSearchStream):
    """
    TODO
    """
    
    name = "conversations"
    schema_filepath = SCHEMAS_DIR / "conversations.json"
    updated_at = "conversation_updated_at"
    query_context = "conversation"


class CustomersStream(CustomerSearchStream):
    """
    TODO
    """

    name = "customers"
    schema_filepath = SCHEMAS_DIR / "customers.json"
    updated_at = "customer_updated_at"
    query_context = "customer"


class KObjectsStream(CustomerSearchStream):
    """
    TODO
    """

    name = "kobjects"
    schema_filepath = SCHEMAS_DIR / "kobjects.json"
    updated_at = "kobject_updated_at"
    query_context = "kobject"

class MessagesStream(CustomerSearchStream):
    """
    TODO
    """

    name = "messages"
    schema_filepath = SCHEMAS_DIR / "messages.json"
    updated_at = "message_updated_at"
    query_context = "message"

class NotesStream(CustomerSearchStream):
    """
    TODO
    """

    name = "notes"
    schema_filepath = SCHEMAS_DIR / "notes.json"
    updated_at = "note_updated_at"
    query_context = "note"

class ShortcutsStream(KustomerStream):
    """
    TODO
    """

    name = "shortcut"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcuts.json"


class TagsStream(KustomerStream):
    """
    TODO
    """

    name = "tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "tags.json"


class TeamsStream(KustomerStream):
    """
    TODO
    """

    name = "team"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "teams.json"


class UsersStream(KustomerStream):
    """
    TODO
    """

    name = "users"
    path = "users"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "users.json"
