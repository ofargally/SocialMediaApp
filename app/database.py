# Set up SQLALCHEMY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

user_name = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host_name = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    f"postgresql+psycopg://{user_name}:{password}@{host_name}/{db_name}")

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
