#!/usr/bin/env python3


"""Get the capabilities of a remote device with NETCONF"""

from ncclient import manager


IOS_HOST = "sandbox-iosxe-recomm-1.cisco.com" # https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
NETCONF_PORT = "830"
USERNAME = "developer"
PASSWORD = "C1sco12345"
LOOPBACK_ID = "53"
LOOPBACK_IP = "1.1.1.1"
MASK = "255.255.255.255"
TYPE="ianaift:softwareLoopback"
DESC="New loopback added using python"


def add_loopback():

    add_loop_interface = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback{id}</name>
                <description>{desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    {type}
                </type>
                <enabled>{status}</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{ip}</ip>
                        <netmask>{mask}</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>
    """.format(id=LOOPBACK_ID, ip=LOOPBACK_IP, mask=MASK, type=TYPE, status="true", desc=DESC)

    with manager.connect(
        host=IOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:

        print("\n Adding loopback {} with IP address {} to device {}...\n".\
            format(LOOPBACK_ID, LOOPBACK_IP, IOS_HOST))
        netconf_response = device.edit_config(target="running", config=add_loop_interface)
        print(netconf_response)

if __name__ == "__main__":
    add_loopback()