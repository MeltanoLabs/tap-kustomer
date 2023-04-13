
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import CustomerSearchStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# Streams to export
__all__ = [
    "CompanyStream"
]

    
class CompanyStream(CustomerSearchStream):
    """
    TODO
    """

    name = "company"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company.json"
