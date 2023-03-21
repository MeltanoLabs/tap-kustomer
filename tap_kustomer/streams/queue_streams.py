
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "queue"

# Streams to export
__all__ = [
    "QueueStream",
	"TeamQueueStream"
]

    
class QueueStream(kustomerStream):
    """
    TODO
    """

    name = "queue"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "queue.json"


class TeamQueueStream(kustomerStream):
    """
    TODO
    """

    name = "team_queue"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "team_queue.json"

