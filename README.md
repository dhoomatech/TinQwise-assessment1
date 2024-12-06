# TinQwise-assessment1
TinQwise Assessment 1

# Personalized Book Recommendation API

## Description

The **Personalized Book Recommendation API** provides an API for users to get book recommendations based on their reading preferences, genres, and previous interactions. The system uses a basic algorithm to match users with books that are most likely to interest them.

This API exposes endpoints for managing books, users, and recommendations. It supports functionalities like:
- Retrieving a list of available books
- Creating, updating, and deleting books
- Generating personalized recommendations based on user preferences

## Features

- **Book management**: Add, update, delete, and view books.
- **User preferences**: Users can define their favorite genres and reading history.
- **Personalized recommendations**: The system will recommend books to users based on their preferences.
- **CRUD operations**: Full Create, Read, Update, Delete support for books and user preferences.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vishnuvvp007/TinQwise-assessment1.git
   cd TinQwise-assessment1

2. **Set up a virtual environment:**

   python -m venv venv
   source venv/bin/activate

3. **Install the required dependencies:**
   pip install -r requirements.txt

4. **Set up the database:**
   python manage.py migrate

5. **Create a superuser (optional for admin access):**
   python manage.py createsuperuser

6. **Run the server:**
   python manage.py runserver


## Access the API:

The API will be running at http://127.0.0.1:8000/.

You can use the following endpoints:

    User:
       POST /api/users/ : Create a new user
       GET /api/users/{id}/  : Retrieve user details
    
    Books:
        GET /api/books/: List all books
        POST /api/books/: Add a new book

    User Preferences:
        POST /api/users/{id}/preferences/: Record a preference
        DELETE /api/users/{id}/preferences/: Reset a user's preferences

    Recommendations:
        GET /api/users/{id}/recommendations/: Get book recommendations.