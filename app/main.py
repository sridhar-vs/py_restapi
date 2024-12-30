from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_api():
    return {"message": "Hello from main.py"}

@app.get("/")
def read_root():
    return {"message": "Hello from the root of main.py"}
