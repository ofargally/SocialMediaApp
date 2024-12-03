from typing import List
from .. import utils, models, oauth2
from ..schemas import UserCreate, UserResponse
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


# ------ USER STUFF -------

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("user created")
    # Check if user has already been created
    check_user_query = db.query(models.User).filter(
        models.User.email == user.username)
    if check_user_query.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this email already exists")
    # Hash password and apply
    user.password = utils.hash(user.password)
    new_user = models.User(email=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
               detail=f"USER WITH ID: {id} does not exist"))
    return user


@router.get("/{id}/followers", response_model=List[UserResponse])
def get_followers_list(id: int, limit: int = 10, current_user: any = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    # check if id exists:
    check_id = db.query(models.User).filter(models.User.id == id).first()
    if not check_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} was not found")
    followers = db.query(models.User).join(models.Follow, models.User.id == models.Follow.follower_id).filter(
        models.Follow.followed_id == id).limit(limit).all()
    return followers


@router.get("/{id}/followees", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def get_followed_list(id: int, limit: int = 10, current_user: any = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    # check if id exists:
    check_id = db.query(models.User).filter(models.User.id == id).first()
    if not check_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} was not found")
    followees = db.query(models.User).join(models.Follow, models.User.id == models.Follow.followed_id).filter(
        models.Follow.follower_id == id).limit(limit).all()
    return followees
