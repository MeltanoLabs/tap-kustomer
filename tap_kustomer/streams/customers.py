from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


__all__ = [
    "CustomersStream"
]

class CustomersStream(CustomerSearchStream):
    """
    TODO
    """

    name = "customers"
    schema_filepath = SCHEMAS_DIR / "customers.json"
    updated_at = "customer_updated_at"
    query_context = "customer"
