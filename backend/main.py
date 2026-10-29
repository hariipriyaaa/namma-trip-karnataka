"""FastAPI application entrypoint."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import APP_NAME, FRONTEND_ORIGINS, API_PREFIX
from backend.routes.itinerary import router as itinerary_router
from backend.routes.dialect import router as dialect_router

app = FastAPI(
    title=APP_NAME,
    description="Curated Karnataka travel circuits, itinerary generation and regional Kannada phrasebook.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS + ["*"] if "*" in FRONTEND_ORIGINS else FRONTEND_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(itinerary_router, prefix=API_PREFIX)
app.include_router(dialect_router, prefix=API_PREFIX)

@app.get("/")
def root():
    return {"name": APP_NAME, "status": "ok", "docs": "/docs", "health": "/health"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "namma-trip-karnataka"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
