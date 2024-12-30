from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    message: str

class Login(BaseModel):
    username: str
    password: str



@app.get("/")
def read_root():
    return {"Good morning d eruma..."}

@app.post("/items/")
async def create_item(item: Item):
    if item.name == "sridhar":
        return {"name" : item.name}
    else: 
        return "sridhar"

@app.post('/login')
def create_item(login: Login):
    if login.password == "123":
        return "login sucess" 
    else: 
        return "login Failed"
    

