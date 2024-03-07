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
from typing import Iterable, Iterator, Optional, Sequence, TypeVar, Union

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import (
    AttributeName,
    CoordinateSystemUid,
    Number,
    ObjectUid,
)

# noinspection PyProtectedMember
from uai_openlabel.utils import convert_values, no_default, unpack_sequence_of_length_1

__all__: list[str] = []


class BooleanType(Enum):
    Value = "value"


B = TypeVar("B", bound="BooleanData")


@dataclass
class BooleanData(JsonSnakeCaseSerializableMixin):
    val: bool = field(default_factory=lambda: no_default(field="BooleanData.val"), metadata=required)

    attributes: Optional["Attributes"] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: Optional[AttributeName] = field(default=None)
    type: Optional[BooleanType] = field(default=None)

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        self.val = unpack_sequence_of_length_1(self.val, field_name_for_logging)
        converted_val = convert_values(
            values=[self.val],
            conversion_target=bool,
            dont_convert=[],
            field_name_for_logging=field_name_for_logging,
        )[0]
        self.val = converted_val

    @classmethod
    def static_example(cls: builtins.type[B]) -> B:
        """An attribute that only has one value."""
        return cls(
            val=True,
            name="has_driver",
            type=BooleanType.Value,
        )

    @classmethod
    def dynamic_example(cls: builtins.type[B], toggle_value: bool = False) -> B:
        """An attribute that may take one of two values, toggleable via the toggle_value switch."""
        return cls(
            val=False if toggle_value else True,
            name="brake_lights_on",
            type=BooleanType.Value,
        )


class NumberType(Enum):
    Value = "value"
    Min = "min"
    Max = "max"


N = TypeVar("N", bound="NumberData")


@dataclass
class NumberData(JsonSnakeCaseSerializableMixin):
    val: Number = field(default_factory=lambda: no_default(field="NumberData.val"), metadata=required)

    attributes: Optional["Attributes"] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: Optional[AttributeName] = field(default=None)
    type: Optional[NumberType] = field(default=None)

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        self.val = unpack_sequence_of_length_1(self.val, field_name_for_logging)
        converted_val = convert_values(
            values=[self.val],
            conversion_target=float,
            dont_convert=[int],
            field_name_for_logging=field_name_for_logging,
        )[0]
        self.val = converted_val

    @classmethod
    def static_example(cls: builtins.type[N]) -> N:
        """An attribute that only has one value."""
        return cls(
            val=4,
            name="nr_wheels",
            type=NumberType.Value,
        )

    @classmethod
    def dynamic_example(cls: builtins.type[N], toggle_value: bool = False) -> N:
        """An attribute that may take one of two values, toggleable via the toggle_value switch."""
        return cls(
            val=5 if toggle_value else 4,
            name="leaves_on_hood",
            type=NumberType.Value,
        )


class TextType(Enum):
    Value = "value"


T = TypeVar("T", bound="TextData")


@dataclass
class TextData(JsonSnakeCaseSerializableMixin):
    val: str = field(default_factory=lambda: no_default(field="TextData.val"), metadata=required)

    attributes: Optional["Attributes"] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: Optional[AttributeName] = field(default=None)
    type: Optional[TextType] = field(default=None)

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        self.val = unpack_sequence_of_length_1(self.val, field_name_for_logging, "")
        converted_val = convert_values(
            values=[self.val],
            conversion_target=str,
            dont_convert=[ObjectUid],
            field_name_for_logging=field_name_for_logging,
        )[0]
        self.val = converted_val

    @classmethod
    def static_example(cls: builtins.type[T]) -> T:
        """An attribute that only has one value."""
        return cls(
            val="red",
            name="color",
            type=TextType.Value,
        )

    @classmethod
    def dynamic_example(cls: builtins.type[T], toggle_value: bool = False) -> T:
        """An attribute that may take one of two values, toggleable via the toggle_value switch."""
        return cls(
            val="NE" if toggle_value else "ENE",
            name="compass_heading",
            type=TextType.Value,
        )


class VectorType(Enum):
    Values = "values"
    Ranges = "ranges"


V = TypeVar("V", bound="VectorData")


@dataclass
class VectorData(JsonSnakeCaseSerializableMixin):
    val: Union[Sequence[Number], Sequence[str]] = field(
        default_factory=lambda: no_default(field="VectorData.val"), metadata=required
    )

    attributes: Optional["Attributes"] = field(default=None)
    coordinate_system: Optional[CoordinateSystemUid] = field(default=None)
    name: Optional[AttributeName] = field(default=None)
    type: Optional[VectorType] = field(default=None)

    def __post_init__(self) -> None:
        """apischema doesn't allow subclasses of the annotated types, so we need to cast them."""
        field_name_for_logging = f"{self.__class__.__name__}.val"
        converted_val = convert_values(
            values=self.val,
            conversion_target=float,
            dont_convert=[int, str, ObjectUid],
            field_name_for_logging=field_name_for_logging,
        )
        self.val = tuple(converted_val)

    @classmethod
    def static_example(cls: builtins.type[V]) -> V:
        """An attribute that only has one value."""
        return cls(
            val=["tobi", "veith", "daniel"],
            name="previous_drivers",
            type=VectorType.Values,
        )

    @classmethod
    def dynamic_example(cls: builtins.type[V], toggle_value: bool = False) -> V:
        """An attribute that may take one of two values, toggleable via the toggle_value switch."""
        return cls(
            val=[0.2, 0.7, 0.3] if toggle_value else [0.5, 0.1, 0.4],
            name="radio_coefficients",
            type=VectorType.Values,
        )


GenericData = Union[BooleanData, NumberData, TextData, VectorData]


A = TypeVar("A", bound="Attributes")


@dataclass
class Attributes(JsonSnakeCaseSerializableMixin, Iterable[GenericData]):
    boolean: Optional[Sequence[BooleanData]] = field(default=None)
    num: Optional[Sequence[NumberData]] = field(default=None)
    text: Optional[Sequence[TextData]] = field(default=None)
    vec: Optional[Sequence[VectorData]] = field(default=None)

    def __iter__(self) -> Iterator[GenericData]:
        """Iterates over all the data, in all fields, in this order: boolean, num, text, vec."""
        for field_name in self.__dataclass_fields__:
            attributes = self.__getattribute__(field_name)
            if attributes is None:
                continue
            for a in attributes:
                yield a

    @classmethod
    def static_attributes_example(cls: builtins.type[A]) -> A:
        """Contains attributes meant to be static."""
        return cls(
            boolean=[BooleanData.static_example()],
            num=[NumberData.static_example()],
            text=[TextData.static_example()],
            vec=[VectorData.static_example()],
        )

    @classmethod
    def dynamic_attributes_example(cls: builtins.type[A], toggle_value: bool = False) -> A:
        """Contains attributes meant to be dynamic. Use the toggle_value switch to vary them."""
        return cls(
            boolean=[BooleanData.dynamic_example(toggle_value)],
            num=[NumberData.dynamic_example(toggle_value)],
            text=[TextData.dynamic_example(toggle_value)],
            vec=[VectorData.dynamic_example(toggle_value)],
        )
