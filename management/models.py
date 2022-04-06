from pydantic import BaseModel
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
from check import PyObjectId




# CREATE MODEL
class Student(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name:str = Field(...)
    last_name:str = Field(...)
    age:int = Field(...)
    nationality:str = Field(...)
    class_name:str = Field(...)
    nationality_id:str = Field(...)
    email:EmailStr = Field(...)
    room:str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
                "example": {
                "first_name":"Jane",
                "last_name":"Kattie",
                "age":21,
                "nationality":"Kenyan",
                "class_name":"LisaLab",
                "nationality_id":"23763722",
                "email":"jane@gmail.com",
                "room":"Tanga",
                }

        }
