# Data Pusher - CustomerLabs Digital Solution Pvt. Ltd Python Developer Assessment

This project was developed as part of the Python Developer Assessment for CustomerLabs Digital Solution Pvt. Ltd. It is a Django-based web application that receives data for specific accounts and forwards it to multiple destinations using webhook URLs, demonstrating proficiency in Python, Django, and RESTful API development.

## Project Overview

Data Pusher provides a flexible system for managing accounts, destinations, and incoming data. It showcases the implementation of key features required in modern web applications, including secure data handling, webhook integration, and API documentation.

## Key Features

- Account management with automatic generation of secret tokens
- Destination management for each account
- Receive incoming JSON data and forward it to multiple destinations
- View incoming data for each account
- RESTful API with Swagger documentation
- Admin interface for easy data management

## Technologies Utilized

- Python 3.8+
- Django 3.2+
- Django REST Framework
- drf-yasg for Swagger documentation
- SQLite (demonstrating database integration, easily switchable to other databases)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/kaviarasanmani/Data-Pusher-Webhook-Integrationt
   cd Data-Pusher-Webhook-Integration.git
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

The application will be accessible at `http://localhost:8000`.

## API Endpoints

The following RESTful API endpoints are implemented:

- `/api/accounts/`: CRUD operations for accounts
- `/api/destinations/`: CRUD operations for destinations
- `/api/account/<uuid:account_id>/destinations/`: Retrieve destinations for a specific account
- `/server/incoming_data/`: Receive incoming data (requires `CL-X-TOKEN` header)
- `/api/account/<uuid:account_id>/incoming-data/`: View incoming data for a specific account

For comprehensive API documentation, visit:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Usage Guide

1. Create an account via the `/api/accounts/` endpoint or the admin interface.
2. Note the automatically generated `app_secret_token` for the account.
3. Create destinations for the account using the `/api/destinations/` endpoint or admin interface.
4. To send data, make a POST request to `/server/incoming_data/` with the `CL-X-TOKEN` header set to the account's `app_secret_token`.
5. The application will forward the data to all destinations associated with the account.
6. View incoming data for an account using the `/api/account/<uuid:account_id>/incoming-data/` endpoint.

## Admin Interface

The Django admin interface is accessible at `http://localhost:8000/admin/`. Use it to manage accounts, destinations, and view incoming data.

## Assessment Criteria

This project demonstrates proficiency in:

1. Django and Django REST Framework
2. RESTful API design and implementation
3. Database modeling and relationships
4. Authentication and security practices
5. API documentation using Swagger
6. Test-driven development
7. Code organization and best practices

## Note to Assessors

This project was developed as per the requirements specified in the Python Developer Assessment for CustomerLabs Digital Solution Pvt. Ltd. It showcases the ability to create a robust, scalable web application with a focus on data handling and API development.
