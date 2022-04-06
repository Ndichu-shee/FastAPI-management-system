from pydantic import BaseModel, Field,EmailStr
from typing import Optional


class Student(BaseModel):
    first_name:str = Field(...)
    last_name:str = Field(...)
    age:int = Field(...)
    nationality:str = Field(...)
    class_name:str = Field(...)
    nationality_id:str = Field(...)
    email:EmailStr = Field(...)
    room:str = Field(...)

    class config:
        schema_extra = {
            "example": {
                "first_name":"Joyce",
                "last_name":"Ndichu",
                "age":23,
                "nationality":"Kenyan",
                "class_name":"LisaLab",
                "nationality_id":"23763722",
                "email":"ndichujoyce@gmail.com",
                "room":"Tanga",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}