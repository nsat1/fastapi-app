from fastapi import APIRouter

from core.config import settings
from .fastapi_users_routers import fastapi_users
from api.dependencies.auth.backend import authentication_backend


router = APIRouter(tags=["Auth"])

router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
