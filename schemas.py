from typing import List,Optional
from pydantic import BaseModel # we created schemas file to store the data in the database


class BlogSchema(BaseModel): # creating pydantic model to get title and body,schema for the blog
    title: str
    body: str
    # user_id: int
    class Config():
        orm_mode = True

class Blog(BlogSchema):
    class Config():
        orm_mode =True   



class User(BaseModel):
    name: str
    email: str
    password: str

class UpdateUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogSchema]=[]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    # creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None