from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Related to SQL Alchemy
from . import models
from .database import engine
from .routers import post, user, auth, vote
# This line create all the models - not needed with Alembic as we can use
# Autogenerate to create models
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# domains that should be able to connect to our API, should be configured to allow our webapp only
# unless the API is being developed for specific purposes
origins = ["https://www.google.com"]

# Middleware is a function that runs before each request

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def root():
    return "Hello Message"
