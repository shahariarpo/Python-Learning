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


@app.get("/get-by-name")
def get_employee(name: str = None):                     #str = None makes it non-required
    for employee_id in employees:
        if employees[employee_id]["name"] == name:
            return employees[employee_id]
    return {"Data": "Not Found"}