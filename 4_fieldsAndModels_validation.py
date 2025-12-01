# 4_fieldsAndModels_validation.py

from pydantic import BaseModel,Field,field_validator,model_validator


class Signup(BaseModel):
    username:str=Field(
        ...,
        min_length=8
    )
    password:str
    repassword:str
    mobile:int

    @field_validator("mobile")
    def validatae_mobile(cls,value):
        if len(str(value))!=10:
            raise ValueError('mobile number is 10 digits')
               
        if str(value)[0] not in ["9","8","7"]:
            raise ValueError("Incorrect mobile Number")
    
        return value
    
    @model_validator(mode="after")
    def pass_validation(self):
        if self.password!=self.repassword:
            raise ValueError("password is not match")
        
        if len(self.password)<8:
            raise ValueError("password min lunght is 8")

        return self


userSignup=Signup(username="AyushCHoudhary",password="12345678",repassword="12345678",mobile=8244434123)
print(userSignup)
























