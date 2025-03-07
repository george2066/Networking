import uuid

import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.staticfiles import StaticFiles
from sqladmin import Admin

from admin.auth import authentication_backend
from admin.views import UserAdmin
from api.v1.users import router as users_router
from auth.db import User
from auth.manager import get_user_manager
from auth.core import auth_backend
from auth.shemas import UserRead, UserCreate
from db.connectors import engine
from frontend.pages.router import router as frontend_router


app = FastAPI()
fastapi_users = FastAPIUsers[User, uuid.UUID] (
    get_user_manager,
    [auth_backend]
)

admin = Admin(app, engine, authentication_backend=authentication_backend)

app.mount('/static', StaticFiles(directory='frontend/static'), name='static')

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(frontend_router)
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix='/auth/jwt', tags=['auth'])
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'])
admin.add_view(UserAdmin)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)