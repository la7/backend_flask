# Flask User Management API

This project is a Flask application that provides a RESTful API for managing user data. It includes functionalities for creating, reading, updating, and deleting users, along with Swagger documentation for easy API exploration.

## Project Structure

```
backend_flask
├── app
│   ├── app.py                # Main entry point of the Flask application
│   ├── swagger.py            # Swagger configuration and documentation setup
│   ├── models.py             # Database models
│   ├── routes.py             # API routes
│   └── __init__.py           # App package initialization
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd backend_flask
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app/app.py
   ```

5. **Access the API:**
   The API will be available at `http://localhost:5000/`.

## API Documentation

The API documentation is available at [http://localhost:5000/swagger](http://localhost:5000/swagger).

## Endpoints

- **GET /**: Retrieve a list of all users.
- **GET /<int:num>**: Retrieve a single user by ID.
- **POST /user**: Create a new user.
- **DELETE /delete/<int:num>**: Delete a user by ID.
- **PUT /update/<int:id>**: Update a user by ID.
- **PATCH /update/<int:id>**: Partially update a user by ID.

## Additional Information

Make sure to update the `swagger.json` file to define your API endpoints and their specifications for the Swagger UI to work correctly. 

This setup will allow you to document your Flask API using Swagger and provide an interactive interface for testing the endpoints.

## API Documentation
View the interactive API documentation [here](http://127.0.0.1:5000/apidocs).
