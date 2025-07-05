from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from gcdms.schemas import User as sUser, UserCreate as sUserCreate
from gcdms.crud import get_user_by_username, create_user
from gcdms.dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=sUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: sUserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await create_user(db=db, user=user)
