from sqlalchemy.orm import Session

from app.database.models import Employee
from app.schemas.employee import EmployeeCreate


def create_employee(db: Session, employee: EmployeeCreate):
    new_employee = Employee(
        name=employee.name,
        email=employee.email
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employees(db: Session):
    return db.query(Employee).all()
