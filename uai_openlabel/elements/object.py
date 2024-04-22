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

import builtins
from dataclasses import dataclass, field
from typing import Mapping, Optional, Sequence, TypeVar, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.data_types.generic_data import Attributes

# noinspection PyProtectedMember
from uai_openlabel.data_types.geometric_data import (
    Poly2D,
    Poly3D,
    RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler,
    ThreeDBoundingBoxQuaternion,
    TwoDBoundingBox,
)

# noinspection PyProtectedMember
from uai_openlabel.elements.element_data_pointer import ElementDataPointer

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval, no_default

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import AttributeName, OntologyUid, ResourceUid

__all__: list[str] = []


D = TypeVar("D", bound="ObjectData")


@dataclass
class ObjectData(Attributes):
    # TODO When implementing these, don't forget to add them to data_to_pointer_type_mapping.py
    # boolean, num, text, vec defined in Attributes
    # area_reference: Optional[Sequence[...]] = field(default=None)
    bbox: Optional[Sequence[TwoDBoundingBox]] = field(default=None)
    # binary: Optional[Sequence[...]] = field(default=None)
    cuboid: Optional[Sequence[Union[ThreeDBoundingBoxEuler, ThreeDBoundingBoxQuaternion]]] = field(default=None)
    # image: Optional[Sequence[...]] = field(default=None)
    # line_reference: Optional[Sequence[...]] = field(default=None)
    # mat: Optional[Sequence[...]] = field(default=None)
    # mesh: Optional[Sequence[...]] = field(default=None)
    # point2d: Optional[Sequence[...]] = field(default=None)
    # point3d: Optional[Sequence[...]] = field(default=None)
    poly2d: Optional[Sequence[Poly2D]] = field(default=None)
    poly3d: Optional[Sequence[Poly3D]] = field(default=None)
    rbbox: Optional[Sequence[RotatedTwoDBoundingBox]] = field(default=None)

    @classmethod
    def cuboid_with_dynamic_attributes_example(
        cls: type[D],
        toggle_attribute_value: bool,
        cuboid_translation: tuple[float, float, float],
    ) -> D:
        example = cls.dynamic_attributes_example(toggle_attribute_value)

        euler_angles = (0.0, 0.0, 0.0)
        cuboid_size = (4.1, 1.75, 1.45)
        example.cuboid = [
            ThreeDBoundingBoxEuler(
                val=cuboid_translation + euler_angles + cuboid_size,
                name="bounding_box",
            )
        ]
        return example


T = TypeVar("T", bound="Object")


@dataclass
class Object(JsonSnakeCaseSerializableMixin):
    """
    A structure to represent information about physical entities in scenes.
    Examples of objects are pedestrians, cars, the ego-vehicle, traffic signs, lane markings, building, and trees.

    :param name: A friendly identifier of the element, is not unique but employed by human users to rapidly identify elements in the scene, for example, Peter.
    :param type: The classification of the object
    :param frame_intervals: An array of frame intervals where the object exists.
    :param ontology_uid: A string identifier of the ontology which contains the definition of the type of the element.
    :param resource_uid: A string identifier of the resource which contains additional information on the type of the element.
    :param object_data: Container of static information about the object.
    :param object_data_pointers: Pointers to element data at frames.
    """

    name: str = field(default_factory=lambda: no_default(field="Object.name"), metadata=required)
    type: str = field(default_factory=lambda: no_default(field="Object.type"), metadata=required)

    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    ontology_uid: Optional[OntologyUid] = field(default=None)
    resource_uid: Optional[ResourceUid] = field(default=None)
    object_data: Optional[ObjectData] = field(default=None)
    object_data_pointers: Optional[Mapping[AttributeName, ElementDataPointer]] = field(default=None)

    @classmethod
    def car_example(
        cls: builtins.type[T],
        name: str,
        frame_interval: FrameInterval,
        object_data_pointers: Optional[dict[AttributeName, ElementDataPointer]] = None,
    ) -> T:
        return cls(
            name=name,
            type="car",
            frame_intervals=[frame_interval],
            object_data=ObjectData.static_attributes_example(),
            object_data_pointers=object_data_pointers,
        )


F = TypeVar("F", bound="ObjectInFrame")


@dataclass
class ObjectInFrame(JsonSnakeCaseSerializableMixin):
    object_data: ObjectData = field(
        default_factory=lambda: no_default(field="ObjectInFrame.object_data"),
        metadata=required,
    )

    @classmethod
    def example(
        cls: builtins.type[F],
        toggle_attribute_values: bool,
        cuboid_translation: tuple[float, float, float],
    ) -> F:
        return cls(
            object_data=ObjectData.cuboid_with_dynamic_attributes_example(
                toggle_attribute_value=toggle_attribute_values,
                cuboid_translation=cuboid_translation,
            )
        )
