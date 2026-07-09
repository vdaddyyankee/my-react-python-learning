from fastapi import FastAPI
from app.api.employee import router as employee_router

app = FastAPI(title="Employee Management System", version="1.0.0")
app.include_router(employee_router)

@app.get("/")
def home() -> dict:
    return {
        "message": "Welcome Vijay"
    }