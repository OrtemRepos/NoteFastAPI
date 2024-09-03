from fastapi import FastAPI, Depends
from auth.database import User
from auth.auth import (
    auth_backend,
    fastapi_users,
    current_active_user,
    current_super_user,
)
from auth.schemas import UserRead, UserCreate, UserUpdate
from web import user, note

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
app.include_router(
    note.router
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.id}!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
