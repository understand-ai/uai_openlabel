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
from enum import Enum
from typing import Optional, Sequence

from apischema.metadata import required

# noinspection PyProtectedMember
from uai_openlabel.serializer import JsonSnakeCaseSerializableMixin

# noinspection PyProtectedMember
from uai_openlabel.types_and_constants import URI

# noinspection PyProtectedMember
from uai_openlabel.utils import no_default

__all__: list[str] = []


class BoundaryMode(Enum):
    Include = "include"
    Exclude = "exclude"


@dataclass
class DetailedOntology(JsonSnakeCaseSerializableMixin):
    """
    Section 7.9 of the OpenLABEL standard specification
    """

    uri: URI = field(
        default_factory=lambda: no_default(field="DetailedOntology.uri"),
        metadata=required,
    )

    # TODO Add validation that boundary_mode must be provided if boundary_Sequence is set
    boundary_sequence: Optional[Sequence[str]] = field(default=None)
    boundary_mode: Optional[BoundaryMode] = field(default=None)
