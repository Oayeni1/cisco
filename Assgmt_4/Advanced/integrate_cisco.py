'''You can integrate **Cisco DNA Center API with a
custom dashboard by using Python and the Requests
(Python library) to retrieve network data through
the REST API, then display it on your dashboard.'''

import requests

base_url = "https://dnac-ip"
token = "your_token"

url = f"{base_url}/dna/intent/api/v1/network-device"
headers = {"X-Auth-Token": token}

response = requests.get(url, headers=headers, verify=False)
devices = response.json()["response"]

for device in devices:
    print(device["hostname"], device["managementIpAddress"])


    '''How it works

1️⃣ Python sends a GET request to Cisco DNA Center API.
2️⃣ The API returns network device data in JSON format.
3️⃣ Python processes the data.
4️⃣ The data can then be displayed on a custom dashboard (web app, monitoring page, etc.).'''