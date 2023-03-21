
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "team"

# Streams to export
__all__ = [
    "TeamStream",
	"TeamMemberStream"
]

    
class TeamStream(kustomerStream):
    """
    TODO
    """

    name = "team"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "team.json"


class TeamMemberStream(kustomerStream):
    """
    TODO
    """

    name = "team_member"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "team_member.json"

