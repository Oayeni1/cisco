# Get the authentication token

import requests

auth_url = "https://dnac-ip/dna/system/api/v1/auth/token"
response = requests.post(auth_url, auth=("admin", "password"), verify=False)

token = response.json()["Token"]



# Use the token in API requests

headers = {"X-Auth-Token": token}

url = "https://dnac-ip/dna/intent/api/v1/network-device"
response = requests.get(url, headers=headers, verify=False)

print(response.json())