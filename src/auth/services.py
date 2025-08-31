from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import CreateUser
from .models import User
from sqlmodel import select
from .utils import generate_password_hash

class AuthService:
    async def get_user(self, user: CreateUser, session:AsyncSession):
        statement = select(User).where(User.email == user.email)

        result = await session.exec(statement)

        return result.first()

    async def signup(self, user: CreateUser, session: AsyncSession):
        password_hash = generate_password_hash(user.password)

        new_user = User(
        email=user.email,
        password_hash=password_hash
    )
        session.add(new_user)
    

        await session.commit()

        await session.refresh(new_user)
        return new_user
