from fastapi import FastAPI,Body,status,HTTPException
from typing import Optional
from models import Student
from fastapi.encoders import jsonable_encoder
from database import add_student,retrieve_students,retrieve_student,delete_student
from database import school_collection


app = FastAPI(title="School Mangement System")


@app.post("/Student", tags=["Students"],status_code=201)
async def add_student_data(student_data: dict,student: Student = Body(...)) -> dict:
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return (new_student, "A new student has been added in the system")



@app.get("/Students",tags=["Students"])
async def get_students():
    students = await retrieve_students()
    if students:
        return (students, "Students details retrieved successfully")
    return (students, "There are no students registred yet")

@app.get("/{id}",tags=["Students"])
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return (student, "Student details retrieved successfully")
    return HTTPException (status_code=404,detail='student id not found')

@app.delete("/{id}",tags=["Students"])
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return (
           "Student deleted successfully"
        )
    return (
         HTTPException (status_code=404,detail='student id not found')

    )
    #624c90b77969c684b23e980d
    #624c9394f2a487d01364c6ec