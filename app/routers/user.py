from .. import utils, models
from ..schemas import UserCreate, UserResponse
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter


# ------ USER STUFF -------

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print("user created")
    # Hash password and apply
    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    print("lllll")
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
               detail=f"USER WITH ID: {id} does not exist"))
    return user
