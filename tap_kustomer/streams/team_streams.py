
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    "TeamStream"
]

    
class TeamStream(KustomerStream):
    """
    TODO
    """

    name = "team"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "team.json"
