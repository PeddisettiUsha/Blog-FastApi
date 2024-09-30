from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
import schemas,database, models
from . import oauth2  # Relative import from the same package
from sqlalchemy.orm import Session
from repository import blog


router = APIRouter(
    prefix="/blog", # to get path blog we are defined at here
    tags= ['Blogs']  #in swaggetui we get instead ofdefault we get blogs
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog]) #Response Model , to remove blog we are defined in router
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)  #store blog to DB
def create(request: schemas.BlogSchema,db : Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # new_blog = models. Blog(title=request.title, body=request.body,user_id= 1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)   #Delete a blog
def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)

    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with id {id} not found")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)  # upate a blog
def update(id:int, request: schemas.BlogSchema, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)

    # if not blog.first():
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with id {id} not found")

    # blog.update(request.dict())
    # db.commit()
    # return 'updated'
    return blog.update(id,request,db)

# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs']) #Response Model
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)   #get blog from the DB  # Response model
def show(id:int, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # if not blog:  #Exceptions and status code

    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return{'details': f'Blog with the id {id} is not available'} instead of this two lines we can use raise HTTP Exception
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'Blog with the id {id} is not available')
    # return blog
    return blog.show(id,db)
