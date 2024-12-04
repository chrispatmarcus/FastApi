from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'heyyy'

@app.get('/about')
def about():
    return{'data':'about page'}

@app.get('/blog')
def index(limit=10, published:bool=True):
    if published:
        return{'data':f'{limit} published blogs from the db'}
    else:
        return{'data':f'{limit} blogs from the db'}


@app.get('/blog/{id}')
def show(id):
    return{'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return{'data':'comments'}

class Blog(BaseModel):
    title:str
    body:str
    


@app.post('/blog')
def create_blog(request:Blog):
    
    return{'data':f"blog is created with title as {request.title}"}


