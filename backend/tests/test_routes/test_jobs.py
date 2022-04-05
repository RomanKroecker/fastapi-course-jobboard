# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:28:48 2022

@author: RomKey
"""
import json


def test_create_job(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company":"testhoo",
        "company_url":"https://www.yahoo.com",
        "location":"USA,NY",
        "description":"Testing",
        "date_posted":"2022-07-20"
        }
    
    
    response = client.post("/job/create-job",json.dumps(data))
    assert response.status_code == 200
    