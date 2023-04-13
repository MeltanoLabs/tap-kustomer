from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

__all__ = [
    "ConversationsStream"
]

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class ConversationsStream(CustomerSearchStream):
    """
    TODO
    """

    name = "conversations"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"
    schema_filepath = SCHEMAS_DIR / "conversations.json"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "conversation_updated_at"
    query_context = "conversation"