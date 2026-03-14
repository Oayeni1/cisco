import requests

#For example >> Cisco DNA Center details
base_url = "https://dnac-ip-address"
username = "admin"
password = "paswd01"

#for example >> Step 1: Get token
auth_url = f"{base_url}/dna/system/api/v1/auth/token"
response = requests.post(auth_url, auth=(username, password), verify=False)
token = response.json()["Token"]

#for example >> Step 2: Get device list
headers = {"X-Auth-Token": token}
devices_url = f"{base_url}/dna/intent/api/v1/network-device"

devices = requests.get(devices_url, headers=headers, verify=False)

print(devices.json())