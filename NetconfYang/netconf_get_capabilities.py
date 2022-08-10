#!/usr/bin/env python3


"""Get the capabilities of a remote device with NETCONF"""

from ncclient import manager


IOS_HOST = "sandbox-iosxe-recomm-1.cisco.com" # https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
NETCONF_PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"


def get_capabilities():
    """
    Method that prints NETCONF capabilities of remote device"""
    with manager.connect(
        host=IOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:
    
        print("\n***NETCONF Capabilities for device {}".format(IOS_HOST))
        for capability in device.server_capabilities:
            print(capability)


if __name__ == "__main__":
    get_capabilities()