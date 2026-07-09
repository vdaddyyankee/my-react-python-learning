from fastapi import APIRouter, Depends  # type: ignore[import]
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import create_employee, get_employees as list_employees

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeResponse)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = create_employee(db, employee)
    return new_employee


@router.get("/", response_model=list[EmployeeResponse])
def list_employee_routes(db: Session = Depends(get_db)):
    return list_employees(db)
