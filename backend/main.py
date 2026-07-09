from fastapi import FastAPI
from app.database.connection import engine

app = FastAPI(title="Employee Management API")

@app.get("/")
def home():
    return {
        "message": "FastAPI + MySQL Connected"
    }