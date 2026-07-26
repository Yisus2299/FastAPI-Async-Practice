from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.database import get_db

router = APIRouter()

