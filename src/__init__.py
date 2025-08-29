from fastapi import FastAPI
from src.products.routes  import product_router
from src.db.main import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
        print("\n------Server Startes-----\n")
        await init_db()
        yield
        print("\n------Server Closed------\n")

version = "1"
app = FastAPI(
    title = "Shopa",
    description = "Shopa marketplace API",
    version= version,
    lifespan=lifespan
)

app.include_router(product_router, prefix=f"/api/v{version}/product")