# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:47:04 2022

@author: RomKey
"""

from core.config import settings
from fastapi import FastAPI


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return{"detail":"Hi World"}