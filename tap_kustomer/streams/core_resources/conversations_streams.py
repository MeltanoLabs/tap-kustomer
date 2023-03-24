from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas"

# Streams to export
__all__ = ["ConversationsStream"]

    
class ConversationsStream(kustomerStream):
    """
    Get conversations
    """

    name = "conversations"
    path = "conversations"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema_filepath = SCHEMAS_DIR / "conversations.json"

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        """Extract the updatedAt timestamp for the replication key"""
        row["updatedAt"] = row["attributes"].pop("updatedAt")
        return super().post_process(row, context)

