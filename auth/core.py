from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy
)

from settings import secret

cookie_transport = CookieTransport(cookie_name='networking', cookie_max_age=3600)

KEY = secret.secret.get_secret_value()

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=KEY, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

