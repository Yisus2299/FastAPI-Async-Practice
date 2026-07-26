from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # General Configuration
    APP_NAME: str = "API Refresh"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
        # Database Configuration
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/mydb"
    
    # Security Configuration
    SECRET_KEY: str = "alekkzyran"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()