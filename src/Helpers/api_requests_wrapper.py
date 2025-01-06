# Pre built methods for the GET , POST, PATCH, DELETE request

import  json
import requests

import  requests
from requests import delete
from requests.auth import AuthBase


def get_request(Url,auth):
    response=requests.get(url=Url,auth=auth )
    return response.json()


def post_request(URl,Auth,pay_load,Headers,in_jsonResponse):
    post_response=requests.post(url=URl,data=json.dumps(pay_load),headers=Headers,auth=Auth)
    if in_jsonResponse==True:
        return post_response.json()
    return post_response

def put_request(URl,Auth,pay_load,Headers,in_jsonResponse):
    put_response=requests.put(url=URl,data=json.dumps(pay_load),headers=Headers,auth=Auth)
    if in_jsonResponse==True:
        return put_response.json()
    return put_response

def patch_request(URl,Auth,pay_load,Headers,in_jsonResponse):
    patch_response=requests.patch(url=URl,data=json.dumps(pay_load),headers=Headers,auth=Auth)
    if in_jsonResponse==True:
        return patch_response.json()
    return patch_response

def delete_request(URl,Auth,pay_load,Headers,in_jsonResponse):
    delete_response=requests.delete(url=URl,data=json.dumps(pay_load),headers=Headers,auth=Auth)
    if in_jsonResponse==True:
        return delete_response.json()
    return delete_response