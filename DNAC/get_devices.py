#!/usr/bin/env python3

import requests
import json
from auth import get_token

requests.packages.urllib3.disable_warnings()

base_path = "https://sandboxdnac.cisco.com"
user = "devnetuser"
passwd = "Cisco123!"

token = get_token(base_path, user, passwd)
headers = {'Content-Type': 'application/json', 'x-auth-token': token}

def get_devices():
    url = f"{base_path}/dna/intent/api/v1/network-device"
    response = requests.get(url, headers=headers, verify=False)
    data = json.loads(response.text)["response"]
    for item in data:
        device_type = item["type"]
        desc = item["description"]
        serial_number = item["serialNumber"]
        sw_type = item["softwareType"]
        version = item["softwareVersion"]
        management_ip = item["managementIpAddress"]
        hostname = item["hostname"]
        series = item["series"]
        print(f"Hostname: {hostname}")
        print(f"Series: {series}")
        print(f"Device Type: {device_type}")
        print(f"Description: {desc}")
        print(f"Management IP: {management_ip}")
        print(f"Software Type: {sw_type}")
        print(f"Software Version: {version}")
        print(f"SN: {serial_number}\n")
        
        
        
                
if __name__ == "__main__":
    get_devices()