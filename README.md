# WebHookApp

WebHookApp is a Django-based web application that allows you to manage and trigger webhooks for various events. It uses Celery for handling asynchronous tasks, such as firing events and making HTTP requests to subscribed webhooks.

## Features

- Create and manage webhooks for specific events.
- Trigger events to notify subscribed webhooks.
- Asynchronous task processing using Celery.
- Automatic retry mechanism for failed webhook requests.

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.8 or higher)
- Django
- Celery
- RabbitMQ (or any other message broker supported by Celery)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KKBhati07/Webhook-App.git

2. Install dependencies

    ```bash
    cd WebHookApp
    pip install -r requirements.txt

3. Apply Migrations

    ```bash
    python manage.py migrate

4. Start Celery worker
    ```bash
    celery -A webhookapp worker -l INFO

5. Start development server
    ```bash
    python manage.py runserver


