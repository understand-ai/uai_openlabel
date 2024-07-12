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

import logging
from dataclasses import dataclass
from typing import Any, Optional, Protocol

import pytest

from uai_openlabel import (
    Poly2D,
    Poly2DMode,
    Poly3D,
    RotatedTwoDBoundingBox,
    ThreeDBoundingBoxEuler,
    ThreeDBoundingBoxQuaternion,
    TwoDBoundingBox,
    VectorData,
)


@dataclass
class GeometricDataProtocol(Protocol):
    val: Any
    name: str  # name is mandatory in all GeometricData


@pytest.mark.parametrize(
    "class_name,val_length,conversion_target,types_not_needing_conversion,extra_init_kwargs",
    [
        # conversion_target is automatically added to types_not_needing_conversion
        [VectorData, None, float, [int, str], {}],
        [TwoDBoundingBox, 4, float, [int], {}],
        [RotatedTwoDBoundingBox, 5, float, [int], {}],
        [ThreeDBoundingBoxEuler, 9, float, [int], {}],
        [ThreeDBoundingBoxQuaternion, 10, float, [int], {}],
        [
            Poly2D,
            None,
            float,
            [int, str],
            {"closed": False, "mode": Poly2DMode.Absolute},
        ],
        [Poly3D, None, float, [int], {"closed": False}],
    ],
)
def test_values_are_converted_and_tested_for_length(
    class_name: type[GeometricDataProtocol],
    val_length: Optional[int],
    conversion_target: type,
    types_not_needing_conversion: list[type],
    extra_init_kwargs: dict,
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.INFO)

    # Test data that doesn't need conversion
    data_length = val_length if val_length is not None else 4
    for conversion_source in [*types_not_needing_conversion, conversion_target]:
        vals_not_needing_conversion = [conversion_source(1.1)] * data_length

        caplog.clear()
        data = class_name(val=vals_not_needing_conversion, name="example", **extra_init_kwargs)

        assert len(caplog.messages) == 0
        assert all(isinstance(v, conversion_source) for v in data.val)

    # Test data that needs conversion
    class NotExactlyConversionTarget(conversion_target): ...

    vals_needing_conversion = [NotExactlyConversionTarget(1.1)] * data_length

    caplog.clear()
    data = class_name(val=vals_needing_conversion, name="example", **extra_init_kwargs)
    converted_val_types = [v.__class__ for v in data.val]

    assert len(caplog.messages) == 1 and class_name.__name__ in caplog.messages[0]
    assert all([t == conversion_target for t in converted_val_types])

    # Make sure it raises exception for wrong length if length is important
    if val_length is not None:
        vals_of_wrong_length = [conversion_target(1.1)] * (val_length - 1)
        with pytest.raises(ValueError, match=str(val_length)):
            class_name(val=vals_of_wrong_length, name="example", **extra_init_kwargs)
