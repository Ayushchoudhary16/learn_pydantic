from pydantic import BaseModel

class User(BaseModel):
    user_id:int
    name:str
    age:int
    isactive:bool

user=User(user_id=1,name="Ayush",age=21,isactive=True)
print(user)



from pydantic import BaseModel,PositiveInt
from typing import Literal,List,Optional

class Orders(BaseModel):
    user_id:PositiveInt
    product_ids:List[int]
    payment_mode:Literal["online","cash"]
    delivery_note:Optional[str]=None

order=Orders(user_id=1,product_ids=[4,4],payment_mode="online",delivery_note="itarsi")
print(order)

















