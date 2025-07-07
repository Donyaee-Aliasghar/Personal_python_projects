from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..auth import hash_password, verify_password, create_access_token
from ..schemas import auth as auth_schemas
from ..schemas.user import UserCreate, UserOut
from ..dependencies import get_db
from ..crud.user import create_user, get_user_by_username

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hash_password(user.password)
    user_data = UserCreate(username=user.username, email=user.email, password=hashed_password)
    created_user = create_user(db, user_data)
    return created_user


@router.post("/login", response_model=auth_schemas.Token)
def login(form_data: auth_schemas.UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username) 
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
