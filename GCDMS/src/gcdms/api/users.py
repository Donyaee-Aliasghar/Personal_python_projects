from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserOut
from ..crud.user import create_user, get_user, get_users
from ..dependencies import get_db
from typing import List


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)
