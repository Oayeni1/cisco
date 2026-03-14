import requests

url = "https://dnac-ip/dna/intent/api/v1/template-programmer/template/deploy"
headers = {
    "X-Auth-Token": "your_token",
    "Content-Type": "application/json"
}

data = {
    "templateId": "template_id_here",
    "targetInfo": [
        {
            "id": "device_id_here",
            "type": "MANAGED_DEVICE"
        }
    ]
}

response = requests.post(url, headers=headers, json=data, verify=False)

print(response.json())



'''What this code does

1️⃣ Connects to the Cisco DNA Center API
2️⃣ Sends a POST request to deploy a template
3️⃣ Specifies the template ID and target device
4️⃣ Returns the deployment result'''