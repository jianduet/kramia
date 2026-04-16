from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api import auth
from app.api import cotizaciones

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KRAMIA",
    description="Sistema de costeo para la industria textil",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(cotizaciones.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "app": "KRAMIA",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}