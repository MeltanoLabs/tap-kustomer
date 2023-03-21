
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "note"

# Streams to export
__all__ = [
    "NoteStream",
	"NoteTeamMentionStream",
	"NoteUserMentionStream"
]

    
class NoteStream(kustomerStream):
    """
    TODO
    """

    name = "note"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "note.json"


class NoteTeamMentionStream(kustomerStream):
    """
    TODO
    """

    name = "note_team_mention"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "note_team_mention.json"


class NoteUserMentionStream(kustomerStream):
    """
    TODO
    """

    name = "note_user_mention"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "note_user_mention.json"

