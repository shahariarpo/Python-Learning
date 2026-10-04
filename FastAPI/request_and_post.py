from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

employees = {
    1: {
        "name": "John Smith",
        "Id": 122,
        "Salary": 50000
    },
    2: {
        "name": "Jane Doe",
        "Id": 123,
        "Salary": 45000
    }
}

class Employee(BaseModel):
    name: str
    eId: int
    salary: int

@app.post("/create-employee/{employee_id}")
def create(employee_id: int, employee: Employee):
    if employee_id in employees:
        return {"Error": "Employee Exists"}
    employees[employee_id] = employee
    return employees[employee_id]