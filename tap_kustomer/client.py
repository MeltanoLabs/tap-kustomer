"""REST client handling, including kustomerStream base class."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import parse_qsl

import requests
from singer_sdk.authenticators import SimpleAuthenticator
from singer_sdk.exceptions import ConfigValidationError
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.paginators import BaseHATEOASPaginator
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class RESTPaginator(BaseHATEOASPaginator):
    # Where the pagination is
    next_page_token_jsonpath = "$[links].next"

    def get_next_page_url(
        self,
        response: requests.Response,
        previous_token: Any | None,
    ) -> Any | None:
        """Return the url for the next page.

        Args:
            response: The HTTP ``requests.Response`` object.
            previous_token: The previous page token value.

        Returns:
            The next pagination token.
        """
        # If pagination is required, return a url which can be used to get the
        # next page. If this is the final page, return "None" to end the
        # pagination loop.

        all_matches = extract_jsonpath(self.next_page_token_jsonpath, response.json())
        first_match = next(iter(all_matches), None)
        next_page_token = first_match

        return next_page_token


class kustomerStream(RESTStream):
    """kustomer stream class."""

    # Use a dynamic url_base depending on the `prod_point` config
    @property
    def url_base(self) -> str:
        """
        Return the API URL root based on the provided prod point 1 (US), 2 (EU).
        https://developer.kustomer.com/kustomer-api-docs/reference/getting-started-with-kustomer-api#using-the-kustomer-api
        """
        if self.config["prod_point"] == 1:
            # US endpoint
            return "https://api.kustomerapp.com"
        # EU endpoint
        elif self.config["prod_point"] == 2:
            return "https://api.prod2.kustomerapp.com"

        raise ConfigValidationError(
            "prod_point configuration must be either 1 (for US) or 2 (for EU)."
        )

    # Where the data is
    records_jsonpath = "$[data][*]"

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

    @property
    def base_url_params(
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

        # TODO: Check these parameters work as can't find reference to them in the docs
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
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
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        # TODO: Delete this method if not needed.
        return row
