# helper.py

import json
import pprint
import requests

url_base = 'http://127.0.0.1:5000'
url_home = url_base + '/'

route_dict = {}
route_dict[''] = '/'
route_dict['login'] = '/login'
route_dict['register'] = '/register'

def req(endpoint='',data={},method='GET'):
    url = url_base + route_dict[endpoint]
    req = requests.Request(url=url,method=method,data=data)
    r = req.prepare()
    with requests.Session() as s:
        resp = s.send(r)
        return resp

def read_resp(resp):
    content = json.loads(resp.content.decode())
    return content

def print_resp(resp):
    data = read_resp(resp)
    pprint.pprint(data)

username = 'test_user'
password = 'badpass'
data = { 'username' : username, 'password': password}

