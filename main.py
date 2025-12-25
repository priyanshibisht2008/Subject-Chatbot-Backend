from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins =[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running"}

@app.get("/api/hello")
def say_hello():
    return {"message": "Hello from FastAPI backend"}

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/api/users")
def create_user(user: User):
    return {
        "status": "success",
        "name": user.name,
        "email": user.email
    }