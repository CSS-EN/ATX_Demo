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
    req = requests.get(NETWORKDEVICELISTURL, headers=hdr, verify=False)
    return req.json()

def print_device_list():
    device_json = get_network_devices()
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))

def print_interface_info(interface_info):
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for int in interface_info['response']:
        print("{0:42}{1:10}{2:12}{3:18}{4:17}{5:10}{6:15}".
              format(str(int['portName']),
                     str(int['vlanId']),
                     str(int['portMode']),
                     str(int['portType']),
                     str(int['duplex']),
                     str(int['status']),
                     str(int['lastUpdated'])))

def get_device_interface(device_id):
    hdr = {'x-auth-token': auth_token(), 'content-type': 'application/json'}
    querystring = {"macAddress": device_id}

print_device_list()
print_interface_info() 

#Change