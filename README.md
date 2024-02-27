# uai_openlabel

This repository is an implementation of the [ASAM OpenLABEL](https://www.asam.net/standards/detail/openlabel/) v1.0.0 standard. 
OpenLABEL defines a JSON schema for saving annotations in the context of data labeling. 

## How to use

This library can be installed via pip using `pip install uai_openlabel` or with poetry using `poetry add uai_openlabel`. 

The entry point to the uai_openlabel data structure is `OpenLabel`, importable via `from uai_openlabel import OpenLabel`. 
To export an example OpenLABEL file and save it to disk, do

```python
import json
from pathlib import Path
from uai_openlabel import OpenLabel

example = OpenLabel.example()
with Path("where/to/save/example.json").open("w") as f:
    json.dump(example.to_dict(exclude_none=True), f)
```

Use `to_dict(exlude_none=True)` to remove any none-valued fields from the dataclass.
This makes the export much more compact and is also the way the official ASAM examples are serialized.


# Development

## Poetry
This package uses Poetry, a tool for dependency management and packaging.
Please install it via the official installer from [here](https://python-poetry.org/docs/).

## Working with this repository
This repository employs several tools to ensure a constant and good code quality.

### Black
[Black](https://black.readthedocs.io/en/stable/index.html) is a code formatter that we use to assure consistent code style across our projects.
Use it in-between, or after your code changes, via `poetry run black .` in the root directory of this repository.

### MyPy
[Mypy](https://mypy.readthedocs.io/en/stable/) is a static type checker for Python.
Mypy can be run with `poetry run mypy .` in the root directory of this repository.

### Ruff
[Ruff](https://docs.astral.sh/ruff/) is a Python linter and code formatter. 
It can be run with `poetry run ruff .` in the root directory of this repository. 


## Things left to be implemented

Not implemented because they aren't needed yet.

* Section `7.10.2 Semantic segmentation: image`
* Section `7.10.4 Mesh`
* Section `7.10.5 Mat and binary`
* Section `7.10.6 Point2d and Point3d`

Please choose a test-driven-development: Find an example JSON in the OpenLABEL spec and create a de- & re-serialization
test for it. Then implement the features required to pass the test.


## Debugging apischema

Debugging problems in (de)serialization with apischema is tricky because apischema is in a compiled state when
installing it from PyPI.
To have a better debugging experience, it is advisable to clone the [apischema repository](https://github.com/wyfo/apischema)
locally alongside this repository.
Then, set the apischema dependency as `apischema = { path="../apischema", develop=true }` in `pyproject.toml`.
Follow up with `poetry lock; poetry install --sync`.
Now you can more easily get the keys and values where apischema is throwing exceptions. 


## MyPy specialties in this library

### Mapping instead of dict

Throughout this repository, you'll find the usage of `Mapping` type decorators instead of `dict`. 
The type `Mapping` is _covariant_, while `dict` is _invariant_ 
(read about it [here](https://mypy.readthedocs.io/en/stable/generics.html#variance-of-generic-types)).  
This is important if you want to extend the base OpenLABEL spec with a customer-specific spec that overrides fields 
and narrows down the type, like such:   

```python
from dataclasses import dataclass, field
from typing import Mapping


class LowerCaseStr(str):
    def __init__(self, val: str):
        if not val.islower():
            raise ValueError(f"{val} isn't lower-case")


@dataclass
class Action:
    name: str = field()


@dataclass
class CustomAction(Action):
    name: LowerCaseStr = field()


@dataclass
class OpenLabel:
    # Setting the type to dict will cause a MyPy error
    actions: Mapping[str, Action] = field()


@dataclass
class CustomOpenLabel(OpenLabel):
    actions: dict[str, CustomAction] = field()
```

### Why all these `_no_default` default values? 

When creating dataclasses that inherit from each other, an issue that can occur is that a subclass has a field without 
a default, while the parent class contains fields with defaults. 
When this occurs, you'll see `TypeErrors` when trying to execute it, and PyCharm will complain too. 

To fix this, there are several possibilities, the best of them are discussed [here](https://stackoverflow.com/a/53085935/5568461). 
Other possibilities involve using metaclass magic and a deep forest of complicated code that would make the code harder to 
understand. 

The cleanest solution that a) doesn't double the class count, b) is understood by PyCharm, and c) sticks with plain dataclasses, 
is the following: 
On fields that may not be left empty according to the official OpenLABEL spec, we set a `default_factory` that raises an exception.

In order for apischema to work, we have to add the `apischema.metadata.required` in the field's metadata, 
otherwise apischema will call the default factory before checking if there even is a value to be deserialized. 
