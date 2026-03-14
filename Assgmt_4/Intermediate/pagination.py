import requests

url = "https://dnac-ip/dna/intent/api/v1/network-device"
headers = {"X-Auth-Token": "your_token"}

page = 1
limit = 50

while True:
    params = {"offset": (page-1)*limit, "limit": limit}
    response = requests.get(url, headers=headers, params=params, verify=False)
    data = response.json()["response"]

    if not data:
        break

    for device in data:
        print(device["hostname"])

    page += 1




    '''What this does

Requests devices 50 at a time

Moves to the next page using offset

Stops when no more results are returned.

✅ Simple idea:
Python repeatedly calls the Cisco API,
collecting each page of results until all devices are retrieved.'''