from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: int
    year_joined: int

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    salary: Optional[int] = None
    year_joined: Optional[int] = None

app = FastAPI()

employees = {}

@app.put("/update-employee/{employee_id}")
def update_employee(eId: int, employee: UpdateEmployee):
    if eId not in employees:
        raise HTTPException(status_code=400, detail="Not in the database")
    employees[eId] = employee
    return employee
