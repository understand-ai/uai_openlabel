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

from deepdiff import DeepDiff

from test_uai_openlabel.utils_for_tests import get_json_content
from uai_openlabel import OpenLabel


def test_db_openlabel_example() -> None:
    content = get_json_content(
        "test_uai_openlabel/test_asam_examples/modified_19_vegetation_curve_19.1_labels.json"
    )
    parsed = OpenLabel.from_dict(content)
    back_to_dict = dict(parsed.to_dict(exclude_none=True))

    diff = DeepDiff(content, back_to_dict)
    assert len(diff.affected_paths) == 0


def test_bbox_simple() -> None:
    content = get_json_content(
        "test_uai_openlabel/test_asam_examples/openlabel100_test_bbox_simple.json"
    )
    parsed = OpenLabel.from_dict(content)
    back_to_dict = dict(parsed.to_dict(exclude_none=True))

    diff = DeepDiff(content, back_to_dict)
    assert len(diff.affected_paths) == 0


def test_bbox_simple_with_attributes() -> None:
    content = get_json_content(
        "test_uai_openlabel/test_asam_examples/openlabel100_test_bbox_simple_attributes.json"
    )
    parsed = OpenLabel.from_dict(content)
    back_to_dict = dict(parsed.to_dict(exclude_none=True))

    diff = DeepDiff(content, back_to_dict)
    assert len(diff.affected_paths) == 0


def test_example_cuboids() -> None:
    content = get_json_content(
        "test_uai_openlabel/test_asam_examples/openlabel100_example_cuboids.json"
    )
    parsed = OpenLabel.from_dict(content)
    back_to_dict = dict(parsed.to_dict(exclude_none=True))

    diff = DeepDiff(content, back_to_dict)
    assert len(diff.affected_paths) == 0
