from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection using your connection string
client = MongoClient(os.getenv('MONGO_URI'))
db = client["iiith_sports_council"]
members_collection = db["members"]


# Helper function to convert MongoDB documents to a serializable format
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc


# Pydantic model
class Member(BaseModel):
    name: str
    position: str
    email: str

    class Config:
        # To allow parsing of data containing ObjectId
        orm_mode = True


# API to get council info
@app.get("/council_info")
def get_council_info():
    return {
        "council_name": "Sports Council IIIT Hyderabad",
        "description": "Managing sports activities and events at IIIT-H.",
    }


# API to get members list
@app.get("/members")
def get_members():
    members = list(members_collection.find())
    serialized_members = [serialize_doc(member) for member in members]
    return serialized_members


# Run the FastAPI app
# Use the command below to run the server:
# uvicorn main:app --reload
