# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:49:07 2022

@author: RomKey
"""
from sqlalchemy.orm import Session
import random 
import string 


from schemas.users import UserCreate
from db.repository.users import create_new_user


def random_lower_string() ->str:
    return "".join(random.choices(string.ascii_lowercase, k=32))



def create_random_owner(db:Session):
    username = random_lower_string()
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    user_schema = UserCreate(username=username, email=email, password=password)
    user = create_new_user(user=user_schema, db=db)
    return user