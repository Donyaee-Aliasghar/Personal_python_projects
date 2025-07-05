from fastapi import FastAPI
from gcdms.database import engine, Base
from gcdms.api.users import router as urouter
from gcdms.api.patients import router as prouter


app = FastAPI(title="Genomic & Clinical Data Management System")

app.include_router(urouter)
app.include_router(prouter)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Welcome to Genomanager API"}
