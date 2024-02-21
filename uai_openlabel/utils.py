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
from typing import Any, Optional, Sequence, TypeVar, Union

__all__: list[str] = []


logger = logging.getLogger(__name__)


def no_default(field: str) -> Any:
    message = f"Must set a value for {field}"
    raise ValueError(message)


T = TypeVar("T")
V = TypeVar("V")


def unpack_sequence_of_length_1(
    seq: Union[T, list[T], tuple[T]],
    field_name_for_logging: str,
    stand_in_for_empty_seq: Optional[T] = None,
) -> T:
    if not isinstance(seq, list) and not isinstance(seq, tuple):
        return seq

    if stand_in_for_empty_seq is not None and len(seq) == 0:
        return stand_in_for_empty_seq

    if len(seq) != 1:
        raise ValueError(
            f"Got a sequence of values when initializing {field_name_for_logging}. "
            "Only the special case of a sequence length of 1 can be handled. "
        )
    return seq[0]


def convert_values(
    values: Sequence[Any],
    conversion_target: type[T],
    dont_convert: Sequence[type[V]],
    field_name_for_logging: str,
) -> Sequence[Union[T, V]]:
    """No need to add conversion target to dont_convert"""
    extended_dont_convert = [conversion_target] + [t for t in dont_convert]
    to_be_converted = [v.__class__ not in extended_dont_convert for v in values]
    if any(to_be_converted):
        logger.info(
            "The values of field %s aren't of types %s and will be converted to %s",
            field_name_for_logging,
            [t.__name__ for t in extended_dont_convert],
            conversion_target.__name__,
        )

    # see https://github.com/python/mypy/issues/10343
    converted_val = [conversion_target(v) if to_be_converted[i] else v for i, v in enumerate(values)]  # type: ignore[call-arg]
    return converted_val
