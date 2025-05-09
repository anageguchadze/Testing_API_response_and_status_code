# Testing_API_response_and_status_code

This project demonstrates how to test a specific API endpoint using Django REST Framework (DRF). The goal is to verify that the `/api/items/` endpoint returns a `200 OK` status code and a correctly structured JSON response containing all items in the database.

## ✅ Task Description

- Create a Django model called `Item` with `name` and `description` fields.
- Create a DRF `ModelViewSet` to expose the `/api/items/` endpoint.
- Implement a test case that:
  - Sends a GET request to `/api/items/`
  - Confirms that the response status code is `200 OK`
  - Verifies that the response is in JSON format
  - Ensures that the returned data is a list
  - Optionally checks the number of returned items

## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework
- pytest or Django’s built-in test framework (`unittest` via `TestCase`)

## 🧩 Code Structure

- `models.py`: Contains the `Item` model.
- `serializers.py`: Defines `ItemSerializer`.
- `views.py`: Implements `ItemViewSet`.
- `urls.py`: Registers the route using DRF's `DefaultRouter`.
- `tests.py`: Contains the test case for verifying the `/api/items/` endpoint.


▶️ Running Tests
python manage.py test

📂 Project Structure
myproject/
│
├── myapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── manage.py
└── README.md

📌 Notes
Make sure the test database is properly set up before running tests.

Adjust the URL prefix (/api/) if you're using a custom base path in your urls.py.

📃 License
This project is provided for educational purposes only.