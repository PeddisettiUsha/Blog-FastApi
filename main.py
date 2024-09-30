# from typing import List
from fastapi import FastAPI   #Depends,status,Response,HTTPException
import models  #schemas
from database import engine   # get_db # SessionLocal
# from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from hashing import Hash
from routers import blog, user,authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

