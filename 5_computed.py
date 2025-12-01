# 5_computed.py

from pydantic import BaseModel,computed_field

class CartItems(BaseModel):
    user_id:int
    product_id:int
    price:int
    quantity:int

    @computed_field()
    @property
    def total_price(self)->int:
        return self.price*self.quantity



cart=CartItems(user_id=1,product_id=2,price=1000,quantity=5)
print(cart)


