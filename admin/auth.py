from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request):
        form = await request.form()
        username, password = form.get('username'), form.get('password')
        ...
        request.session.update({'token': "..."})
        return True


    async def logout(self, request: Request):
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        token = request.session.get('token')

        if not token:
            return False
        ...
        return True


authentication_backend = AdminAuth(secret_key="...")
