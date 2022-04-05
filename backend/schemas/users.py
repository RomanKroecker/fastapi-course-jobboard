# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:47:12 2022

@author: RomKey
"""
from typing import Optional 
from pydantic import BaseModel, EmailStr 


class UserCreate(BaseModel):
    username : str 
    email : EmailStr 
    password : str