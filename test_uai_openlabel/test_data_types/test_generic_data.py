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
from typing import Any, Protocol

import pytest

from uai_openlabel import (
    Attributes,
    NumberData,
    ObjectData,
    ObjectUid,
    TextData,
    VectorData,
)


def test_attributes_iter_yields_all() -> None:
    attributes = Attributes.static_attributes_example()
    assert len(list(attributes)) == 4


def test_object_data_iter_yields_all() -> None:
    object_data = ObjectData.cuboid_with_dynamic_attributes_example(False, (0, 0, 0))
    assert len(list(object_data)) == 5, "__iter__ probably missed the cuboid"


@dataclass
class GenericDataProtocol(Protocol):
    val: Any


@pytest.mark.parametrize(
    "class_name,conversion_target,types_not_needing_conversion",
    [
        # conversion_target is automatically added to types_not_needing_conversion
        [NumberData, float, [int]],
        [TextData, str, []],
        # VectorData is tested in test_geometric_data
    ],
)
def test_values_are_converted_from_single_element_sequence(
    class_name: type[GenericDataProtocol],
    conversion_target: type,
    types_not_needing_conversion: list[type],
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.INFO)

    # Test data that doesn't need conversion
    for conversion_source in [*types_not_needing_conversion, conversion_target]:
        vals_not_needing_conversion = [conversion_source(1.1)]

        caplog.clear()
        data = class_name(val=vals_not_needing_conversion)

        assert len(caplog.messages) == 0
        assert isinstance(data.val, conversion_source)

    # Test data that needs conversion
    class NotExactlyConversionTarget(conversion_target): ...

    vals_needing_conversion = [NotExactlyConversionTarget(1.1)]

    caplog.clear()
    data = class_name(val=vals_needing_conversion)
    assert len(caplog.messages) == 1 and class_name.__name__ in caplog.messages[0]
    assert isinstance(data.val, conversion_target)


def test_object_uid_in_vector_data(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO)
    object_uid = [ObjectUid("075c92c1-7375-49b7-9ebe-76c0f1eac398")]

    data = VectorData(val=object_uid, name="example")

    assert isinstance(data, VectorData)
    assert len(caplog.messages) == 0


def test_object_uid_in_text_data(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO)
    object_uid = ObjectUid("075c92c1-7375-49b7-9ebe-76c0f1eac398")

    data = TextData(val=object_uid, name="example")

    assert isinstance(data, TextData)
    assert len(caplog.messages) == 0
