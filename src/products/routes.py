from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import ProductCreate, ProductUpdate, ProductRead
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from .services import ProductService
from uuid import UUID
from typing import List

product_router = APIRouter()
product_service = ProductService()

@product_router.get("/", response_model = List[ProductRead])
async def get_all_products(session: AsyncSession = Depends(get_session)):
        products = await product_service.get_all_products(session)
        return products

@product_router.get("/{id}", response_model = ProductRead)
async def get_product(id:UUID,session: AsyncSession = Depends(get_session)):
        product = await product_service.get_product(id, session)
        if product:
                return product
        else: 
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Product not found")

@product_router.patch("/update/{id}")
async def update_product(id:UUID, update: ProductUpdate, session: AsyncSession = Depends(get_session)):
        updated = await product_service.update_product(id, update, session)

        if updated:
                return updated
        else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Product not found")

@product_router.post("/add_product")
async def add_product(product:ProductCreate, session: AsyncSession = Depends(get_session)):
        product_add = await product_service.add_product(product, session)

        return product_add

@product_router.delete("/delete/{id}")
async def delete_product(id, session: AsyncSession = Depends(get_session)):
        deleted = await product_service.delete_product(id, session)

        if not deleted:
                raise HTTPException(status_code=404, detail="Product not found")
        
        return {"detail": "Product deleted successfully"}