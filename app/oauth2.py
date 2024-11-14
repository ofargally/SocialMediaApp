# import jwt
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import schemas
load_dotenv()

# TokenURL is the endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# USE OPENSSL Library to generate this: TERMINAL: openssl rand -hex 32

SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_code(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token


def verify_access_token(token: str, credentials_exception):
    # anytime we are working with code that can result in an error,
    # we should do try except
    try:
        # decode JWT token sent from user
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        print("payload", payload)
        print("type", type(payload))
        # Extract ID
        id: str = payload.get("user_id")
        # if No ID send in 404
        if not id:
            raise (credentials_exception)
        # verify that the data in the token matches the pydantic schema we have
        token_data = schemas.TokenData(user_id=id)
        print("TOKEN_DATA:", token_data)
    except JWTError:
        raise credentials_exception
    return token_data

# pass as a dependency to our API endpoints
# Take token from request automatically
# Exract id, verify token, fetch the user from db and
# add as a parameter


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Need to check the header protocols
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="INVALID CREDENTIALS", headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token, credentials_exception)


# Explanation: Anytime we have a protected endpoint (requires user authentication),
# We can add in an extra dependency into said endpoint that verifies the user token
