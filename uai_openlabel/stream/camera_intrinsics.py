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
from typing import Optional, Sequence

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import Number, Pixel

# noinspection PyProtectedMember
from uai_openlabel.utils import no_default

__all__: list[str] = []


@dataclass
class FisheyeCameraIntrinsics(JsonSnakeCaseSerializableMixin):
    height_px: Pixel = field(
        default_factory=lambda: no_default(field="FisheyeCameraIntrinsics.height_px"),
        metadata=required,
    )
    width_px: Pixel = field(
        default_factory=lambda: no_default(field="FisheyeCameraIntrinsics.width_px"),
        metadata=required,
    )
    lens_coeffs: Sequence[Number] = field(
        default_factory=lambda: no_default(field="FisheyeCameraIntrinsics.lens_coeffs"),
        metadata=required,
    )

    center_x_px: Optional[Pixel] = field(default=None)
    center_y_px: Optional[Pixel] = field(default=None)
    focal_length_x: Optional[Pixel] = field(default=None)
    focal_length_y: Optional[Pixel] = field(default=None)

    def __post_init__(self) -> None:
        nr_lens_coeffs = len(self.lens_coeffs)
        if nr_lens_coeffs < 4 or nr_lens_coeffs > 5:
            raise ValueError("lens_coeffs must contain 4 or 5 elements")


@dataclass
class PinholeCameraIntrinsics(JsonSnakeCaseSerializableMixin):
    camera_matrix: Sequence[Pixel] = field(
        default_factory=lambda: no_default(field="PinholeCameraIntrinsics.camera_matrix"),
        metadata=required,
    )
    distortion_coeffs: Sequence[Pixel] = field(
        default_factory=lambda: no_default(field="PinholeCameraIntrinsics.distortion_coeffs"),
        metadata=required,
    )
    height_px: Pixel = field(
        default_factory=lambda: no_default(field="PinholeCameraIntrinsics.height_px"),
        metadata=required,
    )
    width_px: Pixel = field(
        default_factory=lambda: no_default(field="PinholeCameraIntrinsics.width_px"),
        metadata=required,
    )

    def __post_init__(self) -> None:
        if len(self.camera_matrix) != 12:
            raise ValueError("camera_matrix must consist of exactly 12 elements")

        nr_distortion_coeffs = len(self.distortion_coeffs)
        if nr_distortion_coeffs < 5 or nr_distortion_coeffs > 14:
            raise ValueError("distortion_coeffs must be between 5 and 14 elements long")


@dataclass
class CustomCameraIntrinsics(JsonSnakeCaseSerializableMixin):
    ...
