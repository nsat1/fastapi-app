import logging

from typing import Optional, TYPE_CHECKING, Union

from fastapi_users import (
    BaseUserManager,
    IntegerIDMixin,
    models,
    InvalidPasswordException,
)

from core.config import settings
from core.models.user import User
from core.schemas.user import UserCreate

if TYPE_CHECKING:
    from fastapi import Request


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self,
        user: models.UP,
        request: Optional["Request"] = None,
    ) -> None:
        log.warning(
            "User %r has registered.",
            user.id,
        )

    async def on_after_forgot_password(
        self,
        user: models.UP,
        token: str,
        request: Optional["Request"] = None,
    ) -> None:
        log.warning(
            "User %r has forgot password. Reset token %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self,
        user: models.UP,
        token: str,
        request: Optional["Request"] = None,
    ) -> None:
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )

    async def validate_password(
        self, password: str, user: Union[UserCreate, User]
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain e-mail")
