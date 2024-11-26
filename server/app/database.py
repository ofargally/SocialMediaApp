# Set up SQLALCHEMY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from . import config

DB_USERNAME = config.settings.DB_USERNAME
DB_PASSWORD = config.settings.DB_PASSWORD
DB_HOST = config.settings.DB_HOST
DB_NAME = config.settings.DB_NAME
DB_PORT = config.settings.DB_PORT

engine = create_engine(
    f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# The session object is what is responsible for talking with the databases
# Everytime we get a request, we are gonna get the session and through it send SQL to db
# and after request is done, we should close the session out
# So we call this function everytime we get a request (any requests) from our API end points


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
