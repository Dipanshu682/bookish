# Bookish

Bookish is a Django-based application for buying and selling books. Users can list books for sale, purchase books, and leave reviews.

## Features

- User registration and authentication
- List books for sale
- Buy books
- Leave reviews on books
- User profiles
- Search Books
- Pagination of Book Listings
- Django Signals for Notifications and Other Actions

## Technologies Used

- Django
- SQLite (default database)
- Bootstrap (for front-end styling)

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Dipanshu682/bookish.git
   cd bookish
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Open your browser and go to `http://127.0.0.1:8000/`**

## Usage

- Register a new account or log in with an existing account.
- List a new book for sale.
- Browse the list of available books and purchase one.
- Leave a review for a book you have purchased.
