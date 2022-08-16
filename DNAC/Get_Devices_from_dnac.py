#!/usr/bin/env python3

import requests
from prettytable import PrettyTable


dnac_devices = PrettyTable(["Hostname", "Platform ID", "Software Type", "Software Version", "Uptime"])
dnac_devices.padding_width = 1

# Disregard insecure warning due to SSL Certificate
requests.packages.urllib3.disable_warnings()

dnac = {
    "host": "sandboxdnac.cisco.com",
    "port": 443,
    "username": "devnetuser",
    "password": "Cisco123!"
}

headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": ""
}

def dnac_login(host, username, password):
    url = "https://{}/api/system/v1/auth/token".format(host)
    response = requests.post(url, auth=(username, password), headers=headers, verify=False)
    if response.ok:
        return response.json()["Token"]


def network_device_list(host, token):
    url = "https://{}/api/v1/network-device".format(host)
    headers["X-Auth-Token"] = token
    response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        data = response.json()
        for item in data["response"]:
            dnac_devices.add_row([item["hostname"], item["platformId"], item["softwareType"], item["softwareVersion"], item["upTime"]])



if __name__ == "__main__":
    token = dnac_login(dnac["host"], dnac["username"], dnac["password"])
    network_device_list(dnac["host"], token)

    print(dnac_devices)