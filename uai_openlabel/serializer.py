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

from dataclasses import is_dataclass
from typing import Any, Protocol, TypeVar, cast, runtime_checkable

import apischema

__all__: list[str] = []

T = TypeVar("T", bound="JsonSnakeCaseSerializableMixin")


@runtime_checkable
class DataclassLike(Protocol):
    """
    there is no good way yet to statically assert a class is a "real" dataclass, instead we use this best-effort protocol
    to type check if a class is a dataclass cf. https://stackoverflow.com/a/55240861/7723404
    """

    __dataclass_fields__: dict[str, Any]


class JsonSnakeCaseSerializableMixin(DataclassLike):
    def to_dict(
        self,
        encode_json: bool = False,
        exclude_none: bool = False,
        exclude_defaults: bool = False,
    ) -> dict:
        #  we need to runtime check that we are actually a dataclass here since we can't stop people from inheriting
        # from the mixin without being a dataclass AND statically type-narrow to fulfill the static typing requirements
        if not is_dataclass(self) or not isinstance(self, DataclassLike):
            raise TypeError("JSONSerialization is only supported for dataclasses")

        return apischema.serialize(
            aliaser=apischema.utils.to_snake_case,
            additional_properties=True,
            obj=self,
            exclude_none=exclude_none,
            exclude_defaults=exclude_defaults,
        )

    @classmethod
    def from_dict(cls: type[T], kvs: dict[str, Any], *, infer_missing: bool = False) -> T:
        # we need to runtime check that we are actually a dataclass here since we can't stop people from inheriting
        # from the mixin without being a dataclass
        if not is_dataclass(cls):
            raise TypeError("JSONDeserialization is only supported for dataclasses")

        return cast(
            T,
            apischema.deserialize(
                aliaser=apischema.utils.to_snake_case,
                additional_properties=True,
                data=kvs,
                type=cls,
            ),
        )
