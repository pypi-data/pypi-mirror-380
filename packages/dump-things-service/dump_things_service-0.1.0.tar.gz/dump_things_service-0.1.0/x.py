from __future__ import annotations

import re
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

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
    root: dict[str, Any] = {}
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
     'default_prefix': 'inm7fs',
     'description': 'The classes and slots in this schema support modeling ...\n'
                    '\n'
                    "More information may be available on the schema's [about "
                    'page](about).\n'
                    '\n'
                    'The schema definition is available as\n'
                    '\n'
                    '- [JSON-LD context](../unreleased.jsonld)\n'
                    '- [LinkML YAML](../unreleased.yaml)\n'
                    '- [OWL TTL](../unreleased.owl.ttl)\n'
                    '- [SHACL TTL](../unreleased.shacl.ttl)\n',
     'emit_prefixes': ['dlidentifiers',
                       'dlthings',
                       'dltypes',
                       'inm7',
                       'inm7fb',
                       'inm7fs',
                       'rdf',
                       'rdfs',
                       'skos',
                       'xsd'],
     'id': 'https://concepts.inm7.de/s/flat-data/unreleased',
     'imports': ['inm7schemas:flat-base/unreleased'],
     'license': 'CC-BY-4.0',
     'name': 'inm7-flat-data-schema',
     'prefixes': {'ADMS': {'prefix_prefix': 'ADMS',
                           'prefix_reference': 'http://www.w3.org/ns/adms#'},
                  'dash': {'prefix_prefix': 'dash',
                           'prefix_reference': 'http://datashapes.org/dash#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dlidentifiers': {'prefix_prefix': 'dlidentifiers',
                                    'prefix_reference': 'https://concepts.datalad.org/s/identifiers/unreleased/'},
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
                  'inm7fb': {'prefix_prefix': 'inm7fb',
                             'prefix_reference': 'https://concepts.inm7.de/s/flat-base/unreleased/'},
                  'inm7fs': {'prefix_prefix': 'inm7fs',
                             'prefix_reference': 'https://concepts.inm7.de/s/flat-data/unreleased/'},
                  'inm7schemas': {'prefix_prefix': 'inm7schemas',
                                  'prefix_reference': 'https://concepts.inm7.de/s/'},
                  'inm7usrmgt': {'prefix_prefix': 'inm7usrmgt',
                                 'prefix_reference': 'https://inm7.de/ns/usrmgt/'},
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
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'},
                  'w3ctr': {'prefix_prefix': 'w3ctr',
                            'prefix_reference': 'https://www.w3.org/TR/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'schema-flatdata.yaml',
     'status': 'eunal:concept-status/DRAFT',
     'title': 'Data models for INM7 study-related concepts for data discovery'} )

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

    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/ThingMixin","dlthings:ThingMixin"] = Field(default="dlthings:ThingMixin", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/AttributeSpecification","dlthings:AttributeSpecification"] = Field(default="dlthings:AttributeSpecification", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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
         'slot_usage': {'annotations': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                     'value': 5}},
                                        'name': 'annotations'},
                        'attributes': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                    'value': 3}},
                                       'name': 'attributes'},
                        'broad_mappings': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                        'value': 9}},
                                           'name': 'broad_mappings'},
                        'characterized_by': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                          'value': 2}},
                                             'name': 'characterized_by'},
                        'close_mappings': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                        'value': 8}},
                                           'name': 'close_mappings'},
                        'description': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                     'value': 4}},
                                        'name': 'description'},
                        'exact_mappings': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                        'value': 7}},
                                           'name': 'exact_mappings'},
                        'narrow_mappings': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                         'value': 10}},
                                            'name': 'narrow_mappings'},
                        'pid': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                             'value': 1}},
                                'name': 'pid'},
                        'related_mappings': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                          'value': 11}},
                                             'name': 'related_mappings'},
                        'relations': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                   'value': 6}},
                                      'name': 'relations'}}})

    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/Thing","dlthings:Thing"] = Field(default="dlthings:Thing", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Property(Thing):
    """
    An RDF property, a `Thing` used to define a `predicate`, for example in a `Statement`.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlthings:Property',
         'exact_mappings': ['rdf:Property'],
         'from_schema': 'https://concepts.datalad.org/s/things/v1'})

    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/Property","dlthings:Property"] = Field(default="dlthings:Property", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.datalad.org/s/things/v1/ValueSpecification","dlthings:ValueSpecification"] = Field(default="dlthings:ValueSpecification", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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


class Identifier(ConfiguredBaseModel):
    """
    An identifier is a label that uniquely identifies an item in a particular context. Some identifiers are globally unique. All identifiers are unique within their individual scope.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlidentifiers:Identifier',
         'close_mappings': ['ADMS:Identifier'],
         'from_schema': 'https://concepts.datalad.org/s/identifiers/unreleased',
         'slot_usage': {'notation': {'name': 'notation', 'required': True}}})

    creator: Optional[str] = Field(default=None, description="""An agent responsible for making an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Identifier'],
         'exact_mappings': ['dcterms:creator'],
         'notes': ['The `range` is only `uriorcurie` here (and not `Thing`), because '
                   'we have an `ifabsent` declaration for DOIs that only work with '
                   'this type. And even for that it needs a patch.'],
         'slot_uri': 'dlidentifiers:creator'} })
    notation: str = Field(default=..., description="""String of characters such as \"T58:5\" or \"30:4833\" used to uniquely identify a concept within the scope of a given concept scheme.""", json_schema_extra = { "linkml_meta": {'alias': 'notation',
         'domain_of': ['Identifier'],
         'exact_mappings': ['skos:notation'],
         'slot_uri': 'dlidentifiers:notation'} })
    schema_type: Literal["https://concepts.datalad.org/s/identifiers/unreleased/Identifier","dlidentifiers:Identifier"] = Field(default="dlidentifiers:Identifier", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class IssuedIdentifier(Identifier):
    """
    An identifier that was issued by a particular agent with a notation that has no (or an undefined) relation to the nature of the identified entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlidentifiers:IssuedIdentifier',
         'exact_mappings': ['ADMS:Identifier'],
         'from_schema': 'https://concepts.datalad.org/s/identifiers/unreleased',
         'see_also': ['https://semiceu.github.io/ADMS/releases/2.00/#Identifier']})

    schema_agency: Optional[str] = Field(default=None, description="""Name of the agency that issued an identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_agency',
         'domain_of': ['IssuedIdentifier'],
         'exact_mappings': ['ADMS:schemaAgency'],
         'slot_uri': 'dlidentifiers:schema_agency'} })
    creator: Optional[str] = Field(default=None, description="""An agent responsible for making an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Identifier'],
         'exact_mappings': ['dcterms:creator'],
         'notes': ['The `range` is only `uriorcurie` here (and not `Thing`), because '
                   'we have an `ifabsent` declaration for DOIs that only work with '
                   'this type. And even for that it needs a patch.'],
         'slot_uri': 'dlidentifiers:creator'} })
    notation: str = Field(default=..., description="""String of characters such as \"T58:5\" or \"30:4833\" used to uniquely identify a concept within the scope of a given concept scheme.""", json_schema_extra = { "linkml_meta": {'alias': 'notation',
         'domain_of': ['Identifier'],
         'exact_mappings': ['skos:notation'],
         'slot_uri': 'dlidentifiers:notation'} })
    schema_type: Literal["https://concepts.datalad.org/s/identifiers/unreleased/IssuedIdentifier","dlidentifiers:IssuedIdentifier"] = Field(default="dlidentifiers:IssuedIdentifier", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class ComputedIdentifier(Identifier):
    """
    An identifier that has been derived from information on the identified entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlidentifiers:ComputedIdentifier',
         'from_schema': 'https://concepts.datalad.org/s/identifiers/unreleased',
         'narrow_mappings': ['spdx:Checksum']})

    creator: Optional[str] = Field(default=None, description="""An agent responsible for making an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Identifier'],
         'exact_mappings': ['dcterms:creator'],
         'notes': ['The `range` is only `uriorcurie` here (and not `Thing`), because '
                   'we have an `ifabsent` declaration for DOIs that only work with '
                   'this type. And even for that it needs a patch.'],
         'slot_uri': 'dlidentifiers:creator'} })
    notation: str = Field(default=..., description="""String of characters such as \"T58:5\" or \"30:4833\" used to uniquely identify a concept within the scope of a given concept scheme.""", json_schema_extra = { "linkml_meta": {'alias': 'notation',
         'domain_of': ['Identifier'],
         'exact_mappings': ['skos:notation'],
         'slot_uri': 'dlidentifiers:notation'} })
    schema_type: Literal["https://concepts.datalad.org/s/identifiers/unreleased/ComputedIdentifier","dlidentifiers:ComputedIdentifier"] = Field(default="dlidentifiers:ComputedIdentifier", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Checksum(ComputedIdentifier):
    """
    A Checksum is a value that allows to check the integrity of the contents of a file. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlidentifiers:Checksum',
         'exact_mappings': ['spdx:Checksum'],
         'from_schema': 'https://concepts.datalad.org/s/identifiers/unreleased',
         'slot_usage': {'creator': {'description': 'Identifies the software agent '
                                                   '(algorithm) used to produce the '
                                                   'subject `Checksum`.',
                                    'exact_mappings': ['spdx:algorithm'],
                                    'name': 'creator',
                                    'required': True},
                        'notation': {'description': 'Lower case hexadecimal encoded '
                                                    'checksum digest value.',
                                     'exact_mappings': ['spdx:checksumValue'],
                                     'name': 'notation',
                                     'range': 'HexBinary',
                                     'required': True}}})

    creator: str = Field(default=..., description="""Identifies the software agent (algorithm) used to produce the subject `Checksum`.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Identifier'],
         'exact_mappings': ['spdx:algorithm'],
         'notes': ['The `range` is only `uriorcurie` here (and not `Thing`), because '
                   'we have an `ifabsent` declaration for DOIs that only work with '
                   'this type. And even for that it needs a patch.'],
         'slot_uri': 'dlidentifiers:creator'} })
    notation: str = Field(default=..., description="""Lower case hexadecimal encoded checksum digest value.""", json_schema_extra = { "linkml_meta": {'alias': 'notation',
         'domain_of': ['Identifier'],
         'exact_mappings': ['spdx:checksumValue'],
         'slot_uri': 'dlidentifiers:notation'} })
    schema_type: Literal["https://concepts.datalad.org/s/identifiers/unreleased/Checksum","dlidentifiers:Checksum"] = Field(default="dlidentifiers:Checksum", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class DOI(IssuedIdentifier):
    """
    Digital Object Identifier (DOI; ISO 26324), an identifier system governed by the DOI Foundation, where individual identifiers are issued by one of several registration agencies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dlidentifiers:DOI',
         'from_schema': 'https://concepts.datalad.org/s/identifiers/unreleased',
         'slot_usage': {'creator': {'description': 'By default, the creator is '
                                                   'identified as "https://doi.org".',
                                    'ifabsent': 'string(https://doi.org)',
                                    'name': 'creator'},
                        'notation': {'description': 'The identifier notation is '
                                                    'specified without a URL-prefix, '
                                                    'or a `doi:` prefix.',
                                     'name': 'notation'},
                        'schema_agency': {'description': 'By default, the schema '
                                                         'agency is identified as `DOI '
                                                         'Foundation`.',
                                          'ifabsent': 'string(DOI Foundation)',
                                          'name': 'schema_agency'}},
         'unique_keys': {'value': {'description': 'The DOI notation is globally unique '
                                                  'within the scope of DOIs',
                                   'unique_key_name': 'value',
                                   'unique_key_slots': ['notation']}}})

    schema_agency: Optional[str] = Field(default="DOI Foundation", description="""By default, the schema agency is identified as `DOI Foundation`.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_agency',
         'domain_of': ['IssuedIdentifier'],
         'exact_mappings': ['ADMS:schemaAgency'],
         'ifabsent': 'string(DOI Foundation)',
         'slot_uri': 'dlidentifiers:schema_agency'} })
    creator: Optional[str] = Field(default="https://doi.org", description="""By default, the creator is identified as \"https://doi.org\".""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Identifier'],
         'exact_mappings': ['dcterms:creator'],
         'ifabsent': 'string(https://doi.org)',
         'notes': ['The `range` is only `uriorcurie` here (and not `Thing`), because '
                   'we have an `ifabsent` declaration for DOIs that only work with '
                   'this type. And even for that it needs a patch.'],
         'slot_uri': 'dlidentifiers:creator'} })
    notation: str = Field(default=..., description="""The identifier notation is specified without a URL-prefix, or a `doi:` prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'notation',
         'domain_of': ['Identifier'],
         'exact_mappings': ['skos:notation'],
         'slot_uri': 'dlidentifiers:notation'} })
    schema_type: Literal["https://concepts.datalad.org/s/identifiers/unreleased/DOI","dlidentifiers:DOI"] = Field(default="dlidentifiers:DOI", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class CurationAid(ConfiguredBaseModel):
    """
    Technical helper providing curation-related slots.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:CurationAid',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixin': True})

    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })


class Person(CurationAid, Thing):
    """
    A person.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:Person',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'additional_names': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                          'value': 3}},
                                             'name': 'additional_names'},
                        'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 10}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'emails': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                'value': 6}},
                                   'name': 'emails',
                                   'recommended': True},
                        'family_name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                     'value': 1}},
                                        'name': 'family_name',
                                        'recommended': True},
                        'given_name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                    'value': 2}},
                                       'name': 'given_name',
                                       'recommended': True},
                        'honorific_name_prefix': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                               'value': 4}},
                                                  'name': 'honorific_name_prefix'},
                        'honorific_name_suffix': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                               'value': 5}},
                                                  'name': 'honorific_name_suffix'},
                        'member_of': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                   'value': 8}},
                                      'name': 'member_of'},
                        'offices': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                 'value': 9}},
                                    'name': 'offices'},
                        'orcid': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                               'value': 7}},
                                  'name': 'orcid',
                                  'recommended': True}}})

    additional_names: Optional[list[str]] = Field(default=None, title="Additional names", description="""Additional name(s) associated with the subject, such as one or more middle names, or a nick name.""", json_schema_extra = { "linkml_meta": {'alias': 'additional_names',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['Person']} })
    family_name: Optional[str] = Field(default=None, title="Family name", description="""The (inherited) family name of the subject. In many Western languages this is the \"last name\".""", json_schema_extra = { "linkml_meta": {'alias': 'family_name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Person'],
         'recommended': True} })
    given_name: Optional[str] = Field(default=None, title="Given name", description="""The given (non-inherited) name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'given_name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Person'],
         'recommended': True} })
    honorific_name_prefix: Optional[str] = Field(default=None, title="Title or prefix", description="""The honorific prefix(es) of the subject's name. For example, (academic/formal) titles like \"Mrs\", or \"Dr\", \"Dame\".""", json_schema_extra = { "linkml_meta": {'alias': 'honorific_name_prefix',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'domain_of': ['Person']} })
    honorific_name_suffix: Optional[str] = Field(default=None, title="Suffix", description="""The honorific suffix(es) of the subject's name. For example, generation labels (\"III\"), or indicators of an academic degree, a profession, or a position (\"MD\", \"BA\").""", json_schema_extra = { "linkml_meta": {'alias': 'honorific_name_suffix',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['Person']} })
    emails: Optional[list[str]] = Field(default=None, title="Email(s)", description="""Associated email address.""", json_schema_extra = { "linkml_meta": {'alias': 'emails',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain_of': ['Person'],
         'recommended': True} })
    member_of: Optional[list[str]] = Field(default=None, title="Member of", description="""The subject is a member of an organization.""", json_schema_extra = { "linkml_meta": {'alias': 'member_of',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['Person']} })
    orcid: Optional[str] = Field(default=None, title="ORCID", description="""Associated ORCID identifier (see https://orcid.org).""", json_schema_extra = { "linkml_meta": {'alias': 'orcid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['Person'],
         'recommended': True} })
    offices: Optional[list[str]] = Field(default=None, title="Office room(s)", description="""Room(s) that are the office(s) of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'offices',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['Person']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/Person","inm7fb:Person"] = Field(default="inm7fb:Person", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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


class Site(CurationAid, Thing):
    """
    A place or region where entities (building, office, etc.) reside.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:Site',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 2}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/Site","inm7fb:Site"] = Field(default="inm7fb:Site", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Building(CurationAid, Thing):
    """
    A structure with a roof and walls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:Building',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 1}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True},
                        'site': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 2}},
                                 'name': 'site'}}})

    name: str = Field(default=..., title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    site: Optional[str] = Field(default=None, title="Site", description="""Site where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'site',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Building']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/Building","inm7fb:Building"] = Field(default="inm7fb:Building", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class BuildingLevel(CurationAid, Thing):
    """
    A single level or floor of a (multilevel) building.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:BuildingLevel',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'building': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                  'value': 2}},
                                     'name': 'building'},
                        'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 1}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    building: Optional[str] = Field(default=None, title="Building", description="""Building where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'building',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['BuildingLevel']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/BuildingLevel","inm7fb:BuildingLevel"] = Field(default="inm7fb:BuildingLevel", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Organization(CurationAid, Thing):
    """
    A social or legal institution such as a company, a society, or a university.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:Organization',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 6}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'leaders': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                 'value': 4}},
                                    'name': 'leaders'},
                        'name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True},
                        'organization_type': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                           'value': 3}},
                                              'name': 'organization_type'},
                        'parent_organization': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                             'value': 5}},
                                                'name': 'parent_organization'},
                        'short_name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                    'value': 2}},
                                       'name': 'short_name'}}})

    name: str = Field(default=..., title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    parent_organization: Optional[str] = Field(default=None, title="Parent organization", description="""An organization the subject is a part of.""", json_schema_extra = { "linkml_meta": {'alias': 'parent_organization',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['Organization']} })
    organization_type: Optional[OrganizationType] = Field(default=None, title="Organization type", description="""Type of an organization.""", json_schema_extra = { "linkml_meta": {'alias': 'organization_type',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['Organization']} })
    leaders: Optional[list[str]] = Field(default=None, title="Leader(s)", description="""Person(s) that are formal or informal leaders of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'leaders',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'domain_of': ['Organization']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/Organization","inm7fb:Organization"] = Field(default="inm7fb:Organization", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Room(CurationAid, Thing):
    """
    An area within a building enclosed by walls and floor and ceiling.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'inm7fb:Room',
         'from_schema': 'https://concepts.inm7.de/s/flat-base/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'building_level': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                        'value': 2}},
                                           'name': 'building_level'},
                        'display_label': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                                       'value': 3}},
                                          'name': 'display_label',
                                          'recommended': True},
                        'name': {'annotations': {'sh:order': {'tag': 'sh:order',
                                                              'value': 1}},
                                 'name': 'name',
                                 'required': True}}})

    name: str = Field(default=..., title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    building_level: Optional[str] = Field(default=None, title="Building level", description="""Building level where the subject is located.""", json_schema_extra = { "linkml_meta": {'alias': 'building_level',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['Room']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['CurationAid'],
         'recommended': True,
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-base/unreleased/Room","inm7fb:Room"] = Field(default="inm7fb:Room", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Dataset(CurationAid, Thing):
    """
    A collection of data, published or curated by a single agent. This is a conceptual entity. A single dataset might be available in more than one representation, with differing schematic layouts, formats, and serializations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    conforms_to: Optional[str] = Field(default=None, description="""An established standard to which the subject conforms.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'comments': ['This property SHOULD be used to indicate a model, schema, '
                      'ontology, view or profile that the subject conforms to.'],
         'domain_of': ['Dataset'],
         'exact_mappings': ['dcterms:conformsTo']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Dataset","inm7fs:Dataset"] = Field(default="inm7fs:Dataset", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class DataItem(CurationAid, Thing):
    """
    A single data item, the building block of Datasets. This is a conceptual entity. A DataItem might be available in more than one representation, with differing formats, and serializations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    distributions: Optional[list[str]] = Field(default=None, description="""Available distributions of the dataset or data item.""", json_schema_extra = { "linkml_meta": {'alias': 'distributions',
         'broad_mappings': ['sio:SIO_000341'],
         'domain_of': ['DataItem'],
         'exact_mappings': ['dcat:distribution']} })
    dimensions: Optional[list[str]] = Field(default=None, description="""Associated outcome variables.""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions', 'domain_of': ['DataItem', 'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/DataItem","inm7fs:DataItem"] = Field(default="inm7fs:DataItem", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Distribution(Thing):
    """
    A specific representation of a resource, which may come in the form of a physical object, or an electronic file, or an archive or directory of many files, may be standalone or part of a larger collection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased'})

    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Distribution","inm7fs:Distribution"] = Field(default="inm7fs:Distribution", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Dimension(CurationAid, Thing):
    """
    A dependent or outcome variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Dimension","inm7fs:Dimension"] = Field(default="inm7fs:Dimension", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Factor(CurationAid, Thing):
    """
    A tag associated with a categorical, independent variable in a study design. Factors can have an investigative role (e.g., treatments), or have an organizational nature (e.g., site labels).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The relationship of a factor "level" with the broader factor '
                      'can be described via `broader_mappings`.'],
         'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    factor_level_of: Optional[str] = Field(default=None, description="""A factor the subject is a (sub)level of.""", json_schema_extra = { "linkml_meta": {'alias': 'factor_level_of', 'domain_of': ['Factor']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Factor","inm7fs:Factor"] = Field(default="inm7fs:Factor", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Instrument(CurationAid, Thing):
    """
    A material entity that is designed to perform a function in a scientific investigation, but is not a reagent.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['obo:OBI_0000968'],
         'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Instrument","inm7fs:Instrument"] = Field(default="inm7fs:Instrument", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Protocol(CurationAid, Thing):
    """
    A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['obo:OBI_0000272'],
         'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Protocol","inm7fs:Protocol"] = Field(default="inm7fs:Protocol", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Study(CurationAid, Thing):
    """
    TODO
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    dimensions: Optional[list[str]] = Field(default=None, description="""Associated outcome variables.""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions', 'domain_of': ['DataItem', 'Study']} })
    factors: Optional[list[str]] = Field(default=None, description="""Influencing factors.""", json_schema_extra = { "linkml_meta": {'alias': 'factors', 'domain_of': ['Study', 'StudyActivity']} })
    instruments: Optional[list[str]] = Field(default=None, description="""Employed instruments.""", json_schema_extra = { "linkml_meta": {'alias': 'instruments', 'domain_of': ['Study', 'StudyActivity']} })
    protocols: Optional[list[str]] = Field(default=None, description="""Implemented protocols.""", json_schema_extra = { "linkml_meta": {'alias': 'protocols', 'domain_of': ['Study', 'StudyActivity']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    short_name: Optional[str] = Field(default=None, title="Short name", description="""A shortened name for the subject. For example, an acronym, initialism, nickname, or other abbreviation of the name or title.""", json_schema_extra = { "linkml_meta": {'alias': 'short_name',
         'domain_of': ['Organization',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Study","inm7fs:Study"] = Field(default="inm7fs:Study", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class StudyActivity(CurationAid, Thing):
    """
    An activity in the context of a study, where one or more subjects are studied under the influence of certain factors, with one or more instruments, following a set of protocols
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    factors: Optional[list[str]] = Field(default=None, description="""Influencing factors.""", json_schema_extra = { "linkml_meta": {'alias': 'factors', 'domain_of': ['Study', 'StudyActivity']} })
    instruments: Optional[list[str]] = Field(default=None, description="""Employed instruments.""", json_schema_extra = { "linkml_meta": {'alias': 'instruments', 'domain_of': ['Study', 'StudyActivity']} })
    protocols: Optional[list[str]] = Field(default=None, description="""Implemented protocols.""", json_schema_extra = { "linkml_meta": {'alias': 'protocols', 'domain_of': ['Study', 'StudyActivity']} })
    study: Optional[str] = Field(default=None, description="""Study context.""", json_schema_extra = { "linkml_meta": {'alias': 'study', 'domain_of': ['StudyActivity', 'Subject']} })
    subjects: Optional[list[str]] = Field(default=None, description="""Studied subjects.""", json_schema_extra = { "linkml_meta": {'alias': 'subjects', 'domain_of': ['StudyActivity']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/StudyActivity","inm7fs:StudyActivity"] = Field(default="inm7fs:StudyActivity", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class Subject(CurationAid, Thing):
    """
    A subject is an entity being investigated in a study. This is a contextual entity. One and the same entity can be different subjects in two different studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid'],
         'slot_usage': {'specimen_of': {'name': 'specimen_of', 'range': 'Subject'}}})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    specimen_of: Optional[str] = Field(default=None, description="""Source subject.""", json_schema_extra = { "linkml_meta": {'alias': 'specimen_of', 'domain_of': ['Subject']} })
    study: Optional[str] = Field(default=None, description="""Study context.""", json_schema_extra = { "linkml_meta": {'alias': 'study', 'domain_of': ['StudyActivity', 'Subject']} })
    subject_type: Optional[str] = Field(default=None, description="""A classifier that identifies the nature/type of a subject. For specimen (a subject derived/taken from another subject), this classifier should be more precise than the classifier of the source subject.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_type', 'domain_of': ['Subject']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/Subject","inm7fs:Subject"] = Field(default="inm7fs:Subject", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
         'exact_mappings': ['dcterms:type'],
         'slot_uri': 'rdf:type'} })


class SubjectType(CurationAid, Thing):
    """
    Classifier for the nature of a subject.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://concepts.inm7.de/s/flat-data/unreleased',
         'mixins': ['CurationAid']})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Site',
                       'Building',
                       'BuildingLevel',
                       'Organization',
                       'Room',
                       'Dataset',
                       'Dimension',
                       'Factor',
                       'Instrument',
                       'Protocol',
                       'Study',
                       'Subject',
                       'SubjectType']} })
    curation_comments: Optional[list[str]] = Field(default=None, title="Comments", description="""A comment about a metadata record either providing additional information for a record curation, or leaving a comment after curation occurred. This can be used to include information that is deemed relevant, but could not be expressed in the provided fields.""", json_schema_extra = { "linkml_meta": {'alias': 'curation_comments',
         'annotations': {'dash:singleLine': {'tag': 'dash:singleLine', 'value': False}},
         'domain_of': ['CurationAid']} })
    display_label: Optional[str] = Field(default=None, title="Record display label", description="""Label to shown when the record is displayed as an item.""", json_schema_extra = { "linkml_meta": {'alias': 'display_label',
         'domain_of': ['CurationAid'],
         'slot_uri': 'skos:prefLabel'} })
    identifiers: Optional[list[Union[Identifier,IssuedIdentifier,ComputedIdentifier,Checksum,DOI]]] = Field(default=None, description="""An unambiguous reference to the subject within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifiers',
         'domain_of': ['CurationAid'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlidentifiers:identifier'} })
    record_contact: Optional[str] = Field(default=None, title="Record contact", description="""Person to contact regarding questions about information in this metadata record.""", json_schema_extra = { "linkml_meta": {'alias': 'record_contact', 'domain_of': ['CurationAid']} })
    pid: str = Field(default=..., title="Persistent identifier", description="""Persistent and globally unique identifier of a `Thing`.""", json_schema_extra = { "linkml_meta": {'alias': 'pid',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 1}},
         'domain_of': ['Thing'],
         'exact_mappings': ['dcterms:identifier',
                            'schema:identifier',
                            'ADMS:identifier'],
         'slot_uri': 'dlthings:pid'} })
    relations: Optional[dict[str, Union[Thing,Property,ValueSpecification,Person,Site,Building,BuildingLevel,Organization,Room,Dataset,DataItem,Distribution,Dimension,Factor,Instrument,Protocol,Study,StudyActivity,Subject,SubjectType]]] = Field(default=None, title="Relations", description="""Declares an unqualified relation of the subject `Thing` to another `Thing`. This schema slot is used to define related things inline. If such a definition is not needed. A qualified relationship can be declared directly using the `characterized_by` slot.""", json_schema_extra = { "linkml_meta": {'alias': 'relations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 6}},
         'domain': 'Thing',
         'domain_of': ['Thing'],
         'exact_mappings': ['dcat:relation', 'dcterms:relation'],
         'relational_role': 'OBJECT',
         'slot_uri': 'dlthings:relation',
         'symmetric': True} })
    annotations: Optional[dict[str, Union[str, Annotation]]] = Field(default=None, title="Annotations", description="""A record of properties of the metadata record on a subject, a collection of tag/text tuples with the semantics of OWL Annotation.""", json_schema_extra = { "linkml_meta": {'alias': 'annotations',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 5}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:NCIT_C44272'],
         'slot_uri': 'dlthings:annotations'} })
    broad_mappings: Optional[list[str]] = Field(default=None, title="Broad mappings", description="""A list of terms from different schemas or terminology systems that have broader meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 9}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:broadMatch'} })
    close_mappings: Optional[list[str]] = Field(default=None, title="Close mappings", description="""A list of terms from different schemas or terminology systems that have close meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 8}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:closeMatch'} })
    description: Optional[str] = Field(default=None, title="Description", description="""A free-text account of the subject.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 4}},
         'broad_mappings': ['obo:IAO_0000300'],
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['dcterms:description', 'rdfs:comment'],
         'slot_uri': 'dlthings:description'} })
    exact_mappings: Optional[list[str]] = Field(default=None, title="Exact mappings", description="""A list of terms from different schemas or terminology systems that have identical meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 7}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:exactMatch'} })
    attributes: Optional[list[AttributeSpecification]] = Field(default=None, title="Attributes", description="""Declares a relation that associates a `Thing` (or another attribute) with an attribute, where an attribute is an intrinsic characteristic, such as a quality, capability, disposition, function, or is an externally derived attribute determined from some descriptor (e.g. a quantity, position, label/identifier). Technically, this declaration is done via an `AttributeSpecification` that combines a `predicate` with a value declaration and the attribute-related slots of a `Thing`. Importantly, such attributes are declared inline, because they do not have a unique identifier. If an identifier is available, a `Thing` declaration (see `relation`), and a qualification of that relationship via a `Statement` (see `characterized_by`) should be preferred.""", json_schema_extra = { "linkml_meta": {'alias': 'attributes',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 3}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['sio:SIO_000008'],
         'slot_uri': 'dlthings:attributes'} })
    characterized_by: Optional[list[Statement]] = Field(default=None, title="Is characterized by", description="""Qualifies relationships between a subject `Thing` and an object `Thing` with a `Statement` declaring a `predicate` on the nature of the relationship.""", json_schema_extra = { "linkml_meta": {'alias': 'characterized_by',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 2}},
         'domain_of': ['ThingMixin'],
         'exact_mappings': ['obo:RO_0000053'],
         'slot_uri': 'dlthings:characterized_by'} })
    narrow_mappings: Optional[list[str]] = Field(default=None, title="Narrow mappings", description="""A list of terms from different schemas or terminology systems that have narrower meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 10}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:narrowMatch'} })
    related_mappings: Optional[list[str]] = Field(default=None, title="Related mappings", description="""A list of terms from different schemas or terminology systems that have related meaning.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'annotations': {'sh:order': {'tag': 'sh:order', 'value': 11}},
         'domain_of': ['ThingMixin'],
         'is_a': 'mappings',
         'slot_uri': 'skos:relatedMatch'} })
    schema_type: Literal["https://concepts.inm7.de/s/flat-data/unreleased/SubjectType","inm7fs:SubjectType"] = Field(default="inm7fs:SubjectType", description="""State that the subject is an instance of a particular schema class. Typically, no explicit value needs to be assigned to this slot, because it matches the class type of a particular record. However, this slots can be used as a type designator of a schema element for validation and schema structure handling purposes. This is used to indicate specialized schema classes for properties that accept a hierarchy of classes as their range.""", json_schema_extra = { "linkml_meta": {'alias': 'schema_type',
         'designates_type': True,
         'domain_of': ['ThingMixin', 'Identifier'],
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
Identifier.model_rebuild()
IssuedIdentifier.model_rebuild()
ComputedIdentifier.model_rebuild()
Checksum.model_rebuild()
DOI.model_rebuild()
CurationAid.model_rebuild()
Person.model_rebuild()
Site.model_rebuild()
Building.model_rebuild()
BuildingLevel.model_rebuild()
Organization.model_rebuild()
Room.model_rebuild()
Dataset.model_rebuild()
DataItem.model_rebuild()
Distribution.model_rebuild()
Dimension.model_rebuild()
Factor.model_rebuild()
Instrument.model_rebuild()
Protocol.model_rebuild()
Study.model_rebuild()
StudyActivity.model_rebuild()
Subject.model_rebuild()
SubjectType.model_rebuild()
