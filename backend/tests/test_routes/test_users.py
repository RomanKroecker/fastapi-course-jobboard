# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:26:56 2022

@author: RomKey
"""
import json


def test_create_user(client):
    data = {"username":"testusername","email":"abc@test.com","password":"12344515"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["email"] == "abc@test.com"
    assert response.json()["is_active"] == True