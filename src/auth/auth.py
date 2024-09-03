from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    JWTStrategy,
    AuthenticationBackend,
    CookieTransport,
)

from auth.manager import get_user_manager
from model.model import User

SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, int](  # type: ignore
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(superuser=True, active=True)
