
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "conversation"

# Streams to export
__all__ = [
    "ConversationAssignedTeamHistoryStream",
	"ConversationAssignedUserHistoryStream",
	"ConversationChannelHistoryStream",
	"ConversationHistoryStream"
]

    
class ConversationAssignedTeamHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_assigned_team_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_assigned_team_history.json"


class ConversationAssignedUserHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_assigned_user_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_assigned_user_history.json"


class ConversationChannelHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_channel_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_channel_history.json"


class ConversationHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_history.json"

