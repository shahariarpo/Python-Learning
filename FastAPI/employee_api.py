from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    salary: int
    year_joined: int

employees = {}

@app.post("/create-employee")
def create_employee(employee_id: int, employee: Employee):
    if employee_id in employees:
        return{"Error": "Employee Exists"}
    employees[employee_id] = employee
    return employees[employee_id]

@app.get("/get-employee")
def get_employee(eId: Optional[int] = None, name: Optional[str] = None):
    if eId in employees:
        return employees[eId]
    if(name):
        for i in employees:
            if employees[i].name == name:
                return employees[i]
    raise HTTPException(status_code= 404, detail="Not found")