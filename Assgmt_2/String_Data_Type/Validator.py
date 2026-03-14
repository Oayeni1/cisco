def validate_cisco_config(config):
    errors = []

    lines = config.splitlines()

    # Check if config is empty
    if not config.strip():
        errors.append("Configuration is empty.")

    # Check for hostname
    if not any(line.strip().lower().startswith("hostname") for line in lines):
        errors.append("Missing hostname.")

    # Check for at least one interface
    interfaces = [line for line in lines if line.strip().lower().startswith("interface")]
    if not interfaces:
        errors.append("No interfaces configured.")

    # Check if at least one IP address exists
    if not any("ip address" in line.lower() for line in lines):
        errors.append("No IP address configured.")

    # Return results
    if errors:
        return False, errors
    else:
        return True, ["Configuration looks valid."]
        
# Example Usage:
config = """
hostname Router1
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
"""

valid, messages = validate_cisco_config(config)

print("Valid:", valid)
for msg in messages:
    print(msg)