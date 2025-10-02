"""Information Model classes common to SDMX 2.1 and 3.0."""
# Class definitions are grouped by section of the spec, but these sections occasionally
# appear out of order so that classes are defined before they are referenced by others.

import logging
import sys
from abc import ABC, abstractmethod
from collections import ChainMap
from copy import copy
from dataclasses import InitVar, dataclass, field, fields
from datetime import date, datetime, timedelta
from enum import Enum
from functools import lru_cache
from itertools import product
from operator import attrgetter, itemgetter
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Generator,
    Generic,
    Iterable,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    TypeVar,
    Union,
    get_args,
    get_origin,
)

from sdmx.compare import Comparable
from sdmx.dictlike import DictLikeDescriptor
from sdmx.rest import Resource
from sdmx.urn import URN
from sdmx.util import direct_fields, only, preserve_dunders

from .internationalstring import (
    DEFAULT_LOCALE,
    InternationalString,
    InternationalStringDescriptor,
)
from .version import Version

if TYPE_CHECKING:
    from dataclasses import Field
    from typing import Self

__all__ = [
    # Re-exported from other modules
    "DEFAULT_LOCALE",
    "InternationalString",
    "Version",
    # From the current module, in the order they appear in this file.
    # Classes named Base* are not included
    "ConstrainableArtefact",
    "AnnotableArtefact",
    "IdentifiableArtefact",
    "NameableArtefact",
    "VersionableArtefact",
    "MaintainableArtefact",
    "ActionType",
    "ConstraintRoleType",
    "FacetValueType",
    "ExtendedFacetValueType",
    "SubmissionStatusType",
    "UsageStatus",
    "Item",
    "ItemScheme",
    "FacetType",
    "Facet",
    "Representation",
    "Code",
    "Codelist",
    "ISOConceptReference",
    "Concept",
    "ConceptScheme",
    "Component",
    "ComponentList",
    "Category",
    "CategoryScheme",
    "Categorisation",
    "Contact",
    "Organisation",
    "Agency",
    "OrganisationScheme",
    "AgencyScheme",
    "Structure",
    "StructureUsage",
    "DimensionComponent",
    "Dimension",
    "TimeDimension",
    "DimensionDescriptor",
    "GroupDimensionDescriptor",
    "AttributeRelationship",
    "DimensionRelationship",
    "GroupRelationship",
    "DataAttribute",
    "AttributeDescriptor",
    "AllDimensions",
    "KeyValue",
    "TimeKeyValue",
    "AttributeValue",
    "Key",
    "GroupKey",
    "SeriesKey",
    "CodingFormat",
    "Level",
    "HierarchicalCode",
    "ConstraintRole",
    "StartPeriod",
    "EndPeriod",
    "CubeRegion",
    "MetadataTargetRegion",
    "DataConsumer",
    "DataProvider",
    "DataConsumerScheme",
    "DataProviderScheme",
    "Datasource",
    "SimpleDatasource",
    "QueryDatasource",
    "RESTDatasource",
    "ProvisionAgreement",
    "CustomType",
    "CustomTypeScheme",
    "NamePersonalisation",
    "NamePersonalisationScheme",
    "Ruleset",
    "RulesetScheme",
    "Transformation",
    "UserDefinedOperator",
    "UserDefinedOperatorScheme",
    "FromVTLSpaceKey",
    "ToVTLSpaceKey",
    "VTLConceptMapping",
    "VTLDataflowMapping",
    "VTLMappingScheme",
    "TransformationScheme",
    "MessageText",
    "StatusMessage",
    "SubmissionResult",
]

log = logging.getLogger(__name__)

# Utility classes not specified in the SDMX standard


class _MissingID(str):
    def __str__(self):
        return "(missing id)"

    # Supplied to allow this as a default value for dataclass fields
    def __hash__(self):
        return hash(None)  # pragma: no cover

    def __eq__(self, other):
        return isinstance(other, self.__class__)


#: Singleton used for :attr:`.IdentifiableArtefact.id` if none given.
MissingID = _MissingID()


# §3.2: Base structures


class ConstrainableArtefact:
    """SDMX ConstrainableArtefact."""


@dataclass
class BaseAnnotation:
    #: Can be used to disambiguate multiple annotations for one AnnotableArtefact.
    id: Optional[str] = None
    #: Title, used to identify an annotation.
    title: Optional[str] = None
    #: Specifies how the annotation is processed.
    type: Optional[str] = None
    #: A link to external descriptive text.
    url: Optional[str] = None

    #: Content of the annotation.
    text: InternationalStringDescriptor = InternationalStringDescriptor()

    @property
    def value(self) -> Optional[str]:
        """A non-localised version of the Annotation content.

        This feature was added by SDMX 3.0.0. In :class:`v30.Annotation`, this can be
        read and written. In this default implementation and in :class:`v21.Annotation`
        the value is always :any:`None`.

        :mod:`sdmx` provides a common attribute so that both classes have identical type
        signatures.
        """
        return None


@dataclass
class AnnotableArtefact(Comparable):
    #: :class:`Annotations <.Annotation>` of the object.
    #:
    #: :mod:`.sdmx` implementation detail: The IM does not specify the name of this
    #: feature.
    annotations: list[BaseAnnotation] = field(default_factory=list)

    def get_annotation(self, **attrib):
        """Return a :class:`Annotation` with given `attrib`, e.g. 'id'.

        If more than one `attrib` is given, all must match a particular annotation.

        Raises
        ------
        KeyError
            If there is no matching annotation.
        """
        for anno in self.annotations:
            if all(getattr(anno, key, None) == value for key, value in attrib.items()):
                return anno

        raise KeyError(attrib)

    def pop_annotation(self, **attrib):
        """Remove and return a :class:`Annotation` with given `attrib`, e.g. 'id'.

        If more than one `attrib` is given, all must match a particular annotation.

        Raises
        ------
        KeyError
            If there is no matching annotation.
        """
        for i, anno in enumerate(self.annotations):
            if all(getattr(anno, key, None) == value for key, value in attrib.items()):
                return self.annotations.pop(i)

        raise KeyError(attrib)

    def eval_annotation(self, id: str, globals=None):
        """Retrieve the annotation with the given `id` and :func:`eval` its contents.

        This can be used for unpacking Python values (e.g. :class:`dict`) stored as an
        annotation on an AnnotableArtefact (e.g. :class:`~sdmx.model.Code`).

        Returns :obj:`None` if no attribute exists with the given `id`.
        """
        try:
            value = str(self.get_annotation(id=id).text)
        except KeyError:  # No such attribute
            return None

        try:
            return eval(value, globals or {})
        except Exception as e:  # Something that can't be eval()'d, e.g. a plain string
            log.debug(f"Could not eval({value!r}): {e}")
            return value


@dataclass
class IdentifiableArtefact(AnnotableArtefact):
    #: Unique identifier of the object.
    id: str = MissingID
    #: Universal resource identifier that may or may not be resolvable.
    uri: Optional[str] = None
    #: Universal resource name. For use in SDMX registries; all registered objects have
    #: a URN.
    urn: Optional[str] = None

    def __post_init__(self):
        # Validate URN, if any
        self._urn = URN(self.urn)

        if self.id is MissingID:
            # Try to retrieve an item ID from the URN, if any
            self.id = self._urn.item_id or self._urn.id or MissingID
        elif self.urn and self.id not in (self._urn.item_id or self._urn.id):
            # Ensure explicit ID is consistent with URN
            raise ValueError(f"ID {self.id} does not match URN {self.urn}")
        elif not isinstance(self.id, str):
            raise TypeError(
                f"IdentifiableArtefact.id must be str; got {type(self.id).__name__}"
            )

    def __eq__(self, other):
        """Equality comparison.

        IdentifiableArtefacts can be compared to other instances. For convenience, a
        string containing the object's ID is also equal to the object.
        """
        if isinstance(other, self.__class__):
            return self.id == other.id
        elif isinstance(other, str):
            return self.id == other

    def __gt__(self, other: Any) -> bool:
        # NB __lt__ handles the case where other is the same type as self
        if isinstance(other, str):
            return self.id > other
        else:
            return NotImplemented

    def __hash__(self):
        return id(self) if self.id == MissingID else hash(self.id)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, IdentifiableArtefact):
            other_id = other.id
        elif isinstance(other, str):
            other_id = other
        else:
            return NotImplemented
        return self.id < other_id

    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"

    @classmethod
    def _preserve(cls, *names: str):
        """Copy dunder `names` from IdentifiableArtefact to a decorated class."""

        def decorator(other_cls):
            for name in map(lambda s: f"__{s}__", names):
                candidates = filter(None, map(lambda k: getattr(k, name), cls.__mro__))
                setattr(other_cls, name, next(candidates))
            return other_cls

        return decorator


@dataclass
@IdentifiableArtefact._preserve("eq", "post_init")
class NameableArtefact(IdentifiableArtefact):
    #: Multi-lingual name of the object.
    name: InternationalStringDescriptor = InternationalStringDescriptor()
    #: Multi-lingual description of the object.
    description: InternationalStringDescriptor = InternationalStringDescriptor()

    def _repr_kw(self) -> MutableMapping[str, str]:
        name = self.name.localized_default()
        return dict(
            cls=self.__class__.__name__, id=self.id, name=f": {name}" if name else ""
        )

    def __repr__(self) -> str:
        return "<{cls} {id}{name}>".format(**self._repr_kw())


@dataclass
class VersionableArtefact(NameableArtefact):
    #: A version string following an agreed convention.
    version: Union[str, Version, None] = None
    #: Date from which the version is valid.
    valid_from: Optional[str] = None
    #: Date from which the version is superseded.
    valid_to: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()

        if not self.version:
            self.version = self._urn.version
        elif isinstance(self.version, str) and self.version == "None":
            self.version = None
        elif self.urn and self.version != self._urn.version:
            raise ValueError(
                f"Version {self.version!r} does not match URN {self.urn!r}"
            )

    def _repr_kw(self) -> MutableMapping[str, str]:
        return ChainMap(
            super()._repr_kw(),
            dict(version=f"({self.version})" if self.version else ""),
        )


@dataclass
class MaintainableArtefact(VersionableArtefact):
    #: True if the object is final; otherwise it is in a draft state.
    is_final: Optional[bool] = None
    #: :obj:`True` if the content of the object is held externally; i.e., not
    #: the current :class:`Message`.
    is_external_reference: Optional[bool] = None
    #: URL of an SDMX-compliant web service from which the object can be retrieved.
    service_url: Optional[str] = None
    #: URL of an SDMX-ML document containing the object.
    structure_url: Optional[str] = None
    #: Association to the Agency responsible for maintaining the object.
    maintainer: Optional["Agency"] = None

    def __post_init__(self):
        super().__post_init__()

        if self.urn:
            if self.maintainer and self.maintainer.id != self._urn.agency:
                raise ValueError(
                    f"Maintainer {self.maintainer} does not match URN {self.urn}"
                )
            else:
                self.maintainer = Agency(id=self._urn.agency)

    def _repr_kw(self) -> MutableMapping[str, str]:
        return ChainMap(
            super()._repr_kw(),
            dict(maint=f"{self.maintainer}:" if self.maintainer else ""),
        )

    def __repr__(self) -> str:
        return "<{cls} {maint}{id}{version}{name}>".format(**self._repr_kw())


class BaseConstraint(ABC, MaintainableArtefact):
    """ABC for SDMX 2.1 and 3.0 Constraint."""

    @abstractmethod
    def __contains__(self, name): ...


# §3.4: Data Types

#: Per the standard…
#:
#: ..
#:
#:    …used to specify the action that a receiving system should take when processing
#:    the content that is the object of the action:
#:
#:    Append
#:       Data or metadata is an incremental update for an existing data/metadata set or
#:       the provision of new data or documentation (attribute values) formerly absent.
#:       If any of the supplied data or metadata is already present, it will not replace
#:       that data or metadata.
#:    Replace
#:       Data/metadata is to be replaced and may also include additional data/metadata
#:       to be appended.
#:    Delete
#:       Data/Metadata is to be deleted.
#:    Information
#:       Data and metadata are for information purposes.
#:
#:    — SDMX 3.0.0 Section 2 §3.4.2.1
ActionType = Enum("ActionType", "delete replace append information")

ConstraintRoleType = Enum("ConstraintRoleType", "allowable actual")

#: SDMX FacetValueType.
#:
#: In the SDMX 2.0 IM, three diagrams in the spec show this enumeration containing
#: 'gregorianYearMonth' but not 'gregorianYear' or 'gregorianMonth'. The table in
#: §3.6.3.3 Representation Constructs does the opposite. One ESTAT query (via SGR) shows
#: a real-world usage of 'gregorianYear'; while one query shows usage of
#: 'gregorianYearMonth'; so all three are included.
FacetValueType = Enum(
    "FacetValueType",
    """string bigInteger integer long short decimal float double boolean uri count
    inclusiveValueRange alpha alphaNumeric numeric exclusiveValueRange incremental
    observationalTimePeriod standardTimePeriod basicTimePeriod gregorianTimePeriod
    gregorianYear gregorianMonth gregorianYearMonth gregorianDay reportingTimePeriod
    reportingYear reportingSemester reportingTrimester reportingQuarter reportingMonth
    reportingWeek reportingDay dateTime timesRange month monthDay day time duration
    keyValues identifiableReference dataSetReference """
    # SDMX 3.0 only
    "geospatialInformation",
)


#: SDMX ExtendedFaceValueType.
#:
#: This enumeration is identical to :class:`.FacetValueType` except for one additional
#: member, "Xhtml". This member is used only in metadata.
ExtendedFacetValueType = Enum(
    "ExtendedFacetValueType",
    """string bigInteger integer long short decimal float double boolean uri count
    inclusiveValueRange alpha alphaNumeric numeric exclusiveValueRange incremental
    observationalTimePeriod standardTimePeriod basicTimePeriod gregorianTimePeriod
    gregorianYear gregorianMonth gregorianYearMonth gregorianDay reportingTimePeriod
    reportingYear reportingSemester reportingTrimester reportingQuarter reportingMonth
    reportingWeek reportingDay dateTime timesRange month monthDay day time duration
    keyValues identifiableReference dataSetReference Xhtml""",
)

#: See :ref:`impl-im-reg`.
SubmissionStatusType = Enum("SubmissionStatusType", "success failure warning")

UsageStatus = Enum("UsageStatus", "mandatory conditional")


# §3.5: Item Scheme

IT = TypeVar("IT", bound="Item")


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class Item(NameableArtefact, Generic[IT]):
    parent: Optional[Union[IT, "ItemScheme"]] = None
    child: list[IT] = field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()

        try:
            # Add this Item as a child of its parent
            self.parent.append_child(self)
        except AttributeError:
            pass  # No parent

        # Add this Item as a parent of its children
        for c in self.child:
            c.parent = self

    def __contains__(self, item):
        """Recursive containment."""
        for c in self.child:
            if item == c or item in c:
                return True

    def __iter__(self, recurse=True):
        yield self
        for c in self.child:
            yield from iter(c)

    @property
    def hierarchical_id(self):
        """Construct the ID of an Item in a hierarchical ItemScheme.

        Returns, for example, 'A.B.C' for an Item with id 'C' that is the child of an
        item with id 'B', which is the child of a root Item with id 'A'.

        See also
        --------
        .ItemScheme.get_hierarchical
        """
        return (
            f"{self.parent.hierarchical_id}.{self.id}"
            if isinstance(self.parent, self.__class__)
            else self.id
        )

    def append_child(self, other: IT):
        if other not in self.child:
            self.child.append(other)
        other.parent = self

    def get_child(self, id) -> IT:
        """Return the child with the given *id*."""
        for c in self.child:
            if c.id == id:
                return c
        raise ValueError(id)

    def get_scheme(self):
        """Return the :class:`ItemScheme` to which the Item belongs, if any."""
        try:
            # Recurse
            return self.parent.get_scheme()
        except AttributeError:
            # Either this Item is a top-level Item whose .parent refers to the
            # ItemScheme, or it has no parent
            return self.parent


@dataclass
class ItemScheme(MaintainableArtefact, Generic[IT]):
    """SDMX-IM Item Scheme.

    The IM states that ItemScheme “defines a *set* of :class:`Items <.Item>`…” To
    simplify indexing/retrieval, this implementation uses a :class:`dict` for the
    :attr:`items` attribute, in which the keys are the :attr:`~.IdentifiableArtefact.id`
    of the Item.

    Because this may change in future versions, user code should not access
    :attr:`items` directly. Instead, use the :func:`getattr` and indexing features of
    ItemScheme, or the public methods, to access and manipulate Items:

    >>> foo = ItemScheme(id='foo')
    >>> bar = Item(id='bar')
    >>> foo.append(bar)
    >>> foo
    <ItemScheme: 'foo', 1 items>
    >>> (foo.bar is bar) and (foo['bar'] is bar) and (bar in foo)
    True

    """

    # TODO add delete()
    # TODO add sorting capability; perhaps sort when new items are inserted

    # NB the IM does not specify; this could be True by default, but would need to check
    # against the automatic construction in .reader.*.
    is_partial: Optional[bool] = None

    #: Members of the ItemScheme. Both ItemScheme and Item are abstract classes.
    #: Concrete classes are paired: for example, a :class:`.Codelist` contains
    #: :class:`Codes <.Code>`.
    items: dict[str, IT] = field(default_factory=dict)

    # The type of the Items in the ItemScheme. This is necessary because the type hint
    # in the class declaration is static; not meant to be available at runtime.
    _Item: ClassVar[type] = Item

    # Convenience access to items
    def __getattr__(self, name: str) -> IT:
        # Provided to pass test_dsd.py
        try:
            return self.__dict__["items"][name]
        except KeyError:
            raise AttributeError(name)

    def __getitem__(self, name: str) -> IT:
        return self.__dict__["items"][name]

    def get(self, id: str, default: Union[str, IT, None] = None) -> Union[str, IT]:
        """Get an Item by its `id`; if not present, return `default`."""
        return self.__dict__["items"].get(id, default)

    def get_hierarchical(self, id: str) -> IT:
        """Get an Item by its :attr:`~.Item.hierarchical_id`."""
        if "." not in id:
            return self.items[id]
        else:
            for item in self.items.values():
                if item.hierarchical_id == id:
                    return item
        raise KeyError(id)

    def __contains__(self, item: Union[str, IT]) -> bool:
        """Check containment.

        No recursive search on children is performed as these are assumed to be included
        in :attr:`items`. Allow searching by Item or its id attribute.
        """
        if isinstance(item, str):
            return item in self.items
        return item in self.items.values()

    def __iter__(self):
        return iter(self.items.values())

    def extend(self, items: Iterable[IT]):
        """Extend the ItemScheme with members of `items`.

        Parameters
        ----------
        items :
            Elements must be of the same class as :attr:`items`.
        """
        for i in items:
            self.append(i)

    def __len__(self):
        return len(self.items)

    def append(self, item: IT):
        """Add *item* to the ItemScheme.

        Parameters
        ----------
        item :
            Item to add. Elements must be of the same class as :attr:`items`.
        """
        if item.id in self.items:
            raise ValueError(f"Item with id {repr(item.id)} already exists")
        self.items[item.id] = item
        if item.parent is None:
            item.parent = self

    def __repr__(self):
        return "<{cls} {maint}{id}{version} ({N} items){name}>".format(
            **self._repr_kw(), N=len(self.items)
        )

    def setdefault(self, obj=None, **kwargs) -> IT:
        """Retrieve the item *name*, or add it with *kwargs* and return it.

        The returned object is a reference to an object in the ItemScheme, and is of the
        appropriate class.
        """
        if obj and len(kwargs):
            raise ValueError(
                "cannot give both *obj* and keyword arguments to setdefault()"
            )

        if not obj:
            # Replace a string 'parent' ID with a reference to the object
            parent = kwargs.pop("parent", None)
            if isinstance(parent, str):
                kwargs["parent"] = self[parent]

            # Instantiate an object of the correct class
            obj = self._Item(**kwargs)

        try:
            # Add the object to the ItemScheme
            self.append(obj)
        except ValueError:
            # Already present; return the existing object, discard the candidate
            return self[obj.id]
        else:
            return obj


# §3.6: Structure


@dataclass
class FacetType:
    #:
    is_sequence: Optional[bool] = None
    #:
    min_length: Optional[int] = None
    #:
    max_length: Optional[int] = None
    #:
    min_value: Optional[float] = None
    #:
    max_value: Optional[float] = None
    #:
    start_value: Optional[float] = None
    #:
    end_value: Optional[str] = None
    #:
    interval: Optional[float] = None
    #:
    time_interval: Optional[timedelta] = None
    #:
    decimals: Optional[int] = None
    #:
    pattern: Optional[str] = None
    #:
    start_time: Optional[datetime] = None
    #:
    end_time: Optional[datetime] = None
    #: SDMX 3.0 only; not present in SDMX 2.1
    sentinel_values: Optional[str] = None

    def __post_init__(self):
        for name in "max_length", "min_length":
            try:
                setattr(self, name, int(getattr(self, name)))
            except TypeError:
                pass


@dataclass
class Facet:
    #:
    type: FacetType = field(default_factory=FacetType)
    #:
    value: Optional[str] = None
    #:
    value_type: Optional[FacetValueType] = None


@dataclass
class Representation:
    #:
    enumerated: Optional[ItemScheme] = None
    #:
    non_enumerated: list[Facet] = field(default_factory=list)

    def __repr__(self):
        return "<{}: {}, {}>".format(
            self.__class__.__name__, self.enumerated, self.non_enumerated
        )


# §4.3: Codelist


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class Code(Item["Code"]):
    """SDMX Code."""


@dataclass
@ItemScheme._preserve("repr")
class Codelist(ItemScheme[IT]):
    """SDMX Codelist."""

    _Item = Code


# §4.4: Concept Scheme


@dataclass
class ISOConceptReference:
    #:
    agency: str
    #:
    id: str
    #:
    scheme_id: str


class Concept(Item["Concept"]):
    #:
    core_representation: Optional[Representation] = None
    #:
    iso_concept: Optional[ISOConceptReference] = None


@dataclass
@ItemScheme._preserve("repr")
class ConceptScheme(ItemScheme[Concept]):
    _Item = Concept


# SDMX 2.1 §3.3: Basic Inheritance
# SDMX 3.0 §3.6: The Structure Pattern


@dataclass
@IdentifiableArtefact._preserve("hash", "repr")
class Component(IdentifiableArtefact):
    #:
    concept_identity: Optional[Concept] = None
    #:
    local_representation: Optional[Representation] = None

    def __contains__(self, value):
        for repr in [
            getattr(self.concept_identity, "core_representation", None),
            self.local_representation,
        ]:
            enum = getattr(repr, "enumerated", None)
            if enum is not None:
                return value in enum
        raise TypeError("membership not defined for non-enumerated representations")


CT = TypeVar("CT", bound=Component)


@dataclass
class ComponentList(IdentifiableArtefact, Generic[CT]):
    #:
    components: list[CT] = field(default_factory=list)
    #: Counter used to automatically populate :attr:`.DimensionComponent.order` values.
    auto_order = 1

    # The default type of the Components in the ComponentList. See comment on
    # ItemScheme._Item
    _Component: ClassVar[type] = Component

    # Convenience access to the components
    def append(self, value: CT) -> None:
        """Append *value* to :attr:`components`."""
        if hasattr(value, "order") and value.order is None:
            value.order = max(self.auto_order, len(self.components) + 1)
            self.auto_order = value.order + 1
        self.components.append(value)

    def extend(self, values: Iterable[CT]) -> None:
        """Extend :attr:`components` with *values*."""
        for value in values:
            self.append(value)

    def get(self, id) -> CT:
        """Return the component with the given *id*."""
        # Search for an existing Component
        for c in self.components:
            if c.id == id:
                return c
        raise KeyError(id)

    def getdefault(self, id, cls=None, **kwargs) -> CT:
        """Return or create the component with the given *id*.

        If the component is automatically created, its :attr:`.Dimension.order`
        attribute is set to the value of :attr:`auto_order`, which is then incremented.

        Parameters
        ----------
        id : str
            Component ID.
        cls : type, optional
            Hint for the class of a new object.
        kwargs
            Passed to the constructor of :class:`.Component`, or a Component subclass if
            :attr:`.components` is overridden in a subclass of ComponentList.
        """
        try:
            return self.get(id)
        except KeyError:
            pass  # No match

        # Create a new object of a class:
        # 1. Given by the cls argument,
        # 2. Specified by a subclass' _default_type attribute, or
        # 3. Hinted for a subclass' components attribute.
        cls = cls or self._Component
        component = cls(id=id, **kwargs)

        if "order" not in kwargs and hasattr(component, "order"):
            # For automatically created dimensions, give a serial value to the order
            # property
            component.order = self.auto_order
            self.auto_order += 1

        self.components.append(component)
        return component

    # Properties of components
    def __getitem__(self, index: int) -> CT:
        """Convenience access to :attr:`components` by index.

        To retrieve components by ID, use :meth:`get`.
        """
        return self.components[index]

    def __len__(self):
        return len(self.components)

    def __iter__(self):
        return iter(self.components)

    def __repr__(self):
        return "<{}: {}>".format(
            self.__class__.__name__, "; ".join(map(repr, self.components))
        )

    def __eq__(self, other):
        """ID equal and same components occur in same order."""
        return super().__eq__(other) and all(
            s == o for s, o in zip(self.components, other.components)
        )

    # Must be reset because __eq__ is defined
    def __hash__(self):
        return super().__hash__()


# §4.5: Category Scheme


class Category(Item["Category"]):
    """SDMX-IM Category."""


class CategoryScheme(ItemScheme[Category]):
    _Item = Category


@dataclass
class Categorisation(MaintainableArtefact):
    #:
    category: Optional[Category] = None
    #:
    artefact: Optional[IdentifiableArtefact] = None


# §4.6: Organisations


@dataclass
class Contact:
    """Organization contact information.

    IMF is the only known data provider that returns messages with :class:`Contact`
    information. These differ from the IM in several ways. This class reflects these
    differences:

    - 'name' and 'org_unit' are InternationalString, instead of strings.
    - 'email' may be a list of e-mail addresses, rather than a single address.
    - 'fax' may be a list of fax numbers, rather than a single number.
    - 'uri' may be a list of URIs, rather than a single URI.
    - 'x400' may be a list of strings, rather than a single string.
    """

    #:
    name: InternationalStringDescriptor = InternationalStringDescriptor()
    #:
    org_unit: InternationalStringDescriptor = InternationalStringDescriptor()
    #:
    telephone: Optional[str] = None
    #:
    responsibility: InternationalStringDescriptor = InternationalStringDescriptor()
    #:
    email: list[str] = field(default_factory=list)
    #:
    fax: list[str] = field(default_factory=list)
    #:
    uri: list[str] = field(default_factory=list)
    #:
    x400: list[str] = field(default_factory=list)


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class Organisation(Item["Organisation"]):
    #:
    contact: list[Contact] = field(default_factory=list)


class OrganisationScheme(ItemScheme[IT]):
    """SDMX OrganisationScheme (abstract class)."""

    _Item = Organisation


# @NameableArtefact._preserve("repr")
class Agency(Organisation):
    """SDMX-IM Organization.

    This class is identical to its parent class.
    """


class AgencyScheme(OrganisationScheme[Agency]):
    _Item = Agency


class DataConsumer(Organisation, ConstrainableArtefact):
    """SDMX DataConsumer."""


class DataConsumerScheme(OrganisationScheme[DataConsumer]):
    _Item = DataConsumer


class DataProvider(Organisation, ConstrainableArtefact):
    """SDMX DataProvider."""


class DataProviderScheme(OrganisationScheme[DataProvider]):
    _Item = DataProvider


# SDMX 3.0 §5.3: Data Structure Definition


@dataclass(repr=False)
class Structure(MaintainableArtefact):
    @classmethod
    @lru_cache
    def _cl_fields(cls) -> tuple[tuple["Field", bool, type[ComponentList]], ...]:
        """Tuple of fields typed as ComponentList or DictLike[…, ComponentList]."""
        result = []
        for f in fields(cls):
            is_dictlike = get_origin(f.type) is DictLikeDescriptor
            cl_type = get_args(f.type)[1] if is_dictlike else f.type
            if type(cl_type) is type and issubclass(cl_type, ComponentList):
                result.append((f, is_dictlike, cl_type))
        return tuple(result)

    @property
    def grouping(self) -> Sequence[ComponentList]:
        """A collection of all the ComponentLists associated with a subclass."""
        result: list[ComponentList] = []
        for f, is_dictlike, _ in self._cl_fields():
            value = getattr(self, f.name)
            if is_dictlike:
                result.extend(value.values())
            else:
                result.append(value)
        return result

    def replace_grouping(self, cl: ComponentList) -> None:
        """Replace existing component list with `cl`."""
        try:
            (field, is_dictlike, _), *_ = filter(
                lambda t: t[2] is type(cl), self._cl_fields()
            )
        except ValueError:
            raise TypeError(f"No grouping of type {type(cl)} on {type(self)}")

        if is_dictlike:
            # Set an element in e.g. BaseDataStructureDefinition.group_dimension
            getattr(self, field.name).setdefault(cl.id, cl)
        else:
            # Set an instance attribute, e.g. BaseDataStructureDefinition.attributes
            setattr(self, field.name, cl)


class StructureUsage(MaintainableArtefact):
    #:
    structure: Optional[Structure] = None


@dataclass
@IdentifiableArtefact._preserve("eq", "hash", "repr")
class DimensionComponent(Component):
    """SDMX DimensionComponent (abstract class)."""

    #:
    order: Optional[int] = None


@dataclass
@IdentifiableArtefact._preserve("eq", "hash", "repr")
class Dimension(DimensionComponent):
    """SDMX Dimension."""

    #:
    concept_role: Optional[Concept] = None


class TimeDimension(DimensionComponent):
    """SDMX TimeDimension."""


@dataclass
class DimensionDescriptor(ComponentList[DimensionComponent]):
    """Describes a set of dimensions.

    IM: “An ordered set of metadata concepts that, combined, classify a statistical
    series, and whose values, when combined (the key) in an instance such as a data set,
    uniquely identify a specific observation.”

    :attr:`.components` is a :class:`list` (ordered) of :class:`Dimension`,
    :class:`MeasureDimension`, and/or :class:`TimeDimension`.
    """

    _Component = Dimension

    def __post_init__(self):
        try:
            # Sort components by already assigned 'order' attributes
            self.components = sorted(self.components, key=lambda c: c.order)
        except TypeError:
            pass  # Some or all of the order attributes are None

    def assign_order(self):
        """Assign the :attr:`.DimensionComponent.order` attribute.

        The Dimensions in :attr:`components` are numbered, starting from 1.
        """
        for i, component in enumerate(self.components):
            component.order = i + 1

    def order_key(self, key):
        """Return a key ordered according to the DSD."""
        result = key.__class__()
        for dim in sorted(self.components, key=attrgetter("order")):
            try:
                result.values[dim.id] = key[dim.id]
            except KeyError:
                continue
        return result

    @classmethod
    def from_key(cls, key):
        """Create a new DimensionDescriptor from a *key*.

        For each :class:`KeyValue` in the *key*:

        - A new :class:`Dimension` is created.
        - A new :class:`Codelist` is created, containing the
          :attr:`KeyValue.value`.

        Parameters
        ----------
        key : :class:`Key` or :class:`GroupKey` or :class:`SeriesKey`
        """
        dd = cls()
        for order, (id, kv) in enumerate(key.values.items()):
            cl = Codelist(id=id)
            cl.append(Code(id=str(kv.value)))
            dd.components.append(
                Dimension(
                    id=id,
                    local_representation=Representation(enumerated=cl),
                    order=order,
                )
            )
        return dd


class GroupDimensionDescriptor(DimensionDescriptor):
    #:
    attachment_constraint: Optional[bool] = None
    # #:
    # constraint: Optional[AttachmentConstraint] = None

    def assign_order(self):
        """:meth:`assign_order` has no effect for GroupDimensionDescriptor."""
        pass


@dataclass
class AttributeRelationship:
    pass


@dataclass
class DimensionRelationship(AttributeRelationship):
    #:
    dimensions: list[DimensionComponent] = field(default_factory=list)
    #: NB the IM says "0..*" here in a diagram, but the text does not match.
    group_key: Optional["GroupDimensionDescriptor"] = None


@dataclass
class GroupRelationship(AttributeRelationship):
    #: “Retained for compatibility reasons” in SDMX 2.1 versus 2.0; not used by
    #: :mod:`sdmx`.
    group_key: Optional["GroupDimensionDescriptor"] = None


@dataclass
@NameableArtefact._preserve("eq", "hash")
class DataAttribute(Component):
    #:
    related_to: Optional[AttributeRelationship] = None
    #:
    usage_status: Optional[UsageStatus] = None
    #:
    concept_role: Optional[Concept] = None


class AttributeDescriptor(ComponentList[DataAttribute]):
    _Component = DataAttribute


@dataclass(repr=False)
@IdentifiableArtefact._preserve("hash")
class BaseDataStructureDefinition(Structure, ConstrainableArtefact):
    """Common features of SDMX 2.1 and 3.0 DataStructureDefinition (**DSD**)."""

    #: A :class:`AttributeDescriptor` that describes the attributes of the data
    #: structure.
    attributes: AttributeDescriptor = field(default_factory=AttributeDescriptor)
    #: A :class:`DimensionDescriptor` that describes the dimensions of the data
    #: structure.
    dimensions: DimensionDescriptor = field(default_factory=DimensionDescriptor)
    #: Mapping from  :attr:`.GroupDimensionDescriptor.id` to
    #: :class:`.GroupDimensionDescriptor`.
    group_dimensions: DictLikeDescriptor[str, GroupDimensionDescriptor] = (
        DictLikeDescriptor()
    )

    # Specific types to be used in concrete subclasses
    MemberValue: ClassVar[type["BaseMemberValue"]]
    MemberSelection: ClassVar[type["BaseMemberSelection"]]
    ConstraintType: ClassVar[type[BaseConstraint]]

    # Convenience methods
    def iter_keys(
        self, constraint: Optional[BaseConstraint] = None, dims: list[str] = []
    ) -> Generator["Key", None, None]:
        """Iterate over keys.

        Parameters
        ----------
        constraint : :class:`Constraint <.BaseConstraint>`, optional
            If given, only yield Keys that are within the constraint.
        dims : list of str, optional
            If given, only iterate over allowable values for the Dimensions with these
            IDs. Other dimensions have only a single value like "(DIM_ID)", where
            DIM_ID is the ID of the dimension.
        """
        # NB for performance, the implementation tries to use iterators and avoid
        #    constructing full-length tuples/lists at any point

        _constraint = constraint or NullConstraint
        dims = dims or [dim.id for dim in self.dimensions.components]

        # Utility to return an immutable function that produces KeyValues. The
        # arguments are frozen so these can be set using loop variables and stored in a
        # map() object that isn't modified on future loops
        def make_factory(id=None, value_for=None):
            return lambda value: KeyValue(id=id, value=value, value_for=value_for)

        # List of iterables of (dim.id, KeyValues) along each dimension
        all_kvs: list[Iterable[KeyValue]] = []

        # Iterate over dimensions
        for dim in self.dimensions.components:
            if (
                dim.id not in dims
                or dim.local_representation is None
                or dim.local_representation.enumerated is None
            ):
                # `dim` is not enumerated by an ItemScheme, or not included in the
                # `dims` argument and not to be iterated over. Create a placeholder.
                all_kvs.append(
                    [KeyValue(id=dim.id, value=f"({dim.id})", value_for=dim)]
                )
            else:
                # Create a KeyValue for each Item in the ItemScheme; filter through any
                # constraint.
                all_kvs.append(
                    filter(
                        _constraint.__contains__,
                        map(
                            make_factory(id=dim.id, value_for=dim),
                            dim.local_representation.enumerated,
                        ),
                    ),
                )

        # Create Key objects from Cartesian product of KeyValues along each dimension
        # NB this does not work with DataKeySet
        # TODO improve to work with DataKeySet
        yield from filter(_constraint.__contains__, map(Key, product(*all_kvs)))

    def make_constraint(self, key):
        """Return a constraint for `key`.

        `key` is a :class:`dict` wherein:

        - keys are :class:`str` ids of Dimensions appearing in this DSD's
          :attr:`dimensions`, and
        - values are '+'-delimited :class:`str` containing allowable values, *or*
          iterables of :class:`str`, each an allowable value.

        For example::

            cc2 = dsd.make_constraint({'foo': 'bar+baz', 'qux': 'q1+q2+q3'})

        ``cc2`` includes any key where the 'foo' dimension is 'bar' *or* 'baz', *and*
        the 'qux' dimension is one of 'q1', 'q2', or 'q3'.

        Returns
        -------
        ContentConstraint
            A constraint with one :class:`CubeRegion` in its
            :attr:`data_content_region <ContentConstraint.data_content_region>` ,
            including only the values appearing in `key`.

        Raises
        ------
        ValueError
            if `key` contains a dimension IDs not appearing in :attr:`dimensions`.
        """
        # Make a copy to avoid pop()'ing off the object in the calling scope
        key = key.copy()

        cr = CubeRegion()
        for dim in self.dimensions:
            mvs = set()
            try:
                values = key.pop(dim.id)
            except KeyError:
                continue

            values = values.split("+") if isinstance(values, str) else values
            for value in values:
                # TODO validate values
                mvs.add(self.MemberValue(value=value))

            cr.member[dim] = self.MemberSelection(
                included=True, values_for=dim, values=mvs
            )

        if len(key):
            raise ValueError(
                "Dimensions {!r} not in {!r}".format(list(key.keys()), self.dimensions)
            )

        return self.ConstraintType(
            data_content_region=[cr],
            role=ConstraintRole(role=ConstraintRoleType.allowable),
        )

    @classmethod
    def from_keys(cls, keys):
        """Return a new DSD given some *keys*.

        The DSD's :attr:`dimensions` refers to a set of new :class:`Concepts <Concept>`
        and :class:`Codelists <Codelist>`, created to represent all the values observed
        across *keys* for each dimension.

        Parameters
        ----------
        keys : iterable of :class:`Key`
            or of subclasses such as :class:`SeriesKey` or :class:`GroupKey`.
        """
        iter_keys = iter(keys)
        dd = DimensionDescriptor.from_key(next(iter_keys))

        for k in iter_keys:
            for i, (id, kv) in enumerate(k.values.items()):
                try:
                    dd[i].local_representation.enumerated.append(Code(id=str(kv.value)))
                except ValueError:
                    pass  # Item already exists

        return cls(dimensions=dd)

    def make_key(self, key_cls, values: Mapping, extend=False, group_id=None):
        """Make a :class:`.Key` or subclass.

        Parameters
        ----------
        key_cls : Key or SeriesKey or GroupKey
            Class of Key to create.
        values : dict
            Used to construct :attr:`.Key.values`.
        extend : bool, optional
            If :obj:`True`, make_key will not return :class:`KeyError` on missing
            dimensions. Instead :attr:`dimensions` (`key_cls` is Key or SeriesKey) or
            :attr:`group_dimensions` (`key_cls` is GroupKey) will be extended by
            creating new Dimension objects.
        group_id : str, optional
            When `key_cls` is :class`.GroupKey`, the ID of the
            :class:`.GroupDimensionDescriptor` that structures the key.

        Returns
        -------
        Key
            An instance of `key_cls`.

        Raises
        ------
        KeyError
            If any of the keys of `values` is not a Dimension or Attribute in the DSD.
        """
        # Methods to get dimensions and attributes
        get_method = "getdefault" if extend else "get"
        dim = getattr(self.dimensions, get_method)
        attr = getattr(self.attributes, get_method)

        # Arguments for creating the Key
        args: dict[str, Any] = dict(described_by=self.dimensions)

        if key_cls is GroupKey:
            # Get the GroupDimensionDescriptor, if indicated by group_id
            gdd = self.group_dimensions.get(group_id, None)

            if group_id and not gdd and not extend:
                # Cannot create
                raise KeyError(group_id)
            elif group_id and extend:
                # Create the GDD
                gdd = GroupDimensionDescriptor(id=group_id)
                self.group_dimensions[gdd.id] = gdd

                # GroupKey will have same ID and be described by the GDD
                args = dict(id=group_id, described_by=gdd)

                # Dimensions to be retrieved from the GDD
                def dim(id):  # noqa: F811
                    # Get from the DimensionDescriptor
                    new_dim = self.dimensions.getdefault(id)
                    # Add to the GDD
                    gdd.components.append(new_dim)
                    return gdd.get(id)

            else:
                # Not described by anything
                args = dict()

        key = key_cls(**args)

        # Convert keyword arguments to either KeyValue or AttributeValue
        keyvalues = []
        for order, (id, value) in enumerate(values.items()):
            if id in self.attributes.components:
                # Reference a DataAttribute from the AttributeDescriptor
                da = attr(id)
                # Store the attribute value, referencing da
                key.attrib[da.id] = AttributeValue(value=value, value_for=da)
                continue

            # Reference a Dimension from the DimensionDescriptor. If extend=False and
            # the Dimension does not exist, this will raise KeyError.
            value_for = dim(id)

            # Use the dimension's order instead of the order in `values`
            order = value_for.order

            # If an itemscheme is available, convert `value` into an Item
            if value_for.local_representation:
                if cl := value_for.local_representation.enumerated:
                    value = cl.get(value, value)

            # Store a KeyValue, to be sorted later
            keyvalues.append((order, KeyValue(id=id, value=value, value_for=value_for)))

        # Sort the values according to *order*
        key.values.update({kv.id: kv for _, kv in sorted(keyvalues)})

        return key


@dataclass(repr=False)
class BaseDataflow(StructureUsage, ConstrainableArtefact):
    """Common features of SDMX 2.1 DataflowDefinition and 3.0 Dataflow."""

    structure: BaseDataStructureDefinition = field(
        default_factory=BaseDataStructureDefinition
    )

    def __post_init__(self):
        super().__post_init__()

        # Factory default `structure` inherits is_external_reference from the data flow
        if self.structure.is_external_reference is None:
            self.structure.is_external_reference = self.is_external_reference

    def iter_keys(
        self, constraint: Optional[BaseConstraint] = None, dims: list[str] = []
    ) -> Generator["Key", None, None]:
        """Iterate over keys.

        See also
        --------
        .BaseDataStructureDefinition.iter_keys
        """
        yield from self.structure.iter_keys(constraint=constraint, dims=dims)


class _AllDimensions:
    pass


#: A singleton.
AllDimensions = _AllDimensions()


# §5.4: Data Set


def value_for_dsd_ref(kind, args, kwargs):
    """Maybe replace a string 'value_for' in *kwargs* with a DSD reference."""
    try:
        dsd = kwargs.pop("dsd")
        descriptor = getattr(dsd, kind + "s")
        kwargs["value_for"] = descriptor.get(kwargs["value_for"])
    except KeyError:
        pass
    return args, kwargs


@dataclass
class KeyValue:
    """One value in a multi-dimensional :class:`Key`."""

    #:
    id: str
    #: The actual value.
    value: Any
    #:
    value_for: Optional[DimensionComponent] = None

    dsd: InitVar[BaseDataStructureDefinition] = None

    def __post_init__(self, dsd):
        if dsd:
            self.value_for = getattr(dsd, "dimensions").get(self.value_for)

    def __eq__(self, other):
        """Compare the value to a simple Python built-in type or other key-like.

        `other` may be :class:`.KeyValue` or :class:`.ComponentValue`; if so, and both
        `self` and `other` have :attr:`.value_for`, these must refer to the same object.
        """
        other_value = self._compare_value(other)
        result = self.value == other_value
        if isinstance(other, (KeyValue, ComponentValue)):
            result &= (
                self.value_for in (None, other.value_for) or other.value_for is None
            )
        return result

    @staticmethod
    def _compare_value(other):
        if isinstance(other, (KeyValue, ComponentValue, BaseMemberValue)):
            return other.value
        else:
            return other

    def __lt__(self, other):
        return self.value < self._compare_value(other)

    def __str__(self):
        return f"{self.id}={self.value}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.id}={self.value}>"

    def __hash__(self):
        # KeyValue instances with the same id & value hash identically
        return hash(self.id + str(self.value))


class TimeKeyValue(KeyValue):
    """SDMX TimeKeyValue.

    Identical to its parent class.
    """


@dataclass
class AttributeValue(Comparable):
    """SDMX AttributeValue.

    In the spec, AttributeValue is an abstract class. Here, it serves as both the
    concrete subclasses CodedAttributeValue and UncodedAttributeValue.

    .. important:: The SDMX 3.0.0 “Summary of major changes and new functionality”
       document mentions (§2.3 Information Model, p.8) “new features such as
       multiple measures and value arrays for measures and attributes,” and the
       SDMX-ML 3.0.0 examples (such as `ECB_EXR_CA.xml <https://github.com/sdmx-twg/
       sdmx-ml/blob/29f1a3d856c4259429f5ec0eae811653adc5cdb5/samples/
       Data%20-%20Complex%20Data%20Attributes/ECB_EXR_CA.xml>`_) indicate that this
       can be a “value array,” but the SDMX 3.0.0 IM (Figure 31/§5.4.2, p.84) gives
       only ‘String’ as the type of :py:`UncodedAttributeValue.value`. No class for
       multiple values is described.

       As a consequence, when such multiply-valued attributes are parsed from SDMX-ML,
       the type annotation for :attr:`value` will be incorrect. The actual type may be
       :py:`list[str]`, :py:`list[Code]`, or something else.

    .. todo:: Separate and enforce properties of Coded- and UncodedAttributeValue.
    """

    #:
    value: Union[str, Code]
    #:
    value_for: Optional[DataAttribute] = None
    #:
    start_date: Optional[date] = None

    dsd: InitVar[BaseDataStructureDefinition] = None

    def __post_init__(self, dsd):
        if dsd:
            self.value_for = getattr(dsd, "attributes").get(self.value_for)

    def __eq__(self, other):
        """Compare the value to a Python built-in type, e.g. str."""
        return self.value == other

    def __str__(self):
        # self.value directly for UncodedAttributeValue
        return getattr(
            self.value,
            "id",
            self.value if isinstance(self.value, str) else repr(self.value),
        )

    def __repr__(self):
        return "<{}: {}={}>".format(self.__class__.__name__, self.value_for, self.value)


@dataclass
class Key:
    """SDMX Key class.

    The constructor takes an optional list of keyword arguments; the keywords are used
    as Dimension or Attribute IDs, and the values as KeyValues.

    For convenience, the values of the key may be accessed directly:

    >>> k = Key(foo=1, bar=2)
    >>> k.values['foo']
    1
    >>> k['foo']
    1

    Parameters
    ----------
    dsd : DataStructureDefinition <.BaseDataStructureDefinition>
        If supplied, the :attr:`~.BaseDataStructureDefinition.dimensions` and
        :attr:`~.BaseDataStructureDefinition.attributes` are used to separate the
        `kwargs` into :class:`KeyValues <.KeyValue>` and
        :class:`AttributeValues <.AttributeValue>`. The `kwargs` for
        :attr:`described_by`, if any, must be
        :attr:`~.BaseDataStructureDefinition.dimensions` or appear in
        :attr:`~.BaseDataStructureDefinition.group_dimensions`.
    kwargs
        Dimension and Attribute IDs, and/or the class properties.

    """

    #:
    attrib: DictLikeDescriptor[str, AttributeValue] = DictLikeDescriptor()
    #:
    described_by: Optional[DimensionDescriptor] = None
    #: Individual KeyValues that describe the key.
    values: DictLikeDescriptor[str, KeyValue] = DictLikeDescriptor()

    def __init__(self, arg: Union[Mapping, Sequence[KeyValue], None] = None, **kwargs):
        # Handle kwargs corresponding to attributes
        self.attrib.update(kwargs.pop("attrib", {}))

        # DimensionDescriptor
        dd = kwargs.pop("described_by", None)
        self.described_by = dd

        if arg and isinstance(arg, Mapping):
            if len(kwargs):
                raise ValueError(
                    "Key() accepts either a single argument, or keyword arguments; not "
                    "both."
                )
            kwargs.update(arg)

        kvs: Iterable[tuple] = []

        if isinstance(arg, Sequence):
            # Sequence of already-prepared KeyValues; assume already sorted
            kvs = map(lambda kv: (kv.id, kv), arg)
        else:
            # Convert bare keyword arguments to KeyValue
            _kvs = []
            for order, (id, value) in enumerate(kwargs.items()):
                args = dict(id=id, value=value)
                if dd:
                    # Reference the Dimension
                    args["value_for"] = dd.get(id)
                    # Use the existing Dimension's order attribute
                    order = args["value_for"].order

                # Store a KeyValue, to be sorted later
                _kvs.append((order, (id, KeyValue(**args))))

            # Sort the values according to *order*, then unwrap
            kvs = map(itemgetter(1), sorted(_kvs))

        self.values.update(kvs)

    def __len__(self):
        """The length of the Key is the number of KeyValues it contains."""
        return len(self.values)

    def __contains__(self, other):
        """A Key contains another if it is a superset."""
        try:
            return all([self.values[k] == v for k, v in other.values.items()])
        except KeyError:
            # 'k' in other does not appear in this Key()
            return False

    def __iter__(self):
        yield from self.values.values()

    # Convenience access to values by name
    def __getitem__(self, name) -> "KeyValue":
        return self.values[name]

    def __setitem__(self, name, value):
        # Convert a bare string or other Python object to a KeyValue instance
        if not isinstance(value, KeyValue):
            value = KeyValue(id=name, value=value)
        self.values[name] = value

    # Convenience access to values by attribute
    def __getattr__(self, name):
        try:
            return self.values[name]
        except KeyError:
            raise AttributeError(name)

    # Copying
    def __copy__(self):
        result = type(self)()
        if self.described_by:
            result.described_by = self.described_by
        result.values.update_fast(self.values)
        return result

    def copy(self, arg=None, **kwargs):
        result = copy(self)
        for id, value in kwargs.items():
            result[id] = value
        return result

    def __add__(self, other):
        result = copy(self)
        if not isinstance(other, Key) and other is not None:
            raise NotImplementedError
        else:
            result.values.update_fast(other.values)
        return result

    def __radd__(self, other):
        if other is None:
            return copy(self)
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if hasattr(other, "values"):
            # Key
            return all(
                [a == b for a, b in zip(self.values.values(), other.values.values())]
            )
        elif hasattr(other, "key_value"):
            # DataKey
            return all(
                [a == b for a, b in zip(self.values.values(), other.key_value.values())]
            )
        elif isinstance(other, str) and len(self.values) == 1:
            return self.values[0] == other
        else:
            raise ValueError(other)

    def __hash__(self):
        # Hash of the individual KeyValues, in order
        return hash(tuple(hash(kv) for kv in self.values.values()))

    def __lt__(self, other: "Self") -> bool:
        return sorted(self.values.values()) < sorted(other.values.values())

    # Representations

    def __str__(self):
        return "({})".format(", ".join(map(str, self.values.values())))

    def __repr__(self):
        return "<{}: {}>".format(
            self.__class__.__name__, ", ".join(map(str, self.values.values()))
        )

    def order(self, value=None):
        if value is None:
            value = self
        try:
            return self.described_by.order_key(value)
        except AttributeError:
            return value

    def get_values(self):
        return tuple([kv.value for kv in self.values.values()])


@dataclass
@preserve_dunders(Key, "hash")
class GroupKey(Key):
    #:
    id: Optional[str] = None
    #:
    described_by: Optional[GroupDimensionDescriptor] = None

    def __init__(self, arg: Optional[Mapping] = None, **kwargs):
        # Remove the 'id' keyword argument
        id = kwargs.pop("id", None)
        super().__init__(arg, **kwargs)
        self.id = id


@dataclass
class SeriesKey(Key):
    #: :mod:`sdmx` extension not in the IM.
    group_keys: set[GroupKey] = field(default_factory=set)

    __eq__ = Key.__eq__
    __hash__ = Key.__hash__
    __repr__ = Key.__repr__

    @property
    def group_attrib(self):
        """Return a view of attributes on all :class:`GroupKey` including the series."""
        # Needed to pass existing tests
        view = dict()
        for gk in self.group_keys:
            view.update(gk.attrib)
        return view


@dataclass
class BaseObservation(Comparable):
    """Common features of SDMX 2.1 and 3.0 Observation.

    This class also implements the IM classes ObservationValue, UncodedObservationValue,
    and CodedObservation.
    """

    #:
    attached_attribute: DictLikeDescriptor[str, AttributeValue] = DictLikeDescriptor()
    #:
    series_key: Optional[SeriesKey] = None
    #: Key for dimension(s) varying at the observation level.
    dimension: Optional[Key] = None
    #: Data value.
    value: Optional[Union[Any, Code]] = None
    #: :mod:`sdmx` extension not in the IM.
    group_keys: set[GroupKey] = field(default_factory=set)

    @property
    def attrib(self):
        """Return a view of combined observation, series & group attributes."""
        view = self.attached_attribute.copy()
        view.update(getattr(self.series_key, "attrib", {}))
        for gk in self.group_keys:
            view.update(gk.attrib)
        return view

    @property
    def dim(self):
        return self.dimension

    @property
    def key(self):
        """Return the entire key, including KeyValues at the series level."""
        return (self.series_key or SeriesKey()) + self.dimension

    def __len__(self):
        # FIXME this is unintuitive; maybe deprecate/remove?
        return len(self.key)

    def __str__(self):
        return "{0.key}: {0.value}".format(self)


@dataclass
class BaseDataSet(AnnotableArtefact):
    """Common features of SDMX 2.1 and 3.0 DataSet."""

    #: Action to be performed
    action: Optional[ActionType] = None
    #:
    valid_from: Optional[str] = None

    #: Association to the :class:`Dataflow <.BaseDataflow>` that contains the data set.
    described_by: Optional[BaseDataflow] = None

    #: Association to the :class:`DataStructure <.BaseDataStructureDefinition` that
    #: defines the structure of the data set.
    structured_by: Optional[BaseDataStructureDefinition] = None

    #: All observations in the DataSet.
    obs: list[BaseObservation] = field(default_factory=list)

    #: Map of series key → list of observations.
    #: :mod:`sdmx` extension not in the IM.
    series: DictLikeDescriptor[SeriesKey, list[BaseObservation]] = DictLikeDescriptor()
    #: Map of group key → list of observations.
    #: :mod:`sdmx` extension not in the IM.
    group: DictLikeDescriptor[GroupKey, list[BaseObservation]] = DictLikeDescriptor()

    def __post_init__(self):
        if self.action and not isinstance(self.action, ActionType):
            self.action = ActionType[self.action]

    def __len__(self):
        return len(self.obs)

    def _add_group_refs(self, target) -> None:
        """Associate *target* with groups in this dataset.

        *target* may be an instance of SeriesKey or Observation.
        """

        for group_key in self.group:
            if group_key in (target if isinstance(target, SeriesKey) else target.key):
                target.group_keys.add(group_key)
                if isinstance(target, BaseObservation):
                    self.group[group_key].append(target)

    def add_obs(
        self,
        observations: Iterable[BaseObservation],
        series_key: Optional[SeriesKey] = None,
    ) -> None:
        """Add `observations` to the data set, and to a series with `series_key`.

        Checks consistency and adds group associations.
        """
        if series_key is not None:
            # Associate series_key with any GroupKeys that apply to it
            self._add_group_refs(series_key)
            # Maybe initialize empty series
            self.series.setdefault(series_key, [])

        for obs in observations:
            # Associate the observation with any GroupKeys that contain it
            self._add_group_refs(obs)

            # Store a reference to the observation
            self.obs.append(obs)

            if series_key is not None:
                if obs.series_key is None:
                    # Assign the observation to the SeriesKey
                    obs.series_key = series_key
                else:
                    # Check that the Observation is not associated with a different
                    # SeriesKey
                    assert obs.series_key is series_key

                # Store a reference to the observation
                self.series[series_key].append(obs)

    def __str__(self):
        return (
            f"<DataSet structured_by={self.structured_by!r} with {len(self)} "
            "observations>"
        )


# §7.3: Metadata Structure Definition


class AttributeComponent(Component):
    """SDMX 3.0 AttributeComponent.

    .. note:: This intermediate, abstract class is not present in the SDMX 2.1 IM.
    """


@dataclass
class MetadataAttribute(AttributeComponent):
    """SDMX MetadataAttribute."""

    is_presentational: Optional[bool] = None
    max_occurs: Optional[int] = None
    min_occurs: Optional[int] = None

    parent: Optional["MetadataAttribute"] = None
    child: list["MetadataAttribute"] = field(default_factory=list)


class BaseMetadataStructureDefinition(Structure, ConstrainableArtefact):
    """ABC for SDMX 2.1 and 3.0 MetadataStructureDefinition."""


class BaseMetadataflow(StructureUsage, ConstrainableArtefact):
    """ABC for SDMX 2.1 MetadataflowDefinition and SDMX 3.0 Metadataflow."""


# §7.4 MetadataSet


@dataclass
class BaseTextAttributeValue:
    """ABC for SDMX 2.1 and 3.0 TextAttributeValue."""

    text: InternationalStringDescriptor = InternationalStringDescriptor()


@dataclass
class BaseXHTMLAttributeValue:
    """ABC for SDMX 2.1 and 3.0 XHTMLAttributeValue."""

    value: str


@dataclass
class BaseMetadataSet:
    """ABC for SDMX 2.1 and 3.0 MetadataSet."""

    action: Optional[ActionType] = None

    reporting_begin: Optional[date] = None
    reporting_end: Optional[date] = None

    publication_period: Optional[date] = None
    publication_year: Optional[date] = None

    #: Association to the metadata flow definition of which the metadataset is part.
    described_by: Optional[BaseMetadataflow] = None

    #: Note that the class of this attribute differs from SDMX 2.1 to SDMX 3.0.
    #: Compare :attr:`.v21.MetadataSet.structured_by` and
    #: :attr:`.v30.MetadataSet.structured_by`.
    structured_by: Optional[IdentifiableArtefact] = None


# SDMX 2.1 §8: Hierarchical Code List
# SDMX 3.0 §8: Hierarchy


@dataclass
class CodingFormat(Comparable):
    """SDMX CodingFormat."""

    coding_format: Facet = field(default_factory=Facet)


@dataclass
class Level(NameableArtefact):
    """SDMX Level."""

    parent: Optional[Union["Level", Any]] = None  # NB second element is "Hierarchy"
    child: Optional["Level"] = None

    code_format: CodingFormat = field(default_factory=CodingFormat)


@dataclass
class HierarchicalCode(IdentifiableArtefact):
    """SDMX HierarchicalCode."""

    #: Date from which the construct is valid.
    valid_from: Optional[str] = None
    #: Date from which the construct is superseded.
    valid_to: Optional[str] = None

    #: The Code that is used at the specific point in the hierarchy.
    code: Optional[Code] = None

    level: Optional[Level] = None

    parent: Optional[Union["HierarchicalCode", Any]] = (
        None  # NB second element is "Hierarchy"
    )
    child: list["HierarchicalCode"] = field(default_factory=list)


# SDMX 2.1 §10.2: Constraint inheritance
# SDMX 3.0 §12: Constraints


@dataclass
class ConstraintRole:
    #:
    role: ConstraintRoleType


@dataclass
class ComponentValue:
    #:
    value_for: Component
    #:
    value: Any


@dataclass
class TimeDimensionValue(ComponentValue):
    time_value: Any
    operator: str


class BaseSelectionValue:
    """ABC for SDMX 2.1 and 3.0 SelectionValue."""


@dataclass
class BaseMemberValue:
    """Common features of SDMX 2.1 and 3.0 MemberValue."""

    #:
    value: str
    #:
    cascade_values: Optional[bool] = None

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == (other.value if isinstance(other, KeyValue) else other)

    def __repr__(self):
        return f"{repr(self.value)}" + (" + children" if self.cascade_values else "")


@dataclass
class Period:
    """Class not specified in the IM."""

    is_inclusive: bool
    period: datetime


class StartPeriod(Period):
    pass


class EndPeriod(Period):
    pass


@dataclass
class BaseDataKey:
    """Common features of SDMX 2.1 and 3.0 DataKey."""

    #: :obj:`True` if the :attr:`keys` are included in the :class:`.Constraint`;
    # :obj:`False` if they are excluded.
    included: bool
    #: Mapping from :class:`.Component` to :class:`.ComponentValue` comprising the key.
    key_value: dict[Component, ComponentValue] = field(default_factory=dict)


@dataclass
class BaseDataKeySet:
    """Common features of SDMX 2.1 and 3.0 DataKeySet."""

    #: :obj:`True` if the :attr:`keys` are included in the
    #: :class:`Constraint <.BaseConstraint>`; :obj:`False` if they are excluded.
    included: bool
    #: :class:`DataKeys <.BaseDataKey>` appearing in the set.
    keys: list[BaseDataKey] = field(default_factory=list)

    def __len__(self):
        """:func:`len` of the DataKeySet = :func:`len` of its :attr:`keys`."""
        return len(self.keys)

    def __contains__(self, item):
        return any(item == dk for dk in self.keys)


@dataclass
class BaseMemberSelection:
    """Common features of SDMX 2.1 and 3.0 MemberSelection."""

    #:
    values_for: Component
    #:
    included: bool = True
    #: Value(s) included in the selection. Note that the name of this attribute is not
    #: stated in the IM, so 'values' is chosen for the implementation in this package.
    values: list[BaseSelectionValue] = field(default_factory=list)

    def __contains__(self, value):
        """Compare KeyValue to MemberValue."""
        return any(mv == value for mv in self.values) is self.included

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} {self.values_for.id} "
            f"{'not ' if not self.included else ''}in {{"
            f"{', '.join(map(repr, self.values))}}}>"
        )


@dataclass
class CubeRegion:
    #:
    included: bool = True
    #:
    member: dict[DimensionComponent, BaseMemberSelection] = field(default_factory=dict)

    def __contains__(self, other: Union["Key", "KeyValue"]) -> bool:
        """Membership test.

        `other` may be either:

        - :class:`.Key` —all its :class:`.KeyValue` are checked.
        - :class:`.KeyValue` —only the one :class:`.Dimension` for which `other` is a
          value is checked

        Returns
        -------
        bool
            :obj:`True` if:

            - :attr:`.included` *and* `other` is in the CubeRegion;
            - if :attr:`.included` is :obj:`False` *and* `other` is outside the
              CubeRegion; or
            - the `other` is KeyValue referencing a Dimension that is not included in
              :attr:`.member`.
        """
        if isinstance(other, Key):
            result = all(other[ms.values_for.id] in ms for ms in self.member.values())
        elif other.value_for is None:
            # No Dimension reference to use
            result = False
        elif other.value_for not in self.member or len(self.member) > 1:
            # This CubeRegion doesn't have a MemberSelection for the KeyValue's
            # Component; or it concerns additional Components, so inclusion can't be
            # determined
            return True
        else:
            # Check whether the KeyValue is in the indicated dimension
            result = other.value in self.member[other.value_for]

        # Return the correct sense
        return result is self.included

    def to_query_string(self, structure):
        all_values = []

        for dim in structure.dimensions:
            if isinstance(dim, TimeDimension):
                # TimeDimensions handled by query parameters
                continue
            ms = self.member.get(dim, None)
            values = sorted(mv.value for mv in ms.values) if ms else []
            all_values.append("+".join(values))

        return ".".join(all_values)

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} {'in' if self.included else 'ex'}clude "
            f"{' '.join(map(repr, self.member.values()))}>"
        )


@dataclass
class MetadataTargetRegion:
    #:
    is_included: bool = True


class _NullConstraint:
    """Constraint that allows anything."""

    def __contains__(self, value):
        return True


NullConstraint = _NullConstraint()

# SDMX 2.1 §11: Data Provisioning
# SDMX 3.0 §13: Data Provisioning


class Datasource:
    url: str


class SimpleDatasource(Datasource):
    pass


class QueryDatasource(Datasource):
    # Abstract.
    # NB the SDMX-IM inconsistently uses this name and 'WebServicesDatasource'.
    pass


class RESTDatasource(QueryDatasource):
    pass


@dataclass
@MaintainableArtefact._preserve("hash")
class ProvisionAgreement(MaintainableArtefact, ConstrainableArtefact):
    #:
    structure_usage: Optional[StructureUsage] = None
    #:
    data_provider: Optional[DataProvider] = None


# SDMX 3.0 §15: Validation and Transformation Language


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class CustomType(Item["CustomType"]):
    data_type: Optional[str] = None
    null_value: Optional[str] = None
    output_format: Optional[str] = None
    vtl_literal_format: Optional[str] = None
    vtl_scalar_type: Optional[str] = None


class CustomTypeScheme(ItemScheme[CustomType]):
    _Item = CustomType


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class NamePersonalisation(Item["NamePersonalisation"]):
    vtl_default_name: Optional[str] = None


class NamePersonalisationScheme(ItemScheme[NamePersonalisation]):
    _Item = NamePersonalisation


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class Ruleset(Item["Ruleset"]):
    definition: Optional[str] = None
    scope: Optional[str] = None
    type: Optional[str] = None


class RulesetScheme(ItemScheme[Ruleset]):
    _Item = Ruleset


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class Transformation(Item["Transformation"]):
    expression: Optional[str] = None
    result: Optional[str] = None


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class UserDefinedOperator(Item["UserDefinedOperator"]):
    definition: Optional[str] = None


class UserDefinedOperatorScheme(ItemScheme[UserDefinedOperator]):
    _Item = UserDefinedOperator


@dataclass
class VTLSpaceKey:
    key: str


class FromVTLSpaceKey(VTLSpaceKey):
    pass


class ToVTLSpaceKey(VTLSpaceKey):
    pass


class VTLMapping(Item["VTLMapping"]):
    pass


#: Mappings from SDMX to VTL.
SDMXtoVTL = Enum("SDMXtoVTL", "basic pivot basic-a2m pivot-a2m")

#: Mappings from VTL to SDMX.
VTLtoSDMX = Enum("VTLtoSDMX", "basic unpivot m2a")


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class VTLConceptMapping(VTLMapping):
    concept_alias: Optional[Concept] = None


@dataclass
@NameableArtefact._preserve("eq", "hash", "repr")
class VTLDataflowMapping(VTLMapping):
    dataflow_alias: Optional[BaseDataflow] = None
    from_vtl_method: Sequence[VTLSpaceKey] = field(default_factory=list)
    from_vtl_superspace: Optional[VTLSpaceKey] = None
    to_vtl_method: Optional[SDMXtoVTL] = None
    to_vtl_subspace: Sequence[VTLSpaceKey] = field(default_factory=list)


class VTLMappingScheme(ItemScheme[VTLMapping]):
    _Item = VTLMapping


@dataclass
class TransformationScheme(ItemScheme[Transformation]):
    _Item = Transformation

    custom_type_scheme: Optional[CustomTypeScheme] = None
    name_personalisation_scheme: Optional[NamePersonalisationScheme] = None
    ruleset_scheme: Optional[RulesetScheme] = None
    user_defined_operator_scheme: Optional[UserDefinedOperatorScheme] = None
    vtl_mapping_scheme: Optional[VTLMappingScheme] = None

    def update_ref(self, ref):
        for f in direct_fields(self.__class__):
            if isinstance(ref, get_args(f.type)[0]):
                setattr(self, f.name, ref)
                return
        raise TypeError(type(ref))


class BaseContentConstraint:
    """ABC for SDMX 2.1 and 3.0 ContentConstraint."""


# Section 5 Registry / §7.4.3 Registration Response


@dataclass
class MessageText:
    """SDMX MessageText.

    See :ref:`impl-im-reg`.
    """

    code: int = 0
    text: InternationalStringDescriptor = InternationalStringDescriptor()


@dataclass
class StatusMessage:
    """SDMX StatusMessage.

    See :ref:`impl-im-reg`.
    """

    status: SubmissionStatusType
    text: list[MessageText] = field(default_factory=list)


@dataclass
class SubmissionResult:
    """SDMX SubmissionResult.

    See :ref:`impl-im-reg`.
    """

    maintainable_object: MaintainableArtefact
    action: ActionType
    status_message: StatusMessage
    external_dependencies: bool = False


# Internal

#: The SDMX-IM groups classes into 'packages'; these are used in :class:`URNs <.URN>`.
PACKAGE = dict()

_PACKAGE_CLASS: dict[str, set] = {
    "base": {
        "Agency",
        "AgencyScheme",
        "DataProvider",
        "DataConsumerScheme",
        "DataProviderScheme",
        "OrganisationScheme",
    },
    "categoryscheme": {
        "Category",
        "Categorisation",
        "CategoryScheme",
        "ReportingTaxonomy",
    },
    "codelist": {
        "Code",
        "Codelist",
        "HierarchicalCode",
        "HierarchicalCodelist",  # SDMX 2.1
        "Hierarchy",
        "Level",
        "ValueList",  # SDMX 3.0
    },
    "conceptscheme": {"Concept", "ConceptScheme"},
    "datastructure": {
        "Dataflow",  # SDMX 3.0
        "DataflowDefinition",  # SDMX 2.1
        "DataStructure",  # SDMX 3.0
        "DataStructureDefinition",  # SDMX 2.1
        "StructureUsage",
    },
    "mapping": {"CodelistMap", "StructureSet"},
    "metadatastructure": {
        "MetadataflowDefinition",  # SDMX 2.1
        "Metadataflow",  # SDMX 3.0
        "MetadataStructureDefinition",
    },
    "registry": {"ContentConstraint", "ProvisionAgreement"},
    "transformation": {
        "CustomTypeScheme",
        "NamePersonalisationScheme",
        "RulesetScheme",
        "TransformationScheme",
        "UserDefinedOperatorScheme",
        "VTLMappingScheme",
    },
}

for package, classes in _PACKAGE_CLASS.items():
    PACKAGE.update({cls: package for cls in classes})

PARENT = {
    Agency: AgencyScheme,
    Category: CategoryScheme,
    Code: Codelist,
    Concept: ConceptScheme,
    Dimension: DimensionDescriptor,
    TimeDimension: DimensionDescriptor,
    DataProvider: DataProviderScheme,
    GroupDimensionDescriptor: BaseDataStructureDefinition,
}


@dataclass
class ClassFinder:
    module_name: str
    name_map: dict[str, str] = field(default_factory=dict)
    parent_map: dict[type, type] = field(default_factory=dict)

    def __post_init__(self):
        self._module = sys.modules[self.module_name]
        self._parent = ChainMap(PARENT, self.parent_map)

    @lru_cache()
    def get_class(self, name: Union[str, Resource], package=None) -> Optional[type]:
        """Return a class for `name` and (optional) `package` names."""
        if isinstance(name, Resource):
            # Convert a Resource enumeration value to a string

            # Expected class name in lower case; maybe just the enumeration value
            match = Resource.class_name(name).lower()

            # Match class names in lower case. If no match or >2, only() returns None,
            # and KeyError occurs below
            name = only(filter(lambda g: g.lower() == match, dir(self._module)))

        # Change names that differ between URNs and full class names
        name = self.name_map.get(name, name)

        try:
            cls = getattr(self._module, name)
        except (AttributeError, TypeError):
            return None

        if package and package != PACKAGE[cls.__name__]:
            raise ValueError(f"Package {repr(package)} invalid for {name}")

        return cls

    def parent_class(self, cls):
        """Return the class that contains objects of type `cls`.

        For example, if `cls` is :class:`.PrimaryMeasure`, returns
        :class:`.v21.MeasureDescriptor`.
        """
        return self._parent[cls]

    def dir(self):
        """For module.__dir__."""
        return sorted(self._module.__all__ + __all__)

    def getattr(self, name):
        """For module.__getattr__."""
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(name)

    # To allow lru_cache() above
    def __hash__(self):
        return hash(self.module_name)


def __getattr__(name: str):
    if name == "Annotation":
        from warnings import warn

        from .v21 import Annotation

        warn(
            "from sdmx.model.common import Annotation. Use one of sdmx.model.{v21,v30}",
            DeprecationWarning,
            stacklevel=2,
        )
        return Annotation
    raise AttributeError(name)
