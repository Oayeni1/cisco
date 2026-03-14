def get_hostname(config):
    """
    Extract hostname from a Cisco configuration string.
    """
    # Split the config into individual lines
    lines = config.splitlines()
    
    # Loop through each line
    for line in lines:
        line = line.strip()  # remove leading/trailing spaces
        if line.lower().startswith("hostname"):
            # The hostname is the word after 'hostname'
            return line.split()[1]  # split by spaces and take second word
    
    # If no hostname is found
    return None

# Example usage
cisco_config = """
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
Hostname Router1
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
!
"""

hostname = get_hostname(cisco_config)
print("Cisco Device Hostname:", hostname)