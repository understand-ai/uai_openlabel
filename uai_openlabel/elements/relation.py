# Copyright © 2024 understandAI GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Sequence

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval, no_default

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import ElementUid, OntologyUid, ResourceUid

__all__: list[str] = []


class RdfAgentType(Enum):
    Object = "object"
    Action = "action"
    Event = "event"
    Context = "context"


@dataclass
class RdfAgent(JsonSnakeCaseSerializableMixin):
    """
    :param type: The OpenLABEL type of element.
    :param uid: The element UID this RDF agent refers to.
    """

    type: RdfAgentType = field(default_factory=lambda: no_default(field="RdfAgent.type"), metadata=required)
    uid: ElementUid = field(default_factory=lambda: no_default(field="RdfAgent.uid"), metadata=required)


@dataclass
class Relation(JsonSnakeCaseSerializableMixin):
    """
    A relation is a type of element which connects two or more other elements, for example, objects, actions, contexts, or events.
    RDF triples are used to structure the connection with one or more subjects, a predicate, and one or more semantic objects.

    :param frame_intervals: The array of frame intervals where this relation exists or is defined.
    :param name: Name of the relation. It is a friendly name and not used for indexing.
    :param ontology_uid: This is the UID of the ontology where the type of this relation is defined.
    :param rdf_objects: This is the Sequence of RDF semantic objects of this relation.
    :param rdf_subjects: This is the Sequence of RDF semantic subjects of this relation.
    :param resource_uid: This is a JSON object that contains links to external resources.
        Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs.
        Resource_uid values are strings describing the identifier of the element in the external resource.
    :param type: The type of a relation defines the class the predicated of the relation corresponds to.
    """

    name: str = field(default_factory=lambda: no_default(field="Relation.name"), metadata=required)
    type: str = field(default_factory=lambda: no_default(field="Relation.type"), metadata=required)
    rdf_objects: Sequence[RdfAgent] = field(
        default_factory=lambda: no_default(field="Relation.rdf_objects"),
        metadata=required,
    )
    rdf_subjects: Sequence[RdfAgent] = field(
        default_factory=lambda: no_default(field="Relation.rdf_subjects"),
        metadata=required,
    )

    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    ontology_uid: Optional[OntologyUid] = field(default=None)
    resource_uid: Optional[ResourceUid] = field(default=None)
