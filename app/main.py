from fastapi import FastAPI
from app.routers.extract import router as extract_router

app = FastAPI(
    title="Medical Amount Detection Service",
    version="1.0"
)

app.include_router(extract_router)
