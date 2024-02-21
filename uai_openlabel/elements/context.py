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
from typing import Mapping, Optional, Sequence

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.data_types.generic_data import Attributes

# noinspection PyProtectedMember
from uai_openlabel.elements.element_data_pointer import ElementDataPointer

# noinspection PyProtectedMember
from uai_openlabel.frame_interval import FrameInterval, no_default

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import AttributeName, OntologyUid, ResourceUid

__all__: list[str] = []


@dataclass
class Context(JsonSnakeCaseSerializableMixin):
    """
    Other descriptive information about the scene that contains no spatial or temporal information and therefore
    is not targeted by actions or events, for example:
     - properties of the scene, such as Urban or Highway.
     - weather conditions, such as Sunny or Cloudy.
     - general information about the location, such as Germany or Spain.
    """

    name: str = field(
        default_factory=lambda: no_default(field="Context.name"), metadata=required
    )
    type: str = field(
        default_factory=lambda: no_default(field="Context.type"), metadata=required
    )

    frame_intervals: Optional[Sequence[FrameInterval]] = field(default=None)
    ontology_uid: Optional[OntologyUid] = field(default=None)
    resource_uid: Optional[ResourceUid] = field(default=None)
    context_data: Optional[Attributes] = field(default=None)
    context_data_pointers: Optional[Mapping[AttributeName, ElementDataPointer]] = field(
        default=None
    )


@dataclass
class ContextInFrame(JsonSnakeCaseSerializableMixin):
    context_data: Attributes = field(
        default_factory=lambda: no_default(field="ContextInFrame.context_data"),
        metadata=required,
    )
