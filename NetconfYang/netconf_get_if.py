#!/usr/bin/env python3


"""Get the capabilities of a remote device with NETCONF"""

from ncclient import manager
import xmltodict
import xml.dom.minidom

IOS_HOST = "sandbox-iosxe-recomm-1.cisco.com" # https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
NETCONF_PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"

# Create an xml filter to targeted NETCONF queries

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface></interface>
        </interfaces>
</filter>
"""

print("Opening NETCONF Connection to {}".format(IOS_HOST))

with manager.connect(
        host=IOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:

        print("Sending a <get-config> operation to the device.\n")
        netconf_reply = device.get_config(source="running", filter=netconf_filter)

        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        interfaces = netconf_data["interfaces"]["interface"]

        print("\nThe interface status of the device is:")

        for interface in interfaces:
            print("Interface {} enabled status is {}".format(
                    interface["name"],
                    interface["enabled"]
                )
            )