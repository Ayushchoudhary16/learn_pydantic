from pydantic import BaseModel,Field


class Student(BaseModel):
    name:str=Field(
        ...,                #... describe the require field
        min_length=6,
        max_length=20,
        description="name of the student."
    )
    fees:int=Field(
        ...,
        ge=25000,
        le=50000
    )
    email:str=Field(
        default=""
    )


student1=Student(name="Ayush Choudhary",fees=35000)
print(student1)












