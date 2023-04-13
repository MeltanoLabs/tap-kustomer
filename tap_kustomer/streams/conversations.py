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
    schema_filepath = SCHEMAS_DIR / "conversations.json"
    updated_at = "conversation_updated_at"
    query_context = "conversation"