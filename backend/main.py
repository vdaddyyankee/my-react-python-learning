from fastapi import FastAPI
from app.database.connection import engine
from app.database.models import Base
from app.api.employee import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")
app.include_router(employee_router)

@app.get("/")
def home():
    return {
        "message": "FastAPI + MySQL Connected"
    }