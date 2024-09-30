from sqlalchemy.orm import Session
from hashing import Hash
import models,schemas
from fastapi import HTTPException,status

def create(request: schemas.User,db:Session): # create a User(Signup)Route
    new_user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db:Session):
     user = db.query(models.User).filter(models.User.id == id).first()
     if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with the {id} is not available")
     return user

def destroy(id:int,db: Session):
     user = db.query(models.User).filter(models.User.id == id).first()

     if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
     
     db.delete(user)
     db.commit()
     return 'done'

def update(id: int, request, db: Session):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.update(request.dict())  # Ensure request is a Pydantic model with `dict()` method
    db.commit()
    return 'updated'
