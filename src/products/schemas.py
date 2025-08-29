from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class ProductCreate(BaseModel):
    productName: str
    price: int
    quantity: int
    
class ProductUpdate(BaseModel):
    productName: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None
    
class ProductRead(BaseModel):
    uid: UUID
    productName: str
    price: int
    quantity: int
    created_at: datetime
    updated_at: datetime  
