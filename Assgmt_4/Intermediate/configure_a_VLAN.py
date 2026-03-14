import requests
import json

url = "https://switch-ip/ins"
headers = {"Content-Type": "application/json"}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "vlan 10 ; name Sales",
    "output_format": "json"
  }
}

response = requests.post(url, headers=headers, json=payload,
                         auth=("admin", "password"), verify=False)

print(response.json())