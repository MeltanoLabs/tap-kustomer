from __future__ import annotations

from tap_kustomer.client import kustomerStream

from singer_sdk import typing as th  # JSON Schema typing helpers

# Streams to export
__all__ = [
    "MessagesStream"
]

    
class MessagesStream(kustomerStream):
    """
    TODO
    """

    name = "messages"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "message_updated_at"
    query_context = "message"

    schema = th.PropertiesList(
        th.Property("updated_at", th.DateTimeType, description=""),
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("externalId", th.StringType, description=""),
                th.Property("channel", th.StringType, description=""),
                th.Property("app", th.StringType, description=""),
                th.Property("size", th.NumberType, description=""),
                th.Property("direction", th.StringType, description=""),
                th.Property("preview", th.StringType, description=""),
                th.Property("status", th.StringType, description=""),
                th.Property("assignedTeams", th.ArrayType(th.StringType), description=""),
        ))).to_dict()
