from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()

class Usuario(SQLModel):
    username = str
    password = str

usuario_db = Usuario(username = "diegosantillan625@gmail.com", password = "123456789")

class Credenciales(SQLModel):
    username = str
    password =str

@app.post("/login")
def login(data: Credenciales):
    for user in usuario_db:
        if user.username == data.username and user.password == data.password:
            return {"mensaje": "Login succesful, bienvenido diego"}
    else: return {"mensaje": "wrong password or username"}
