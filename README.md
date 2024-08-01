# Bookish

Bookish is a Django-based application for buying and selling books. Users can list books for sale, purchase books, and leave reviews.

## Features

- User registration and authentication
- List books for sale
- Buy books
- Leave reviews on books
- User profiles

## Technologies Used

- Django
- SQLite (default database)
- Bootstrap (for front-end styling)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/Dipansh682/bookish.git
cd bookish

2. Create a virtual environment and activate it:

python -m venv venv
.\venv\Scripts\activate # On Mac use `source venv/bin/activate`

3. Install the required packages:

pip install -r requirements.txt

4. Apply the migrations:

python manage.py migrate

5. Create a superuser:

python manage.py createsuperuser

6. Run the development server:

python manage.py runserver

7. Open your browser and go to `http://127.0.0.1:8000/`