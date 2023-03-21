
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "user"

# Streams to export
__all__ = [
    "NotificationStream",
	"SnoozeStream",
	"UserStream",
	"UserRoleStream"
]

    
class NotificationStream(kustomerStream):
    """
    TODO
    """

    name = "notification"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "notification.json"


class SnoozeStream(kustomerStream):
    """
    TODO
    """

    name = "snooze"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "snooze.json"


class UserStream(kustomerStream):
    """
    TODO
    """

    name = "user"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "user.json"


class UserRoleStream(kustomerStream):
    """
    TODO
    """

    name = "user_role"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "user_role.json"

