from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
        url=Config.DATABASE_URL,
        echo=True
    )


async def init_db():
    async with engine.begin() as conn:
        from src.products.models import Product

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():

    Session = sessionmaker(
        bind = engine,
        class_= AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session