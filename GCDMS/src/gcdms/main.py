from fastapi import FastAPI
from gcdms.database import engine, Base
from gcdms.api.users import router as urouter
from gcdms.api.patients import router as prouter
from gcdms.api.genetic_variants import router as gvrouter
from gcdms.api.genetic_samples import router as gsrouter
from gcdms.api.clinical_records import router as grrouter
from gcdms.api.analysis_results import router as arrouter


app = FastAPI(title="Genomic & Clinical Data Management System")

app.include_router(urouter)
app.include_router(prouter)
app.include_router(gvrouter)
app.include_router(gsrouter)
app.include_router(grrouter)
app.include_router(arrouter)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Welcome to Genomanager API"}
