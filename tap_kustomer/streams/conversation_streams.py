from __future__ import annotations

from tap_kustomer.client import kustomerStream

from singer_sdk import typing as th  # JSON Schema typing helpers

__all__ = [
    "ConversationsStream",
]

class ConversationsStream(kustomerStream):
    """
    TODO
    """

    name = "conversations"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "conversation_updated_at"
    query_context = "conversation"

    schema = th.PropertiesList(
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("updated_at", th.DateTimeType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("name", th.StringType, description=""),
                th.Property("preview", th.StringType, description=""),
                th.Property("channels", th.ArrayType(th.StringType), description=""),
        th.Property("status", th.StringType, description=""),
        ))).to_dict()
