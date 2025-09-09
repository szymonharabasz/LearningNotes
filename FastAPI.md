## Type hints and Pydantic
Type union:
```python
from typing import Union
x: Union(str, int)
# or newer
x: str | int
```
Other *generics* in `typing:` `List`, `Dict`, `Sequence`, `Callable`, `Iterator`.

Literal types:
```python
from typing import Literal
account_type: Literal("personal", "business")
```

Advanced annotations are also `Optional`, `Union`. `self`, `New`
#### Using Pydantic:
```python
from pydantic import BaseModel, ValidationError
try:
    u = User(
        id="one",
        username="freethrow",
        email="email@gmail.com",
        dob=datetime(1975, 5, 13),
    )
    print(u)
except ValidationError as e:
    print(e)
```