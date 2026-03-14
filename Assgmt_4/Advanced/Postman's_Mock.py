'''You can use **Postman Mock Server to simulate a 
REST API when testing integrations with 
Cisco platforms like Cisco DNA Center.'''

# Open Postman
'''Create a Collection
Open Postman
Create a new collection
Add a request (example API).'''

'GET /dna/intent/api/v1/network-device'

'''Create a Mock Server
Click the collection
Select Mock Collection
Postman generates a mock server URL.'''

'https://mock-server-id.mock.pstmn.io/network-device'

'''Define Example Responses
Inside the request:
Add an Example Response
Provide sample JSON data.'''

{
  "response": [
    {"hostname": "Switch1"},
    {"hostname": "Router1"}
  ]
}

'''Lastly, Send Request to Mock Server

Use the generated mock server URL instead of the real Cisco API.

Postman will return the fake response.'''