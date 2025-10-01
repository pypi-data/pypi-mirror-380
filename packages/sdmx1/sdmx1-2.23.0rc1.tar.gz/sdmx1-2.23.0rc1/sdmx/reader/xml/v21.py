"""SDMX-ML v2.1 reader."""
# Contents of this file are organized in the order:
#
# - Utility methods and global variables.
# - Reference and Reader classes.
# - Parser functions for sdmx.message classes, in the same order as message.py
# - Parser functions for sdmx.model classes, in the same order as model.common/model.v21
#
# When accessing sdmx.model classes, use:
#
# - common.Class for classes common to multiple/all versions of the SDMX IM.
# - v21.Class for classes specific to v21 of the IM.
# - reader.model.Class or reader.model.get_class for code that can handle classes from
#   either version 2.1 or 3.0.0 of the IM and SDMX-ML. When used in .reader.xml.v30,
#   these references will be to sdmx.model.v30.

import logging
import re
from copy import copy
from itertools import chain, filterfalse
from sys import maxsize
from typing import Any, MutableMapping, Optional, cast

from dateutil.parser import isoparse
from lxml import etree
from lxml.etree import QName

import sdmx.urn
from sdmx import message
from sdmx.exceptions import XMLParseError  # noqa: F401
from sdmx.format import Version
from sdmx.model import common, v21
from sdmx.tools import dimensions_to_attributes

from .common import (
    BaseReference,
    NotReference,
    XMLEventReader,
    add_localizations,
    setdefault_attrib,
    to_snake,
)

log = logging.getLogger(__name__)


class _NoText:
    pass


# Sentinel value for XML elements with no text; used to distinguish from "" and None
NoText = _NoText()


class Reference(BaseReference):
    @classmethod
    def info_from_element(cls, elem):
        try:
            # Use the first child
            elem = elem[0]
        except IndexError:
            raise NotReference

        # Extract information from the XML element
        if elem.tag == "Ref":
            # Element attributes give target_id, id, and version
            result = dict(
                target_id=elem.attrib["id"],
                agency=elem.attrib.get("agencyID", None),
                id=elem.attrib.get("maintainableParentID", elem.attrib["id"]),
                version=elem.attrib.get("maintainableParentVersion", None)
                or elem.attrib.get("version", None),
            )

            # Attributes of the element itself, if any
            for k in ("class", "package"):
                result[k] = elem.attrib.get(k, None)
        elif elem.tag == "URN":
            result = sdmx.urn.match(elem.text)
            # If the URN doesn't specify an item ID, it is probably a reference to a
            # MaintainableArtefact, so target_id and id are the same
            result.update(target_id=result["item_id"] or result["id"])
        else:
            raise NotReference

        return result


class Reader(XMLEventReader):
    """SDMX-ML 2.1 reader."""

    xml_version = Version["2.1"]
    Reference = Reference


# Shorthand
start = Reader.start
end = Reader.end
possible_reference = Reader.possible_reference


def _get_id(reader, elem) -> str:
    """Retrieve an ID attribute for `elem`."""
    if QName(elem).namespace:  # Element with namespace → generic SDMX-ML
        return elem.attrib["id"]
    else:  # No namespace → structure-specific SDMX-ML
        return re.split(r"[:\.]", elem.attrib[reader.qname("xsi", "type")])[-1]


# Tags to skip entirely
start(
    "com:Annotations com:Footer footer:Message "
    # Key and observation values
    "gen:ObsDimension gen:ObsValue gen:Value "
    # Tags that are bare containers for other XML elements
    """
    str:Categorisations str:CategorySchemes str:Codelists str:Concepts
    str:ConstraintAttachment str:Constraints str:CustomTypes str:Dataflows
    str:DataStructureComponents str:DataStructures str:FromVtlSuperSpace
    str:HierarchicalCodelists str:Metadataflows str:MetadataStructures
    str:MetadataStructureComponents str:NamePersonalisations str:OrganisationSchemes
    str:ProvisionAgreements str:Rulesets str:StructureSets str:ToVtlSubSpace
    str:Transformations str:UserDefinedOperators str:VtlMappings
    """
    # Contents of references
    ":Ref :URN"
)(None)


# Parsers for sdmx.message classes


@start(
    """
    mes:Error mes:GenericData mes:GenericMetadata mes:GenericTimeSeriesData
    mes:StructureSpecificData mes:StructureSpecificMetadata
    mes:StructureSpecificTimeSeriesData
    """
)
@start("mes:Structure", only=False)
def _message(reader: Reader, elem):
    """Start of a Message."""
    # <mes:Structure> within <mes:Header> of a data message is handled by
    # _header_structure() below.
    if getattr(elem.getparent(), "tag", None) == reader.qname("mes", "Header"):
        return

    ss_without_structure = False

    # Retrieve any {Metad,D}ataStructure definition given to Reader.convert()
    supplied_structure = reader.get_single(common.Structure, subclass=True)

    # Handle
    qname = QName(elem)
    if "StructureSpecific" in elem.tag:
        if supplied_structure is None:
            log.warning(f"xml.Reader got no structure=… argument for {qname.localname}")
            ss_without_structure = True
        elif isinstance(supplied_structure, reader.model.MetadataStructureDefinition):
            add_mds_events(reader, supplied_structure)
    elif supplied_structure:
        log.info("Use supplied structure=… argument for non–structure-specific message")

    # Store values for other methods
    reader.push("SS without structure", ss_without_structure)
    if elem.tag.endswith("Data"):
        reader.push(
            "DataSetClass", reader.model.get_class(f"{QName(elem).localname}Set")
        )

    # Handle namespaces mapped on `elem` but not part of the standard set
    existing_ns = set(reader.format.NS.values())
    for namespace in filterfalse(existing_ns.__contains__, elem.nsmap.values()):
        # Use _ds_start() and _ds_end() to handle <{namespace}DataSet> elements
        reader.parser[QName(namespace, "DataSet"), "start"] = _ds_start
        reader.parser[QName(namespace, "DataSet"), "end"] = _ds_end

    # Instantiate the message object
    return reader.class_for_tag(elem.tag)()


@end("mes:Header")
def _header(reader, elem):
    # Attach to the Message
    header = message.Header(
        extracted=reader.pop_single("Extracted") or None,
        id=reader.pop_single("ID") or None,
        prepared=reader.pop_single("Prepared") or None,
        receiver=reader.pop_single("Receiver") or None,
        reporting_begin=reader.pop_single("ReportingBegin") or None,
        reporting_end=reader.pop_single("ReportingEnd") or None,
        sender=reader.pop_single("Sender") or None,
        test=str(reader.pop_single("Test")).lower() == "true",
    )
    add_localizations(header.source, reader.pop_all("Source"))

    reader.get_single(message.Message, subclass=True).header = header

    # TODO add these to the Message class
    # Appearing in data messages from WB_WDI and the footer.xml specimen
    reader.pop_all("DataSetAction")
    reader.pop_all("DataSetID")
    # Appearing in the footer.xml specimen
    reader.pop_all("Timezone")


@end("mes:Receiver mes:Sender")
def _header_org(reader, elem):
    reader.push(
        elem,
        reader.nameable(
            reader.class_for_tag(elem.tag), elem, contact=reader.pop_all(common.Contact)
        ),
    )


@end("mes:Structure", only=False)
def _header_structure(reader, elem):
    """<mes:Structure> within <mes:Header> of a {Metad,D}ataMessage."""
    # The root node of a structure message is handled by _message(), above.
    if elem.getparent() is None:
        return

    msg = reader.get_single(message.DataMessage, subclass=True)
    assert msg is not None

    # Retrieve a structure supplied to the reader, e.g. for a structure specific message
    provided_structure = reader.get_single(common.Structure, subclass=True)

    # Resolve the <com:Structure> child to an object, maybe is_external_reference=True
    header_structure = reader.pop_resolved_ref("Structure")

    # The header may give either a StructureUsage, or a specific reference to a subclass
    # like BaseDataflow. Resolve the <str:StructureUsage> child, if any, and remove it
    # from the stack.
    header_su = reader.pop_resolved_ref("StructureUsage")
    reader.pop_single(type(header_su))

    # Store a specific reference to a data flow specifically
    if isinstance(header_su, reader.class_for_tag("str:Dataflow")):
        msg.dataflow = header_su

    # DSD to use: the provided one; the one referenced by <com:Structure>; or a
    # candidate constructed using the information contained in `header_su` (if any)
    structure = provided_structure or (
        reader.maintainable(
            msg.structure_type,
            None,
            id=header_su.id,
            maintainer=header_su.maintainer,
            version=header_su.version,  # NB this may not always be the case
        )
        if header_su
        else header_structure
    )

    if header_structure and header_su:
        # Ensure the constructed candidate and the one given directly are equivalent
        assert header_structure == structure
    elif header_su and not provided_structure:
        reader.push(structure)
    elif structure is None:  # pragma: no cover
        raise RuntimeError

    # Store on the data flow
    msg.dataflow.structure = structure

    # Store under the structure ID, so it can be looked up by that ID
    reader.push(elem.attrib["structureID"], structure)

    # Store as objects that won't cause a parsing error if it is left over
    reader.ignore.update({id(structure), id(header_structure)})

    try:
        # Information about the 'dimension at observation level'
        dim_at_obs = elem.attrib["dimensionAtObservation"]
    except KeyError:
        pass
    else:
        # Store
        if dim_at_obs == "AllDimensions":
            # Use a singleton object
            dim = common.AllDimensions
        elif provided_structure:
            # Use existing dimension from the provided DSD
            dim = structure.dimensions.get(dim_at_obs)
        else:
            # Force creation of the 'dimension at observation' level
            dim = structure.dimensions.getdefault(
                dim_at_obs,
                cls=(
                    common.TimeDimension
                    if "TimeSeries" in elem.getparent().getparent().tag
                    else common.Dimension
                ),
                # TODO later, reduce this
                order=maxsize,
            )
        msg.observation_dimension = dim


@end("footer:Footer")
def _footer(reader, elem):
    # Get attributes from the child <footer:Message>
    args = dict()
    setdefault_attrib(args, elem[0], "code", "severity")
    if "code" in args:
        args["code"] = int(args["code"])

    reader.get_single(message.Message, subclass=True).footer = message.Footer(
        text=list(map(common.InternationalString, reader.pop_all("Text"))), **args
    )


@end("mes:Structures")
def _structures(reader, elem):
    """End of a structure message."""
    msg = reader.get_single(message.StructureMessage)

    # Populate dictionaries by ID
    for attr, name in msg.iter_collections():
        target = getattr(msg, attr)

        # Store using maintainer, ID, and version
        tmp = {
            (getattr(obj.maintainer, "id", None), obj.id, obj.version): obj
            for obj in reader.pop_all(name, subclass=True)
        }

        # TODO Move this to StructureMessage
        # Construct string IDs
        if len(set(k[0:2] for k in tmp.keys())) < len(tmp):
            # Some non-unique (maintainer ID, object ID) pairs; include version
            id_expr = "{0}:{1}({2})"
        elif len(set(k[1] for k in tmp.keys())) < len(tmp):
            # Some non-unique object IDs; include maintainer ID
            id_expr = "{0}:{1}"
        else:
            # Only object ID
            id_expr = "{1}"

        for k, obj in tmp.items():
            target[id_expr.format(*k)] = obj


# Parsers for sdmx.model classes
# §3.2: Base structures


@end(
    """
    com:AnnotationTitle com:AnnotationType com:AnnotationURL com:None com:URN com:Value
    mes:DataSetAction :ReportPeriod md:ReportPeriod mes:DataSetID mes:Email mes:Fax
    mes:ID mes:Telephone mes:Test mes:Timezone mes:URI mes:X400 str:CodelistAliasRef
    str:DataType str:Email str:Expression str:NullValue str:OperatorDefinition
    str:PersonalisedName str:Result str:RulesetDefinition str:Telephone str:URI
    str:VtlDefaultName str:VtlScalarType
    """
)
def _text(reader, elem):
    # If elem.text is None, push a sentinel value
    reader.push(elem, elem.text or NoText)


@start("com:StructuredText")
def _st(reader, elem):
    """Contained XHTML."""
    reader.push(elem, elem[0])


@end("mes:Extracted mes:Prepared mes:ReportingBegin mes:ReportingEnd")
def _datetime(reader, elem):
    text, n = re.subn(r"(.*\.)(\d{6})\d+(\+.*)", r"\1\2\3", elem.text)
    if n > 0:
        log.debug(f"Truncate sub-microsecond time in <{QName(elem).localname}>")

    reader.push(elem, isoparse(text))


@end(
    """
    com:AnnotationText com:Name com:Description com:Text mes:Source mes:Department
    mes:Role str:Department str:Role
    """
)
def _localization(reader, elem):
    reader.push(
        elem,
        (elem.attrib.get(reader.qname("xml:lang"), common.DEFAULT_LOCALE), elem.text),
    )


@end(
    """
    com:Structure com:StructureUsage :ObjectReference md:ObjectReference
    str:AttachmentGroup str:CodeID str:ConceptIdentity str:ConceptRole
    str:DimensionReference str:Enumeration str:Parent str:Source str:Structure
    str:StructureUsage str:Target
    """
)
def _ref(reader: Reader, elem):
    cls_hint = reader.peek("ItemAssociation class") or None

    localname = QName(elem).localname

    if not cls_hint and localname in ("CodeID", "Parent", "Target"):
        # Use the *grand*-parent of the <Ref> or <URN> for a class hint
        tag = elem.getparent().tag

        if QName(tag).localname == "Categorisation" and localname == "Target":
            # XSD CategoryReferenceType needs a specific class hint
            cls_hint = common.Category
        else:
            cls_hint = reader.class_for_tag(tag)
    elif not cls_hint and localname == "Structure":
        # <com:Structure>/<str:Structure>: use message property for a class hint
        msg = reader.get_single(message.DataMessage, subclass=True)
        if msg:
            cls_hint = cast(type[message.DataMessage], type(msg))(
                version=reader.xml_version
            ).structure_type
        elif QName(elem.getparent()).localname == "Dataflow":
            # In a StructureMessage
            cls_hint = reader.model.DataStructureDefinition

    try:
        ref = reader.reference(elem, cls_hint)
    except ValueError as e:
        # Handle references to known non-standard classes; see
        # https://github.com/khaeru/sdmx/issues/180
        info = e.args[1]
        if info["package"] == "publicationtable":
            log.warning(
                "Cannot resolve reference to non-SDMX class "
                f"'{info['package']}.{info['class']}'"
            )
            # Push the dict of reference info, in case the user wants to make use of it
            ref = info
        else:  # pragma: no cover
            raise

    reader.push(QName(elem).localname, ref)


@end("com:Annotation")
def _a(reader, elem):
    url = reader.pop_single("AnnotationURL")
    args = dict(
        title=reader.pop_single("AnnotationTitle"),
        type=reader.pop_single("AnnotationType"),
        url=None if url is NoText else url,
    )

    # Annotation.value: SDMX 3.0.0 only
    if value := reader.pop_single("AnnotationValue"):
        args["value"] = value

    # Optional 'id' attribute
    setdefault_attrib(args, elem, "id")

    a = reader.model.Annotation(**args)
    add_localizations(a.text, reader.pop_all("AnnotationText"))

    return a


# §3.5: Item Scheme


@start(
    """
    str:Agency str:Code str:Category str:Concept str:CustomType str:DataConsumer
    str:DataProvider
    """,
    only=False,
)
def _item_start(reader, elem):
    try:
        if elem[0].tag in ("Ref", "URN"):
            # `elem` is a reference, so it has no name/etc.; don't stash
            return
    except IndexError:
        # No child elements; stash() anyway, but it will be a no-op
        pass

    # Avoid stealing the name & description of the parent ItemScheme from the stack
    reader.stash(reader.model.Annotation, "Name", "Description")


@end(
    """
    str:Agency str:Code str:Category str:Concept str:DataConsumer str:DataProvider
    """,
    only=False,
)
# <str:DataProvider> is a reference, e.g. in <str:ConstraintAttachment>
# Restore "Name" and "Description" that may have been stashed by _item_start
@possible_reference(unstash=True)
def _item_end(reader: Reader, elem):
    cls = reader.class_for_tag(elem.tag)
    item = reader.nameable(cls, elem)

    # Hierarchy is stored in two ways

    # (1) XML sub-elements of the parent. These have already been parsed.
    for e in elem:
        if e.tag == elem.tag:
            # Found 1 child XML element with same tag → claim 1 child object
            item.append_child(reader.pop_single(cls))

    # (2) through <str:Parent>. These may be backward or forward references. Backward
    # references can be resolved through pop_resolved_ref(), but forward references
    # cannot.
    if parent := reader.pop_resolved_ref("Parent"):
        if getattr(parent.get_scheme(), "is_external_reference", False):
            # Forward reference
            reader.push("item parent", (item.id, parent.id))
        else:
            # Backward reference
            parent.append_child(item)

    # Agency and subclasses
    if hasattr(item, "contact"):
        item.contact = reader.pop_all(common.Contact)

    reader.unstash()
    return item


@end(
    """
    str:AgencyScheme str:Codelist str:ConceptScheme str:CategoryScheme
    str:CustomTypeScheme str:DataConsumerScheme str:DataProviderScheme
    str:NamePersonalisationScheme str:RulesetScheme str:UserDefinedOperatorScheme
    str:VtlMappingScheme
    """
)
@possible_reference()  # <str:CustomTypeScheme> in <str:Transformation>
def _itemscheme(reader: Reader, elem):
    cls: type[common.ItemScheme] = reader.class_for_tag(elem.tag)

    try:
        args = dict(is_partial=elem.attrib["isPartial"])
    except KeyError:  # e.g. ValueList in .v30
        args = {}

    is_ = reader.maintainable(cls, elem, **args)

    # Iterate over all Item objects *and* their children
    iter_all = chain(*[iter(item) for item in reader.pop_all(cls._Item, subclass=True)])

    # Set of objects already added to `items`
    seen: dict[Any, Any] = dict()

    # Flatten the list, with each item appearing only once
    for i in filter(lambda i: i not in seen, iter_all):
        try:
            is_.append(seen.setdefault(i, i))
        except ValueError:  # pragma: no cover
            # Existing item, e.g. created by a reference in the same message
            # TODO "no cover" since this doesn't occur in the test suite; check whether
            #      this try/except can be removed.
            pass

    # Add deferred forward references
    for child_id, parent_id in reader.pop_all("item parent"):
        try:
            is_[parent_id].append_child(is_[child_id])
        except KeyError:
            if not is_.is_partial:  # pragma: no cover
                raise

    return is_


# §3.6: Structure


@end("str:EnumerationFormat str:TextFormat")
def _facet(reader, elem):
    # Convert attribute names from camelCase to snake_case
    args = {to_snake(key): val for key, val in elem.items()}

    # FacetValueType is given by the "textType" attribute. Convert case of the value:
    # in XML, first letter is uppercase; in the spec and Python enum, lowercase. SDMX-ML
    # default is "String".
    tt = args.pop("text_type", "String")
    try:
        fvt = common.FacetValueType[f"{tt[0].lower()}{tt[1:]}"]
    except KeyError:
        # ExtendedFacetValueType instead. Convert case of the value: in XML, the string
        # is "XHTML", upper case; in the spec and Python enum, "Xhtml", title case.
        fvt = common.ExtendedFacetValueType[f"{tt[0]}{tt[1:].lower()}"]

    # NB Erratum: "isMultiLingual" appears in XSD schemas ("The isMultiLingual attribute
    #    indicates for a text format of type 'string', whether the value should allow
    #    for multiple values in different languages") and in samples, but is not
    #    mentioned anywhere in the information model. Discard.
    args.pop("is_multi_lingual", None)

    # All other attributes are for FacetType
    ft = common.FacetType(**args)

    reader.push(elem, common.Facet(type=ft, value_type=fvt))


@end("str:CoreRepresentation str:LocalRepresentation")
def _rep(reader, elem):
    return common.Representation(
        enumerated=reader.pop_resolved_ref("Enumeration"),
        non_enumerated=list(
            chain(reader.pop_all("EnumerationFormat"), reader.pop_all("TextFormat"))
        ),
    )


# §4.4: Concept Scheme


@end("str:Concept", only=False)
def _concept(reader, elem):
    concept = _item_end(reader, elem)
    concept.core_representation = reader.pop_single(common.Representation)
    return concept


# §3.3: Basic Inheritance

COMPONENT = """
    str:Attribute str:Dimension str:GroupDimension str:IdentifiableObjectTarget
    str:KeyDescriptorValuesTarget str:MeasureDimension str:MetadataAttribute
    str:PrimaryMeasure str:ReportPeriodTarget str:TimeDimension
    """


@start(COMPONENT, only=False)
def _component_start(reader: Reader, elem):
    reader.stash(reader.class_for_tag(elem.tag))


def _maybe_unbounded(value: str) -> Optional[int]:
    return None if value == "unbounded" else int(value)


# TODO Reduce complexity from 12 → ≤10, by adding separate parsers for some COMPONENTs
@end(COMPONENT, only=False)
@possible_reference(unstash=True)
def _component_end(reader: Reader, elem):  # noqa: C901
    cls = reader.class_for_tag(elem.tag)

    args = dict(
        id=elem.attrib.get("id", common.MissingID),
        local_representation=reader.pop_single(common.Representation),
    )
    if position := elem.attrib.get("position"):
        args["order"] = int(position)

    # Resolve a ConceptIdentity reference
    ci_ref = reader.pop_single("ConceptIdentity")
    try:
        args["concept_identity"] = reader.resolve(ci_ref)
    except KeyError:
        message = (
            f"Could not resolve {cls.__name__}.concept_identity reference to {ci_ref!s}"
        )
        log.error(message)
        args.setdefault("annotations", []).append(
            reader.model.Annotation(id=f"{__name__}-parse-error", text=message)
        )

    # DataAttributeOnly
    if us := elem.attrib.get("assignmentStatus"):
        args["usage_status"] = common.UsageStatus[us.lower()]

    if cr := reader.pop_resolved_ref("ConceptRole"):
        args["concept_role"] = cr

    # DataAttribute only
    if ar := reader.pop_all(common.AttributeRelationship, subclass=True):
        assert len(ar) == 1, ar
        args["related_to"] = ar[0]

    if cls is v21.MetadataAttribute:
        setdefault_attrib(args, elem, "isPresentational", "maxOccurs", "minOccurs")
        if "is_presentational" in args:
            args["is_presentational"] = bool(args["is_presentational"])
        for name in "max_occurs", "min_occurs":
            if name in args:
                args[name] = _maybe_unbounded(args[name])
        if children := reader.pop_all(cls):
            args["child"] = children
    elif cls is v21.IdentifiableObjectTarget:
        args["object_type"] = reader.model.get_class(elem.attrib["objectType"])

    reader.unstash()

    # SDMX 2.1 spec §3A, part III, p.140: “The id attribute holds an explicit
    # identification of the component. If this identifier is not supplied, then it is
    # assumed to be the same as the identifier of the concept referenced from the
    # concept identity.”
    if args["id"] is common.MissingID:
        args["id"] = getattr(args["concept_identity"], "id", None) or args["id"]

    return reader.identifiable(cls, elem, **args)


@end(
    """
    str:AttributeList str:DimensionList str:Group str:MetadataTarget str:MeasureList
    str:ReportStructure
    """
)
@possible_reference(cls_hint=common.GroupDimensionDescriptor)  # <str:Group>
def _cl(reader: Reader, elem):
    # Retrieve the DSD (or MSD)
    dsd: common.Structure = reader.peek("current DSD")
    assert dsd is not None

    # Determine the class
    cls = reader.class_for_tag(elem.tag)

    args = dict(
        # Retrieve the components
        components=reader.pop_all(common.Component, subclass=True),
        # SDMX-ML spec for, e.g. DimensionList: "The id attribute is provided in this
        # case for completeness. However, its value is fixed to 'DimensionDescriptor'."
        id=elem.attrib.get("id", cls.__name__),
    )

    if cls is common.GroupDimensionDescriptor:
        assert isinstance(dsd, common.BaseDataStructureDefinition)
        # Replace components with references
        args["components"] = [
            dsd.dimensions.get(ref.target_id)
            for ref in reader.pop_all("DimensionReference")
        ]
    elif cls is v21.ReportStructure:
        assert isinstance(dsd, reader.model.MetadataStructureDefinition)
        # Assemble MetadataTarget references for the `report_for` field
        args["report_for"] = list()
        for target_ref in reader.pop_all(reader.Reference):
            args["report_for"].append(dsd.target[target_ref.id])
    else:
        args["id"] = elem.attrib.get("id", cls.__name__)

    cl = reader.identifiable(cls, elem, **args)

    try:
        # DimensionDescriptor only
        cl.assign_order()
    except AttributeError:
        pass

    # Assign to the DSD eagerly (instead of in _dsd_end()) for reference by next
    # ComponentList e.g. so that AttributeRelationship can reference the
    # DimensionDescriptor
    dsd.replace_grouping(cl)


# §4.5: Category Scheme


@end("str:Categorisation")
def _cat(reader, elem):
    return reader.maintainable(
        common.Categorisation,
        elem,
        artefact=reader.pop_resolved_ref("Source"),
        category=reader.pop_resolved_ref("Target"),
    )


# §4.6: Organisations


@start("mes:Contact str:Contact", only=False)
def _contact_start(reader, elem):
    # Avoid stealing the name of the parent Item
    reader.stash("Name")


@end("mes:Contact str:Contact", only=False)
def _contact_end(reader, elem):
    contact = common.Contact(
        email=reader.pop_all("Email"),
        fax=reader.pop_all("Fax"),
        telephone=reader.pop_single("Telephone"),
        uri=reader.pop_all("URI"),
        x400=reader.pop_all("X400"),
    )

    add_localizations(contact.name, reader.pop_all("Name"))
    add_localizations(contact.org_unit, reader.pop_all("Department"))
    add_localizations(contact.responsibility, reader.pop_all("Role"))

    reader.unstash()

    return contact


# §10.3: Constraints


@end("str:Key")
def _key0(reader, elem):
    # NB this method handles two different usages of an identical tag
    parent = QName(elem.getparent()).localname

    if parent == "DataKeySet":
        # DataKey within DataKeySet
        return reader.model.DataKey(
            included=elem.attrib.get("isIncluded", True),
            # Convert MemberSelection/MemberValue from _ms() to ComponentValue
            key_value={
                ms.values_for: common.ComponentValue(
                    value_for=ms.values_for, value=ms.values.pop().value
                )
                for ms in reader.pop_all(reader.model.MemberSelection)
            },
        )
    else:
        # VTLSpaceKey within VTLMapping
        cls = {
            "FromVtlSuperSpace": common.FromVTLSpaceKey,
            "ToVtlSubSpace": common.ToVTLSpaceKey,
        }[parent]

        return cls(key=elem.text)


@end("str:DataKeySet")
def _dks(reader, elem):
    return reader.model.DataKeySet(
        included=elem.attrib["isIncluded"], keys=reader.pop_all(reader.model.DataKey)
    )


@end("com:StartPeriod com:EndPeriod")
def _p(reader, elem):
    cls = reader.class_for_tag(elem.tag)
    return cls(is_inclusive=elem.attrib["isInclusive"], period=isoparse(elem.text))


@end("com:TimeRange")
def _tr(reader, elem):
    return v21.RangePeriod(
        start=reader.pop_single(v21.StartPeriod), end=reader.pop_single(v21.EndPeriod)
    )


def _ms_component(reader, elem, kind):
    """Identify the Component for a ValueSelection."""
    # Navigate from the current ContentConstraint to a ConstrainableArtefact
    cc_content = reader.stack[reader.Reference]
    if len(cc_content) > 1:
        log.info(
            f"Resolve reference to <{kind[1].__name__} {elem.attrib['id']}> using first"
            f" of {len(cc_content)} constrained objects"
        )
    obj = reader.resolve(next(iter(cc_content.values())))

    if isinstance(obj, common.BaseDataflow):
        # The constrained DFD has a corresponding DSD, which has a Dimension- or
        # AttributeDescriptor
        dsd = obj.structure
    elif isinstance(obj, common.BaseDataStructureDefinition):
        # The DSD is constrained directly
        dsd = obj
    else:
        log.warning(f"Not implemented: constraints attached to {type(obj)}")
        dsd = None

    try:
        # Get the component list
        cl = getattr(dsd, kind[0])
    except AttributeError:
        # Failed because the ContentConstraint is attached to something, e.g.
        # DataProvider, that does not provide an association to a DSD. Try to get a
        # Component from the current scope with matching ID.
        return None, reader.get_single(kind[1], id=elem.attrib["id"], subclass=True)

    # Get the Component
    try:
        c = cl.get(elem.attrib["id"])
    except KeyError:
        if dsd.is_external_reference:
            # No component with the given ID exists, but the DSD is an external
            # reference → create the component automatically
            c = cl.getdefault(elem.attrib["id"])
        else:
            raise

    return cl, c


def _ms_agency_id(elem):
    """Return the MemberSelection → CubeRegion → ContentConstraint → agencyID."""
    try:
        return elem.getparent().getparent().attrib["agencyID"]
    except Exception:  # pragma: no cover
        return None


@end("com:Attribute com:KeyValue")
def _ms(reader, elem):
    """MemberSelection."""
    arg = dict()

    # Identify the component
    # Values are for either a Dimension or Attribute, based on tag name
    kinds = {
        "KeyValue": ("dimensions", common.Dimension),
        "Attribute": ("attributes", common.DataAttribute),
    }
    kind = kinds.get(QName(elem).localname)

    try:
        cl, values_for = _ms_component(reader, elem, kind)
    except KeyError:
        # Maybe work around khaeru/sdmx#102
        # TODO handle quirks via callbacks in data source modules .source.imf
        if _ms_agency_id(elem) == "IMF" and kind[0] == "dimensions":
            log.warning(
                "Work around incorrect use of CubeRegion/KeyValue in IMF "
                "StructureMessage; see https://github.com/khaeru/sdmx/issues/102"
            )
            cl, values_for = _ms_component(reader, elem, kinds["Attribute"])
        else:  # pragma: no cover
            raise

    arg.update(values_for=values_for)

    # Convert to SelectionValue
    mvs = reader.pop_all("Value")
    trv = reader.pop_all(v21.TimeRangeValue, subclass=True)
    if mvs:
        arg["values"] = list(map(lambda v: reader.model.MemberValue(value=v), mvs))
    elif trv:
        arg["values"] = trv
    else:  # pragma: no cover
        raise RuntimeError

    if values_for is None:
        log.warning(
            f"{cl} has no {kind[1].__name__} with ID {elem.attrib['id']}; XML element "
            "ignored and SelectionValues discarded"
        )
        return None
    else:
        return reader.model.MemberSelection(**arg)


@end("str:CubeRegion")
def _cr(reader, elem):
    return common.CubeRegion(
        included=elem.attrib["include"],
        # Combine member selections for Dimensions and Attributes
        member={
            ms.values_for: ms for ms in reader.pop_all(reader.model.MemberSelection)
        },
    )


@end("str:ContentConstraint")
def _cc(reader, elem):
    cls = reader.class_for_tag(elem.tag)

    # The attribute is called "type" in SDMX-ML 2.1; "role" in 3.0
    for name in "type", "role":
        try:
            cr_str = elem.attrib[name].lower().replace("allowed", "allowable")
        except KeyError:
            pass

    content = set()
    for ref in reader.pop_all(reader.Reference):
        resolved = reader.resolve(ref)
        if resolved is None:
            log.warning(f"Unable to resolve {cls.__name__}.content ref:\n  {ref}")
        else:
            content.add(resolved)

    return reader.maintainable(
        cls,
        elem,
        role=common.ConstraintRole(role=common.ConstraintRoleType[cr_str]),
        content=content,
        data_content_keys=reader.pop_single(reader.model.DataKeySet),
        data_content_region=reader.pop_all(common.CubeRegion),
    )


# §5.2: Data Structure Definition


@end("str:None")
def _ar_kind(reader: Reader, elem):
    return reader.class_for_tag(elem.tag)()


@end("str:AttributeRelationship")
def _ar(reader, elem):
    dsd = reader.peek("current DSD")

    refs = reader.pop_all(reader.Reference)
    if not len(refs):
        return

    # Iterate over parsed references to Components
    args = dict(dimensions=list())
    for ref in refs:
        # Use the <Ref id="..."> to retrieve a Component from the DSD
        if issubclass(ref.target_cls, common.DimensionComponent):
            component = dsd.dimensions.get(ref.target_id)
            args["dimensions"].append(component)
        elif ref.target_cls is v21.PrimaryMeasure:
            # Since <str:AttributeList> occurs before <str:MeasureList>, this is
            # usually a forward reference. We *could* eventually resolve it to confirm
            # consistency (the referenced ID is same as the PrimaryMeasure.id), but
            # that doesn't affect the returned value, since PrimaryMeasureRelationship
            # has no attributes.
            return v21.PrimaryMeasureRelationship()
        elif ref.target_cls is common.GroupDimensionDescriptor:
            args["group_key"] = dsd.group_dimensions[ref.target_id]

    ref = reader.pop_single("AttachmentGroup")
    if ref:
        args["group_key"] = dsd.group_dimensions[ref.target_id]

    if len(args["dimensions"]):
        return common.DimensionRelationship(**args)
    else:
        args.pop("dimensions")
        return common.GroupRelationship(**args)


@start("str:DataStructure str:MetadataStructure", only=False)
@possible_reference()  # <str:DataStructure> in <str:ConstraintAttachment>
def _structure_start(reader: Reader, elem):
    # Get any external reference created earlier, or instantiate a new object
    cls = reader.class_for_tag(elem.tag)
    obj = reader.maintainable(cls, elem)

    if obj not in reader.stack[cls]:
        # A new object was created
        reader.push(obj)

    # Store a separate reference to the current DSD
    reader.push("current DSD", obj)


@end("str:DataStructure str:MetadataStructure", only=False)
def _structure_end(reader, elem):
    obj = reader.pop_single("current DSD")

    if obj:
        # Collect annotations, name, and description
        obj.annotations = list(reader.pop_all(reader.model.Annotation))
        add_localizations(obj.name, reader.pop_all("Name"))
        add_localizations(obj.description, reader.pop_all("Description"))


@end("str:Dataflow str:Metadataflow")
@possible_reference()  # <str:Dataflow> in <str:ConstraintAttachment>
def _dfd(reader: Reader, elem):
    structure = reader.pop_resolved_ref("Structure")
    if structure is None:
        log.warning(
            "Not implemented: forward reference to:\n" + etree.tostring(elem).decode()
        )
        arg = {}
    else:
        arg = dict(structure=structure)

    # Create first to collect names
    return reader.maintainable(reader.class_for_tag(elem.tag), elem, **arg)


# §5.4: Data Set


@end("gen:Attributes")
def _avs(reader, elem):
    ad = reader.get_single("DataSet").structured_by.attributes

    result = {}
    for e in elem.iterchildren():
        da = ad.getdefault(e.attrib["id"])
        result[da.id] = common.AttributeValue(value=e.attrib["value"], value_for=da)

    reader.push("Attributes", result)


@end("gen:ObsKey gen:GroupKey gen:SeriesKey")
def _key1(reader, elem):
    cls = reader.class_for_tag(elem.tag)

    kv = {e.attrib["id"]: e.attrib["value"] for e in elem.iterchildren()}

    dsd = reader.get_single("DataSet").structured_by

    return dsd.make_key(cls, kv, extend=True)


@end(":Series gen:Series")
def _series(reader, elem):
    ds = reader.get_single("DataSet")
    if QName(elem).namespace:  # Generic: collect a parsed <gen:SeriesKey> element
        sk = reader.pop_single(common.SeriesKey)
    else:  # Structure-specific: construct the key from attributes of `elem`
        sk = ds.structured_by.make_key(
            common.SeriesKey, elem.attrib, extend=reader.peek("SS without structure")
        )
    sk.attrib.update(reader.pop_single("Attributes") or {})
    ds.add_obs(reader.pop_all(reader.model.Observation), series_key=sk)


@end(":Group gen:Group")
def _group(reader, elem):
    ds = reader.get_single("DataSet")

    if QName(elem).namespace:  # Generic: collect as parsed <gen:GroupKey>
        gk = reader.pop_single(common.GroupKey)
    else:  # Structure-specific: construct the key from attributes of `elem`
        # First remove the group ID
        attrib = copy(elem.attrib)
        group_id = attrib.pop(reader.qname("xsi", "type"), None)

        gk = ds.structured_by.make_key(
            common.GroupKey, attrib, extend=reader.peek("SS without structure")
        )

        if group_id:
            # The group_id is in a format like "foo:GroupName", where "foo" is an XML
            # namespace
            ns, group_id = group_id.split(":")
            assert ns in elem.nsmap

            try:
                gk.described_by = ds.structured_by.group_dimensions[group_id]
            except KeyError:
                if not reader.peek("SS without structure"):
                    raise

    gk.attrib.update(reader.pop_single("Attributes") or {})

    # Group association of Observations is done in _ds_end()
    ds.group[gk] = []


@end("gen:Obs")
def _obs(reader, elem):
    dim_at_obs = reader.get_single(message.DataMessage).observation_dimension
    dsd = reader.get_single("DataSet").structured_by

    args = dict()

    for e in elem.iterchildren():
        localname = QName(e).localname
        if localname == "Attributes":
            args["attached_attribute"] = reader.pop_single("Attributes")
        elif localname == "ObsDimension":
            # Mutually exclusive with ObsKey
            args["dimension"] = dsd.make_key(
                common.Key, {dim_at_obs.id: e.attrib["value"]}
            )
        elif localname == "ObsKey":
            # Mutually exclusive with ObsDimension
            args["dimension"] = reader.pop_single(common.Key)
        elif localname == "ObsValue":
            args["value"] = e.attrib["value"]

    return reader.model.Observation(**args)


@end(":Obs")
def _obs_ss(reader, elem):
    # True if the user failed to provide a DSD to use in parsing structure-specific data
    ss_without_structure = reader.peek("SS without structure")
    dim_at_obs = reader.get_single(message.DataMessage).observation_dimension

    # Retrieve the PrimaryMeasure from the DSD for the current data set
    dsd = reader.get_single("DataSet").structured_by

    try:
        # Retrieve the PrimaryMeasure in a supplied DSD, or one created in a previous
        # call to _obs_ss()
        pm = dsd.measures[0]
    except IndexError:
        # No measures in the DSD
        if ss_without_structure:
            # Create one, assuming the ID OBS_VALUE
            # TODO also add an external reference to the SDMX cross-domain concept
            pm = dsd.measures.getdefault(id="OBS_VALUE")
        else:  # pragma: no cover
            raise  # DSD was provided but lacks a PrimaryMeasure

    # StructureSpecificData message—all information stored as XML attributes of the
    # <Observation>
    # Observation value from an attribute; usually "OBS_VALUE"
    value = elem.attrib.pop(pm.id, None)

    # Transform an attribute like xsi:type="{ns}:{value}" to {dim_at_obs.id}={value}
    try:
        tmp = elem.attrib.pop(reader.qname("xsi:type"))
    except KeyError:
        pass
    else:
        _, elem.attrib[dim_at_obs.id] = tmp.split(":", maxsplit=2)

    if ss_without_structure and dim_at_obs is not common.AllDimensions:
        # Create the observation key
        key = dsd.make_key(common.Key, {dim_at_obs.id: elem.attrib.pop(dim_at_obs.id)})
        # Remaining element attributes are SDMX attribute values
        aa = {}
        for ak, av in elem.attrib.items():
            # Create the DataAttribute in the DSD
            da = dsd.attributes.getdefault(id=ak)
            aa[ak] = common.AttributeValue(value_for=da, value=av)
    else:
        # Use all remaining attributes as dimensions; extend the DSD if appropriate
        key = dsd.make_key(common.Key, elem.attrib, extend=ss_without_structure)
        # Remove attributes from the Key to be attached to the Observation
        aa = key.attrib
        key.attrib = {}

    return reader.model.Observation(
        dimension=key, value=value, value_for=pm, attached_attribute=aa
    )


@start("mes:DataSet", only=False)
def _ds_start(reader, elem):
    # Create an instance of a DataSet subclass
    ds = reader.peek("DataSetClass")()

    # Retrieve the (message-local) ID referencing a data structure definition
    id = elem.attrib.get("structureRef", None) or elem.attrib.get(
        reader.qname("data:structureRef"), None
    )

    # Get a reference to the DSD that structures the data set
    # Provided in the <mes:Header> / <mes:Structure>
    dsd = reader.get_single(id)
    if not dsd:
        # Fall back to a DSD provided as an argument to read_message()
        dsd = reader.get_single(reader.model.DataStructureDefinition)

        if not dsd:  # pragma: no cover
            raise RuntimeError("No DSD when creating DataSet")

        log.debug(
            f'Use provided {dsd!r} for structureRef="{id}" not defined in message'
        )

    ds.structured_by = dsd

    reader.push("DataSet", ds)


@end("mes:DataSet", only=False)
def _ds_end(reader, elem) -> None:
    ds: "common.BaseDataSet" = reader.pop_single("DataSet")

    # Collect attributes attached to the data set. SDMX 2.1 only; this attribute is
    # removed in SDMX 3.0.0.
    if hasattr(ds, "attrib"):
        ds.attrib.update(reader.pop_single("Attributes") or {})

    # Collect observations not grouped by SeriesKey
    ds.add_obs(reader.pop_all(reader.model.Observation))

    if reader.peek("SS without structure"):
        # Possibly convert some inferred dimensions to attributes based on the contents
        # of data

        # Identify dimensions appearing at observation, series, and group keys
        dims = dict(
            obs=set(chain(*[o.dimension.values.keys() for o in ds.obs if o.dimension])),
            series=set(chain(*[sk.values.keys() for sk in ds.series])),
            group=set(chain(*[gk.values.keys() for gk in ds.group])),
        )

        # IDs that appear only on group keys and not on series- or observation keys are
        # likely DataAttribute, not Dimension → convert
        if to_attr := dims["group"] - dims["obs"] - dims["series"]:
            dimensions_to_attributes(ds, to_attr)

    # Add any group associations not made above in add_obs() or in _series()
    for obs in ds.obs:
        ds._add_group_refs(obs)

    # Add the data set to the message
    reader.get_single(message.DataMessage).data.append(ds)


# §7.3: Metadata Structure Definition

# §7.4: Metadata Set


@start("mes:MetadataSet", only=False)
def _mds_start(reader, elem):
    # Create an instance of a MetadataSet
    mds = reader.class_for_tag(elem.tag)()

    # Retrieve the (message-local) ID referencing a data structure definition
    id = (
        elem.attrib.get("structureRef", None)
        or elem.attrib.get(reader.qname("md:structureRef"), None)
        or elem.attrib.get(reader.qname("md_ss:structureRef"), None)
    )

    # Get a reference to the MSD that structures the data set
    # Provided in the <mes:Header> / <mes:Structure>
    msd = reader.get_single(id)
    if not msd:  # pragma: no cover
        # Fall back to a MSD provided as an argument to read_message()
        msd = reader.get_single(common.BaseMetadataStructureDefinition, subclass=True)

        if not msd:
            raise RuntimeError("No MSD when creating DataSet")

        log.debug(
            f'Use provided {msd!r} for structureRef="{id}" not defined in message'
        )

    mds.structured_by = msd

    reader.push("MetadataSet", mds)


@end("mes:MetadataSet", only=False)
def _mds_end(reader, elem):
    # Retrieve the current MetadataSet
    mds = reader.pop_single("MetadataSet")

    # Collect the contained MetadataReports
    mds.report.extend(reader.pop_all(v21.MetadataReport))

    # Collect the ID of the ReportStructure; update the `mds`
    rs_id = set(reader.pop_all("ReportStructure.id"))
    if not mds.structured_by.is_external_reference:
        assert 1 == len(rs_id)
        mds.report_structure = mds.structured_by.report_structure[rs_id.pop()]

    # Add the data set to the message
    reader.get_single(message.MetadataMessage).data.append(mds)


@end(":Report md:Report")
def _md_report(reader: Reader, elem):
    cls = reader.class_for_tag(elem.tag)

    # Identify a ReportStructure within the MetadataStructureDefinition
    rs_id = _get_id(reader, elem)

    # Retrieve a reference to the ReportStructure
    mds = reader.get_single("MetadataSet")
    assert isinstance(mds, v21.MetadataSet) and mds.structured_by is not None
    if not mds.structured_by.is_external_reference:
        rs = mds.structured_by.report_structure[rs_id]
    else:
        rs = None

    # Also push `rs_id`, to be collected in _mds_end()
    reader.push("ReportStructure.id", rs_id)

    # Collect the ID of the MetadataTarget
    mdt_id = set(reader.pop_all("MetadataTarget.id"))
    assert 1 == len(mdt_id)
    # Locate the MetadataTarget
    try:
        mdt = next(
            filter(lambda mdt: {mdt.id} == mdt_id, getattr(rs, "report_for", []))
        )
    except StopIteration:
        mdt = None

    return cls(
        target=mdt,
        attaches_to=reader.pop_single(v21.TargetObjectKey),
        metadata=reader.pop_single("AttributeSet"),
    )


@end(":Target md:Target")
def _tov(reader: Reader, elem):
    cls = reader.class_for_tag(elem.tag)

    # Retrieve the ID for a MetadataTarget within the ReportStructure; push to be
    # collected in _md_report()
    reader.push("MetadataTarget.id", _get_id(reader, elem))

    return cls(
        key_values={
            v.value_for: v for v in reader.pop_all(v21.TargetObjectValue, subclass=True)
        }
    )


@end(":ReferenceValue md:ReferenceValue")
def _rv(reader: Reader, elem):
    cls = reader.class_for_tag(elem[0].tag)

    mds = reader.get_single(common.BaseMetadataStructureDefinition, subclass=True)

    # TODO resolve the TargetObject
    del mds

    # Retrieve the ID for a TargetObject. If structure-specific, the "xsi:type"
    # attribute has a value like "esms:CATEGORY_TARGET.ReportPeriodTarget"
    args = dict(value_for=_get_id(reader, elem))

    if cls is v21.TargetReportPeriod:
        args["report_period"] = reader.pop_single("ReportPeriod")
    elif cls is reader.model.TargetIdentifiableObject:
        or_ = reader.pop_resolved_ref("ObjectReference")
        reader.ignore.add(id(or_.parent))
        args["obj"] = or_

    return cls(**args)


def add_mds_events(reader: Reader, mds: common.BaseMetadataStructureDefinition):
    """Add parser events for structure-specific metadata."""

    # TODO these persist after reading a particular message; avoid this
    def _add_events_for_ma(ma: common.MetadataAttribute):
        reader.end(f":{ma.id}")(_ra)
        for child in ma.child:
            _add_events_for_ma(child)

    for rs in getattr(mds, "report_structure", {}).values():
        for ma in rs.components:
            _add_events_for_ma(ma)


@start(":AttributeSet md:AttributeSet", only=False)
def _as_start(reader: Reader, elem):
    # Avoid collecting previous/sibling ReportedAttribute as children of this one
    reader.stash("ReportedAttribute")


@end(":AttributeSet md:AttributeSet", only=False)
def _as_end(reader: Reader, elem):
    # Collect ReportedAttributes from the current AttributeSet in a list
    reader.push("AttributeSet", reader.pop_all("ReportedAttribute"))
    # Unstash others from the same level
    reader.unstash()


@end("md:ReportedAttribute")
def _ra(reader: Reader, elem):
    args: MutableMapping[str, Any] = dict()

    # Unstash and retrieve child ReportedAttribute
    child = reader.pop_single("AttributeSet")
    if child:
        args.update(child=child)

    # TODO Match value_for to specific common.MetadataAttribute in the ReportStructure
    # # Retrieve the current MetadataSet, MDSD, and ReportStructure
    # mds = cast(v21.MetadataSet, reader.get_single("MetadataSet"))

    try:
        # Set `value_for` using the "id" attribute
        args["value_for"] = elem.attrib["id"]
    except KeyError:
        args["value_for"] = elem.tag

    # Identify a concrete subclass of v21.ReportedAttribute
    xhtml_value_root_elem = reader.pop_single("StructuredText")
    if xhtml_value_root_elem is not None:
        cls: type = v21.XHTMLAttributeValue
        args["value"] = xhtml_value_root_elem
    else:
        # TODO Distinguish v21.EnumeratedAttributeValue
        cls = v21.OtherNonEnumeratedAttributeValue
        try:
            args["value"] = elem.attrib["value"]
        except KeyError:
            if not child:  # pragma: no cover
                raise

    # Push onto a common ReportedAttribute stack; not a subclass-specific stack
    reader.push("ReportedAttribute", cls(**args))


# §8: Hierarchical Code List


@start("str:HierarchicalCode", only=False)
def _hc_start(reader: Reader, elem):
    # Stash:
    # - any NameableArtefacts belonging to the parent Hierarchy or HierarchicalCode
    # - any references to Code or Level belonging to a parent HierarchicalCode
    reader.stash(
        reader.model.Annotation,
        "Name",
        "Description",
        reader.Reference,
        name="ex str:HierarchicalCode",
    )


@end("str:HierarchicalCode", only=False)
def _hc_end(reader: Reader, elem):
    # Retrieve up to 2 references: one to a Code, one to a Level
    refs = {
        getattr(r, "cls", None): r
        for r in [reader.pop_single(reader.Reference) for _ in range(2)]
    }

    # Resolve the reference to a Code
    if code := reader.resolve(refs.pop(common.Codelist, None)):
        pass
    else:
        # Retrieve and resolve a reference to the Codelist
        cl_alias = reader.pop_single("CodelistAliasRef")
        cl_ref = reader.peek("CodelistAlias")[cl_alias]
        cl = reader.resolve(cl_ref)

        # Manually resolve the CodeID
        code_id = reader.pop_single("CodeID").id
        try:
            code = cl[code_id]
        except KeyError:
            if cl.is_external_reference:
                code = cl.setdefault(id=code_id)
            else:  # pragma: no cover
                raise

    # Handle the reference to a Level
    level = None
    if level_ref := refs.pop(reader.model.Hierarchy, None):
        try:
            level = reader.resolve(level_ref)
        except TypeError:
            level = common.Level(id=level_ref.id)

    # Create the HierarchicalCode
    obj = reader.identifiable(
        reader.class_for_tag(elem.tag), elem, code=code, level=level
    )

    # Count children represented as XML sub-elements of the parent
    n_child = sum(e.tag == elem.tag for e in elem)
    # Collect this many children and append them to `obj`
    obj.child.extend(reversed([reader.pop_single(type(obj)) for i in range(n_child)]))

    reader.unstash(name="ex str:HierarchicalCode")

    return obj


@end("str:Level")
@possible_reference()
def _l(reader: Reader, elem):
    cls = reader.class_for_tag(elem.tag)

    return reader.nameable(cls, elem, child=reader.pop_single(cls))


@start("str:Hierarchy", only=False)
def _h_start(reader: Reader, elem):
    # Stash any NameableArtefact objects belonging to the parent HierarchicalCodelist
    reader.stash(
        reader.model.Annotation, "Name", "Description", name="ex str:Hierarchy"
    )


@end("str:Hierarchy", only=False)
def _h_end(reader: Reader, elem):
    result = reader.nameable(
        reader.class_for_tag(elem.tag),
        elem,
        has_formal_levels=eval(elem.attrib.get("leveled", "false").title()),
        codes={c.id: c for c in reader.pop_all(common.HierarchicalCode)},
        level=reader.pop_single(common.Level),
    )

    reader.unstash(name="ex str:Hierarchy")

    return result


@end("str:IncludedCodelist")
def _icl(reader: Reader, elem):
    obj = reader.reference(elem, common.Codelist)

    if reader.peek("CodelistAlias") is None:
        reader.push("CodelistAlias", dict())
    reader.peek("CodelistAlias")[elem.attrib["alias"]] = obj

    return None


@end("str:HierarchicalCodelist")
def _hcl(reader: Reader, elem):
    cls = reader.class_for_tag(elem.tag)
    reader.pop_all("CodelistAlias")
    return reader.maintainable(
        cls, elem, hierarchy=reader.pop_all(reader.model.Hierarchy)
    )


# §9: Structure Set and Mappings


@start("str:CodelistMap", only=False)
def _ismap_start(reader: Reader, elem):
    cls: type[v21.ItemSchemeMap] = reader.class_for_tag(elem.tag)
    # Push class for reference while parsing sub-elements
    reader.push("ItemAssociation class", cls._ItemAssociation._Item)


@end("str:CodelistMap", only=False)
def _ismap_end(reader: Reader, elem):
    cls: type[common.ItemSchemeMap] = reader.class_for_tag(elem.tag)

    # Remove class from stacks
    reader.pop_single("ItemAssociation class")

    # Retrieve the source and target ItemSchemes
    source: common.ItemScheme = reader.pop_resolved_ref("Source")
    target: common.ItemScheme = reader.pop_resolved_ref("Target")

    # Iterate over the ItemAssociation instances
    ia_all = list()
    for ia in reader.pop_all(cls._ItemAssociation):
        for name, scheme in ("source", source), ("target", target):
            # ia.source is a Reference; retrieve its ID
            id_ = getattr(ia, name).id
            try:
                # Use the ID to look up an Item in the ItemScheme
                item = scheme[id_]
            except KeyError:
                if scheme.is_external_reference:
                    # Externally-referenced ItemScheme → create the Item
                    item = scheme.setdefault(id=id_)
                else:  # pragma: no cover
                    raise
            setattr(ia, name, item)

        ia_all.append(ia)

    return reader.nameable(
        cls, elem, source=source, target=target, item_association=ia_all
    )


@end("str:CodeMap")
def _item_map(reader: Reader, elem):
    cls: type[v21.ItemAssociation] = reader.class_for_tag(elem.tag)

    # Store Source and Target as Reference instances
    return reader.annotable(
        cls,
        elem,
        source=reader.pop_single("Source"),
        target=reader.pop_single("Target"),
    )


@end("str:StructureSet")
def _ss(reader: Reader, elem):
    return reader.maintainable(
        v21.StructureSet,
        elem,
        # Collect all ItemSchemeMaps
        item_scheme_map=reader.pop_all(v21.ItemSchemeMap, subclass=True),
    )


# §11: Data Provisioning


@end("str:ProvisionAgreement")
@possible_reference()  # <str:ProvisionAgreement> in <str:ConstraintAttachment>
def _pa(reader, elem):
    return reader.maintainable(
        common.ProvisionAgreement,
        elem,
        structure_usage=reader.pop_resolved_ref("StructureUsage"),
        data_provider=reader.pop_resolved_ref(Reference),
    )


# §??: Validation and Transformation Language


@end("str:CustomType", only=False)
def _ct(reader: Reader, elem):
    ct = _item_end(reader, elem)
    ct.data_type = reader.pop_single("DataType")
    ct.null_value = reader.pop_single("NullValue")
    ct.vtl_scalar_type = reader.pop_single("VtlScalarType")
    return ct


@end("str:NamePersonalisation")
def _np(reader: Reader, elem):
    np = _item_end(reader, elem)
    np.personalised_name = reader.pop_single("PersonalisedName")
    np.vtl_default_name = reader.pop_single("VtlDefaultName")
    return np


@end("str:FromVtlMapping")
def _vtlm_from(reader: Reader, elem):
    return common.VTLtoSDMX[elem.attrib.get("method", "basic").lower()]


@end("str:ToVtlMapping")
def _vtlm_to(reader: Reader, elem):
    return common.SDMXtoVTL[elem.attrib.get("method", "basic").lower()]


# @start("str:Key")
# def _vtl_sk(reader: Reader, elem):


@end("str:Ruleset")
def _rs(reader: Reader, elem):
    # TODO handle .scope, .type
    return reader.nameable(
        common.Ruleset, elem, definition=reader.pop_single("RulesetDefinition")
    )


@end("str:Transformation")
def _trans(reader: Reader, elem):
    # TODO handle .is_persistent
    return reader.nameable(
        common.Transformation,
        elem,
        expression=reader.pop_single("Expression"),
        result=reader.pop_single("Result"),
    )


@end("str:TransformationScheme")
def _ts(reader: Reader, elem):
    ts = _itemscheme(reader, elem)

    while True:
        ref = reader.pop_single(reader.Reference)
        try:
            resolved = reader.resolve(ref)
            ts.update_ref(resolved)
        except TypeError:
            reader.push(ref)
            break

    return ts


@end("str:UserDefinedOperator")
def _udo(reader: Reader, elem):
    return reader.nameable(
        common.UserDefinedOperator,
        elem,
        definition=reader.pop_single("OperatorDefinition"),
    )


@end("str:VtlMapping")
def _vtlm(reader: Reader, elem):
    ref = reader.resolve(reader.pop_single(reader.Reference))
    args: dict[str, Any] = dict()
    if isinstance(ref, common.BaseDataflow):
        cls: type["common.VTLMapping"] = common.VTLDataflowMapping
        args["dataflow_alias"] = ref
        args["to_vtl_method"] = reader.pop_single(common.SDMXtoVTL)
        args["to_vtl_subspace"] = reader.pop_all(common.ToVTLSpaceKey)
        args["from_vtl_method"] = reader.pop_single(common.VTLtoSDMX)
        args["from_vtl_superspace"] = reader.pop_all(common.FromVTLSpaceKey)
    else:
        cls = common.VTLConceptMapping
        args["concept_alias"] = ref

    return reader.nameable(cls, elem, **args)
