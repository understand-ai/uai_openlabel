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

from enum import Enum

__all__: list[str] = []


class GenericDataType(Enum):
    Boolean = "boolean"
    Number = "num"
    Text = "text"
    Vector = "vec"


class GeometricDataType(Enum):
    TwoDBoundingBox = "bbox"
    RotatedTwoDBoundingBox = "rbbox"
    TwoDPolygon = "poly2d"
    ThreeDPolygon = "poly3d"
    Cuboid = "cuboid"
    Image = "image"
    Matrix = "mat"
    BinaryPayload = "binary"
    Point2d = "point2d"
    Point3d = "point3d"
    LineReference = "line_reference"
    AreaReference = "area_reference"
    Mesh = "mesh"
