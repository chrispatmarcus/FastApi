from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    tags=['blogs']
)

@router.get('/blog', response_model=List[schemas.ShowBlog] )
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog= models.Blog(title=request.title, body=request.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response:Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Blog with the id {id} is not available"}
    return blog

@router.delete('/blog.{id}', status_code=204)
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)

    db.commit()
    return 'blog deleted completely'

@router.put('/blog/{id}', status_code=202)
def update(id, request:schemas.Blog, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update(request)
    db.commit()
    return 'updated'
