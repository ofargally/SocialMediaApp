from fastapi import APIRouter, status, HTTPException, Depends, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/follow",
    tags=["Follow"]
)
