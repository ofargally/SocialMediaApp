from fastapi import APIRouter, status, HTTPException, Depends, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
# the user retrived is not an int, but for some reason the type validation here does not work.
def vote(userVote: schemas.Vote, db: Session = Depends(database.get_db), current_user: any = Depends(oauth2.get_current_user)):
    # Check if post exists at all
    post = db.query(models.Post).filter(
        models.Post.id == userVote.post_id).first()
    if not post:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
               detail="Post was not found"))
    # Continue with other logic:
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == userVote.post_id, models.Vote.user_id == current_user.id)
    vote = vote_query.first()
    if userVote.dir == 1:  # means post should be upvoted
        if vote:  # already existed means we can not upvote it anymore:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Current User {current_user.id} has already upvoted post {vote.post_id}")
        # Otherwise create the new entry row
        new_vote = models.Vote(post_id=userVote.post_id,
                               user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message": "Upvoted Post Successfully"}
    else:  # Not upvoted
        if not vote:
            raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                   detail=f"post {userVote.post_id} has not been voted"))
        # wrong
        # db.delete(vote)
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message": "Removed Upvote!"}
