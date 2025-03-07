import uuid
from typing import Optional

from fastapi_users import BaseUserManager, UUIDIDMixin, models
from fastapi import Request, Depends

from auth.db import User, get_user_db
from settings import secret

KEY = secret.reset.get_secret_value()


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = KEY
    verification_token_secret = KEY

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        print(f'User {user.id} registered')


    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f'User {user.id} forgot password. Reset token: {token}')


    async def on_after_request_verify(
        self, user: models.UP, token: str, request: Optional[Request] = None
    ) -> None:
        print(f'Verification requested for user {user.id}. Verification token: {token}')


async  def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)