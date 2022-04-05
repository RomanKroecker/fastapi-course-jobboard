# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 09:54:03 2022

@author: RomKey
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True,index=True)
    username  = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")