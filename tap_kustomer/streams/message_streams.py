
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "message"

# Streams to export
__all__ = [
    "MessagesStream",
	"MessageAssignedTeamStream",
	"MessageAssignedUserStream",
	"MessageAttachmentStream",
	"MessageCreatedByTeamStream",
	"MessageShortcutStream"
]

    
class MessagesStream(kustomerStream):
    """
    TODO
    """

    name = "messages"
    path = "messages"
    primary_keys = []
    replication_key = "id"
    records_jsonpath = "$[data][*]"

    schema = th.PropertiesList(
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("externalId", th.StringType, description=""),
                th.Property("channel", th.StringType, description=""),
                th.Property("app", th.StringType, description=""),
                th.Property("size", th.NumberType, description=""),
                th.Property("direction", th.StringType, description=""),
                th.Property("preview", th.StringType, description=""),
                # th.Property("sentiment", th.ObjectType(th.StringType), description=""),
        ))).to_dict()

class MessageAssignedTeamStream(kustomerStream):
    """
    TODO
    """

    name = "message_assigned_team"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message_assigned_team.json"


class MessageAssignedUserStream(kustomerStream):
    """
    TODO
    """

    name = "message_assigned_user"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message_assigned_user.json"


class MessageAttachmentStream(kustomerStream):
    """
    TODO
    """

    name = "message_attachment"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message_attachment.json"


class MessageCreatedByTeamStream(kustomerStream):
    """
    TODO
    """

    name = "message_created_by_team"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message_created_by_team.json"


class MessageShortcutStream(kustomerStream):
    """
    TODO
    """

    name = "message_shortcut"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message_shortcut.json"

