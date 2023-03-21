
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "company"

# Streams to export
__all__ = [
    "CompanyStream",
	"CompanyEmailStream",
	"CompanyLocationStream",
	"CompanyPhoneStream",
	"CompanySocialStream",
	"CompanyUrlStream"
]

    
class CompanyStream(kustomerStream):
    """
    TODO
    """

    name = "company"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company.json"


class CompanyEmailStream(kustomerStream):
    """
    TODO
    """

    name = "company_email"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_email.json"


class CompanyLocationStream(kustomerStream):
    """
    TODO
    """

    name = "company_location"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_location.json"


class CompanyPhoneStream(kustomerStream):
    """
    TODO
    """

    name = "company_phone"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_phone.json"


class CompanySocialStream(kustomerStream):
    """
    TODO
    """

    name = "company_social"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_social.json"


class CompanyUrlStream(kustomerStream):
    """
    TODO
    """

    name = "company_url"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_url.json"

