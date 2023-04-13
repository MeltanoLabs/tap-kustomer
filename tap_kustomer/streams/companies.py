
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import CustomerSearchStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# Streams to export
__all__ = [
    "CompaniesStream"
]

    
class CompaniesStream(CustomerSearchStream):
    """
    TODO
    """
    name = "companies"
    updated_at = "company_updated_at"
    query_context = "company"
    schema_filepath = SCHEMAS_DIR / "companies.json"
