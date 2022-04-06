import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.students


school_collection = db.get_collection("school_collection")



