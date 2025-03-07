from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from api.v1.users import get_user

router = APIRouter(prefix='/pages', tags=['pages'])
templates = Jinja2Templates(directory='frontend/templates')

@router.get('/index')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})

@router.get('/card/{email}')
async def get_card(request: Request, user=Depends(get_user)):
    return templates.TemplateResponse('card.html', {'request': request, 'user': user})



