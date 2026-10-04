from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    salary: int
    year_joined: int

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    salary: Optional[int] = None
    year_joined: Optional[int] = None

employees = {}

@app.post("/create-employee")
def create_employee(employee_id: int, employee: Employee):
    if employee_id in employees:
        raise HTTPException(status_code= 400, detail="Employee Exists")
    employees[employee_id] = employee
    return employees[employee_id]

@app.get("/get-employee")
def get_employee(employee_id: Optional[int] = None, name: Optional[str] = None):
    if employee_id in employees:
        return employees[employee_id]
    if(name):
        for i in employees:
            if employees[i].name == name:
                return employees[i]
    raise HTTPException(status_code= 404, detail="Not found")

@app.put("/update-employee")
def update_employee(employee_id: int, employee: UpdateEmployee):
    if employee_id not in employees:
        raise HTTPException(
            status_code= 400, 
            detail="Employee does not exist"
            )
    #Store a copy of employee to retain unchanged information
    existing_employee = employees[employee_id]
    
    #model_dump(exclude_unset = True) fliters out unchanged info
    update_info = employee.model_dump(exclude_unset = True)

    updated_employee = existing_employee.model_copy(update = update_info)

    employees[employee_id] = updated_employee
    return employees[employee_id]

