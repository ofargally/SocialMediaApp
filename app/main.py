from fastapi import FastAPI
# Related to SQL Alchemy
from . import models
from .database import engine
from .routers import post, user, auth, vote
# This line create all the models - not needed with Alembic as we can use
# Autogenerate to create models
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return "Hello Message"
