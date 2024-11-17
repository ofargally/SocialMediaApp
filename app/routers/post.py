from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, oauth2
from ..schemas import PostResponse, CreatePost, UpdatePost, Post
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

# -- POST STUFF --

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# ,, response_model=List[PostResponse]
@router.get("/", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, searchTerm: Optional[str] = ""):
    # 2 This will allow us to retrieve the posts for the user logged in only. Not our specific use case right now
    # posts = db.query(models.Post).filter(
    #    models.Post.owner_id == current_user.id).all()
    # posts = db.query(models.Post).all()
    # By default this is a left inner join
    results_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(searchTerm)).limit(limit).offset(skip)
    results = results_query.all()
    print(results)
    print("OKAY\n")

    for i in range(len(results)):
        elementList = results[i]
        print("ELEMENT LIST", elementList)
        results[i] = {
            "post": elementList[0],
            "votes": elementList[1]
        }
    return results


@router.get("/{id}", response_model=PostResponse)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #    """SELECT * FROM posts WHERE id = %s""", (id,))
    # postRetrieved = cursor.fetchone()
    # print(postRetrieved)
    # filter does what WHERE does
    # .all() is like a loop of everything - we should do first() since we know there is gonna be just one instance

    post_query = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"post with id {id} was not found"))

    # Pre-process to fit our standards - for some reason we get our results in a tuple format,
    # which our JSON serializer is not able to deal with for some reason
    post = {
        "post": post[0],
        "votes": post[1]
    }
    # 2 This will allow us to retrieve the posts for the user logged in only. Not our specific use case right now
    # if post.owner_id != current_user.id:
    #    raise (HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"NOT AUTHORIZED"))
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_posts(post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # can not use f"" -> makes vulnerable for SQL injection - user can insert SQL stuff!
    # SQL library can sanitize the input for us this way!
    # Staged changes
    # cursor.execute(
    #    """INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING *""",
    #    (post.title, post.content, post.published))
    # createdPost = cursor.fetchone()
    # TO SAVE THE DATA (BECAUSE UNTIL THIS POINT THE POST IS CREATED BY NOT COMMITTTED TO DB)
    # WE HAVE TO COMM IT IT USING ONE FINAL STEP
    # conn.commit()
    print(current_user)
    new_post = models.Post(**post.model_dump(), owner_id=int(current_user.id))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
    # postDeleted = cursor.fetchall()
    # print(postDeleted)
    # conn.commit()
    # No need for a return statement in FastAPI in this case since we should handle it via HTTP_204_NO_CONTENT
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    # if the query returns back anything
    if not post:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'Could not find post with id {id}'))
    else:
        if post.owner_id == current_user.id:
            post_query.delete(synchronize_session=False)
            db.commit()
        else:
            raise (HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail=f'NOT AUTHORIZED'))


@router.put("/{id}", response_model=PostResponse)
# Make sure post comes in with the right schema
def update_post(id: int, post: UpdatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    postUpdated = post_query.first()
    if not postUpdated:
        raise (HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f'post with id {id} does not exist!'))
    else:
        if postUpdated.owner_id == current_user.id:
            post_query.update(post.model_dump(),
                              synchronize_session=False)
            db.commit()
            return post_query.first()
        else:
            raise (HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail=f'NOT AUTHORIZED'))
