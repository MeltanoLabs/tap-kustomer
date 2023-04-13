"""kustomer tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_kustomer import streams

from tap_kustomer.client import KustomerStream, CustomerSearchStream

STREAM_TYPES = [
    streams.MessagesStream,
    streams.NotesStream,
    streams.ConversationsStream,
    streams.KObjectsStream,
    streams.CustomersStream,
    streams.UsersStream,
    streams.CompaniesStream
]


class Tapkustomer(Tap):
    """kustomer tap class."""

    name = "tap-kustomer"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The API KEY to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "prod_point",
            th.IntegerType,
            default=1,
            description="The production point of deployment for your organization instance. 1 (US) or 2 (EU).",
        ),
    ).to_dict()

    def discover_streams(self) -> list[KustomerStream, CustomerSearchStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [stream_type(self) for stream_type in STREAM_TYPES]


if __name__ == "__main__":
    Tapkustomer.cli()
