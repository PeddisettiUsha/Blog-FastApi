from fastapi import APIRouter,Depends, HTTPException,status
from fastapi. security import OAuth2PasswordRequestForm
from routers.token import create_access_token
import schemas,database,models,token
from hashing import Hash
from sqlalchemy.orm import Session


router = APIRouter(
    tags = ['Authentication']
)


@router.post('/login') # create login Route
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, # checking the user
                            detail=f"Invalid credentials")
    
    if not Hash.verify(user.password,request.password):   # checking the password
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect Password")
    
    #generate a JWT token and return

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}