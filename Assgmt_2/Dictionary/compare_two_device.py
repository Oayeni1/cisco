 def compare_configs(config1, config2)
    """
    Compare two configuration strings and return differences.
    Returns a dictionary with lines only in config1 and lines only in config2.
    """

    # Split configs into lines and strip whitespace
    lines1 = set(line.strip() for line in config1.splitlines() if line.strip())
    lines2 = set(line.strip() for line in config2.splitlines() if line.strip())

    # Lines in config1 but not in config2
    only_in_config1 = lines1 - lines2

    # Lines in config2 but not in config1
    only_in_config2 = lines2 - lines1

    return {
        "only_in_config1": sorted(only_in_config1),
        "only_in_config2": sorted(only_in_config2)
    }

config_old = """
hostname Router1
interface Gig0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
"""

config_new = """
hostname Router1
interface Gig0/0
 ip address 192.168.1.2 255.255.255.0
 no shutdown
interface Gig0/1
 ip address 10.0.0.1 255.255.255.0
"""

differences = compare_configs(config_old, config_new)

print("Lines only in old config:")
print(differences["only_in_config1"])
print("\nLines only in new config:")
print(differences["only_in_config2"])