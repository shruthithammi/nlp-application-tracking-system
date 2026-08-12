from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.database.connection import Base, engine
from app.database import models  # noqa: F401
from app.api import auth, applications, emails, timeline, notifications

settings = get_settings()
@asynccontextmanager
async def lifespan(app):
    Base.metadata.create_all(bind=engine)
    yield
app = FastAPI(title="ClearHire API", version="1.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origin_list, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router, prefix="/api")
app.include_router(applications.router, prefix="/api")
app.include_router(emails.router, prefix="/api")
app.include_router(timeline.router, prefix="/api")
app.include_router(notifications.router, prefix="/api")
@app.get("/health")
def health(): return {"status":"ok","service":"clearhire-api"}
