from fastapi import FastAPI, Path

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

@app.get("/get-employee/{employee_id}")
def get_employee(employee_id: int = Path(description="The ID of the employee", gt=0, lt= 3)):
    return employees[employee_id]