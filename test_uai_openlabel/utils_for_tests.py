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

import json
import os
from pathlib import Path
from typing import Any, cast


def get_absolute_path(path_relative_to_repo_base_dir: str) -> Path:
    cwd = Path(os.getcwd())

    repo_name = "uai_openlabel"
    first_occurrence_of_repo_name_from_back = next(i for i in reversed(range(len(cwd.parts))) if cwd.parts[i] == repo_name)
    cwd_adjusted_parts = cwd.parts[1 : first_occurrence_of_repo_name_from_back + 1] + Path(path_relative_to_repo_base_dir).parts
    cwd_adjusted_file_path = Path("/" + "/".join(cwd_adjusted_parts))

    if not cwd_adjusted_file_path.exists():
        raise FileNotFoundError(f"Could not find the file {cwd_adjusted_file_path}. Current working dir is {os.getcwd()} with the children {[i for i in Path(os.getcwd()).iterdir()]}")
    return cwd_adjusted_file_path


def get_json_content(path_relative_to_repo_base_dir: str) -> dict[str, Any]:
    corrected_path = get_absolute_path(path_relative_to_repo_base_dir)
    with Path(corrected_path).open("r") as f:
        content = json.load(f)
    return cast(dict[str, Any], content)
