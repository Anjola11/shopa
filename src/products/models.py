from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime, date

class Product(SQLModel,table= True):
    __tablename__ = "products"
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID, primary_key=True, nullable=False,default = uuid.uuid4))
    productName: str
    price: int
    quantity: int
    created_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, nullable=False, default=datetime.now))
    updated_at: datetime = Field(sa_column = Column(pg.TIMESTAMP, nullable=False, default=datetime.now))

