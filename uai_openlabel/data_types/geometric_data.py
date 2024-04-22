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
from typing import Optional, Sequence, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.data_types.generic_data import Attributes

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    AttributeName,
    CoordinateSystemUid,
    Number,
    Pixel,
    Radian,
)

# noinspection PyProtectedMember
from uai_openlabel.utils import convert_values, no_default

__all__: list[str] = []


@dataclass
class TwoDBoundingBox(JsonSnakeCaseSerializableMixin):
    """
    A 2D bounding box is defined as a rectangle by an array of four floating point numbers:

    Attribute	Unit	Description
    x           px      Specify the x-coordinate of the center of the rectangle.
    y           px      Specify the y-coordinate of the center of the rectangle.
    w           px      Specify the width of the rectangle in the x/y-coordinate system (horizontal, x-coordinate dimension).
    h           px      Specify the height of the rectangle in the x/y-coordinate system (vertical, y-coordinate dimension).
    """

    val: tuple[Pixel, Pixel, Pixel, Pixel] = field(
        default_factory=lambda: no_default(field="TwoDBoundingBox.val"),
        metadata=required,
    )

    attributes: Optional[Attributes] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: AttributeName = field(
        default_factory=lambda: no_default(field="TwoDBoundingBox.name"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )
        if len(converted_val) != 4:
            raise ValueError(f"{field_name_for_logging} must have a length of 4")
        self.val = tuple(converted_val)  # type: ignore


@dataclass
class RotatedTwoDBoundingBox(JsonSnakeCaseSerializableMixin):
    """
    The value of a 2D rotated bounding box is defined as a 5-dimensional vector by five numbers:

    Attribute	Unit	Description
    x           px      Specify the x-coordinate of the center of the rectangle.
    y           px      Specify the y-coordinate of the center of the rectangle.
    w           px      Specify the width of the rectangle in the x/y-coordinate system (horizontal, x-coordinate dimension).
    h           px      Specify the height of the rectangle in the x/y-coordinate system (vertical, y-coordinate dimension).
    alpha       rad     Specifies the rotation of the rotated bounding box. It is defined as a right-handed rotation,
                        meaning positive from x-axes to y-axes. The origin of rotation is placed at the center of the bounding box, meaning x, y.
    """

    val: tuple[Pixel, Pixel, Pixel, Pixel, Radian] = field(
        default_factory=lambda: no_default(field="RotatedTwoDBoundingBox.val"),
        metadata=required,
    )

    attributes: Optional[Attributes] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: AttributeName = field(
        default_factory=lambda: no_default(field="RotatedTwoDBoundingBox.name"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )
        if len(converted_val) != 5:
            raise ValueError(f"{field_name_for_logging} must have a length of 5")
        self.val = tuple(converted_val)  # type: ignore


@dataclass
class ThreeDBoundingBoxQuaternion(JsonSnakeCaseSerializableMixin):
    """
    A cuboid in 3D Euclidean space that is defined as val=(x, y, z, qa, qb, qc, qd, sx, sy, and sz), where:

    Attribute	unit	Description
    x           m       The x-coordinate of the 3D position of the center of the cuboid.
    y           m       The y-coordinate of the 3D position of the center of the cuboid.
    z           m       The z-coordinate of the 3D position of the center of the cuboid.
    qa                  Quaternion in non-unit form (x, y, z, and w) as in the SciPy convention.
    qb                  Quaternion in non-unit form (x, y, z, and w) as in the SciPy convention.
    qc                  Quaternion in non-unit form (x, y, z, and w) as in the SciPy convention.
    qd                  Quaternion in non-unit form (x, y, z, and w) as in the SciPy convention.
    sx          m       The x-dimension of the cuboid or the x-coordinate.
    sy          m       The y-dimension of the cuboid or the y-coordinate.
    sz          m       The z-dimension of the cuboid or the z-coordinate.
    """

    val: tuple[Number, Number, Number, Number, Number, Number, Number, Number, Number, Number] = field(
        default_factory=lambda: no_default(field="ThreeDBoundingBoxQuaternion.val"),
        metadata=required,
    )

    attributes: Optional[Attributes] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: AttributeName = field(
        default_factory=lambda: no_default(field="ThreeDBoundingBoxQuaternion.name"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )
        if len(converted_val) != 10:
            raise ValueError(f"{field_name_for_logging} must have a length of 10")
        self.val = tuple(converted_val)  # type: ignore


@dataclass
class ThreeDBoundingBoxEuler(JsonSnakeCaseSerializableMixin):
    """
    A cuboid in 3D Euclidean space defined as val=(x, y, z, rx, ry, rz, sx, sy, and sz), where:

    Attribute	unit	Description
    x           m       The x-coordinate of the 3D position of the center of the cuboid.
    y           m       The y-coordinate of the 3D position of the center of the cuboid.
    z           m       The z-coordinate of the 3D position of the center of the cuboid.
    rx          rad     Euler angles, rx = roll.
    ry          rad     Euler angles, ry = pitch.
    rz          rad     Euler angles, rz = yaw.
    sx          m       The x-dimension of the cuboid or the x-coordinate.
    sy          m       The y-dimension of the cuboid or the y-coordinate.
    sz          m       The z-dimension of the cuboid or the z-coordinate.
    """

    val: tuple[Number, Number, Number, Number, Number, Number, Number, Number, Number] = field(
        default_factory=lambda: no_default(field="ThreeDBoundingBoxEuler.val"),
        metadata=required,
    )

    attributes: Optional[Attributes] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: AttributeName = field(
        default_factory=lambda: no_default(field="ThreeDBoundingBoxEuler.name"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )
        if len(converted_val) != 9:
            raise ValueError(f"{ field_name_for_logging} must have a length of 9")
        self.val = tuple(converted_val)  # type: ignore


class Poly2DMode(Enum):
    """
    Mode of the polyline list of values:
     - "MODE_POLY2D_ABSOLUTE" determines that the poly2d list contains the sequence of (x, y) values of all points of the polyline.
     - "MODE_POLY2D_RELATIVE" specifies that only the first point of the sequence is defined with its (x, y) values, while all the rest are defined relative to it.
     - "MODE_POLY2D_SRF6DCC" specifies that SRF6DCC chain code method is used.
     - "MODE_POLY2D_RS6FCC" specifies that the RS6FCC method is used.
    """

    Absolute = "MODE_POLY2D_ABSOLUTE"
    Relative = "MODE_POLY2D_RELATIVE"
    SRF6DCC = "MODE_POLY2D_SRF6DCC"
    RS6FCC = "MODE_POLY2D_RS6FCC"


@dataclass
class Poly2D(JsonSnakeCaseSerializableMixin):
    """
    A 2D polyline defined as a sequence of 2D points.
    """

    attributes: Optional[Attributes] = field(default=None)

    closed: bool = field(default_factory=lambda: no_default(field="Poly2D.closed"), metadata=required)
    """
    A boolean that defines whether the polyline is closed or not. 
    In case it is closed, it is assumed that the last point of the sequence is connected with the first one.
    """

    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    """Name of the coordinate system in respect of which this object data is expressed."""

    hierarchy: Optional[Sequence[int]] = field(default=None)
    """Hierarchy of the 2D polyline in the context of a set of 2D polylines."""

    mode: Poly2DMode = field(default_factory=lambda: no_default(field="Poly2D.mode"), metadata=required)

    name: AttributeName = field(default_factory=lambda: no_default(field="Poly2D.name"), metadata=required)
    """This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers."""

    val: Union[Sequence[Number], Sequence[str]] = field(
        default_factory=lambda: no_default(field="Poly2D.val"), metadata=required
    )
    """List of numerical values of the polyline, according to its mode."""

    def __post_init__(self) -> None:
        if self.hierarchy is not None and len(self.hierarchy) != 4:
            raise ValueError("Poly2d.hierarchy must be of length 4")

        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int, str],
            field_name_for_logging=field_name_for_logging,
        )
        self.val = tuple(converted_val)


@dataclass
class Poly3D(JsonSnakeCaseSerializableMixin):
    """
    A 3D polyline defined as a sequence of 3D points.
    """

    attributes: Optional[Attributes] = field(default=None)

    closed: bool = field(default_factory=lambda: no_default(field="Poly3D.closed"), metadata=required)
    """
    A boolean that defines whether the polyline is closed or not. 
    In case it is closed, it is assumed that the last point of the sequence is connected with the first one.
    """

    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    """Name of the coordinate system in respect of which this object data is expressed."""

    name: AttributeName = field(default_factory=lambda: no_default(field="Poly3D.name"), metadata=required)
    """This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers."""

    val: Sequence[Number] = field(default_factory=lambda: no_default(field="Poly3D.val"), metadata=required)
    """List of numerical values of the polyline."""

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )
        self.val = tuple(converted_val)


GeometricData = Union[
    TwoDBoundingBox,
    RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler,
    ThreeDBoundingBoxQuaternion,
    Poly2D,
    Poly3D,
]
