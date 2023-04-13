from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# Streams to export
__all__ = [
    "MessagesStream"
]

    
class MessagesStream(CustomerSearchStream):
    """
    TODO
    """

    name = "messages"
    schema_filepath = SCHEMAS_DIR / "messages.json"
    updated_at = "message_updated_at"
    query_context = "message"
