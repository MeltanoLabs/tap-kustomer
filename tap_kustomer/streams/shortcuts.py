
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# Streams to export
__all__ = [
    "ShortcutsStream"
]

    
class ShortcutsStream(KustomerStream):
    """
    TODO
    """

    name = "shortcut"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcuts.json"

