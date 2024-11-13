from passlib.context import CryptContext


# hashing passwords for security
# Define the hashing algorithm for passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)
