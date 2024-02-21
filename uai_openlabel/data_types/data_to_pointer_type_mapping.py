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

from typing import Union

__all__: list[str] = []

# noinspection PyProtectedMember
from uai_openlabel.data_types.data_pointer_types import (
    GenericDataType,
    GeometricDataType,
)

# noinspection PyProtectedMember
from uai_openlabel.data_types.generic_data import (
    BooleanData,
    GenericData,
    NumberData,
    TextData,
    VectorData,
)

# noinspection PyProtectedMember
from uai_openlabel.data_types.geometric_data import (
    GeometricData,
    Poly2D,
    Poly3D,
    RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler,
    ThreeDBoundingBoxQuaternion,
    TwoDBoundingBox,
)

# Don't export this, only the function
DATA_TO_POINTER_TYPE_MAPPING: dict[type[Union[GenericData, GeometricData]], Union[GenericDataType, GeometricDataType]] = {
    # GenericData
    BooleanData: GenericDataType.Boolean,
    NumberData: GenericDataType.Number,
    TextData: GenericDataType.Text,
    VectorData: GenericDataType.Vector,
    # GeometricData
    TwoDBoundingBox: GeometricDataType.TwoDBoundingBox,
    RotatedTwoDBoundingBox: GeometricDataType.RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler: GeometricDataType.Cuboid,
    ThreeDBoundingBoxQuaternion: GeometricDataType.Cuboid,
    Poly2D: GeometricDataType.TwoDPolygon,
    Poly3D: GeometricDataType.ThreeDPolygon,
}


def map_data_to_data_pointer_type(data: Union[GenericData, GeometricData]) -> Union[GenericDataType, GeometricDataType]:
    if data.__class__ not in DATA_TO_POINTER_TYPE_MAPPING:
        raise KeyError(data)
    return DATA_TO_POINTER_TYPE_MAPPING[data.__class__]
