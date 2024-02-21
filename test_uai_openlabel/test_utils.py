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

from typing import Any

import pytest

from uai_openlabel.utils import unpack_sequence_of_length_1


@pytest.mark.parametrize("data", [1, "abc", 0.5])
def test_unpack_sequence_of_length_1(data: Any) -> None:
    logging_snippet = "log me"

    assert (
        unpack_sequence_of_length_1(
            seq=data,
            field_name_for_logging=logging_snippet,
            stand_in_for_empty_seq=data.__class__(1.1),
        )
        == data
    )
    assert (
        unpack_sequence_of_length_1(
            seq=[data],
            field_name_for_logging=logging_snippet,
            stand_in_for_empty_seq=data.__class__(1.1),
        )
        == data
    )
    assert unpack_sequence_of_length_1(
        seq=[],
        field_name_for_logging=logging_snippet,
        stand_in_for_empty_seq=data.__class__(1.1),
    ) == data.__class__(1.1)

    with pytest.raises(ValueError):
        unpack_sequence_of_length_1(
            seq=[data, data],
            field_name_for_logging=logging_snippet,
            stand_in_for_empty_seq=data.__class__(1.1),
        )
