from fastapi import APIRouter, status, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserLogin
from .. import models, utils
router = APIRouter(
    tags=[
        'Authentication'
    ])


@router.post('/login')
def login(user_credentials: UserLogin, db: Session = Depends(get_db())):
    user = db.query(models.User).filter(
        models.User.email == user_credentials.email).first()
    if not user:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
               detail=f"INVALID CREDENTIALS"))
    match = utils.verify(user_credentials.password, user.password)
    if not match:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
               detail="INVALID CREDENTIALS"))
