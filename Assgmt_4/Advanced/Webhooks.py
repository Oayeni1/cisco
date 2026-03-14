# Create a webhook receiver

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return "Webhook received", 200

app.run(port=5000)


'''How it works

1️⃣ Cisco Webex sends an event to your webhook URL
2️⃣ Your Python server receives the POST request
3️⃣ The event data is read using:'''