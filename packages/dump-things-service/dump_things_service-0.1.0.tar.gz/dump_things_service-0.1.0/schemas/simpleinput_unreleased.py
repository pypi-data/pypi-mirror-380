from __future__ import annotations

import re
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

metamodel_version = "None"
version = "UNRELEASED"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'comments': ['ALL CONTENT HERE IS UNRELEASED AND MAY CHANGE ANY TIME'],
     'default_prefix': 'inm7si',
     'description': 'The classes and slots in this schema have the (sole) purpose '
                    'of\n'
                    'informing the auto-generation of UIs for data entry. '
                    'Consequently,\n'
                    'the simplify and lump-together concepts and constructs that '
                    'will\n'
                    'eventually be represented with more appropriate data '
                    'structures\n'
                    'from the `base` schema.\n'
                    '\n'
                    "More information is available on the schema's [about "
                    'page](about).\n'
                    '\n'
                    'The schema definition is available as\n'
                    '\n'
                    '- [JSON-LD context](../unreleased.jsonld)\n'
                    '- [LinkML YAML](../unreleased.yaml)\n'
                    '- [OWL TTL](../unreleased.owl.ttl)\n',
     'emit_prefixes': ['dlthings', 'dltypes', 'inm7', 'rdf', 'rdfs', 'skos', 'xsd'],
     'id': 'https://concepts.inm7.de/s/simpleinput/unreleased',
     'imports': ['dlschemas:things/v1'],
     'license': 'CC-BY-4.0',
     'name': 'inm7-simpleinput-schema',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dlschemas': {'prefix_prefix': 'dlschemas',
                                'prefix_reference': 'https://concepts.datalad.org/s/'},
                  'dlthings': {'prefix_prefix': 'dlthings',
                               'prefix_reference': 'https://concepts.datalad.org/s/things/v1/'},
                  'dltypes': {'prefix_prefix': 'dltypes',
                              'prefix_reference': 'https://concepts.datalad.org/s/types/unreleased/'},
                  'eunal': {'prefix_prefix': 'eunal',
                            'prefix_reference': 'http://publications.europa.eu/resource/authority/'},
                  'inm7': {'prefix_prefix': 'inm7',
                           'prefix_reference': 'https://inm7.de/ns/'},
                  'inm7si': {'prefix_prefix': 'inm7si',
                             'prefix_reference': 'https://concepts.inm7.de/s/simpleinput/unreleased/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'orcid': {'prefix_prefix': 'orcid',
                            'prefix_reference': 'https://orcid.org/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'sh': {'prefix_prefix': 'sh',
                         'prefix_reference': 'http://www.w3.org/ns/shacl#'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'w3ctr': {'prefix_prefix': 'w3ctr',
                            'prefix_reference': 'https://www.w3.org/TR/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'simpleinput_unreleased.yaml',
     'status': 'eunal:concept-status/DRAFT',
     'title': 'INM7 simplified data models for manual metadata entry',
     'types': {'W3CISO8601': {'description': 'W3C variant/subset of IS08601 for '
                                             'specifying date(times). Supported '
                                             'are - YYYY (eg 1997) - YYYY-MM (eg '
                                             '1997-07) - YYYY-MM-DD (eg '
                                             '1997-07-16) - YYYY-MM-DDThh:mmTZD '
                                             '(eg 1997-07-16T19:20+01:00) - '
                                             'YYYY-MM-DDThh:mm:ssTZD (eg '
                                             '1997-07-16T19:20:30+01:00) - '
                                             'YYYY-MM-DDThh:mm:ss.sTZD (eg '
                                             '1997-07-16T19:20:30.45+01:00) where '
                                             'TZD is the time zone designator (Z '
                                             'or +hh:mm or -hh:mm)',
                              'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
                              'name': 'W3CISO8601',
                              'pattern': '^([-+]\\d+)|(\\d{4})|(\\d{4}-[01]\\d)|(\\d{4}-[01]\\d-[0-3]\\d)|(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d\\.\\d+([+-][0-2]\\d:[0-5]\\d|Z))|(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d([+-][0-2]\\d:[0-5]\\d|Z))|(\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d([+-][0-2]\\d:[0-5]\\d|Z))$',
                              'see_also': ['https://www.w3.org/TR/NOTE-datetime'],
                              'typeof': 'string',
                              'uri': 'w3ctr:NOTE-datetime'}}} )

class OrganizationType(str, Enum):
    """
    Classification of organizations.
    """
    # Smallest unit of an organized group.
    team = "team"
    # A group may consist of more than one team.
    group = "group"
    # A unit within a parent organization that comprises multiple groups.
    division = "division"
    # A topical unit comprising multiple divisions or groups.
    institute = "institute"
    # An institute primarily focused on research (as opposed to education).
    researchcenter = "researchcenter"
    # An organization primarily focused on research (as opposed to education), possibly comprising multiple research centers.
    researchorganization = "researchorganization"
    # A division of a university or college
    faculty = "faculty"
    # An institution with a primary focus on undergraduate education.
    college = "college"
    # An institution with a focus on both undergraduate and graduate education.
    university = "university"
    # A private entity operated for a collective, public or social benefit.
    nonprofit = "nonprofit"
    # A company aiming to generate profit.
    business = "business"



class ThingMixin(ConfiguredBaseModel):
    """
    Mix-in with the common interface of `Thing` and `AttributeSpecification`. This interface enables type specifications (`rdf:type`) for things and attributes via a `type` designator slot to indicate specialized schema classes for validation where a slot's `range` is too generic. A thing or attribute can be further describe with statements on qualified relations to other things (`characterized_by`), or inline attributes (`attributes`). A set of `mappings` slots enables the alignment for arbitrary external schemas and terminologies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.datalad.org/s/things/v1', 'mixin': True})

    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/ThingMixin","dlthings:ThingMixin"] = Field(default="dlthings:ThingMixin", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class ValueSpecificationMixin(ConfiguredBaseModel):
    """
    Mix-in for a (structured) value specification. Two slots are provided to define a (literal) value (`value`) and its type (`range`).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.datalad.org/s/things/v1'})

    range: Optional[str] = Field(default=None, description="""Declares that the value of a `Thing` or `AttributeSpecification` are instances of a particular class.""", json_schema_extra = { "linkml_meta": {'alias': 'range',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdfs:range'],
         'slot_uri': 'rdfs:range'} })
    value: Optional[str] = Field(default=None, description="""Value of a thing.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdf:value'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdfs:value'} })


class AttributeSpecification(ValueSpecificationMixin, ThingMixin):
    """
    An attribute is conceptually a thing, but it requires no dedicated identifier (`pid`). Instead, it is linked to a `Thing` via its `attributes` slot and declares a `predicate` on the nature of the relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['dlthings:Thing'],
         'exact_mappings': ['sio:SIO_000614'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1',
         'mixins': ['ThingMixin', 'ValueSpecificationMixin'],
         'slot_usage': {'predicate': {'name': 'predicate', 'required': True}}})

    predicate: str = Field(default=..., description="""Reference to a `Property` within a `Statement`.""", json_schema_extra = { "linkml_meta": {'alias': 'predicate',
         'domain_of': ['AttributeSpecification', 'Statement'],
         'exact_mappings': ['rdf:predicate'],
         'relational_role': 'PREDICATE',
         'slot_uri': 'rdf:predicate'} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/AttributeSpecification","dlthings:AttributeSpecification"] = Field(default="dlthings:AttributeSpecification", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })
    range: Optional[str] = Field(default=None, description="""Declares that the value of a `Thing` or `AttributeSpecification` are instances of a particular class.""", json_schema_extra = { "linkml_meta": {'alias': 'range',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdfs:range'],
         'slot_uri': 'rdfs:range'} })
    value: Optional[str] = Field(default=None, description="""Value of a thing.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdf:value'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdfs:value'} })


class Statement(ConfiguredBaseModel):
    """
    An RDF statement that links a `predicate` (a `Property`) with an `object` (a `Thing`) to the subject to form a triple. A `Statement` is used to qualify a relation to a `Thing` referenced by its identifier. For specifying a qualified relation to an attribute that has no dedicated identifier, use an `AttributeSpecification`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlthings:Statement',
         'exact_mappings': ['rdf:Statement'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1',
         'slot_usage': {'object': {'name': 'object',
                                   'range': 'Thing',
                                   'required': True},
                        'predicate': {'name': 'predicate', 'required': True}}})

    object: str = Field(default=..., description="""Reference to a `Thing` within a `Statement`.""", json_schema_extra = { "linkml_meta": {'alias': 'object',
         'domain_of': ['Statement'],
         'exact_mappings': ['rdf:object'],
         'notes': ['We do not declare a range here to be able to tighten the range in '
                   'subclasses of class that need a particular range. This appears to '
                   'be working around a linkml limitation.'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdf:object'} })
    predicate: str = Field(default=..., description="""Reference to a `Property` within a `Statement`.""", json_schema_extra = { "linkml_meta": {'alias': 'predicate',
         'domain_of': ['AttributeSpecification', 'Statement'],
         'exact_mappings': ['rdf:predicate'],
         'relational_role': 'PREDICATE',
         'slot_uri': 'rdf:predicate'} })


class Thing(ThingMixin):
    """
    The most basic, identifiable item. In addition to the slots that are common between a `Thing` and an `AttributeSpecification` (see `ThingMixin`), two additional slots are provided. The `pid` slot takes the required identifier for a `Thing`. The `relation` slot allows for the inline specification of other `Thing` instances. Such a relation is unqualified (and symmetric), and should be further characterized via a `Statement` (see `characterized_by`). From a schema perspective, the `relation` slots allows for building self-contained, structured documents (e.g., a JSON object) with arbitrarily complex information on a `Thing`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlthings:Thing',
         'exact_mappings': ['schema:Thing'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1',
         'mixins': ['ThingMixin'],
         'slot_usage': {'annotations': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                     'value': 'ThingsPropertyGroup'},
                                                        'sh:name': {'tag': 'sh:name',
                                                                    'value': 'Annotations'},
                                                        'sh:order': {'tag': 'sh:order',
                                                                     'value': 5}},
                                        'name': 'annotations'},
                        'attributes': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                    'value': 'ThingsPropertyGroup'},
                                                       'sh:name': {'tag': 'sh:name',
                                                                   'value': 'Attributes'},
                                                       'sh:order': {'tag': 'sh:order',
                                                                    'value': 3}},
                                       'name': 'attributes'},
                        'broad_mappings': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                        'value': 'ThingsPropertyGroup'},
                                                           'sh:name': {'tag': 'sh:name',
                                                                       'value': 'Broad '
                                                                                'mappings'},
                                                           'sh:order': {'tag': 'sh:order',
                                                                        'value': 9}},
                                           'name': 'broad_mappings'},
                        'characterized_by': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                          'value': 'ThingsPropertyGroup'},
                                                             'sh:name': {'tag': 'sh:name',
                                                                         'value': 'Is '
                                                                                  'characterized '
                                                                                  'by'},
                                                             'sh:order': {'tag': 'sh:order',
                                                                          'value': 2}},
                                             'name': 'characterized_by'},
                        'close_mappings': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                        'value': 'ThingsPropertyGroup'},
                                                           'sh:name': {'tag': 'sh:name',
                                                                       'value': 'Close '
                                                                                'mappings'},
                                                           'sh:order': {'tag': 'sh:order',
                                                                        'value': 8}},
                                           'name': 'close_mappings'},
                        'description': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                     'value': 'ThingsPropertyGroup'},
                                                        'sh:name': {'tag': 'sh:name',
                                                                    'value': 'Description'},
                                                        'sh:order': {'tag': 'sh:order',
                                                                     'value': 4}},
                                        'name': 'description'},
                        'exact_mappings': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                        'value': 'ThingsPropertyGroup'},
                                                           'sh:name': {'tag': 'sh:name',
                                                                       'value': 'Exact '
                                                                                'mappings'},
                                                           'sh:order': {'tag': 'sh:order',
                                                                        'value': 7}},
                                           'name': 'exact_mappings'},
                        'narrow_mappings': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                         'value': 'ThingsPropertyGroup'},
                                                            'sh:name': {'tag': 'sh:name',
                                                                        'value': 'Narrow '
                                                                                 'mappings'},
                                                            'sh:order': {'tag': 'sh:order',
                                                                         'value': 10}},
                                            'name': 'narrow_mappings'},
                        'pid': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                             'value': 'ThingsPropertyGroup'},
                                                'sh:name': {'tag': 'sh:name',
                                                            'value': 'Persistent '
                                                                     'identifier'},
                                                'sh:order': {'tag': 'sh:order',
                                                             'value': 1}},
                                'name': 'pid'},
                        'related_mappings': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                          'value': 'ThingsPropertyGroup'},
                                                             'sh:name': {'tag': 'sh:name',
                                                                         'value': 'Related '
                                                                                  'mappings'},
                                                             'sh:order': {'tag': 'sh:order',
                                                                          'value': 11}},
                                             'name': 'related_mappings'},
                        'relations': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                   'value': 'ThingsPropertyGroup'},
                                                      'sh:name': {'tag': 'sh:name',
                                                                  'value': 'Relations'},
                                                      'sh:order': {'tag': 'sh:order',
                                                                   'value': 6}},
                                      'name': 'relations'}}})

    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/Thing","dlthings:Thing"] = Field(default="dlthings:Thing", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Property(Thing):
    """
    An RDF property, a `Thing` used to define a `predicate`, for example in a `Statement`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlthings:Property',
         'exact_mappings': ['rdf:Property'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1'})

    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/Property","dlthings:Property"] = Field(default="dlthings:Property", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class ValueSpecification(Thing, ValueSpecificationMixin):
    """
    A `Thing` that is a value of some kind. This class can be used to describe an outcome of a measurement, a factual value or constant, or other qualitative or quantitative information with an associated identifier. If no identifier is available, an `AttributeSpecification` can be used within the context of an associated `Thing` (`attributes`).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['obo:OBI_0001933'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1',
         'mixins': ['ValueSpecificationMixin'],
         'slot_usage': {'value': {'name': 'value',
                                  'notes': ['It is required, because when it is not '
                                            'needed, `Thing` should be used as a type. '
                                            'Its absence is therefore likely a sign of '
                                            'an error.'],
                                  'required': True}}})

    range: Optional[str] = Field(default=None, description="""Declares that the value of a `Thing` or `AttributeSpecification` are instances of a particular class.""", json_schema_extra = { "linkml_meta": {'alias': 'range',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdfs:range'],
         'slot_uri': 'rdfs:range'} })
    value: str = Field(default=..., description="""Value of a thing.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['ValueSpecificationMixin'],
         'exact_mappings': ['rdf:value'],
         'notes': ['It is required, because when it is not needed, `Thing` should be '
                   'used as a type. Its absence is therefore likely a sign of an '
                   'error.'],
         'relational_role': 'OBJECT',
         'slot_uri': 'rdfs:value'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/ValueSpecification","dlthings:ValueSpecification"] = Field(default="dlthings:ValueSpecification", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Annotation(ConfiguredBaseModel):
    """
    A tag/value pair with the semantics of OWL Annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.datalad.org/s/things/v1',
         'slot_usage': {'annotation_tag': {'key': True, 'name': 'annotation_tag'}}})

    annotation_tag: str = Field(default=..., description="""A tag identifying an annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_tag', 'domain_of': ['Annotation']} })
    annotation_value: Optional[str] = Field(default=None, description="""The actual annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_value', 'domain_of': ['Annotation']} })


class CurationAid(ConfiguredBaseModel):
    """
    Technical helper providing curation-related slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:CurationAid',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixin': True,
         'slot_usage': {'curation_comments': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                           'value': 'inm7si:CurationAidPropertyGroup'},
                                                              'sh:name': {'tag': 'sh:name',
                                                                          'value': 'Comments'},
                                                              'sh:order': {'tag': 'sh:order',
                                                                           'value': 2}},
                                              'name': 'curation_comments'},
                        'display_name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                      'value': 'inm7si:CurationAidPropertyGroup'},
                                                         'sh:name': {'tag': 'sh:name',
                                                                     'value': 'Display '
                                                                              'name'},
                                                         'sh:order': {'tag': 'sh:order',
                                                                      'value': 1}},
                                         'name': 'display_name',
                                         'recommended': True}}})

    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })


class Person(CurationAid, Thing):
    """
    A person.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Person',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'additional_names': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                          'value': 'inm7si:PersonPropertyGroup'},
                                                             'sh:name': {'tag': 'sh:name',
                                                                         'value': 'Additional '
                                                                                  'names'},
                                                             'sh:order': {'tag': 'sh:order',
                                                                          'value': 3}},
                                             'name': 'additional_names'},
                        'emails': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                'value': 'inm7si:PersonPropertyGroup'},
                                                   'sh:name': {'tag': 'sh:name',
                                                               'value': 'Email(s)'},
                                                   'sh:order': {'tag': 'sh:order',
                                                                'value': 6}},
                                   'name': 'emails',
                                   'recommended': True},
                        'family_name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                     'value': 'inm7si:PersonPropertyGroup'},
                                                        'sh:name': {'tag': 'sh:name',
                                                                    'value': 'Family '
                                                                             'name'},
                                                        'sh:order': {'tag': 'sh:order',
                                                                     'value': 1}},
                                        'name': 'family_name',
                                        'recommended': True},
                        'given_name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                    'value': 'inm7si:PersonPropertyGroup'},
                                                       'sh:name': {'tag': 'sh:name',
                                                                   'value': 'Given '
                                                                            'name'},
                                                       'sh:order': {'tag': 'sh:order',
                                                                    'value': 2}},
                                       'name': 'given_name',
                                       'recommended': True},
                        'honorific_name_prefix': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                               'value': 'inm7si:PersonPropertyGroup'},
                                                                  'sh:name': {'tag': 'sh:name',
                                                                              'value': 'Title '
                                                                                       'or '
                                                                                       'prefix'},
                                                                  'sh:order': {'tag': 'sh:order',
                                                                               'value': 4}},
                                                  'name': 'honorific_name_prefix'},
                        'honorific_name_suffix': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                               'value': 'inm7si:PersonPropertyGroup'},
                                                                  'sh:name': {'tag': 'sh:name',
                                                                              'value': 'Suffix'},
                                                                  'sh:order': {'tag': 'sh:order',
                                                                               'value': 5}},
                                                  'name': 'honorific_name_suffix'},
                        'offices': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                 'value': 'inm7si:PersonPropertyGroup'},
                                                    'sh:name': {'tag': 'sh:name',
                                                                'value': 'Office '
                                                                         'room(s)'},
                                                    'sh:order': {'tag': 'sh:order',
                                                                 'value': 8}},
                                    'name': 'offices'},
                        'orcid': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                               'value': 'inm7si:PersonPropertyGroup'},
                                                  'sh:name': {'tag': 'sh:name',
                                                              'value': 'ORCID'},
                                                  'sh:order': {'tag': 'sh:order',
                                                               'value': 7}},
                                  'name': 'orcid',
                                  'recommended': True}}})

    additional_names: Optional[List[str]] = Field(default=None, description="""Additional name(s) associated with the subject, such as one or more middle names, or a nick name.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_names',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Additional names'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['Person']} })
    family_name: Optional[str] = Field(default=None, description="""The (inherited) family name of the subject. In many Western languages this is the \"last name\".""", json_schema_extra = { "linkml_meta": {'alias': 'family_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Family name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Person'],
         'recommended': True} })
    given_name: Optional[str] = Field(default=None, description="""The given (non-inherited) name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'given_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Given name'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Person'],
         'recommended': True} })
    honorific_name_prefix: Optional[str] = Field(default=None, description="""The honorific prefix(es) of the subject's name. For example, (academic/formal) titles like \"Mrs\", or \"Dr\", \"Dame\".""", json_schema_extra = { "linkml_meta": {'alias': 'honorific_name_prefix',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Title or prefix'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'domain_of': ['Person']} })
    honorific_name_suffix: Optional[str] = Field(default=None, description="""The honorific suffix(es) of the subject's name. For example, generation labels (\"III\"), or indicators of an academic degree, a profession, or a position (\"MD\", \"BA\").""", json_schema_extra = { "linkml_meta": {'alias': 'honorific_name_suffix',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Suffix'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['Person']} })
    emails: Optional[List[str]] = Field(default=None, description="""Associated email address.""", json_schema_extra = { "linkml_meta": {'alias': 'emails',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Email(s)'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain_of': ['Person'],
         'recommended': True} })
    orcid: Optional[str] = Field(default=None, description="""Associated ORCID identifier (see https://orcid.org).""", json_schema_extra = { "linkml_meta": {'alias': 'orcid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'ORCID'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['Person'],
         'recommended': True} })
    offices: Optional[List[str]] = Field(default=None, description="""Room(s) that are the office(s) of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'offices',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:PersonPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Office room(s)'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['Person']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Person","inm7si:Person"] = Field(default="inm7si:Person", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })

    @field_validator('orcid')
    def pattern_orcid(cls, v):
        pattern=re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]{1}$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid orcid format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid orcid format: {v}")
        return v


class Journal(CurationAid, Thing):
    """
    A periodical that publishes (peer-reviewed) academic articles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Journal',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'issn': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:JournalPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'ISSN'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 3}},
                                 'name': 'issn',
                                 'recommended': True},
                        'short_name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                    'value': 'inm7si:JournalPropertyGroup'},
                                                       'sh:name': {'tag': 'sh:name',
                                                                   'value': 'Short '
                                                                            'name'},
                                                       'sh:order': {'tag': 'sh:order',
                                                                    'value': 2}},
                                       'name': 'short_name'},
                        'title': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                               'value': 'inm7si:JournalPropertyGroup'},
                                                  'sh:name': {'tag': 'sh:name',
                                                              'value': 'Title'},
                                                  'sh:order': {'tag': 'sh:order',
                                                               'value': 1}},
                                  'name': 'title',
                                  'required': True}}})

    issn: Optional[str] = Field(default=None, description="""Associated International Standard Serial Number (ISSN) identifier (see https://www.issn.org).""", json_schema_extra = { "linkml_meta": {'alias': 'issn',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'ISSN'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['Journal'],
         'recommended': True} })
    title: str = Field(default=..., description="""A summarily description of the subject. It is closely related to a `name`, but often less compact and more descriptive. Typically used for documents.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Title'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Journal', 'JournalArticle']} })
    short_name: Optional[str] = Field(default=None, description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Short name'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Journal', 'Organization']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Journal","inm7si:Journal"] = Field(default="inm7si:Journal", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })

    @field_validator('issn')
    def pattern_issn(cls, v):
        pattern=re.compile(r"^\d{4}-\d{3}[0-9X]{1}$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid issn format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid issn format: {v}")
        return v


class JournalArticle(CurationAid, Thing):
    """
    A report that is published in a journal.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:JournalArticle',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'authors': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                 'value': 'inm7si:JournalArticlePropertyGroup'},
                                                    'sh:name': {'tag': 'sh:name',
                                                                'value': 'Author(s)'},
                                                    'sh:order': {'tag': 'sh:order',
                                                                 'value': 3}},
                                    'name': 'authors'},
                        'date_published': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                        'value': 'inm7si:JournalArticlePropertyGroup'},
                                                           'sh:name': {'tag': 'sh:name',
                                                                       'value': 'Date '
                                                                                'published'},
                                                           'sh:order': {'tag': 'sh:order',
                                                                        'value': 5}},
                                           'name': 'date_published'},
                        'doi': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                             'value': 'inm7si:JournalArticlePropertyGroup'},
                                                'sh:name': {'tag': 'sh:name',
                                                            'value': 'Digital Object '
                                                                     'Identifier'},
                                                'sh:order': {'tag': 'sh:order',
                                                             'value': 2}},
                                'name': 'doi',
                                'recommended': True},
                        'journal': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                 'value': 'inm7si:JournalArticlePropertyGroup'},
                                                    'sh:name': {'tag': 'sh:name',
                                                                'value': 'Journal'},
                                                    'sh:order': {'tag': 'sh:order',
                                                                 'value': 4}},
                                    'name': 'journal'},
                        'title': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                               'value': 'inm7si:JournalArticlePropertyGroup'},
                                                  'sh:name': {'tag': 'sh:name',
                                                              'value': 'Title'},
                                                  'sh:order': {'tag': 'sh:order',
                                                               'value': 1}},
                                  'name': 'title',
                                  'required': True}}})

    doi: Optional[str] = Field(default=None, description="""Associated Digital Object Identifier (DOI; ISO 26324; see https://doi.org).  The value must be just the DOI without the URL project. So just `10.1038/s41597-022-01163-2` and not `https://doi.org/10.1038/s41597-022-01163-2`.""", json_schema_extra = { "linkml_meta": {'alias': 'doi',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalArticlePropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Digital Object Identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['JournalArticle'],
         'recommended': True} })
    title: str = Field(default=..., description="""A summarily description of the subject. It is closely related to a `name`, but often less compact and more descriptive. Typically used for documents.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalArticlePropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Title'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Journal', 'JournalArticle']} })
    authors: Optional[List[str]] = Field(default=None, description="""People that contributed to a document in the author role.""", json_schema_extra = { "linkml_meta": {'alias': 'authors',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalArticlePropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Author(s)'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['JournalArticle']} })
    journal: Optional[str] = Field(default=None, description="""Journal a document was published in.""", json_schema_extra = { "linkml_meta": {'alias': 'journal',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalArticlePropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Journal'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'domain_of': ['JournalArticle']} })
    date_published: Optional[str] = Field(default=None, description="""Timepoint at which the subject was (last) published.""", json_schema_extra = { "linkml_meta": {'alias': 'date_published',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:JournalArticlePropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Date published'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['JournalArticle']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/JournalArticle","inm7si:JournalArticle"] = Field(default="inm7si:JournalArticle", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Site(CurationAid, Thing):
    """
    A place or region where entities (building, office, etc.) reside.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Site',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:SitePropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Name'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:SitePropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site', 'Building', 'BuildingLevel', 'Organization', 'Room']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Site","inm7si:Site"] = Field(default="inm7si:Site", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Building(CurationAid, Thing):
    """
    A structure with a roof and walls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Building',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:BuildingPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Name'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True},
                        'site': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:BuildingPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Site'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 2}},
                                 'name': 'site'}}})

    name: str = Field(default=..., description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:BuildingPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site', 'Building', 'BuildingLevel', 'Organization', 'Room']} })
    site: Optional[str] = Field(default=None, description="""Site where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'site',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:BuildingPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Site'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Building']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Building","inm7si:Building"] = Field(default="inm7si:Building", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class BuildingLevel(CurationAid, Thing):
    """
    A single level or floor of a (multilevel) building.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:BuildingLevel',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'building': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                  'value': 'inm7si:BuildingLevelPropertyGroup'},
                                                     'sh:name': {'tag': 'sh:name',
                                                                 'value': 'Building'},
                                                     'sh:order': {'tag': 'sh:order',
                                                                  'value': 2}},
                                     'name': 'building'},
                        'name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:BuildingLevelPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Name'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:BuildingLevelPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site', 'Building', 'BuildingLevel', 'Organization', 'Room']} })
    building: Optional[str] = Field(default=None, description="""Building where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'building',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:BuildingLevelPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Building'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['BuildingLevel']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/BuildingLevel","inm7si:BuildingLevel"] = Field(default="inm7si:BuildingLevel", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Organization(CurationAid, Thing):
    """
    A social or legal institution such as a company, a society, or a university.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Organization',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:OrganizationPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Name'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True},
                        'organization_heads': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                            'value': 'inm7si:OrganizationPropertyGroup'},
                                                               'sh:name': {'tag': 'sh:name',
                                                                           'value': 'Head(s)'},
                                                               'sh:order': {'tag': 'sh:order',
                                                                            'value': 4}},
                                               'name': 'organization_heads'},
                        'organization_type': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                           'value': 'inm7si:OrganizationPropertyGroup'},
                                                              'sh:name': {'tag': 'sh:name',
                                                                          'value': 'Type'},
                                                              'sh:order': {'tag': 'sh:order',
                                                                           'value': 3}},
                                              'name': 'organization_type'},
                        'parent_organization': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                             'value': 'inm7si:OrganizationPropertyGroup'},
                                                                'sh:name': {'tag': 'sh:name',
                                                                            'value': 'Parent '
                                                                                     'organization'},
                                                                'sh:order': {'tag': 'sh:order',
                                                                             'value': 5}},
                                                'name': 'parent_organization'},
                        'short_name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                    'value': 'inm7si:OrganizationPropertyGroup'},
                                                       'sh:name': {'tag': 'sh:name',
                                                                   'value': 'Short '
                                                                            'name'},
                                                       'sh:order': {'tag': 'sh:order',
                                                                    'value': 2}},
                                       'name': 'short_name'}}})

    name: str = Field(default=..., description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:OrganizationPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site', 'Building', 'BuildingLevel', 'Organization', 'Room']} })
    short_name: Optional[str] = Field(default=None, description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:OrganizationPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Short name'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Journal', 'Organization']} })
    parent_organization: Optional[str] = Field(default=None, description="""An organization the subject is a part of.""", json_schema_extra = { "linkml_meta": {'alias': 'parent_organization',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:OrganizationPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Parent organization'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['Organization']} })
    organization_type: Optional[OrganizationType] = Field(default=None, description="""Type of an organization.""", json_schema_extra = { "linkml_meta": {'alias': 'organization_type',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:OrganizationPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Type'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['Organization']} })
    organization_heads: Optional[List[str]] = Field(default=None, description="""Person(s) that are formal or informal leaders of an organization.""", json_schema_extra = { "linkml_meta": {'alias': 'organization_heads',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:OrganizationPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Head(s)'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'domain_of': ['Organization']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Organization","inm7si:Organization"] = Field(default="inm7si:Organization", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Room(CurationAid, Thing):
    """
    An area within a building enclosed by walls and floor and ceiling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7si:Room',
         'from_schema': 'https://concepts.inm7.de/s/simpleinput/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'building_level': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                                        'value': 'inm7si:RoomPropertyGroup'},
                                                           'sh:name': {'tag': 'sh:name',
                                                                       'value': 'Building '
                                                                                'level'},
                                                           'sh:order': {'tag': 'sh:order',
                                                                        'value': 2}},
                                           'name': 'building_level'},
                        'name': {'annotations': {'sh:group': {'tag': 'sh:group',
                                                              'value': 'inm7si:RoomPropertyGroup'},
                                                 'sh:name': {'tag': 'sh:name',
                                                             'value': 'Name'},
                                                 'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:RoomPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site', 'Building', 'BuildingLevel', 'Organization', 'Room']} })
    building_level: Optional[str] = Field(default=None, description="""Building level where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'building_level',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:RoomPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Building level'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Room']} })
    curation_comments: Optional[List[str]] = Field(default=None, description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Comments'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid']} })
    display_name: Optional[str] = Field(default=None, description="""Name to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_name',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'inm7si:CurationAidPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Display name'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    pid: str = Field(default=..., description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name',
                                     'value': 'Persistent identifier'},
                         'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[Dict[str, Union[Thing,Property,ValueSpecification,Person,Journal,JournalArticle,Site,Building,BuildingLevel,Organization,Room]]] = Field(default=None, description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Relations'},
                         'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[Dict[str, Union[str, Annotation]]] = Field(default=None, description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Annotations'},
                         'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Broad mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Close mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Description'},
                         'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Exact mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[List[AttributeSpecification]] = Field(default=None, description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Attributes'},
                         'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[List[Statement]] = Field(default=None, description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Is characterized by'},
                         'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Narrow mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[List[str]] = Field(default=None, description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:group': {'tag': 'sh:group',
                                      'value': 'ThingsPropertyGroup'},
                         'sh:name': {'tag': 'sh:name', 'value': 'Related mappings'},
                         'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/simpleinput/unreleased/Room","inm7si:Room"] = Field(default="inm7si:Room", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ThingMixin.model_rebuild()
ValueSpecificationMixin.model_rebuild()
AttributeSpecification.model_rebuild()
Statement.model_rebuild()
Thing.model_rebuild()
Property.model_rebuild()
ValueSpecification.model_rebuild()
Annotation.model_rebuild()
CurationAid.model_rebuild()
Person.model_rebuild()
Journal.model_rebuild()
JournalArticle.model_rebuild()
Site.model_rebuild()
Building.model_rebuild()
BuildingLevel.model_rebuild()
Organization.model_rebuild()
Room.model_rebuild()

