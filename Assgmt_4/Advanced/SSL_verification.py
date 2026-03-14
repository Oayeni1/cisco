'''When using Python to call a REST API from Cisco platforms like Cisco DNA Center,
SSL verification checks the server’s security certificate.

You can handle it using the Requests (Python library).'''

# Disable SSL verification (for testing)

import requests

url = "https://dnac-ip/api"
response = requests.get(url, verify=False)

print(response.json())

# Use a certificate file (recommended)

import requests

url = "https://dnac-ip/api"
response = requests.get(url, verify="certificate.pem")

print(response.json())