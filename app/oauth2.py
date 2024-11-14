# import jwt
from jose import jwt
from datetime import datetime, timedelta

# USE OPENSSL Library to generate this: TERMINAL: openssl rand -hex 32
SECRET_KEY = "83d0c17445b0ca43e29139ad3d41065521ceb40a95d23eb35c85f6ac4c0dd211"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_code(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token
