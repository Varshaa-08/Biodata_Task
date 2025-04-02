import csv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
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

f# Default route to check if FastAPI is running
@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is Running!"}

# API to add a user
@app.post("/add_user/")
async def add_user(user: User):
    users.append(user)
    save_users(users)  # Save to CSV
    return {"message": "User added successfully"}

# API to get all users as an HTML table
@app.get("/get_users/", response_class=HTMLResponse)
async def get_users():
    if not users:
        return "<h2>No users found</h2>"

    # Generate an HTML table
    table_html = "<table border='1' style='border-collapse: collapse; width: 50%; text-align: left;'>"
    table_html += "<tr><th>Name</th><th>Age</th></tr>"
    
    for user in users:
        table_html += f"<tr><td>{user.name}</td><td>{user.age}</td></tr>"
    
    table_html += "</table>"
    
    return table_html  # Returns an HTML table

