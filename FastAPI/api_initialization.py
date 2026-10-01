from fastapi import FastAPI

app = FastAPI()

# initialize the API
@app.get("/")
def api_index():
    return {"name": "First Data",
            "id": 12}