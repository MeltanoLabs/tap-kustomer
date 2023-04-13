from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    "NotesStream"
]

class NotesStream(CustomerSearchStream):
    """
    TODO
    """

    name = "notes"
    schema_filepath = SCHEMAS_DIR / "notes.json"
    updated_at = "note_updated_at"
    query_context = "note"
