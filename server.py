import os

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Retrieve the API key from environment variables
API_KEY = os.getenv("API_KEY")
AIRTABLE_WEBHOOK = os.getenv("AIRTABLE_WEBHOOK")

# Mock data to send to Airtable webhook
def generate_mock_data():
    return {
        "customer_id": "12345",
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "+1-555-555-5555",
        "address": "123 Main St, Anytown, USA",
        "order_id": "67890",
        "order_total": 99.99,
        "order_date": "2024-10-30"
    }

# Route to trigger the webhook, with API key verification
@app.route('/send-webhook', methods=['POST'])
def send_webhook():
    # Check for API key in request headers
    provided_api_key = request.headers.get("X-API-KEY")
    print(API_KEY)
    if provided_api_key != API_KEY:
        return jsonify({"status": "error", "message": "Invalid API key"}), 401

    # URL to Airtable webhook
    airtable_webhook_url = AIRTABLE_WEBHOOK
    payload = generate_mock_data()

    try:
        # Send POST request to Airtable webhook
        response = requests.post(airtable_webhook_url, json=payload)

        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Webhook sent successfully!", "data": payload}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to send webhook.", "response": response.text}), response.status_code

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
