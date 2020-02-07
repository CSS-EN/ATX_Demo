import requests
from requests.auth import HTTPBasicAuth
import getpass
from static_config import *

def auth_token():
    req = requests.post(LOGONURL, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify=False)
    token = req.json()['Token']
    print(token)

auth_token()