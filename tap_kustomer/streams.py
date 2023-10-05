"""Stream classes for tap-kustomer."""

from __future__ import annotations

import json
import typing as t
from pathlib import Path

from tap_kustomer.client import CustomerSearchStream, KustomerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

__all__ = [
    # Parent streams
    "CompaniesStream",
    "ConversationsStream",
    "CustomersStream",
    "KObjectsStream",
    "MessagesStream",
    "NotesStream",
    "ShortcutsStream",
    "SlaStream",
    "SlaVersionStream",
    "TagsStream",
    "TeamsStream",
    "UsersStream",
    # Child streams
    "AttachmentsChildStream",
]

# -----------------------------------------------------------------
# Customer Search streams
# -----------------------------------------------------------------


class CompaniesStream(CustomerSearchStream):
    name = "companies"
    updated_at = "company_updated_at"
    query_context = "company"
    schema_filepath = SCHEMAS_DIR / "companies.json"


class ConversationsStream(CustomerSearchStream):
    name = "conversations"
    schema_filepath = SCHEMAS_DIR / "conversations.json"
    updated_at = "conversation_updated_at"
    query_context = "conversation"

    def get_child_context(
        self,
        record: dict,
        context: dict | None,  # noqa: ARG002
    ) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "id": record["id"],
        }

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        if row["attributes"].get("snooze") is None:
            row["attributes"]["snooze"] = {}

        for attribute_key in ["firstMessageIn", "lastMessageIn"]:
            for meta_key in ["to", "cc", "bcc"]:
                has_meta = "meta" in row["attributes"].get(attribute_key, {})
                value = (
                    row["attributes"]
                    .get(attribute_key, {})
                    .get("meta", {})
                    .get(meta_key)
                )
                typeof = type(value)

                if not has_meta:
                    continue

                if typeof == dict:
                    row["attributes"][attribute_key]["meta"][meta_key] = [value]

                if typeof in [str, type(None)]:
                    row["attributes"][attribute_key]["meta"][meta_key] = [
                        {"contact": value},
                    ]

        # This following would be obsolete by https://github.com/meltano/sdk/issues/1995
        if self.config.get("flattening_enabled", False):
            for attribute_key in ["firstDone", "lastDone"]:
                if row["attributes"][attribute_key].get("createdByTeams") is None:
                    row["attributes"][attribute_key]["createdByTeams"] = []

                if (
                    row["attributes"][attribute_key].get(
                        "outboundMessageCountByChannel",
                    )
                    is None
                ):
                    row["attributes"][attribute_key][
                        "outboundMessageCountByChannel"
                    ] = {}

                if (
                    row["attributes"][attribute_key].get("messageCountByChannel")
                    is None
                ):
                    row["attributes"][attribute_key]["messageCountByChannel"] = {}

            if row["attributes"]["snooze"].get("outboundMessageCountByChannel") is None:
                row["attributes"][attribute_key]["outboundMessageCountByChannel"] = {}

        row["updated_at"] = row["attributes"]["updatedAt"]
        self.max_observed_timestamp = row["updated_at"]

        return row


class CustomersStream(CustomerSearchStream):
    name = "customers"
    schema_filepath = SCHEMAS_DIR / "customers.json"
    updated_at = "customer_updated_at"
    query_context = "customer"


class KObjectsStream(CustomerSearchStream):
    name = "kobjects"
    schema_filepath = SCHEMAS_DIR / "kobjects.json"
    updated_at = "kobject_updated_at"
    query_context = "kobject"


class MessagesStream(CustomerSearchStream):
    name = "messages"
    schema_filepath = SCHEMAS_DIR / "messages.json"
    updated_at = "message_updated_at"
    query_context = "message"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        for meta_key in ["to", "cc", "bcc"]:
            has_meta = "meta" in row["attributes"]
            if has_meta:
                value = row["attributes"]["meta"].get(meta_key)

                if isinstance(value, dict):
                    row["attributes"]["meta"][meta_key] = [value]

                if isinstance(value, str):
                    row["attributes"]["meta"][meta_key] = [{"contact": value}]

        row["updated_at"] = row["attributes"]["updatedAt"]
        self.max_observed_timestamp = row["updated_at"]

        return row


class NotesStream(CustomerSearchStream):
    name = "notes"
    schema_filepath = SCHEMAS_DIR / "notes.json"
    updated_at = "note_updated_at"
    query_context = "note"


class ResourceStream(CustomerSearchStream):
    name = "resource"
    schema_filepath = SCHEMAS_DIR / "resource.json"
    replication_key = None
    resources: t.ClassVar = ["company", "conversation", "customer", "message"]

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> t.Iterable[dict[str, t.Any]]:
        for record in self.resources:
            yield {"resource": record}

    def get_child_context(
        self,
        record: dict,
        context: dict | None,  # noqa: ARG002
    ) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "resource": record["resource"],
        }


# -----------------------------------------------------------------
# Kustomer streams
# -----------------------------------------------------------------


class ShortcutsStream(KustomerStream):
    name = "shortcuts"
    path = "shortcuts"
    schema_filepath = SCHEMAS_DIR / "shortcuts.json"


class SlaStream(KustomerStream):
    name = "slas"
    path = "slas"
    schema_filepath = SCHEMAS_DIR / "slas.json"
    replication_key = None


class SlaVersionStream(KustomerStream):
    name = "sla_versions"
    path = "slas"
    schema_filepath = SCHEMAS_DIR / "sla_versions.json"
    replication_key = None

    # Versions are not in the data key as defined in KustomerStream
    records_jsonpath = "$[included][*]"

    def get_url_params(
        self,
        context: dict | None,
        next_page_token: t.Any | None,  # noqa: ANN401
    ) -> dict[str, t.Any]:
        params = super().get_url_params(context, next_page_token)

        # This ensures that the endpoint returns the version details
        params["versions"] = "all"

        return params


class TagsStream(KustomerStream):
    name = "tags"
    path = "tags"
    schema_filepath = SCHEMAS_DIR / "tags.json"


class TeamsStream(KustomerStream):
    name = "teams"
    path = "teams"
    schema_filepath = SCHEMAS_DIR / "teams.json"


class UsersStream(KustomerStream):
    name = "users"
    path = "users"
    schema_filepath = SCHEMAS_DIR / "users.json"


# -----------------------------------------------------------------
# Child streams
# -----------------------------------------------------------------


class AttachmentsChildStream(KustomerStream):
    name = "attachments"
    parent_stream_type = ConversationsStream
    path = "conversations/{id}/attachments"
    schema_filepath = SCHEMAS_DIR / "attachments.json"
    replication_key = None
    ignore_parent_replication_keys = True


class CustomAttributesStream(KustomerStream):
    name = "custom_attributes"
    parent_stream_type = ResourceStream
    path = "metadata/{resource}"
    schema_filepath = SCHEMAS_DIR / "custom_attributes.json"
    replication_key = None
    ignore_parent_replication_keys = True

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        for k, v in row["attributes"]["properties"].items():
            v["id"] = k
            v["tree"] = json.dumps(v.get("tree", ""))
        row["attributes"]["properties"] = [
            v for _, v in row["attributes"]["properties"].items()
        ]
        return row
