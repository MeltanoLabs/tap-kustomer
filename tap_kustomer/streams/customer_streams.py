from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


__all__ = [
    "CustomerStream"
]

class CustomerStream(CustomerSearchStream):
    """
    TODO
    """

    name = "customer"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "customer_updated_at"
    query_context = "customer"

    schema = th.PropertiesList(
        th.Property("type", th.StringType, description=""),
        th.Property("id", th.StringType, description=""),
        th.Property("updated_at", th.DateTimeType, description=""),
        th.Property("attributes", 
            th.ObjectType(
                th.Property("name", th.StringType, description=""),
                th.Property("displayName", th.StringType, description=""),
                th.Property("displayColor", th.StringType, description=""),
                th.Property("displayIcon", th.StringType, description=""),
                th.Property("externalIds", th.ArrayType(th.StringType), description=""),
                th.Property("sharedExternalIds", th.ArrayType(th.StringType), description=""),
                th.Property("emails", th.ArrayType(
                    th.ObjectType(
                        th.Property("type", th.StringType, description=""),
                        th.Property("verified", th.BooleanType, description=""),
                        th.Property("externalVerified", th.BooleanType, description=""),
                        th.Property("email", th.StringType, description=""),
                    )
                ), description=""),
                th.Property("updatedAt", th.DateTimeType, description=""),
                th.Property("createdAt", th.DateTimeType, description=""),
                th.Property("modifiedAt", th.DateTimeType, description=""),
        ))).to_dict()
