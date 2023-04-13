from __future__ import annotations

from tap_kustomer.client import CustomerSearchStream

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    "KObjectsStream"
]

class KObjectsStream(CustomerSearchStream):
    """
    TODO
    """

    name = "kobjects"
    schema_filepath = SCHEMAS_DIR / "kobjects.json"
    updated_at = "kobject_updated_at"
    query_context = "kobject"
