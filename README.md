# FAQ Management System

A Django-based backend system for managing FAQs with multi-language support, WYSIWYG editor integration, and REST API for fetching FAQs in different languages.

## Features

- **Multi-language FAQ support**: Store and retrieve FAQs in multiple languages (e.g., English, Hindi).
- **WYSIWYG Editor**: Use django-ckeditor for rich text formatting of FAQ answers.
- **REST API**: Fetch FAQs with language-specific translations using query parameters.
- **Caching**: Use Redis to cache FAQ translations for improved performance.
- **Admin Panel**: Manage FAQs through a user-friendly Django admin interface.
- **Tests**: Includes unit tests for models and API endpoints.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default)
- **Caching**: Redis
- **WYSIWYG Editor**: django-ckeditor
- **Translation**: googletrans (Google Translate API)
- **Testing**: pytest

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- Redis (for caching)
- Docker (for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/1ncreo/faq_p.git
   cd faq-management-system
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start Redis:
   - **Local Installation**: Install Redis on your machine (`sudo apt install redis` on Ubuntu).
   - **Docker**: Use the provided `docker-compose.yml` file:
     ```bash
     docker-compose up
     ```

6. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

7. Access the API at `http://localhost:8000/api/faqs/`.

## API Usage

### Endpoints

- **Fetch FAQs**:
  - **URL**: `GET http://localhost:8000/api/faqs/'
  - **Query Parameters**:
    - `lang`: Language code (e.g., `en`, `hi`). Default is English (`en`).

### Examples

- Fetch FAQs in English:
  ```bash
  curl http://localhost:8000/api/faqs/
  ```

- Fetch FAQs in Hindi:
  ```bash
  curl http://localhost:8000/api/faqs/?lang=hi
  ```

## Admin Panel

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Access the admin panel at `http://localhost:8000/admin/`.

3. Add and manage FAQs through the admin interface.

## Running Tests

Run the unit tests to ensure everything works as expected:
   ```bash
   pytest faq_app/tests.py -v
OR
   docker-compose run test
   ```

---

This README provides a comprehensive guide to setting up, using, and managing the FAQ Management System. Contributions are welcome!
