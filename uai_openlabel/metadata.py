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
from typing import Literal, Optional, TypeVar

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

__all__: list[str] = []


T = TypeVar("T", bound="Metadata")


@dataclass
class Metadata(JsonSnakeCaseSerializableMixin):
    schema_version: Literal["1.0.0"] = field(default="1.0.0")
    """	Version number of the OpenLABEL schema this annotation JSON object follows."""

    annotator: Optional[str] = field(default=None)
    """Name or description of the annotator that created the annotations."""

    comment: Optional[str] = field(default=None)
    """Additional information or description about the annotation content."""

    file_version: Optional[str] = field(default=None)
    """Version number of the OpenLABEL annotation content."""

    name: Optional[str] = field(default=None)
    """Name of the OpenLABEL annotation content."""

    tagged_file: Optional[str] = field(default=None)
    """File name or URI of the data file being tagged."""

    @classmethod
    def example(cls: type[T]) -> T:
        return cls(
            schema_version="1.0.0",
            annotator="understand.AI GmbH",
            comment="This is an example OpenLabel file. All labels are imaginary.",
            file_version="1",
            name="Example export",
        )
