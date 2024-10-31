# Python Webhook Server

This Python server is designed to handle webhooks and API calls between various services, including Airtable. It captures JSON data from incoming requests, forwards this data to Airtable via an Airtable webhook, and includes API key-based access for added security.

## Features

- **API Key Authentication**: Secures the webhook endpoint, allowing only requests with the correct API key to access it.
- **Airtable Integration**: Sends JSON data to an Airtable webhook for further processing and storage.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Set up a virtual environment** (optional, recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a `.env` file** in the root of the project to store your environment variables securely:

    ```plaintext
    API_KEY="your_secure_api_key"
    AIRTABLE_WEBHOOK_URL="https://hooks.airtable.com/workflows/v1/genericWebhook/..."
    ```

    - Replace `"your_secure_api_key"` with a unique API key for authenticating requests.
    - Replace `"https://hooks.airtable.com/workflows/v1/genericWebhook/..."` with your Airtable webhook URL.

## Usage

1. **Start the server**:

    ```bash
    python server.py
    ```

2. **Send a POST request** to the server’s `/send-webhook` endpoint, including the `X-API-KEY` header for authentication. Here’s an example using `curl`:

    ```bash
    curl -X POST http://localhost:5000/send-webhook -H "X-API-KEY: your_secure_api_key"
    ```

   - This will trigger the server to process the incoming request and send data to Airtable.

## Project Structure

```plaintext
├── server.py           # Main server file with endpoint logic
├── .env                # Environment variables (API key, Airtable URL)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```


## API Endpoints

### POST `/send-webhook`

#### Description
This endpoint receives JSON data, verifies the provided API key, and forwards the data to Airtable.

#### Headers

- `X-API-KEY`: (Required) The API key for authorization.

#### Request Example

```json
{
    "customer_id": "12345",
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "+1-555-555-5555",
    "address": "123 Main St, Anytown, USA",
    "order_id": "67890",
    "order_total": 99.99,
    "order_date": "2024-10-30"
}
```

## Environment Variables
|Variable|	Description|
|--------|-------------|
|API_KEY|	The secret API key required to access the endpoint|
|AIRTABLE_WEBHOOK_URL	|URL for the Airtable webhook to receive JSON data|

Ensure these values are kept secure and not shared publicly.

## Troubleshooting

Invalid API Key: Ensure the API key in the request matches the one in the .env file. 
Environment Variables Not Loading: Make sure dotenv is installed, and the .env file is in the correct format. 
Airtable Failures: Verify that the correct webhook URL is in the .env file and that it is accessible.
