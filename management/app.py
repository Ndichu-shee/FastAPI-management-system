from models import Student
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI,APIRouter, Body, status, HTTPException
from typing import Optional
from database import db


app = FastAPI(title="School Management System")

@app.get("/")
async def read_main():
    return {"msg": "School Management System"}

@app.post("/student", response_description = "Add a person to the database", response_model=Student,tags=["Students"])
async def add_student(student: Student = Body(...)):
    student = jsonable_encoder(student)
    students = await db["student"].insert_one(student)
    add_student = await db["student"].find_one({"_id":students.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=add_student)

@app.get("/students", response_description="All Registered", response_model=Student,tags=["Students"])
async def all_students():
    students = await db["students"].find().to_list(1000)
    return students


@app.get("/student/{id}", response_description="specific student details", response_model=Student,tags=["Students"])
async def get_student(id: str):
    if (student := await db["student"].find_one({"_id":id})) is not None:
        return student
    raise HTTPException(status_code=404, detail="Student id not found, try using another Id")

@app.delete("/student/{id}", response_description="Delete a student from the system", response_model=Student,tags=["Students"])
async def delete_student(id: str):
    delete_result = await db["student"].delete_one({"_id":id})

    if delete_result.deleted_count == 1:
        JSONResponse(status_code=404, detail="Student id not found, try using another Id")

    JSONResponse(status_code=200)
