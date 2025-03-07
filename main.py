import uvicorn

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from sqladmin import Admin

from admin.auth import authentication_backend
from admin.views import UserAdmin
from api.v1.users import router as users_router
from db.connectors import engine
from frontend.pages.router import router as frontend_router

app = FastAPI()
admin = Admin(app, engine, authentication_backend=authentication_backend)

app.mount('/static', StaticFiles(directory='frontend/static'), name='static')

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(frontend_router)
admin.add_view(UserAdmin)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)