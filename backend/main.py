# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:47:04 2022

@author: RomKey
"""

from fastapi import FastAPI

from core.config import settings
from db.session import engine
from db.base import Base
from apis.version1.route_users import router



def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(router)
    return app





app = start_application()



@app.get("/")
def hello_api():
    return{"detail":"Hi World"}