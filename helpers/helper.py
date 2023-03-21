from collections import defaultdict
from pathlib import Path


def create_class_name(stream_name):
    """Create the CamelCase class name from the snake case name"""
    return "".join(x.title() for x in stream_name.split("_")) + "Stream"


def generate_stream(stream_name):
    """
    Create the template class for the stream
    """

    class_name = create_class_name(stream_name)

    return f"""
class {class_name}(kustomerStream):
    \"\"\"
    TODO
    \"\"\"

    name = "{stream_name}"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "{stream_name}.json"

"""


def create_schema_base(stream_type, stream):
    contents = """
{
    "additionalProperties": false,
    "type": "object",
    "properties": {
    }
}
    """

    # Create the folder if it doesn't exist (with parents)
    folder_name = Path(__file__).parent / "outputs" / "schemas" / stream_type
    folder_name.mkdir(parents=True, exist_ok=True)

    # Create the JSON file
    with open(
        Path(__file__).parent / "outputs" / "schemas" / stream_type / f"{stream}.json",
        "w",
    ) as f:
        f.write(contents)


def create_stream_files(stream_type, streams):
    """Generate a stream file for each group"""

    stream_list = '",\n\t"'.join([create_class_name(x) for x in streams])

    file_headers = f"""
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "{stream_type}"

# Streams to export
__all__ = [
    "{stream_list}"
]

    """

    # Create the file
    my_file_contents = file_headers

    for stream in streams:
        my_file_contents += generate_stream(stream)
        create_schema_base(stream_type, stream)

    with open(
        Path(__file__).parent / "outputs" / f"{stream_type}_streams.py", "w"
    ) as f:
        f.write(my_file_contents)


def create_init_list(all_streams):
    """Create the init file list for imports"""
    contents = ""
    for stream_type, streams in all_streams.items():
        contents += f"from tap_kustomer.streams.{stream_type}_streams import (\n"
        for stream in streams:
            contents += "\t " + create_class_name(stream) + ",\n"
        contents += ")\n\n"

    with open(Path(__file__).parent / "outputs" / "__init__.py", "w") as f:
        f.write(contents)


def generate_files():
    # Load the streams
    with open(Path(__file__).parent / "stream_names.csv", "r") as f:
        stream_list = [i.split(",") for i in f.read().splitlines()[1:]]

    # Split by stream group
    all_streams = defaultdict(list)
    for stream in stream_list:
        all_streams[stream[1]].append(stream[0])

    # Create the contents
    for stream_type, streams in all_streams.items():
        create_stream_files(stream_type, streams)

    # Create the init file list
    create_init_list(all_streams)


if __name__ == "__main__":
    generate_files()
