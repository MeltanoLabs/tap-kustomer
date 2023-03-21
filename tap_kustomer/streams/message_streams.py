
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "message"

# Streams to export
__all__ = [
    "MessageStream",
	"MessageAssignedTeamStream",
	"MessageAssignedUserStream",
	"MessageAttachmentStream",
	"MessageCreatedByTeamStream",
	"MessageShortcutStream"
]

    
class MessageStream(kustomerStream):
    """
    TODO
    """

    name = "message"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "message.json"


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

