from fastapi_users.authentication import AuthenticationBackend

from core.auth.transport import bearer_transport
from .auth_strategy import get_db_strategy


authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=bearer_transport,
    get_strategy=get_db_strategy,
)
