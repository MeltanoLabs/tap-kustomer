"""REST client handling, including kustomerStream base class."""

from __future__ import annotations

from typing import Any, Iterable
from urllib.parse import parse_qsl
from datetime import datetime

from singer_sdk.authenticators import SimpleAuthenticator
from singer_sdk.exceptions import ConfigValidationError
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseHATEOASPaginator
from singer_sdk.streams import RESTStream
from singer_sdk import typing as th  # JSON Schema typing helpers

import requests


class RESTPaginator(BaseHATEOASPaginator):

    def get_next_url(self, response):
        data = response.json()
        next_link = data.get("links")["next"]

        if next_link == "/v1/customers/search?page=101&pageSize=100":
            next_link = data.get("links")["first"]

        return next_link

class kustomerStream(RESTStream):
    """kustomer stream class."""

    # Where the data is
    records_jsonpath = "$[data][*]"

    # Use a dynamic url_base depending on the `prod_point` config
    @property
    def url_base(self) -> str:
        """
        Return the API URL root based on the provided prod point 1 (US), 2 (EU).
        https://developer.kustomer.com/kustomer-api-docs/reference/getting-started-with-kustomer-api#using-the-kustomer-api
        """
        if self.config["prod_point"] == 1:
            # US endpoint
            return "https://api.kustomerapp.com/v1/"
        # EU endpoint
        elif self.config["prod_point"] == 2:
            return "https://api.prod2.kustomerapp.com/v1/"

        raise ConfigValidationError(
            "prod_point configuration must be either 1 (for US) or 2 (for EU)."
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

    def get_new_paginator(self) -> BaseHATEOASPaginator:
        """Return the paginator

        Returns:
            A paginator for handling next page requests
        """
        return RESTPaginator()

    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
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

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        
        row["updated_at"] = row["attributes"]["updatedAt"]
        self.max_observed_timestamp = row["updated_at"]
    
        return row

    def prepare_request_payload(
        self,
        context: dict | None,
        next_page_token: th.TypeVar("_TToken") | None,
    ) -> dict | None:

        if self.max_timestamp:
            gte = self.max_timestamp
        elif self.get_starting_timestamp(context):
            gte = self.get_starting_timestamp(context)
        else:
            gte = datetime.strptime(self.config("start_date"), "%Y-%m-%d")

        if next_page_token and next_page_token.query == 'page=1&pageSize=100':
            self.max_timestamp = self.max_observed_timestamp
            gte = self.max_timestamp

        return {
            "and": [
                {
                self.updated_at: {
                    "gte": f"{gte}"
                    }
                }
            ],
            "sort": [
                {
                self.updated_at: "asc"
                }
            ],
            "queryContext": self.query_context
        }  