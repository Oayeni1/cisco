import re

def map_interfaces_to_ips(config):
    """
    Given a Cisco configuration string, return a dictionary
    mapping interface names to their IP addresses.
    """

    interface_ip_map = {}
    current_intf = None

    lines = config.splitlines()

    # Regex to match IPv4 addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    for line in lines:
        line = line.strip()

        # Detect interface line
        if line.lower().startswith("interface"):
            current_intf = line.split()[1]  # Get interface name

        # Detect IP address line
        elif line.lower().startswith("ip address") and current_intf:
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                interface_ip_map[current_intf] = ip_match.group()
                current_intf = None  # Done with this interface

    return interface_ip_map

config = """
hostname Router1
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.0
 shutdown
"""

intf_map = map_interfaces_to_ips(config)
print(intf_map)