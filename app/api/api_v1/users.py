from fastapi import APIRouter

from core.config import settings
from api.api_v1.fastapi_users_routers import fastapi_users
from core.schemas.user import UserRead, UserUpdate


router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"]
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate)
)