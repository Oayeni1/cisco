device1_config = {
    "GigabitEthernet0/0": "192.168.1.1",
    "GigabitEthernet0/1": "10.0.0.1",
    "GigabitEthernet0/2": "172.16.0.1",
    "GigabitEthernet0/3": "192.168.2.1"
}

device2_config = {
    "GigabitEthernet0/4": "179.18.0.2",
    "GigabitEthernet0/5": "172.169.2.3",
    "GigabitEthernet0/6": "30.22.10.1",
    "GigabitEthernet0/2": "172.16.0.1",
}
# Copy device1_config to avoid modifying original
merged_config = device1_config.copy()

# Merge device2_config into it
merged_config.update(device2_config)

print(merged_config)