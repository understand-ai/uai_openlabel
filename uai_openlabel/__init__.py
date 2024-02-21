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

# noinspection PyProtectedMember
from uai_openlabel.coordinate_system import CoordinateSystem

# noinspection PyProtectedMember
from uai_openlabel.data_types.data_pointer_types import (
    GenericDataType,
    GeometricDataType,
)

# noinspection PyProtectedMember
from uai_openlabel.data_types.data_to_pointer_type_mapping import (
    map_data_to_data_pointer_type,
)

# noinspection PyProtectedMember
from uai_openlabel.data_types.generic_data import (
    Attributes,
    BooleanData,
    BooleanType,
    GenericData,
    NumberData,
    NumberType,
    TextData,
    TextType,
    VectorData,
    VectorType,
)

# noinspection PyProtectedMember
from uai_openlabel.data_types.geometric_data import (
    GeometricData,
    Poly2D,
    Poly2DMode,
    Poly3D,
    RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler,
    ThreeDBoundingBoxQuaternion,
    TwoDBoundingBox,
)

# noinspection PyProtectedMember
from uai_openlabel.elements.action import Action, ActionInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.context import Context, ContextInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.element_data_pointer import (
    ElementDataPointer,
)

# noinspection PyProtectedMember
from uai_openlabel.elements.event import Event, EventInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.object import Object, ObjectData, ObjectInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.relation import RdfAgent, RdfAgentType, Relation

# noinspection PyProtectedMember
from uai_openlabel.frame import Frame, FrameProperties

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval

# noinspection PyProtectedMember
from uai_openlabel.metadata import Metadata

# noinspection PyProtectedMember
from uai_openlabel.ontology import DetailedOntology

# noinspection PyProtectedMember
from uai_openlabel.openlabel import OpenLabel

# noinspection PyProtectedMember
from uai_openlabel.stream.camera_intrinsics import (
    CustomCameraIntrinsics,
    FisheyeCameraIntrinsics,
    PinholeCameraIntrinsics,
)

# noinspection PyProtectedMember
from uai_openlabel.stream.stream import Stream, StreamType

# noinspection PyProtectedMember
from uai_openlabel.stream.stream_properties import (
    CustomCameraStreamProperties,
    FisheyeCameraStreamProperties,
    PinholeCameraStreamProperties,
    StreamProperties,
    SyncByFrameShift,
    SyncByFrameStream,
)

# noinspection PyProtectedMember
from uai_openlabel.tag import Tag

# noinspection PyProtectedMember
from uai_openlabel.transform import (
    EulerTransformData,
    Matrix4x4TransformData,
    QuaternionTransformData,
    Transform,
)

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    URI,
    ActionUid,
    AttributeName,
    ContextUid,
    CoordinateSystemType,
    CoordinateSystemUid,
    ElementUid,
    EventUid,
    FrameUid,
    Meter,
    Number,
    ObjectUid,
    OntologyUid,
    Pixel,
    Radian,
    RelationUid,
    ResourceUid,
    StreamUid,
    TagUid,
    Uid,
)

# noinspection PyProtectedMember
from uai_openlabel.utils import convert_values, no_default

__all__ = [
    # data_types
    "Attributes",
    "BooleanType",
    "BooleanData",
    "NumberType",
    "NumberData",
    "TextType",
    "TextData",
    "VectorType",
    "VectorData",
    "GenericData",
    "TwoDBoundingBox",
    "RotatedTwoDBoundingBox",
    "ThreeDBoundingBoxQuaternion",
    "ThreeDBoundingBoxEuler",
    "Poly2D",
    "Poly2DMode",
    "Poly3D",
    "GeometricData",
    # elements
    "Action",
    "ActionInFrame",
    "Context",
    "ContextInFrame",
    "GeometricDataType",
    "GenericDataType",
    "ElementDataPointer",
    "map_data_to_data_pointer_type",
    "Event",
    "EventInFrame",
    "ObjectData",
    "Object",
    "ObjectInFrame",
    "RdfAgentType",
    "RdfAgent",
    "Relation",
    # stream
    "PinholeCameraIntrinsics",
    "FisheyeCameraIntrinsics",
    "CustomCameraIntrinsics",
    "Stream",
    "StreamType",
    "SyncByFrameStream",
    "SyncByFrameShift",
    "PinholeCameraStreamProperties",
    "FisheyeCameraStreamProperties",
    "CustomCameraStreamProperties",
    "StreamProperties",
    # types_and_constants
    "URI",
    "Uid",
    "FrameUid",
    "ObjectUid",
    "EventUid",
    "OntologyUid",
    "ResourceUid",
    "TagUid",
    "StreamUid",
    "ElementUid",
    "ActionUid",
    "ContextUid",
    "RelationUid",
    "AttributeName",
    "CoordinateSystemUid",
    "CoordinateSystemType",
    "Number",
    "Meter",
    "Radian",
    "Pixel",
    # All the rest
    "CoordinateSystem",
    "FrameInterval",
    "FrameProperties",
    "Frame",
    "Metadata",
    "DetailedOntology",
    "OpenLabel",
    "Tag",
    "Matrix4x4TransformData",
    "QuaternionTransformData",
    "EulerTransformData",
    "Transform",
    "no_default",
    "convert_values",
]
