
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "shortcut"

# Streams to export
__all__ = [
    "ShortcutStream",
	"ShortcutAssignedTeamsStream",
	"ShortcutAssignedUsersStream",
	"ShortcutChannelStream"
]

    
class ShortcutStream(kustomerStream):
    """
    TODO
    """

    name = "shortcut"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcut.json"


class ShortcutAssignedTeamsStream(kustomerStream):
    """
    TODO
    """

    name = "shortcut_assigned_teams"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcut_assigned_teams.json"


class ShortcutAssignedUsersStream(kustomerStream):
    """
    TODO
    """

    name = "shortcut_assigned_users"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcut_assigned_users.json"


class ShortcutChannelStream(kustomerStream):
    """
    TODO
    """

    name = "shortcut_channel"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcut_channel.json"

