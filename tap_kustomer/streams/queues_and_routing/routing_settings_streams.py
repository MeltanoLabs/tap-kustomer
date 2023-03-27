from __future__ import annotations

from pathlib import Path
from typing import Any

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas"

# Streams to export
__all__ = ["RoutingSettingsStream"]

    
class RoutingSettingsStream(kustomerStream):
    """
    Get All Team Routing Settings
    """

    name = "routing_settings"
    path = "routing/settings"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema_filepath = SCHEMAS_DIR / "routing_settings.json"

    def get_url_params(
        self, context: dict | None, next_page_token: Any | None
    ) -> dict[str, Any]:
        params = super().get_url_params(context, next_page_token)

        # TODO: Add additional params here: params["new_param"] = config.get("new_param")

        return params

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        """Extract the updatedAt timestamp for the replication key"""
        row["updatedAt"] = row["attributes"].pop("updatedAt")
        return super().post_process(row, context)

