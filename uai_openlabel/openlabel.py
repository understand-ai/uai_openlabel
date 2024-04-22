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
from typing import Any, Mapping, Optional, Sequence, TypeVar, Union, cast

from uai_openlabel import ElementDataPointer, map_data_to_data_pointer_type

# noinspection PyProtectedMember
from uai_openlabel.coordinate_system import CoordinateSystem

# noinspection PyProtectedMember
from uai_openlabel.elements.action import Action

# noinspection PyProtectedMember
from uai_openlabel.elements.context import Context

# noinspection PyProtectedMember
from uai_openlabel.elements.event import Event

# noinspection PyProtectedMember
from uai_openlabel.elements.object import Object, ObjectData, ObjectInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.relation import Relation

# noinspection PyProtectedMember
from uai_openlabel.frame import Frame

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval

# noinspection PyProtectedMember
from uai_openlabel.metadata import Metadata

# noinspection PyProtectedMember
from uai_openlabel.ontology import DetailedOntology

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.stream.stream import Stream

# noinspection PyProtectedMember
from uai_openlabel.tag import Tag

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    URI,
    ActionUid,
    AttributeName,
    ContextUid,
    CoordinateSystemUid,
    EventUid,
    ObjectUid,
    OntologyUid,
    RelationUid,
    ResourceUid,
    StreamUid,
    TagUid,
    Uid,
)

__all__: list[str] = []

T = TypeVar("T", bound="OpenLabel")
J = TypeVar("J", bound=JsonSnakeCaseSerializableMixin)


@dataclass
class OpenLabel(JsonSnakeCaseSerializableMixin):
    """
    The version of the schema shall be defined inside the metadata structure, using the key schema_version.
    All other entries are optional.

    :param actions: This is the JSON object of OpenLABEL actions. AveasAction keys are strings containing numerical UIDs or 32 bytes UUIDs.
    :param contexts: This is the JSON object of OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs.
    :param coordinate_systems: This is a JSON object which contains OpenLABEL coordinate systems.
        Coordinate system keys can be any string, for example, a friendly coordinate system name.
    :param events: This is the JSON object of OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs.
    :param frame_intervals: This is an array of frame intervals.
    :param frames: This is the JSON object of frames that contain the dynamic, timewise, annotations.
        Keys are strings containing numerical frame identifiers, which are denoted as master frame numbers.
    :param metadata: This JSON object contains information, that is, metadata, about the annotation file itself.
    :param objects: This is the JSON object of OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs.
    :param ontologies: This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs.
        Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional Sequences of included and excluded terms.
    :param relations: This is the JSON object of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs.
    :param resources: This is the JSON object of OpenLABEL resources. Resource keys are strings containing numerical UIDs or 32 bytes UUIDs.
        Resource values are strings that describe an external resource, for example, file name, URLs, that may be
        used to link data of the OpenLABEL annotation content with external existing content.
    :param streams: This is a JSON object which contains OpenLABEL streams. Stream keys can be any string, for example, a friendly stream name.
    :param tags: This is the JSON object of tags. Tag keys are strings containing numerical UIDs or 32 bytes UUIDs.
    """

    metadata: Metadata = field(default_factory=Metadata)

    actions: Optional[Mapping[ActionUid, Action]] = field(default=None)
    contexts: Optional[Mapping[ContextUid, Context]] = field(default=None)
    coordinate_systems: Optional[Mapping[CoordinateSystemUid, CoordinateSystem]] = field(default=None)
    events: Optional[Mapping[EventUid, Event]] = field(default=None)
    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    frames: Optional[Mapping[Uid, Frame]] = field(default=None)
    objects: Optional[Mapping[ObjectUid, Object]] = field(default=None)
    ontologies: Optional[Mapping[OntologyUid, Union[URI, DetailedOntology]]] = field(default=None)
    relations: Optional[Mapping[RelationUid, Relation]] = field(default=None)
    resources: Optional[Mapping[ResourceUid, URI]] = field(default=None)
    streams: Optional[Mapping[StreamUid, Stream]] = field(default=None)
    tags: Optional[Mapping[TagUid, Tag]] = field(default=None)

    @classmethod
    def example(cls: type[T]) -> T:
        """This method creates an example OpenLabel containing the fields that we would usually also fill in our exports."""

        frames = {
            Uid("001"): Frame.example(
                timestamp="1700126000005000",  # ms
                transform_from_and_to=("reference", "world"),
                transform_translation=(1.0, 0.0, 0.0),
                frame_objects={
                    Uid("1"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(1.0, 0.0, 0.0)),
                    Uid("2"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(5.0, 1.0, 0.0)),
                    Uid("3"): ObjectInFrame.example(
                        toggle_attribute_values=True,
                        cuboid_translation=(10.0, 1.0, 0.0),
                    ),
                },
            ),
            Uid("002"): Frame.example(
                timestamp="1700126000005010",  # 10ms later
                transform_from_and_to=("reference", "world"),
                transform_translation=(1.1, 0.0, 0.0),
                frame_objects={
                    Uid("1"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(1.1, 0.0, 0.0)),
                    Uid("2"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(5.1, 1.0, 0.0)),
                    Uid("3"): ObjectInFrame.example(
                        toggle_attribute_values=True,
                        cuboid_translation=(10.1, 1.0, 0.0),
                    ),
                },
            ),
            Uid("003"): Frame.example(
                timestamp="1700126000005020",  # 10ms later
                transform_from_and_to=("reference", "world"),
                transform_translation=(1.2, 0.0, 0.0),
                frame_objects={
                    Uid("1"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(1.2, 0.0, 0.0)),
                    Uid("2"): ObjectInFrame.example(toggle_attribute_values=True, cuboid_translation=(5.1, 1.0, 0.0)),
                    Uid("3"): ObjectInFrame.example(
                        toggle_attribute_values=True,
                        cuboid_translation=(10.2, 1.0, 0.0),
                    ),
                },
            ),
        }

        frame_interval = FrameInterval(frame_start=Uid("1"), frame_end=Uid("3"))

        object_data_pointers: dict[AttributeName, ElementDataPointer] = {}
        attributes_of_dynamic_objects = ObjectData.cuboid_with_dynamic_attributes_example(False, (0.0, 0.0, 0.0))
        for data in attributes_of_dynamic_objects:
            assert data.name is not None, "All attributes must have a name in this example"
            object_data_pointers[data.name] = ElementDataPointer(
                frame_intervals=[frame_interval],
                type=map_data_to_data_pointer_type(data),
            )

        objects = {
            Uid("1"): Object.car_example(
                name="ego_vehicle",
                frame_interval=frame_interval,
                object_data_pointers=object_data_pointers,
            ),
            Uid("2"): Object.car_example(
                name="car1",
                frame_interval=frame_interval,
                object_data_pointers=object_data_pointers,
            ),
            Uid("3"): Object.car_example(
                name="car2",
                frame_interval=frame_interval,
                object_data_pointers=object_data_pointers,
            ),
        }

        coordinate_systems_dict = {
            "world": CoordinateSystem(parent="", type="scene_cs", children=["reference"]),
            "reference": CoordinateSystem(parent="world", type="sensor_cs"),
        }
        return cls(
            metadata=Metadata.example(),
            actions=None,
            contexts=None,
            coordinate_systems=coordinate_systems_dict,
            events=None,
            frame_intervals=[frame_interval],
            frames=cast(Mapping, frames),
            objects=objects,
            ontologies=None,
            relations=None,
            resources=None,
            streams={"reference": Stream.example_lidar_stream("reference")},
            tags=None,
        )

    @classmethod
    def from_dict(cls: type[J], kvs: dict[str, Any], *, infer_missing: bool = False) -> J:
        """
        Any ASAM OpenLABEL JSON data shall have a root key named openlabel.
        """
        if list(kvs.keys()) == ["openlabel"]:
            kvs = kvs["openlabel"]
        return super().from_dict(kvs, infer_missing=infer_missing)

    def to_dict(
        self,
        encode_json: bool = False,
        exclude_none: bool = False,
        exclude_defaults: bool = False,
    ) -> dict:
        serialized = super().to_dict(encode_json, exclude_none, exclude_defaults)
        with_root_key = {"openlabel": serialized}
        return with_root_key
