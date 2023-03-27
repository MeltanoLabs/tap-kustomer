import json
import re
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent / "tap_kustomer" / "streams"

UNWANTED_TAPS = [
    "auth_customer_settings",
    "auth_settings",
    "auth_tokens",
    "auth_tokens_current",
    "p_auth_settings",
    "users_current",
    "brands_default",
    "outbound_accounts",
    "schedules_default",
    "kb_articles_search",
    "kb_articles_search",
    "kb_route",
    "kb_themes_active",
    "routing_work_sessions_current",
    "routing_work_sessions_current_work_items",
    "chat_settings",
    "notifications_users_current_settings",
    "users_current_settings",
]


def create_class_name(stream_name):
    """Create the CamelCase class name from the snake case name"""
    return "".join(x.title() for x in stream_name.split("_")) + "Stream"


def generate_stream(api_url, stream_name, class_name, description="TODO", version=1):
    """
    Create the template class for the stream
    """

    if version == 3:
        v3_replace = """
    # Overwrite the version to use v3
    @property
    def url_base(self) -> str:
        return super().url_base.replace("/v1/", "/v3/")

        """
    else:
        v3_replace = ""

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
{v3_replace}
    def get_url_params(
        self, context: dict | None, next_page_token: Any | None
    ) -> dict[str, Any]:
        params = super().get_url_params(context, next_page_token)

        # TODO: Add additional params here: params["new_param"] = config.get("new_param")

        return params

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        \"\"\"Extract the updatedAt timestamp for the replication key\"\"\"
        row["updatedAt"] = row["attributes"]["updatedAt"]
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
        api_path,
        details["name"],
        details["class"],
        details["description"],
        details["version"],
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


def allow_nullable(my_dict):
    """Replace the properties with oneOf"""

    for key, value in my_dict.items():
        if isinstance(value, dict):
            if key != "properties":
                my_dict[key] = {"oneOf": [{"type": "null"}, allow_nullable(value)]}
            else:
                my_dict[key] = allow_nullable(value)

    return my_dict


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

    # Manually add the undocumented SLAs
    if section == "core_resources":
        paths_section["/slas"] = {
            "get": {
                "summary": "Retrieves all SLAs",
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "/GETanSLAbyIDResponseSuccessversionsall"
                                }
                            }
                        }
                    }
                },
            }
        }

    for api_path in paths_section.keys():
        if (
            "{" not in api_path
            and "=" not in api_path
            and "/p/" not in api_path  # Exclude the public ones - not required
            and "get" in paths_section[api_path].keys()
        ):
            definition = paths_section[api_path]["get"]
            if "deprecated" not in definition or definition["deprecated"] == False:
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

                # Allow fields to be nullable
                schema_json = allow_nullable(schema_json)

                # Add the replication key
                schema_json["properties"]["updatedAt"] = {
                    "type": "string",
                    "format": "date-time",
                }

                # Some endpoints have v3 instead of v1
                version = 3 if "v3" in api_path else 1

                # Remove mention of v1 or v3 from all endpoints
                api_path = api_path.replace("v1/", "").replace("v3/", "")

                name = api_path[1:].replace("/", "_").replace("-", "_")
                name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

                if name not in UNWANTED_TAPS:
                    paths[api_path[1:]] = {
                        "description": description,
                        "schema": schema_json,
                        "name": name,
                        "class": create_class_name(name),
                        "section": section,
                        "version": version,
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

    meltano_yml = ""
    yml_whitespace = "  " * 7

    # Empty the __init__ file
    with open(BASE / "__init__.py", "w") as f:
        f.write("")

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
        for details in sorted(stream_list.values(), key=lambda x: x["class"]):
            print(f'\t{details["class"]},')

        # Display the names for the meltano.yml
        meltano_yml += f"{yml_whitespace}# {section}\n"
        for details in sorted(stream_list.values(), key=lambda x: x["name"]):
            meltano_yml += f'{yml_whitespace}- {details["name"]}.*\n'

    print("-" * 50)
    print(meltano_yml)


if __name__ == "__main__":
    generate_files()
