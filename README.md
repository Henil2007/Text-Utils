# Django Project

This is a Django project created for a small web application.

## Project Structure

- `django_project/` - Django project settings and application configuration
- `templates/` - HTML templates used by the app
- `manage.py` - Django management script
- `db.sqlite3` - SQLite database file

## Requirements

- Python 3.x
- Django

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment if needed:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install Django:

   ```bash
   pip install django
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser at:

   ```text
   http://127.0.0.1:8000/
   ```

## Useful Commands

- Create a new app:

  ```bash
  python manage.py startapp app_name
  ```

- Run the development server:

  ```bash
  python manage.py runserver
  ```

- Apply migrations:

  ```bash
  python manage.py migrate
  ```

## Notes

This project currently includes the default Django setup and template files. You can extend it by adding apps, views, models, and routes as needed.
