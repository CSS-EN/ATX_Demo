import requests
from requests.auth import HTTPBasicAuth
import getpass
from Config import *

def auth_token():
    req = requests.post(LOGONURL, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify=False)
    token = req.json()['Token']
    return token

def get_network_devices():
    hdr = {'x-auth-token': auth_token(), 'content-type': 'application/json'}
    print(hdr)
    req = requests.get(NETWORKDEVICELISTURL, headers=hdr, verify=False)
    print(req.json())

get_network_devices()