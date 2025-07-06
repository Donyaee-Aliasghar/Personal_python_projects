from fastapi import FastAPI
from .database import engine, Base

from .api.users import router as urouter
from .api.patients import router as prouter
from .api.genetic_variants import router as gvrouter
from .api.genetic_samples import router as gsrouter
from .api.clinical_records import router as grrouter
from .api.analysis_results import router as arrouter
from .api.files import router as frouter


app = FastAPI(title="Genomic & Clinical Data Management System")

app.include_router(urouter)
app.include_router(prouter)
app.include_router(gvrouter)
app.include_router(gsrouter)
app.include_router(grrouter)
app.include_router(arrouter)
app.include_router(frouter)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Welcome to Genomanager API"}
