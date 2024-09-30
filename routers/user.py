from fastapi import APIRouter
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException
from hashing import Hash
from repository import user

router = APIRouter(
    prefix= "/user",
    tags = ['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED) #create User
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    # hashedPassword = pwd_cxt.hash(request.password)
    # new_user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser) # creating another router
def get_user(id:int,db: Session = Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         details=f"user with the {id} is not available")
    # return user
    return user.show(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)   #Delete a user
def destroy(id:int, db: Session = Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id == id)

    # if not user.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"user with id {id} not found")
    # user.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return user.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, request: schemas.UpdateUser, db: Session = Depends(get_db)):
    return user.update(id, request, db)
