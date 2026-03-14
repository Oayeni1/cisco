def extract_interfaces(output):
    interfaces = []

    lines = output.splitlines()

    for line in lines:
        line = line.strip()

        # Skip header line
        if line.startswith("Interface") or line == "":
            continue

        # First word in each line is the interface name
        interface_name = line.split()[0]
        interfaces.append(interface_name)

    return interfaces


# Example usage
Cisco_show_ip_brief_output = """
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
Loopback0              10.1.1.1        YES manual up                    up
"""

# Example usage
interfaces = extract_interfaces(Cisco_show_ip_brief_output)

print("Interfaces found:")
for i in interfaces:
    print(i)