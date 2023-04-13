from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    "KObjectStream"
]

class KObjectStream(CustomerSearchStream):
    """
    TODO
    """

    name = "kobjects"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "kobject_updated_at"
    query_context = "kobject"

    schema = th.PropertiesList(
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("updated_at", th.DateTimeType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("externalId", th.StringType, description=""),
                th.Property("title", th.StringType, description=""),
                th.Property("description", th.StringType, description=""),
                th.Property("icon", th.StringType, description=""),
                th.Property("images", th.ArrayType(th.StringType), description=""),
                th.Property("tags", th.ArrayType(th.StringType), description=""),
                th.Property("updatedAt", th.DateTimeType, description=""),
                th.Property("createdAt", th.DateTimeType, description=""),
                th.Property("roleGroupVersions", th.ArrayType(th.StringType), description=""),
        ))).to_dict()
