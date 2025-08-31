from fastapi import APIRouter, Depends, HTTPException,status
from .services import AuthService
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .schemas import CreateUser


auth_router = APIRouter()
auth_service = AuthService()


@auth_router.post("/signup")
async def signup(user: CreateUser, session: AsyncSession = Depends(get_session)):
    verify_user = await auth_service.get_user(user, session)

    if not verify_user:
        new_user = await auth_service.signup(user, session)

        return new_user
    
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    

