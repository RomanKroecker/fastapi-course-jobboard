# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:59:01 2022

@author: RomKey
"""

from passlib.context import CryptContext 

pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwt_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(plain_password):
        return pwt_context.hash(plain_password)
    
    
    
    
    
# print(Hasher.get_password_hash("Hello"))

# print(Hasher.verify_password("Hell", "$2b$12$4OFsEGFhTGmzqXIiuK0.a.eHdI5/WrrSwWBXirQ.v7xk6tmIIdrxC"))

# print(Hasher.verify_password("Hello", "$2b$12$4OFsEGFhTGmzqXIiuK0.a.eHdI5/WrrSwWBXirQ.v7xk6tmIIdrxC"))