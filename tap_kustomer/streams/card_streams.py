
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "card"

# Streams to export
__all__ = [
    "CardStream",
	"CardContextStream"
]

    
class CardStream(kustomerStream):
    """
    TODO
    """

    name = "card"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "card.json"


class CardContextStream(kustomerStream):
    """
    TODO
    """

    name = "card_context"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "card_context.json"

