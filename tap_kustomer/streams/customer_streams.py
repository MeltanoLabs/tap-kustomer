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

    name = "customers"
    path = "customers/search"
    rest_method = "POST"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$[data][*]"
    schema_filepath = SCHEMAS_DIR / "customer.json"

    max_observed_timestamp = None
    max_timestamp = None
    updated_at = "customer_updated_at"
    query_context = "customer"
