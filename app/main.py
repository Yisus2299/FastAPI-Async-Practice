from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.v1 import users

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

# CONFIGURATING CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# INCLUYING ROUTES
app.include_router(users.router, prefix="/api/v1", tags=["users"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}", "version": settings.APP_VERSION}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.APP_VERSION}