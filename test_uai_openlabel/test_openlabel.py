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

from pathlib import Path

from uai_openlabel import OpenLabel


def test_adds_root_key_when_serializing() -> None:
    ol = OpenLabel()
    serialized = ol.to_dict(exclude_none=True)
    assert list(serialized.keys()) == ["openlabel"]
    assert (
        isinstance(serialized["openlabel"], dict)
        and "metadata" in serialized["openlabel"].keys()
    )


def test_deserializes_correctly_with_root_key_given() -> None:
    serialized = {
        "openlabel": {
            "metadata": {"schema_version": "1.0.0", "name": "test"},
        }
    }

    ol = OpenLabel.from_dict(serialized)
    assert ol.metadata.name == "test", "Was not deserialized correctly"


def test_deserializes_correctly_without_root_key_given() -> None:
    serialized = {
        "metadata": {"schema_version": "1.0.0", "name": "test"},
    }

    ol = OpenLabel.from_dict(serialized)
    assert ol.metadata.name == "test", "Was not deserialized correctly"


def test_create_example(tmp_path: Path) -> None:
    example = OpenLabel.example()
    example_json = example.to_dict(exclude_none=True)
    OpenLabel.from_dict(example_json)
