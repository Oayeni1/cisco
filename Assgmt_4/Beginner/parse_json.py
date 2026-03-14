#To Request
import requests

url = "https://dnac-ip/dna/intent/api/v1/network-device"
headers = {"X-Auth-Token": "your_token"}

response = requests.get(url, headers=headers, verify=False)

#To Convert to Json
data = response.json()

#To Access the data
for device in data["response"]:
    print(device["hostname"])