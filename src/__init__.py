from fastapi import FastAPI
from src.products.routes  import product_router
from src.auth.routes import auth_router
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

@app.get("/")
async def root():
    return {"message": "Shopa API is running", "version": version}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(product_router, prefix=f"/api/v{version}/product")
app.include_router(auth_router,prefix=f"/api/v{version}/account")