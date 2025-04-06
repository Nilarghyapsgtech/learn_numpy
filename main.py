from fastapi import FastAPI,Depends
from typing import Annotated
from sqlalchemy.orm import Session
import models
from database import *
from models import *

app=FastAPI()
models.



# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency=Annotated[Session,Depends(get_db)]

# @app.get("/")
# async def db_details(db:db_dependency):
#     return db.query(Todos).all()

user1=User(name='Nilarghya')