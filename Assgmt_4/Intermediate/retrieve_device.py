import requests

base_url = "https://dnac-ip"
token = "your_token"

url = f"{base_url}/dna/intent/api/v1/network-device"
headers = {"X-Auth-Token": token}

response = requests.get(url, headers=headers, verify=False)
devices = response.json()["response"]

for device in devices:
    print(device["hostname"], device["managementIpAddress"])



    '''What the code does

Connects to the Cisco API endpoint.
Sends a GET request to retrieve device inventory.
Converts the response from JSON to Python data.
Prints device hostname and IP address.'''