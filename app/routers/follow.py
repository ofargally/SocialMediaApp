from fastapi import APIRouter, status, HTTPException, Depends, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/follow",
    tags=["Follow"]
)
# Get current user if from whatever user is currently logged in, so what needs to be sent is


@router.post("/{id}", status_code=status.HTTP_201_CREATED)
def create_follow(id: int, db: Session = Depends(database.get_db), current_user: any = Depends(oauth2.get_current_user)):
    # User can not follow themselves
    if id == current_user.id:
        raise (HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
               detail=f"User can not follow themselves"))
    # check if id exists within database
    user_exists = db.query(models.User).filter(models.User.id == id).first()
    if not user_exists:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"User with id {id} was not found"))
    # if the current user is already following user with id, then unfollow
    check_follow_query = db.query(models.Follow).filter(
        models.Follow.follower_id == current_user.id, models.Follow.followed_id == id)
    print(check_follow_query)
    if check_follow_query.first():
        print(check_follow_query.first())
        check_follow_query.delete(synchronize_session=False)
        db.commit()
        return JSONResponse(content={"detail": f"User with id {id} has been unfollowed"})
    new_follow = models.Follow(follower_id=current_user.id, followed_id=id)
    db.add(new_follow)
    db.commit()
    db.refresh(new_follow)
    return JSONResponse(content={"detail": f"User with id {id} has been followed", "CREATED_AT": new_follow.created_at.isoformat()})


# @router.delete("/{id}", status_code=status.HTTP_200_OK)
