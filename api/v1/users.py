from http import HTTPStatus
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr

from api.v1.handlers import (get_all_users,
                             get_user_by_email,
                             post_new_user,
                             delete_user_by_email,
                             update_user_by_email)
from api.v1.models import User, CreateUser
from db.connectors import get_db_session

router = APIRouter()

@router.get("/", response_model=List[User])
async  def get_users(session: AsyncSession = Depends(get_db_session)):
    users = await get_all_users(session)
    if not users:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='No found users')
    else:
        return users


@router.get("/{email}", response_model=User)
async  def get_user(email: EmailStr,
                    session: AsyncSession = Depends(get_db_session)):
    user = await get_user_by_email(session, email=email)
    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='No found user')
    else:
        return user


@router.post("/", response_model=User)
async  def add_user(user: CreateUser, session: AsyncSession = Depends(get_db_session)):
    success = await post_new_user(session, user)
    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='No created user')
    else:
        return user


@router.delete("/{email}", response_model=EmailStr)
async def del_user(email: EmailStr,
                   session: AsyncSession = Depends(get_db_session)):
    success = await delete_user_by_email(session, email)
    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='No deleted user')
    else:
        return email


@router.patch("/{email}", response_model=str)
async def update_user(email: EmailStr, about: str,
                      session: AsyncSession = Depends(get_db_session)):
    success = await update_user_by_email(session, email, about)
    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='No updated user')
    else:
        return about