
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
	"UserStream"
]

class UserStream(KustomerStream):
    """
    TODO
    """

    name = "users"
    path = "users"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "user.json"
