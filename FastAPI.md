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
Pydantic fields allow to define default values (or lack of thereof), as well as more complex validations:
```python
from uuid import uuid4
from datetime import datetime

class UserModelFields(BaseModel):
    id: int = Field(strict=True)
    username: str = Field(aloas="name")
	email: EmailStr = Field()

	model_config = ConfigDict(extra="forbid", populate_by_name=True)

class ChessTournament(BaseModel):
	id: int = Field(strict=True)
	dt: datetime = Field(default_factory=datetime.now)
	name: str = Field(min_length=10, max_length=30)
	num_players: int = Field(ge=4, le=16, multiple_of=2)
	code: str = Field(default_factory=uuid4)
```
To use `EmailStr` one has to add the package `email_validation`.
`model_cofig` is a special field for configurations.

Field serializers:
```python
class Account(BaseModel):
	balance: float
	updated: datetime

	@field_serializer("balance", when_used="always")
	def serialize_balance(self, value: float) -> float:
		return round(value, 2)
	
	@field_serializer("updated", when_used="json")
	def serialize_updated(self, value: datetime) -> str:
		return value.isoformat()
```

Custom field validators:
```python

class Article(BaseModel):
	id: int
	title: str
	content: str
	published: bool

	@field_validator("title")
	@classmethod
	def check_title(cls, v: str) -> str:
		if "FARM stack" not in v:
		raise ValueError('Title must contain "FARM stack"')
		return v.title()
```

Model validators, add to the model class:
```python
@model_validator(mode='after')
def check_passwords_match(self) -> Self:
	pw1 = self.password1
	pw2 = self.password2
	if pw1 is not None and pw2 is not None and pw1 != pw2:
		raise ValueError('passwords do not match')
	return self

@model_validator(mode='before')
@classmethod
def check_private_data(cls, data: Any) -> Any:
	if isinstance(data, dict):
		assert (
			'private_data' not in data
		), 'Private data should not be included'
	return data
```

#### Pydantic settings
Package:
```shell
pip install pydantic-settings
```
Usage:
```python
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
	api_url: str = Field(default="")
	secret_key: str = Field(default="")

	class Config:
		env_file = ".env"

print(Settings().model_dump())
```

## FastAPI basics
Creating an app:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello FastAPI"}

#path parameters:
@app.get("/car/{id}")
async def root(id: int):
	return {"car_id": id}

```
If the file is named `main.py`, then the app is started with
```bash
uvicorn main:app --reload
```

Constraining path parameters:
```python
class AccountType(str, Enum):
	FREE = "free"
	PRO = "pro"

@app.get("/account/{acc_type}/{months}")
async def account(acc_type: AccountType, months: int = Path(..., ge=3, le=12)):
	return {"message": "Account created", "account_type": acc_type, "months": months}
```

Query parameters:
```python
@app.get("/cars/price")
async def cars_by_price(min_price: int = 0, max_price: int = 100000):
	return {"Message": f"Listing cars with prices between {min_price} and {max_price}"}
```

Request body:
```python
@app.post("/cars")
async def new_car(data: Dict = Body(...)):
	return {"message": data}
```
or with a validated model:
```python
class InsertCar(BaseModel):
	brand: str
	model: str
	year: int
	
app = FastAPI()

@app.post("/cars")
async def new_car(data: InsertCar):
	return {"message": data}
```

Headers:
```python
@app.get("/headers")
async def read_headers(user_agent: Annotated[str | None, Header()] = None):
	return {"User-Agent": user_agent}
```

Request object:
```python
@app.get("/cars")
async def raw_request(request: Request):
	return {"message": request.base_url, "all": dir(request)}
```

Forms and files (one has to install `python-multipart`):
```python
import shutil

@app.post("/upload")
async def upload(file: UploadFile = File(...), brand: str = Form(...), model: str = Form(...)):
	with open("saved_file.png", "wb") as buffer:
		shutil.copyfileobj(picture.file, buffer)
	return {"brand": brand, "model": model, "file_name": file.filename}
```

Setting response status:
```python
@app.get("/", status_code=status.HTTP_208_ALREADY_REPORTED)
async def raw_fa_response():
	return {"message": "fastapi response"}
```

HTTP errors:
```python
if car.year > 2022:
	raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail="The car doesn't existyet!")
```