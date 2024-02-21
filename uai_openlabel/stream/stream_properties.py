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
from typing import Optional, Union

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.stream.camera_intrinsics import (
    CustomCameraIntrinsics,
    FisheyeCameraIntrinsics,
    PinholeCameraIntrinsics,
)

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import FrameUid, Number

__all__: list[str] = []


@dataclass
class SyncByFrameStream(JsonSnakeCaseSerializableMixin):
    """
    frame_stream: This is the internal frame number inside the stream this OpenLABEL frame corresponds to.
    timestamp: The timestamp of the data source in this particular Stream object
    """

    frame_stream: Optional[FrameUid] = field(default=None)
    timestamp: Optional[Union[str, Number]] = field(default=None)


@dataclass
class SyncByFrameShift(JsonSnakeCaseSerializableMixin):
    """
    frame_shift: Fixed shift or difference between the OpenLABEL master frame count and this stream's internal frame count.
    """

    frame_shift: Optional[int] = field(default=None)


@dataclass
class PinholeCameraStreamProperties(JsonSnakeCaseSerializableMixin):
    sync: Optional[Union[SyncByFrameStream, SyncByFrameShift]] = field(default=None)
    intrinsics_pinhole: Optional[PinholeCameraIntrinsics] = field(default=None)


@dataclass
class FisheyeCameraStreamProperties(JsonSnakeCaseSerializableMixin):
    sync: Optional[Union[SyncByFrameStream, SyncByFrameShift]] = field(default=None)
    intrinsics_fisheye: Optional[FisheyeCameraIntrinsics] = field(default=None)


@dataclass
class CustomCameraStreamProperties(JsonSnakeCaseSerializableMixin):
    sync: Optional[Union[SyncByFrameStream, SyncByFrameShift]] = field(default=None)
    intrinsics_custom: Optional[CustomCameraIntrinsics] = field(default=None)


StreamProperties = Union[
    PinholeCameraStreamProperties,
    FisheyeCameraStreamProperties,
    CustomCameraStreamProperties,
]
