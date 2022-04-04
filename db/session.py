# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:14:38 2022

@author: RomKey
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 



from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

