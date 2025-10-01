import logging
import re
import zipfile
from functools import lru_cache
from itertools import chain
from operator import itemgetter
from pathlib import Path
from shutil import copytree
from typing import IO, Iterable, Mapping, Optional, Union, cast

from lxml import etree
from lxml.etree import QName

from sdmx.format import Version
from sdmx.format.common import Format

log = logging.getLogger(__name__)

# Tags common to SDMX-ML 2.1 and 3.0

# XML tag name ("str" namespace) and class name are the same
CT1 = [
    "Agency",
    "AgencyScheme",
    "Categorisation",
    "Category",
    "CategoryScheme",
    "Code",
    "Codelist",
    "Concept",
    "ConceptScheme",
    "CustomType",
    "CustomTypeScheme",
    "DataConsumer",
    "DataConsumerScheme",
    "DataProvider",
    "DataProviderScheme",
    "HierarchicalCode",
    "Level",
    "NamePersonalisation",
    "NamePersonalisationScheme",
    "Ruleset",
    "RulesetScheme",
    "TimeDimension",
    "TransformationScheme",
    "UserDefinedOperatorScheme",
]

# XML tag name and class name differ
CT2 = [
    ("model.Annotation", "com:Annotation"),
    ("model.Agency", "str:Agency"),  # Order matters
    ("model.Agency", "mes:Receiver"),
    ("model.Agency", "mes:Sender"),
    ("model.AttributeDescriptor", "str:AttributeList"),
    ("model.Concept", "str:ConceptIdentity"),
    ("model.Codelist", "str:Enumeration"),  # This could possibly be ItemScheme
    ("model.Dimension", "str:Dimension"),  # Order matters
    ("model.Dimension", "str:DimensionReference"),
    ("model.Dimension", "str:GroupDimension"),
    ("model.DataAttribute", "str:Attribute"),
    ("model.DataStructureDefinition", "str:DataStructure"),
    ("model.DimensionDescriptor", "str:DimensionList"),
    ("model.GroupDimensionDescriptor", "str:Group"),
    ("model.GroupDimensionDescriptor", "str:AttachmentGroup"),
    ("model.GroupKey", "gen:GroupKey"),
    ("model.Key", "gen:ObsKey"),
    ("model.MeasureDescriptor", "str:MeasureList"),
    ("model.MetadataStructureDefinition", "str:MetadataStructure"),
    ("model.SeriesKey", "gen:SeriesKey"),
    ("model.Structure", "com:Structure"),
    ("model.Structure", "str:Structure"),
    ("model.StructureUsage", "com:StructureUsage"),
    ("model.VTLMappingScheme", "str:VtlMappingScheme"),
    # Message classes
    ("message.DataMessage", "mes:StructureSpecificData"),
    ("message.MetadataMessage", "mes:GenericMetadata"),
    ("message.MetadataMessage", "mes:StructureSpecificMetadata"),
    ("message.ErrorMessage", "mes:Error"),
    ("message.StructureMessage", "mes:Structure"),
]

NS = {
    "": None,
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    # To be formatted
    "com": "{}/common",
    "data": "{}/data/structurespecific",
    "footer": "{}/message/footer",
    "gen": "{}/data/generic",
    "md_ss": "{}/metadata/structurespecific",
    "md": "{}/metadata/generic",
    "mes": "{}/message",
    "reg": "{}/registry",
    "str": "{}/structure",
}


def validate_xml(
    msg: Union[Path, IO],
    schema_dir: Optional[Path] = None,
    version: Union[str, Version] = Version["2.1"],
    max_errors: int = -1,
) -> bool:
    """Validate SDMX-ML in `msg` against the XML Schema (XSD) documents.

    A log message with level :data:`logging.ERROR` is emitted if validation fails. This
    indicates the first (possibly not only) element in `msg` that is not valid per the
    schemas.

    Parameters
    ----------
    msg
        Path or io-like containing an SDMX-ML message.
    schema_dir
        Directory with SDMX-ML XSD schemas used to validate the message.
    version
        The SDMX-ML schema version to validate against. One of ``2.1`` or ``3.0``.
    max_errors
        Maximum number of messages to log on validation failure.

    Returns
    -------
    bool
        :any:`True` if validation passed, otherwise :any:`False`.

    Raises
    ------
    FileNotFoundError
        if `schema_dir` (or a subdirectory) does not contain :file:`SDMXMessage.xsd`.
        Use :func:`sdmx.install_schemas` to download the schema files.
    NotImplementedError
        if `msg` contains valid XML, but with a root element that is not part of the
        SDMX-ML standard.
    """
    # Retrieve the XMLSchema
    schema = construct_schema(schema_dir, version)

    # Parse the given document
    msg_doc = etree.parse(msg)

    if not schema.validate(msg_doc):
        for i, entry in enumerate(cast(Iterable["etree._LogEntry"], schema.error_log)):
            if (
                i == 0
                and "No matching global declaration available for the validation root"
                in entry.message
            ):
                raise NotImplementedError(
                    f"Validate non-SDMX root element <{msg_doc.getroot().tag}>"
                ) from None
            elif i == max_errors:
                break
            log.log(getattr(logging, entry.level_name), entry.message)

        return False
    else:
        return True


def construct_schema(
    schema_dir: Optional[Path] = None,
    version: Union[str, Version] = Version["2.1"],
) -> "etree.XMLSchema":
    """Construct a :class:`lxml.etree.XMLSchema` for SDMX-ML of the given `version`.

    :file:`SDMXCommon.xsd` includes the documentation:

       XHTMLType allows for mixed content of text and XHTML tags. When using this type,
       one will have to provide a reference to the XHTML schema, since the processing of
       the tags within this type is strict, meaning that they are validated against the
       XHTML schema provided.

    This function does so by inserting an :xml:`<xs:import>` element that refers to
    http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd, which is the URL given by
    https://www.w3.org/TR/xhtml1-schema. With the :class:`.XMLSchema` returned by this
    document, it is possible to validate :xml:`<common:StructuredText>` elements that
    represent :class:`.XHTMLAttributeValue`.
    """
    # Find SDMXMessage.xsd in `schema_dir` or a subdirectory
    schema_dir, version = _handle_validate_args(schema_dir, version)
    for candidate in schema_dir, schema_dir.joinpath(version.name):
        try:
            # Parse the XSD into a schema object
            schema_etree = etree.parse(candidate.joinpath("SDMXMessage.xsd"))
            break
        except Exception:  # e.g. FileNotFoundError
            schema_etree = None

    if schema_etree is None:
        raise FileNotFoundError(f"Could not find XSD files in {schema_dir}")

    # Modify the schema by inserting an <xs:import > reference to the XHTML schema file
    elem = etree.Element(
        "{http://www.w3.org/2001/XMLSchema}import",
        namespace="http://www.w3.org/1999/xhtml",
        schemaLocation="xhtml1-strict.xsd",
    )
    schema_etree.getroot().insert(0, elem)

    # Parse the ElementTree to an XMLSchema and return
    return etree.XMLSchema(schema_etree)


def _extracted_zipball(version: Version, force: bool = False) -> Path:
    """Retrieve, cache, and extract the SDMX-ML schemas for `version`.

    1. Query the GitHub REST API to identify a URL for the `version` in zipball format.
    2. Download and cache the zipball. The file is not downloaded if it already exists.
    3. Unpack the archive.

    Actions (2) and (3) are performed in the user's cache directory (for instance,
    :file:`$HOME/.cache/sdmx/`). :func:`install_schemas` handles copying the extracted
    files to other locations.

    Returns
    -------
    Path
        Path to the root folder of the unpacked archive.
    """
    import platformdirs
    import requests

    # Map SDMX-ML schema versions to repo paths
    version_path = {Version["2.1"]: "v2.1", Version["3.0.0"]: "v3.0.0"}[version]

    # Check the latest release to get the URL to the schema zip
    url_base = "https://api.github.com/repos/sdmx-twg/sdmx-ml"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    release_json = requests.get(
        url=f"{url_base}/releases/tags/{version_path}", headers=headers
    ).json()
    try:
        zipball_url = release_json["zipball_url"]
    except KeyError:  # pragma: no cover
        zipball_url = f"{url_base}/zipball/{version_path}"
        log.debug(f"Could not determine zipball_url from:\n{release_json}\n")
        log.debug(f"Fall back to {zipball_url}")

    # Make a request for the zipball
    resp = requests.get(url=zipball_url, headers=headers)

    # Filename indicated by the HTTP response
    filename = resp.headers["content-disposition"].split("filename=")[-1]
    # Location for the cached zipball
    target = platformdirs.user_cache_path("sdmx").joinpath(filename)

    # Avoid downloading if the same file is already present
    if target.exists() and not force:
        log.info(f"Use existing {target}")
        resp.close()
    else:
        # Write response content to file
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(resp.content)

    with zipfile.ZipFile(target) as zf:
        # The first name list is the top-level directory within the file
        result = target.parent.joinpath(zf.namelist()[0])

        if result.exists() and not force:
            log.info(
                f"Destination {result} exists → skip extraction.\n"
                "Remove the directory or give force=True to override"
            )
        else:
            # Unpack the entire archive
            zf.extractall(target.parent)

    # Fetch a copy of the XHTML1 XSD, which is missing from the SDMX bundle
    resp = requests.get(url="http://www.w3.org/2002/08/xhtml/xhtml1-strict.xsd")
    result.joinpath("schemas", "xhtml1-strict.xsd").write_bytes(resp.content)

    return result


def _handle_validate_args(
    schema_dir: Optional[Path], version: Union[str, Version]
) -> tuple[Path, Version]:
    """Handle arguments for :func:`.install_schemas` and :func:`.validate_xml`."""
    import platformdirs

    supported = {Version["2.1"], Version["3.0.0"]}
    try:
        version = Version[version] if isinstance(version, str) else version
        assert version in supported
    except (AssertionError, KeyError):
        raise NotImplementedError(
            f"SDMX-ML version must be one of {supported}; got {version}"
        ) from None

    # If the user has no preference, download the schemas to the local cache directory
    if not schema_dir:
        schema_dir = platformdirs.user_cache_path("sdmx") / version.name
    schema_dir.mkdir(exist_ok=True, parents=True)

    return schema_dir, version


def install_schemas(
    schema_dir: Optional[Path] = None,
    version: Union[str, Version] = Version["2.1"],
) -> Path:
    """Install SDMX-ML XML Schema documents for use with :func:`.validate_xml`.

    Parameters
    ----------
    schema_dir : .Path, optional
        The directory where XSD schemas will be downloaded to. Default: a subdirectory
        named :file:`sdmx/{version}` within the :meth:`platformdirs.user_cache_path`.
    version : str or Version, optional
        The SDMX-ML schema version to install. One of :py:`Version["2.1"]` (default),
        :py:`Version["3.0.0"]`, or :class:`str` equivalent.

    Returns
    -------
    .Path
        The path containing the installed schemas. If `schema_dir` is given, the return
        value is identical to the parameter.
    """
    schema_dir, version = _handle_validate_args(schema_dir, version)

    # Copy the entire "schemas" subtree recursively
    copytree(
        _extracted_zipball(version).joinpath("schemas"), schema_dir, dirs_exist_ok=True
    )
    return schema_dir


class XMLFormat(Format):
    """Information about an SDMX-ML format."""

    NS: Mapping[str, Optional[str]]
    _class_tag: list

    def __init__(self, model, base_ns: str, class_tag: Iterable[tuple[str, str]]):
        from sdmx import message  # noqa: F401

        self.base_ns = base_ns

        # Construct name spaces
        self.NS = {
            prefix: url if url is None else url.format(base_ns)
            for prefix, url in NS.items()
        }

        # Construct class-tag mapping
        self._class_tag = []

        # Defined in this file
        for name in CT1:
            self._class_tag.append((getattr(model, name), self.qname("str", name)))

        # Defined in this file + those passed to the constructor
        for expr, tag in chain(CT2, class_tag):
            self._class_tag.append((eval(expr), self.qname(tag)))

    @lru_cache()
    def ns_prefix(self, url) -> str:
        """Return the namespace prefix from :attr:`.NS` given its full `url`."""
        for prefix, _url in self.NS.items():
            if url == _url:
                return prefix
        raise ValueError(url)

    _NS_PATTERN = re.compile(r"(\{(?P<ns>.*)\}|(?P<ns_prefix>.*):)?(?P<localname>.*)")

    @lru_cache()
    def qname(self, ns_or_name: str, name: Optional[str] = None) -> QName:
        """Return a fully-qualified tag `name` in namespace `ns`."""
        if isinstance(ns_or_name, QName):
            # Already a QName; do nothing
            return ns_or_name

        if name is None:
            # `ns_or_name` contains the local name ("tag") and possibly a namespace
            # prefix ("ns:tag") or full namespace name ("{foo}tag")
            match = self._NS_PATTERN.fullmatch(ns_or_name)
            assert match
            name = match.group("localname")
            if prefix := match.group("ns_prefix"):
                ns = self.NS[prefix]
            elif ns := match.group("ns"):
                pass
            else:
                ns = None  # Tag without namespace
        else:
            # `ns_or_name` is the namespace prefix; `name` is the local name
            ns = self.NS[ns_or_name]

        return QName(ns, name)

    @lru_cache()
    def class_for_tag(self, tag) -> Optional[type]:
        """Return a message or model class for an XML tag."""
        qname = self.qname(tag)
        results = map(itemgetter(0), filter(lambda ct: ct[1] == qname, self._class_tag))
        try:
            return next(results)
        except StopIteration:
            return None

    @lru_cache()
    def tag_for_class(self, cls):
        """Return an XML tag for a message or model class."""
        results = map(itemgetter(1), filter(lambda ct: ct[0] is cls, self._class_tag))
        try:
            return next(results)
        except StopIteration:
            return None

    # __eq__ and __hash__ to enable lru_cache()
    def __eq__(self, other):
        return self.base_ns == other.base_ns  # pragma: no cover

    def __hash__(self):
        return hash(self.base_ns)
