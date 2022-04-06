import motor.motor_asyncio


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.managements


school_collection = database.get_collection("school_collection")


def student_helper(student) -> dict:
    return {
                "first_name": (student["first_name"]),
                "last_name": (student["last_name"]),
                "age":(student["age"]),
                "nationality":(student["nationality"]),
                "class_name":(student["class_name"]),
                "nationality_id":(student["nationality_id"]),
                "email":(student["email"]),
                "room":(student["room"]),
    }
    


async def add_student(student_data: dict) -> dict:
    student = await school_collection.insert_one(student_data)
    new_student = await school_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

async def retrieve_students():
    students = []
    async for student in school_collection.find():
        students.append(student_helper(student))
    return students
async def get_student_id(student_id):
    student = await school_collection.find_one({"student_id": tudent(student_id)})

    if student:
        return student_helper(student)


async def retrieve_student(id: str) -> dict:
    student = await school_collection.find_one({"_id": (id)})
    if student:
        return student_helper(student)

async def delete_student(id: str):
    student = await school_collection.find_one({"_id": (id)})
    if student:
        await school_collection.delete_one({"_id": (id)})
        return True