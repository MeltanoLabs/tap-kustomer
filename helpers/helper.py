import json
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent / "tap_kustomer" / "streams"


def create_class_name(stream_name):
    """Create the CamelCase class name from the snake case name"""
    return "".join(x.title() for x in stream_name.split("_")) + "Stream"


def generate_stream(api_url, stream_name, class_name, description="TODO"):
    """
    Create the template class for the stream
    """

    return f"""
class {class_name}(kustomerStream):
    \"\"\"
    {description}
    \"\"\"

    name = "{stream_name}"
    path = "{api_url}"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema_filepath = SCHEMAS_DIR / "{stream_name}.json"

    def get_url_params(
        self, context: dict | None, next_page_token: Any | None
    ) -> dict[str, Any]:
        params = super().get_url_params(context, next_page_token)

        # TODO: Add additional params here: params["new_param"] = config.get("new_param")

        return params

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        \"\"\"Extract the updatedAt timestamp for the replication key\"\"\"
        row["updatedAt"] = row["attributes"].pop("updatedAt")
        return super().post_process(row, context)

"""


def create_schema_base(contents, stream_name, section):
    # Create the folder if it doesn't exist (with parents)
    folder_name = BASE / section / "schemas"
    folder_name.mkdir(parents=True, exist_ok=True)

    # Create the JSON file
    with open(folder_name / f"{stream_name}.json", "w") as f:
        json.dump(contents, f)


def create_stream_files(api_path, details):
    """Generate a stream file for each group"""

    file_headers = f"""from __future__ import annotations

from pathlib import Path
from typing import Any

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas"

# Streams to export
__all__ = ["{details['class']}"]

    """

    # Create the file
    my_file_contents = file_headers

    my_file_contents += generate_stream(
        api_path, details["name"], details["class"], details["description"]
    )
    create_schema_base(details["schema"], details["name"], details["section"])

    with open(BASE / details["section"] / f"{details['name']}_streams.py", "w") as f:
        f.write(my_file_contents)


def create_init_list(stream_list):
    """Create the init file list for imports"""

    # Section specific init file
    contents = ""
    for details in sorted(stream_list.values(), key=lambda x: x["name"]):
        contents += f"from tap_kustomer.streams.{details['section']}.{details['name']}_streams import {details['class']}\n"

    with open(BASE / details["section"] / "__init__.py", "w") as f:
        f.write(contents)

    # Add to the main init file
    contents = f"from tap_kustomer.streams.{details['section']} import (\n"
    for details in sorted(stream_list.values(), key=lambda x: x["name"]):
        contents += f"\t{details['class']},\n"

    contents += ")\n\n"

    with open(BASE / "__init__.py", "a") as f:
        f.write(contents)


def get_json_schemas(section):
    """
    This aims to extract the properties from the html of the Kustomer API docs.

    1. Go to a relevant API page in the section e.g. https://developer.kustomer.com/kustomer-api-docs/reference/getcompanies
    2. Open the network tab and refresh the page
    3. Find the response from the /getcompanies?json=on request
    4. Paste the results into `{section}_properties.json`
    """

    # Load the data
    with open(Path(__file__).parent / f"{section}_properties.json", "r") as f:
        main_file = json.load(f)["oasDefinition"]

    paths = {}

    paths_section = main_file["paths"]

    for api_path in paths_section.keys():
        if (
            "{" not in api_path
            and "=" not in api_path
            and "get" in paths_section[api_path].keys()
        ):
            definition = paths_section[api_path]["get"]
            description = definition["summary"]
            schema = definition["responses"]["200"]["content"]["application/json"][
                "schema"
            ]["$ref"].split("/")[-1]
            schema_json = main_file["components"]["schemas"][schema]["properties"]
            if "data" not in schema_json.keys():
                continue

            schema_json = main_file["components"]["schemas"][schema]["properties"][
                "data"
            ]

            if "items" in schema_json:
                schema_json = schema_json["items"]

            # Add the replication key
            schema_json["properties"]["updatedAt"] = {
                "type": "string",
                "format": "date-time",
            }

            name = api_path[1:].replace("/", "_").replace("-", "_")
            name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

            paths[api_path[1:]] = {
                "description": description,
                "schema": schema_json,
                "name": name,
                "class": create_class_name(name),
                "section": section,
            }

    return paths


def generate_files():
    sections = sorted(
        [
            "core_resources",
            "knowledge_base",
            "access_management",
            "apps_platform",
            "queues_and_routing",
            "settings_and_configurations",
            "workflows",
        ]
    )

    for section in sections:
        # Load the streams
        stream_list = get_json_schemas(section)

        # Create the contents
        for api_path, details in stream_list.items():
            create_stream_files(api_path, details)

        # Create the init file list
        create_init_list(stream_list)

        # Display the classnames for the import
        print(f"\t# {section}")
        for details in stream_list.values():
            print(f'\t{details["class"]},')


if __name__ == "__main__":
    generate_files()
