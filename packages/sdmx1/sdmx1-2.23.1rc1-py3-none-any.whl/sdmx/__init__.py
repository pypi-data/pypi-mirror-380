import logging
from importlib.metadata import PackageNotFoundError, version

from sdmx.client import Client, Request, read_url
from sdmx.convert.pandas import to_pandas
from sdmx.format.xml.common import install_schemas, validate_xml
from sdmx.reader import read_sdmx, to_sdmx
from sdmx.rest import Resource
from sdmx.source import add_source, get_source, list_sources
from sdmx.writer.csv import to_csv
from sdmx.writer.xml import to_xml

__all__ = [
    "Client",
    "Request",
    "Resource",
    "add_source",
    "get_source",
    "install_schemas",
    "list_sources",
    "log",
    "read_sdmx",
    "read_url",
    "to_csv",
    "to_pandas",
    "to_xml",
    "to_sdmx",
    "validate_xml",
]


try:
    __version__ = version("sdmx1")
except PackageNotFoundError:  # pragma: no cover
    # Local copy or not installed with setuptools
    __version__ = "999"


#: Top-level logger.
#:
#: .. versionadded:: 0.4
log = logging.getLogger(__name__)
