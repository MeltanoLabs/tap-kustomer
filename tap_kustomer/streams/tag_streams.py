
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "tag"

# Streams to export
__all__ = [
    "CompanyTagStream",
	"ConversationSuggestedTagHistoryStream",
	"ConversationTagHistoryStream",
	"CustomerLastConversationTagStream",
	"CustomerTagStream",
	"KobjectTagStream",
	"ShortcutTagStream",
	"TagStream"
]

    
class CompanyTagStream(kustomerStream):
    """
    TODO
    """

    name = "company_tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "company_tag.json"


class ConversationSuggestedTagHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_suggested_tag_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_suggested_tag_history.json"


class ConversationTagHistoryStream(kustomerStream):
    """
    TODO
    """

    name = "conversation_tag_history"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "conversation_tag_history.json"


class CustomerLastConversationTagStream(kustomerStream):
    """
    TODO
    """

    name = "customer_last_conversation_tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_last_conversation_tag.json"


class CustomerTagStream(kustomerStream):
    """
    TODO
    """

    name = "customer_tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "customer_tag.json"


class KobjectTagStream(kustomerStream):
    """
    TODO
    """

    name = "kobject_tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "kobject_tag.json"


class ShortcutTagStream(kustomerStream):
    """
    TODO
    """

    name = "shortcut_tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "shortcut_tag.json"


class TagStream(kustomerStream):
    """
    TODO
    """

    name = "tag"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "tag.json"

