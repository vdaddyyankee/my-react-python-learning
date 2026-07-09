from fastapi import APIRouter

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/")
def get_employees():
    return {
        "status": "success",
        "status_code": 200,
        "message": "List of employees",
        "items": [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Jane Smith"},
        ],
    }
