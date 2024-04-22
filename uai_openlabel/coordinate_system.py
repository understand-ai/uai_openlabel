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
from typing import Optional, Sequence, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.transform import (
    EulerTransformData,
    Matrix4x4TransformData,
    QuaternionTransformData,
    no_default,
)

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import CoordinateSystemType, CoordinateSystemUid

__all__: list[str] = []


@dataclass
class CoordinateSystem(JsonSnakeCaseSerializableMixin):
    """
    :param children: The Sequence of children for this coordinate system
    :param parent: Each coordinate system can declare its parent coordinate system in the hierarchy
    :param pose_wrt_parent: A default or static pose of this coordinate system with respect to the declared parent.
    :param type: The type of coordinate system is defined so reading applications have a simplified view of the hierarchy.
        Suggested types:
            scene_cs, this corresponds to static coordinate systems.
            local_cs, this is a coordinate system of a rigid body, such as a vehicle, which carries with it the sensors.
            sensor_cs, a coordinate system attached to a sensor.
            custom_cs, any other coordinate system defined by the user.
    """

    parent: CoordinateSystemUid = field(
        default_factory=lambda: no_default(field="CoordinateSystem.parent"),
        metadata=required,
    )
    type: CoordinateSystemType = field(
        default_factory=lambda: no_default(field="CoordinateSystem.type"),
        metadata=required,
    )

    children: Optional[Sequence[CoordinateSystemUid]] = field(
        default=None
    )  # TODO See 7.8 first json example: child can also be what is defined in 6.4
    pose_wrt_parent: Optional[Union[Matrix4x4TransformData, QuaternionTransformData, EulerTransformData]] = field(default=None)
