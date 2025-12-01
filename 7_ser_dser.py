# 7_ser_dser.py

# serialization and desearalization

from pydantic import BaseModel

class Student(BaseModel):
    name:str
    email:str
    age:int
    branch:str
    sem:int
    address:str

data = {
    "name":"Ayush",
    "email":"ayush@gmial.com",
    "age":20,
    "branch":"cse",
    "sem":7,
    "address":"itarsi,Bhopal"
}


# student=Student(**data)                #destructuring the data
student=Student.model_validate(data)     #desealization the data:means convert the data in dictornary to pydnatic class object
# print(student)

print(student.model_dump())             #serialization :convert the data in payntic class object to dictonary



