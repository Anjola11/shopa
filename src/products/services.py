from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from .models import Product
from .schemas import ProductCreate, ProductUpdate
from datetime import datetime
class ProductService:

    async def get_all_products(self, session: AsyncSession):
        statement = select(Product).order_by(desc(Product.created_at))

        result = await session.exec(statement)
        return result.all()

    async def get_product(self,product_id:str, session: AsyncSession):
        statement = select(Product).where(Product.uid == product_id)

        result = await session.exec(statement)

        return result.first()


    async def update_product(self, product_id:str, update: ProductUpdate, session: AsyncSession):
        product_to_update = await self.get_product(product_id, session)
        
        if not product_to_update:
            return None
        
        updated_product = update.model_dump()

        for key, value in updated_product.items():
            if value is not None:
                setattr(product_to_update, key, value)

        await session.commit()

        await session.refresh(product_to_update)

        return product_to_update


    async def add_product(self, product: ProductCreate, session: AsyncSession):
        product_to_add = product.model_dump()

        new_product = Product(**product_to_add)

        if 'created_at' in product_to_add and product_to_add['created_at']:
            new_product.created_at = datetime.strptime(product_to_add['created_at'], "%Y-%m-%d")
        else:
        
            new_product.created_at = datetime.now()

        session.add(new_product)
        
        await session.commit()

        await session.refresh(new_product)

        return new_product


    async def delete_product(self,product_id: str, session: AsyncSession):
        product_to_delete = await self.get_product(product_id, session)

        if not product_to_delete:
            return None

        await session.delete(product_to_delete)

        await session.commit()

        return True

        

   

