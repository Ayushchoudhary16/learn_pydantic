from pydantic import BaseModel,Field
from typing import Annotated


class User(BaseModel):
    name:Annotated[str,Field(...,min_length=8)]
    age:Annotated[int,Field(...,ge=18)]

user=User(name="Ayush Choudhary",age=19)
print(user)




