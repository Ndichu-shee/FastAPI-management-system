from pydantic import BaseModel, Field,EmailStr
from typing import Optional

class Student(BaseModel):
    first_name:str = Field(...)
    last_name:str = Field(...)
    age:int = Field(...)
    nationality:str = Field(...)
    date_of_birth:str = Field(...)
    class_name:str = Field(...)
    nationality_id:str = Field(...)
    email:EmailStr = Field(...)
    admission_date:str = Field(...)
    academic_year:int = Field(...)
    room:str = Field(...)

    class config:
        schema_extra = {
            "example": {
                "first_name":"Joyce",
                "last_name":"Ndichu",
                "age":23,
                "nationality":"Kenyan",
                "date_of_birth":28,
                "class_name":"LisaLab",
                "nationality_id":"23763722",
                "email":"ndichujoyce@gmail.com",
                "admission_date":"1-2-2021",
                "academic_year":"2021",
                "room":"Tanga",
            }
        }