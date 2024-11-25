from fastapi_users import FastAPIUsers

from core.models import User
from api.dependencies.auth.user_manager import get_user_manager
from api.dependencies.auth.backend import authentication_backend


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)
