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
from typing import Mapping, Optional, Sequence, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.data_types.data_pointer_types import (
    GenericDataType,
    GeometricDataType,
)

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval, no_default

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import AttributeName

__all__: list[str] = []


@dataclass
class ElementDataPointer(JsonSnakeCaseSerializableMixin):
    frame_intervals: Sequence[FrameInterval] = field(
        default_factory=lambda: no_default(field="ElementDataPointer.frame_intervals"),
        metadata=required,
    )
    """List of frame intervals of the element data pointed by this pointer."""

    attribute_pointers: Optional[Mapping[AttributeName, GenericDataType]] = field(default=None)
    """
    This is a JSON object which contains pointers to the attributes of the element data pointed by this pointer. 
    The attributes pointer keys shall be the \"name\" of the attribute of the element data this pointer points to.
    """

    type: Optional[Union[GenericDataType, GeometricDataType]] = field(default=None)
