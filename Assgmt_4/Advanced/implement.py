# Get the OAuth access token

import requests

url = "https://ise-ip/oauth2/token"

data = {
    "grant_type": "client_credentials",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
}

response = requests.post(url, data=data, verify=False)

token = response.json()["access_token"]


# Use the token to call the API

headers = {
    "Authorization": f"Bearer {token}"
}

api_url = "https://ise-ip/ers/config/endpoint"

response = requests.get(api_url, headers=headers, verify=False)

print(response.json())


'''Simple idea

Request an OAuth access token from Cisco ISE

Store the token in a variable

Use the token in the Authorization header to access the API.'''