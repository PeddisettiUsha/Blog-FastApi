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


# def get_db():     # paste it in the database
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close


# @app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['blogs'])  #store blog to DB
# # def create(title,body): # we don't get this thing directly so that created pydantic
# #     return {'title':title, 'body':body}
# def create(request: schemas.BlogSchema,db : Session = Depends(get_db)):
#     new_blog = models. Blog(title=request.title, body=request.body,user_id= 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])   #Delete a blog
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#
#     if not blog.first():
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             details=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])  # upate a blog
# def update(id:int, request: schemas.BlogSchema, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.update(request.dict())
#     db.commit()
#     return 'updated'

# # @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs']) #Response Model
# # def all(db: Session = Depends(get_db)):
# #     blogs = db.query(models.Blog).all()
# #     return blogs

# @app.get('/blog/{id}', status_code=200,response_model=schemas.ShowBlog, tags=['blogs'])   #get blog from the DB  # Response model
# def show(id, response: Response, db:Session = Depends(get_db),status_code=200):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()

#     if not blog:  #Exceptions and status code

#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{'details': f'Blog with the id {id} is not available'} instead of this two lines we can use raise HTTP Exception
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Blog with the id {id} is not available')
#     return blog


# pwd_cxt =CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/user', response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED, tags=['users']) #create User
# def create_user(request: schemas.User,db: Session = Depends(get_db)):
#     # hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser, tags=['users']) # creating another router
# def get_user(id:int,db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             details=f"user with the {id} is not available")
#     return user