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
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    dob: datetime
    # defaults and nullables:
    fav_colors: list[str] | None = ["red", "blue"]

try:
	# creating with constructor
    user1 = User(
        id="one",
        username="freethrow",
        email="email@gmail.com",
        dob=datetime(1975, 5, 13),
    )
    print(user1)
    
    # creating from dictionary
    user2 = User.model_validate(
    {
        "id": 1,
        "username": "freethrow",
        "email": "email@gmail.com",
        "password": "somesecret",
    }
)
    
except ValidationError as e:
    print(e)
```
Inspecting the fields of a model:
```python
print(UserModel.model_fields)
```
Specific Pydantic types:
```
StrictInt, StrictString, StrictBool
```
do not allow for type coercion. One can have, for example, a type `email` if one installs it:
```shell
pip install pydantic[email]
```
Pydantic fields allow to define default values (or lack of thereof):
```python
class UserModelFields(BaseModel):
    id: int = Field(…)
    username: str = Field(…)
```