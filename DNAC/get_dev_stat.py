#!/usr/bin/env python3

from dnacentersdk import DNACenterAPI

target_device_type = "Cisco Catalyst 9300 Switch"
session = DNACenterAPI(
    base_url="https://sandboxdnac.cisco.com",
    username="devnetuser",
    password="Cisco123!",
    verify=False
)

devices = session.devices.get_device_list().response

for device in devices:
    if int(device.upTime.split()[0]) > 90:
        if device.type == target_device_type:
            output = session.devices.delete_device_by_id(device.id)
            print(output)

    else:
        selected_device = session.devices.get_device_by_id(device.id)
        output = selected_device.response.inventoryStatusDetail
        print(output)