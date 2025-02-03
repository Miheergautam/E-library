from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import certifi

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "elibrary"

# Secure SSL connection
client = AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where())
db = client[DATABASE_NAME]
books_collection = db["books"]