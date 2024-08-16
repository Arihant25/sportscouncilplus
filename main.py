from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from bson.json_util import dumps

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["iiith_sports_council"]
members_collection = db["members"]
# Debug time
print(members_collection["members"], "GAY")
# Get members
print(list(members_collection.find()))


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
    print(members_collection)
    members = list(members_collection.find())
    print(members)
    return members


# Run the FastAPI app
# Use the command below to run the server:
# uvicorn main:app --reload
