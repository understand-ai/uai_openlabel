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

import builtins
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, TypeVar

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.stream.stream_properties import (
    StreamProperties,
)

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import URI

# noinspection PyProtectedMember

__all__: list[str] = []


class StreamType(Enum):
    Camera = "camera"
    Lidar = "lidar"
    Radar = "radar"
    GPS_IMU = "gps_imu"
    Other = "other"


T = TypeVar("T", bound="Stream")


@dataclass
class Stream(JsonSnakeCaseSerializableMixin):
    """
    From 7.5.3 of the openLABEL standard:
    The sync field within stream_properties defines the frame number of the stream that corresponds to this frame,
    along with timestamping information, if needed.

    This feature is useful for annotating multiple cameras which might not be perfectly aligned.
    In such cases, frame 0 of the ASAM OpenLABEL JSON data corresponds to frame 0 of the first stream to occur.
    In this way, frame_stream shall identify which frame of this stream corresponds to the frame in which it is enclosed.
    """

    description: Optional[str] = field(default=None)
    type: Optional[StreamType] = field(default=None)

    stream_properties: Optional[StreamProperties] = field(default=None)
    uri: Optional[URI] = field(default=None)

    @classmethod
    def example_lidar_stream(cls: builtins.type[T], description: str) -> T:
        return cls(description=description, type=StreamType.Lidar)
