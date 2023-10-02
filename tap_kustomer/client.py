"""REST client handling, including KustomerStream base class."""

from __future__ import annotations

import typing as t
from datetime import timezone
from urllib.parse import parse_qsl

import pendulum
from singer_sdk.authenticators import SimpleAuthenticator
from singer_sdk.exceptions import ConfigValidationError
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseHATEOASPaginator
from singer_sdk.streams import RESTStream

if t.TYPE_CHECKING:
    from urllib.parse import ParseResult

    import requests

UTC = timezone.utc


class PageLimitRESTPaginator(BaseHATEOASPaginator):
    """Pagination class for Kustomer's Customer Search API."""

    def get_next_url(self, response: requests.Response) -> str | None:
        data = response.json()
        next_link = data.get("links")["next"]

        if next_link == "/v1/customers/search?page=101&pageSize=100":
            next_link = data.get("links")["first"]
        return next_link


class RESTPaginator(BaseHATEOASPaginator):
    """Pagination class for Kustomer's REST API endpoints."""

    def get_next_url(self, response: requests.Response) -> str | None:
        data = response.json()
        if "links" in data and "next" in data.get("links"):
            next_link = data.get("links")["next"]
        else:
            next_link = None
        return next_link


class KustomerStream(RESTStream):
    """kustomer base stream class."""

    rest_method = "GET"
    primary_keys = ["id"]  # noqa: RUF012
    replication_key: str | None = "updated_at"
    records_jsonpath = "$[data][*]"

    @property
    def url_base(self) -> str:
        """Return the API URL root based on the provided prod point 1 (US), 2 (EU).

        https://developer.kustomer.com/kustomer-api-docs/reference/getting-started-with-kustomer-api#using-the-kustomer-api.
        """
        if self.config["prod_point"] == 1:
            # US endpoint
            return "https://api.kustomerapp.com/v1/"

        # EU endpoint
        if self.config["prod_point"] == 2:  # noqa: PLR2004
            return "https://api.prod2.kustomerapp.com/v1/"

        msg = "prod_point configuration must be either 1 (for US) or 2 (for EU)."
        raise ConfigValidationError(
            msg,
        )

    @property
    def authenticator(self) -> SimpleAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return SimpleAuthenticator(
            stream=self,
            auth_headers={
                "Authorization": f"Bearer {self.config.get('api_key')}",
            },
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        headers["Accept"] = "application/json"
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ANN401
    ) -> dict[str, t.Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}

        if next_page_token:
            params.update(parse_qsl(next_page_token.query))

        return params

    def parse_response(self, response: requests.Response) -> t.Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        # For incremental models, bring out the nested replication key
        if self.replication_key is not None:
            row["updated_at"] = row["attributes"]["updatedAt"]
            self.max_observed_timestamp = row["updated_at"]

        return row

    def get_new_paginator(self) -> BaseHATEOASPaginator:
        """Return the paginator.

        Returns:
            A paginator for handling next page requests
        """
        return RESTPaginator()


class CustomerSearchStream(KustomerStream):
    """kustomer stream class."""

    rest_method = "POST"
    path = "customers/search"
    primary_keys = ["id"]  # noqa: RUF012
    replication_key: str | None = "updated_at"
    records_jsonpath = "$[data][*]"
    max_observed_timestamp = None
    max_timestamp = None


    def get_new_paginator(self) -> BaseHATEOASPaginator:
        """Return the paginator.

        Returns:
            A paginator for handling next page requests
        """
        return PageLimitRESTPaginator()

    def prepare_request_payload(
        self,
        context: dict | None,
        next_page_token: ParseResult | None,
    ) -> dict | None:
        if self.max_timestamp:
            greater_than = self.max_timestamp
        elif self.get_starting_timestamp(context):
            greater_than = self.get_starting_timestamp(context)
        else:
            greater_than = pendulum.parse(self.config["start_date"])

        if "end_date" in self.config:
            less_than = pendulum.parse(self.config["end_date"])

        else:
            less_than = pendulum.now("UTC")

        if next_page_token and next_page_token.query == "page=1&pageSize=100":
            self.max_timestamp = self.max_observed_timestamp
            greater_than = self.max_timestamp

        return  {
            "and": [{self.updated_at: {"gt": f"{greater_than}"}},
                    {self.updated_at: {"lte": f"{less_than}"}}],
            "sort": [{self.updated_at: "asc"}],
            "queryContext": self.query_context,
        }
