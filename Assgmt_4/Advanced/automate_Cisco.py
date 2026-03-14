'''You can automate configuration on Cisco SD-WAN
by sending API requests with Python using the Requests
(Python library) to the REST API.'''

# Login to SD-WAN API

import requests

url = "https://vmanage-ip/j_security_check"

data = {
    "j_username": "admin",
    "j_password": "password"
}

session = requests.session()
response = session.post(url, data=data, verify=False)

#Send configuration request
api_url = "https://vmanage-ip/dataservice/device"

response = session.get(api_url, verify=False)

print(response.json()) 

'''What the code does

1️⃣ Logs in to the vManage controller
2️⃣ Creates a session for authentication
3️⃣ Sends API requests to retrieve or configure SD-WAN devices
4️⃣ Returns the configuration data.'''