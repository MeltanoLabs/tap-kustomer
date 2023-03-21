
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "customer"

# Streams to export
__all__ = [
    "CustomerStream",
	"CustomerActiveUserStream",
	"CustomerEmailStream",
	"CustomerExternalLinkStream",
	"CustomerLocationStream",
	"CustomerPhoneStream",
	"CustomerSharedEmailStream",
	"CustomerSharedExternalIdStream",
	"CustomerSharedPhoneStream",
	"CustomerSharedSocialStream",
	"CustomerSocialStream",
	"CustomerUrlStream",
	"CustomerWatcherStream",
	"KobjectStream"
]

    
class CustomerStream(kustomerStream):
    """
    TODO
    """

    name = "customer"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer.json"


class CustomerActiveUserStream(kustomerStream):
    """
    TODO
    """

    name = "customer_active_user"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_active_user.json"


class CustomerEmailStream(kustomerStream):
    """
    TODO
    """

    name = "customer_email"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_email.json"


class CustomerExternalLinkStream(kustomerStream):
    """
    TODO
    """

    name = "customer_external_link"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_external_link.json"


class CustomerLocationStream(kustomerStream):
    """
    TODO
    """

    name = "customer_location"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_location.json"


class CustomerPhoneStream(kustomerStream):
    """
    TODO
    """

    name = "customer_phone"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_phone.json"


class CustomerSharedEmailStream(kustomerStream):
    """
    TODO
    """

    name = "customer_shared_email"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_shared_email.json"


class CustomerSharedExternalIdStream(kustomerStream):
    """
    TODO
    """

    name = "customer_shared_external_id"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_shared_external_id.json"


class CustomerSharedPhoneStream(kustomerStream):
    """
    TODO
    """

    name = "customer_shared_phone"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_shared_phone.json"


class CustomerSharedSocialStream(kustomerStream):
    """
    TODO
    """

    name = "customer_shared_social"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_shared_social.json"


class CustomerSocialStream(kustomerStream):
    """
    TODO
    """

    name = "customer_social"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_social.json"


class CustomerUrlStream(kustomerStream):
    """
    TODO
    """

    name = "customer_url"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_url.json"


class CustomerWatcherStream(kustomerStream):
    """
    TODO
    """

    name = "customer_watcher"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_watcher.json"


class KobjectStream(kustomerStream):
    """
    TODO
    """

    name = "kobject"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "kobject.json"

