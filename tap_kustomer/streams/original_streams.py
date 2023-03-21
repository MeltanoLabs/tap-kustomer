"""Stream type classes for tap-kustomer."""

from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream


SCHEMAS_DIR = Path(__file__).parent / "schemas"

# Streams to export
__all__ = [
    "ConversationsStream",
    "CustomersStream",
    # "KobjectsStream",
    "MessagesStream",
    "NotesStream",
    "ShortcutsStream",
    "TagsStream",
    "TeamsStream",
    "UsersStream",
]


class ConversationsStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getconversations

    Retrieves a list of conversations for the organization.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "conversations"
    path = "/v1/conversations"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "conversations.json"


class CustomersStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getcustomers

    Retrieves all customers in your organization. Results include customer data,
    such as their phone number, sentiment score, and the last message in a conversation.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "customers"
    path = "/v1/customers"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "customers.json"


# class KobjectsStream(kustomerStream):
#     """
#     TODO: Identify where this comes from as the original end point doesn't appear to exist now
#     https://github.com/singer-io/tap-kustomer/blob/master/tap_kustomer/streams.py#L39
#     """

#     name = "kobjects"
#     path = "/v1/TODO"
#     primary_keys = ["id"]
#     replication_key = "attributes.modifiedAt"
#     schema_filepath = SCHEMAS_DIR / "kobjects.json"


class MessagesStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getmessages

    Retrieves messages for your Kustomer organization.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "messages"
    path = "/v1/messages"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "messages.json"


class NotesStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getnotesfororg

    Retrieves all notes for a Kustomer organization.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "notes"
    path = "/v1/notes"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "notes.json"


class ShortcutsStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getallshortcuts

    Retrieves all shortcuts.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "shortcuts"
    path = "/v1/shortcuts"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "shortcuts.json"


class TagsStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/gettags

    Returns all Knowledge Base article tags.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "tags"
    path = "/v1/tags"  # TODO - This has now been updated to v3/kb/tags
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "tags.json"


class TeamsStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getteams

    Gets Teams for the Organization

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "teams"
    path = "/v1/teams"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "teams.json"


class UsersStream(kustomerStream):
    """
    https://developer.kustomer.com/kustomer-api-docs/reference/getusers

    Retrieves users within the organization.

    TODO: Check the schema is still correct from the original singer tap
    """

    name = "users"
    path = "/v1/users"
    primary_keys = ["id"]
    replication_key = "attributes.modifiedAt"
    schema_filepath = SCHEMAS_DIR / "users.json"
