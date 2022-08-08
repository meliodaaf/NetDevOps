#!/usr/bin/python3

import json
import sys
import requests



base_path = "https://api.meraki.com/api/v1/"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
headers = {
    "Content": "application/json",
    "X-Cisco-Meraki-API-Key": api_key
}


def get_orgs():
    url = f"{base_path}/organizations"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for item in data:
        org_id = item["id"]
        get_org_networks(org_id)
        
        
def get_org_networks(org_id):
    url = f"{base_path}/organizations/{org_id}/networks"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for item in data:
        net_id = item["id"]
        get_net_devices(net_id)
    

def get_net_devices(net_id):
    url = f"{base_path}/networks/{net_id}/devices"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for item in data:
        try:
            name = item["name"]
        except:
            name = None
        try:
            lan_ip = item["lanIp"]
        except:
            lan_ip = None
        try:
            model = item["model"]
        except:
            model = None
        try:
            serial = item["serial"]
        except:
            serial = None
        print(f"Network Name: {name}")
        print(f"LAN IP: {lan_ip}")
        print(f"Model: {model}")
        print(f"Serial: {serial}\n")
        


if __name__ == "__main__":
    try:
        get_orgs()
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit()
   