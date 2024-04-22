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
from typing import Optional, TypeVar, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    CoordinateSystemUid,
    Number,
    Radian,
)

# noinspection PyProtectedMember
from uai_openlabel.utils import no_default

__all__: list[str] = []


@dataclass
class Matrix4x4TransformData:
    """
    Flattened list of 16 entries encoding a 4x4 homogeneous matrix to enable transform 3D column homogeneous
    vectors 4x1 using right-multiplication of matrices: X_dst = matrix_4x4 * X_src
    """

    matrix4x4: tuple[Number, ...] = field(
        default_factory=lambda: no_default(field="Matrix4x4TransformData.matrix4x4"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        if len(self.matrix4x4) != 16:
            raise ValueError("matrix4x4 must be exactly 16 elements long.")


@dataclass
class QuaternionTransformData(JsonSnakeCaseSerializableMixin):
    """
    A transform can be defined with a quaternion to encode the rotation of a coordinate system
    with respect to another, and a translation.
    """

    quaternion: tuple[Number, Number, Number, Number] = field(
        default_factory=lambda: no_default(field="QuaternionTransformData.quaternion"),
        metadata=required,
    )
    translation: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="QuaternionTransformData.translation"),
        metadata=required,
    )


@dataclass
class EulerTransformData(JsonSnakeCaseSerializableMixin):
    """
    A transform can be defined with a sequence of Euler angles to encode the rotation of a coordinate system
    with respect to another and a translation.
    """

    euler_angles: tuple[Radian, Radian, Radian] = field(
        default_factory=lambda: no_default(field="EulerTransformData.euler_angles"),
        metadata=required,
    )
    sequence: Optional[str] = field(default="ZYX")
    translation: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="EulerTransformData.translation"),
        metadata=required,
    )


T = TypeVar("T", bound="Transform")


@dataclass
class Transform(JsonSnakeCaseSerializableMixin):
    """
    The transforms between coordinate systems may also be defined for each frame, overriding the default static pose.
    Transforms are defined with a friendly name used as index and the following properties:

    src: The name of the source coordinate system. This shall be the name of a valid (declared) coordinate system.
    dst: The destination coordinate system. This shall be the name of a valid (declared) coordinate system.
    transform_src_to_dst: This is the transform expressed in algebraic form, for example, as a 4x4 matrix enclosing a 3D rotation and a 3D translation between the coordinate systems.
    """

    dst: CoordinateSystemUid = field(default_factory=lambda: no_default(field="Transform.dst"), metadata=required)
    src: CoordinateSystemUid = field(default_factory=lambda: no_default(field="Transform.src"), metadata=required)
    transform_src_to_dst: Union[Matrix4x4TransformData, QuaternionTransformData, EulerTransformData] = field(
        default_factory=lambda: no_default(field="Transform.transform_src_to_dst"),
        metadata=required,
    )

    @classmethod
    def no_rotation_example(
        cls: type[T],
        src: CoordinateSystemUid,
        dst: CoordinateSystemUid,
        translation: tuple[float, float, float],
    ) -> T:
        # fmt: off
        translation_without_rotation = (
            1.0, 0.0, 0.0, translation[0], 
            0.0, 1.0, 0.0, translation[1], 
            0.0, 0.0, 1.0, translation[2], 
            0.0, 0.0, 0.0, 1.0
        )
        # fmt: on
        return cls(
            src=src,
            dst=dst,
            transform_src_to_dst=Matrix4x4TransformData(matrix4x4=translation_without_rotation),
        )
