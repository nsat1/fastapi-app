from fastapi import APIRouter

from .fastapi_users_routers import fastapi_users
from api.dependencies.auth.backend import authentication_backend
from core.schemas.user import UserRead, UserCreate

router = APIRouter(tags=["Auth"])

router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)

router.include_router(router=fastapi_users.get_register_router(UserRead, UserCreate))
