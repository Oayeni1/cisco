'''You authenticate by:

1 > Sending a POST request to /api/LekanLogin.json

2 > Including your username and password in JSON
{
  "lekUser": {
    "attributes": {
      "name": Lekan,
      "pwd": lekcisco
    }
  }
}

3 > The APIC server returns a session token used for other API requests'''