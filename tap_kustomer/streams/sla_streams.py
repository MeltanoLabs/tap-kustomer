
from __future__ import annotations

from pathlib import Path

from tap_kustomer.client import kustomerStream

SCHEMAS_DIR = Path(__file__).parent / "schemas" / "sla"

# Streams to export
__all__ = [
    "SlaStream",
	"SlaCriteriaStream",
	"SlaMetricStream",
	"SlaVersionStream"
]

    
class SlaStream(kustomerStream):
    """
    TODO
    """

    name = "sla"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "sla.json"


class SlaCriteriaStream(kustomerStream):
    """
    TODO
    """

    name = "sla_criteria"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "sla_criteria.json"


class SlaMetricStream(kustomerStream):
    """
    TODO
    """

    name = "sla_metric"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "sla_metric.json"


class SlaVersionStream(kustomerStream):
    """
    TODO
    """

    name = "sla_version"
    path = "/v1/TODO"
    primary_keys = ["TODO"]
    replication_key = "TODO"
    schema_filepath = SCHEMAS_DIR / "sla_version.json"

