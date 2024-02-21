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
from typing import Mapping, Optional, TypeVar, Union

# noinspection PyProtectedMember
from uai_openlabel.elements.action import ActionInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.context import ContextInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.event import EventInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.object import ObjectInFrame

# noinspection PyProtectedMember
from uai_openlabel.elements.relation import Relation

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.stream.stream import Stream

# noinspection PyProtectedMember
from uai_openlabel.transform import Transform

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    ActionUid,
    ContextUid,
    EventUid,
    Number,
    ObjectUid,
    RelationUid,
    StreamUid,
)

__all__: list[str] = []


@dataclass
class FrameProperties(JsonSnakeCaseSerializableMixin):
    timestamp: Optional[Union[str, Number]] = field(default=None)
    streams: Optional[Mapping[StreamUid, Stream]] = field(default=None)
    transforms: Optional[Mapping[str, Transform]] = field(default=None)


T = TypeVar("T", bound="Frame")


@dataclass
class Frame(JsonSnakeCaseSerializableMixin):
    """
    In case time-information is needed, for example, for labeling video sequences, the item frames contains a dictionary of containers at frame level.

    The structure of Frame is similar to the openlabel value as it contains dictionaries for the elements,
    meaning objects, actions, events, contexts, and relations.

    Only the dynamic information inside them is detailed.
    In addition, frame_properties may contain information about timestamping details,
    or transforms of specific coordinate systems and other stream properties.
    """

    actions: Optional[Mapping[ActionUid, ActionInFrame]] = field(default=None)
    contexts: Optional[Mapping[ContextUid, ContextInFrame]] = field(default=None)
    events: Optional[Mapping[EventUid, EventInFrame]] = field(default=None)
    frame_properties: Optional[FrameProperties] = field(default=None)
    objects: Optional[Mapping[ObjectUid, ObjectInFrame]] = field(default=None)
    relations: Optional[Mapping[RelationUid, Relation]] = field(
        default=None
    )  # The spec doesn't specify this correctly, see 7.5. Is there sth like a RelationInFrame we should use here?

    @classmethod
    def example(
        cls: type[T],
        timestamp: str,
        transform_from_and_to: tuple[str, str],
        transform_translation: tuple[float, float, float],
        frame_objects: dict[ObjectUid, ObjectInFrame],
    ) -> T:
        src, dst = transform_from_and_to
        return cls(
            actions=None,
            contexts=None,
            events=None,
            frame_properties=FrameProperties(
                timestamp=timestamp,
                transforms={
                    f"{src}_to_{dst}": Transform.no_rotation_example(src=src, dst=dst, translation=transform_translation)
                },
            ),
            objects=frame_objects,
            relations=None,
        )
