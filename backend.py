import csv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import FileResponse
import os

app = FastAPI()
csv_file = "users.csv"  # File to store user data

# Define User model
class User(BaseModel):
    name: str
    age: int

# Function to load users from CSV
def load_users():
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.DictReader(file)
            return [User(name=row["name"], age=int(row["age"])) for row in reader]
    except FileNotFoundError:
        return []

# Function to save users to CSV
def save_users(users):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        for user in users:
            writer.writerow(user.dict())

# Load existing users on startup
users = load_users()

# API to add a user
@app.post("/add_user/")
async def add_user(user: User):
    users.append(user)
    save_users(users)  # Save to CSV
    return {"message": "User added successfully"}

# API to get all users
@app.get("/")
def read_root():
    return FileResponse("index.html")  # Serve the HTML page
