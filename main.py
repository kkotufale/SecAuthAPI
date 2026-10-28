from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes.users import router

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home(): 
    return {"message":"Secure Auth System API is running!"}