#!/usr/bin/env python3


"""Get the capabilities of a remote device with NETCONF"""

from ncclient import manager
import xml.dom.minidom

IOS_HOST = "sandbox-iosxe-recomm-1.cisco.com" # https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
NETCONF_PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"

# Create an xml filter to targeted NETCONF queries

netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>{name}</name>
            </interface>
        </interfaces>
</config>
"""

new_loopback = {}
new_loopback["name"] = "Loopback53"

netconf_data = netconf_interface_template.format(name=new_loopback["name"])

print("The configuration payload to be sent over netconf.\n")
print(netconf_data)

with manager.connect(
        host=IOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:

        print("Sending a <edit-config> operation to the device.\n")
        netconf_reply = device.edit_config(netconf_data, target="running")

print("Here is the raw XML data returnd from the device")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())