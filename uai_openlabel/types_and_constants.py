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

import re
from typing import Union

__all__: list[str] = []


URI = str


UID_PATTERN = re.compile("^(-?[0-9]+|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$")


class Uid(str):
    def __init__(self, val: str):
        matches_pattern = bool(UID_PATTERN.match(val))
        if not matches_pattern:
            raise ValueError(f"{val} doesn't match the OpenLABEL UID pattern {UID_PATTERN.pattern}")
        super().__init__()


# Types found in OpenLABEL root
FrameUid = Union[Uid, int]
OntologyUid = Uid
ResourceUid = Uid
TagUid = Uid
StreamUid = str


# Element UIDs
ElementUid = Uid
ActionUid = ElementUid
ContextUid = ElementUid
EventUid = ElementUid
ObjectUid = ElementUid
RelationUid = ElementUid


# Types found in element attributes
AttributeName = str
CoordinateSystemUid = str
CoordinateSystemType = str


# Units of length and rotation
Number = Union[int, float]  # Sub-pixel precision is supported

Meter = Number
Radian = Number
Pixel = Number
