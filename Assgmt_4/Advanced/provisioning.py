# Authenticate to the APIC

import requests

url = "https://apic-ip/api/aaaLogin.json"

data = {
 "aaaUser": {
   "attributes": {
     "name": "admin",
     "pwd": "password"
   }
 }
}

response = requests.post(url, json=data, verify=False)
token = response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]

# Create a tenant (example provisioning task)

headers = {"Cookie": f"APIC-cookie={token}"}

tenant_url = "https://apic-ip/api/node/mo/uni/tn-NewTenant.json"

payload = {
 "fvTenant": {
   "attributes": {
     "name": "NewTenant"
   }
 }
}

response = requests.post(tenant_url, json=payload, headers=headers, verify=False)

print(response.json())

'''Simple idea

Login to Cisco ACI APIC using the API

Get an authentication token

Send POST requests to create or configure
fabric resources (tenants, networks, policies).'''