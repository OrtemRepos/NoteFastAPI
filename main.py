from fastapi import FastAPI, Depends
import fastapi_users
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate
from web import user

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/user",
    tags=["user"],
)
app.include_router(user.router)

current_active_user = fastapi_users.current_user(active=True)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.username}!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
