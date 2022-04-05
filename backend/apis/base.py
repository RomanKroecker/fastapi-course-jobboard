# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:02:49 2022

@author: RomKey
"""
from fastapi import APIRouter


from apis.version1 import route_users 


api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users",tags=["users"])