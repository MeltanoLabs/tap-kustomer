from __future__ import annotations

from tap_kustomer.client import kustomerStream

from singer_sdk import typing as th  # JSON Schema typing helpers

__all__ = [
    "NoteStream",
]

class NoteStream(kustomerStream):
    """
    TODO
    """

    name = "notes"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "note_updated_at"
    query_context = "note"

    schema = th.PropertiesList(
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("updated_at", th.DateTimeType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("body", th.StringType, description=""),
                th.Property("createdAt", th.StringType, description=""),
                th.Property("updatedAt", th.StringType, description=""),
                th.Property("modifiedAt", th.StringType, description=""),
                th.Property("createdByTeams", th.ArrayType(th.StringType), description=""),
        ))).to_dict()
