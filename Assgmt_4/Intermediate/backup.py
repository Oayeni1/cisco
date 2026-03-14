import requests

base_url = "https://dnac-ip"
token = "your_token"

url = f"{base_url}/dna/intent/api/v1/network-device-config"
headers = {"X-Auth-Token": token}

response = requests.get(url, headers=headers, verify=False)

config = response.json()

with open("backup_config.json", "w") as file:
    file.write(str(config))

print("Backup completed")



'''What the code does

1️⃣ Connects to Cisco DNA Center API
2️⃣ Sends a GET request to retrieve device configuration
3️⃣ Receives configuration data in JSON format
4️⃣ Saves the configuration to a backup file'''