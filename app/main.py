from fastapi import FastAPI
from typing import List
# Related to SQL Alchemy
from . import models
from .database import engine
from .routers import post, user, auth
# This line create all the models
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
def root():
    return "Hello Message"
