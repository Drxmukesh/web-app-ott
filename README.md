# Netflix Clone Project

This project is a web application built using Python and Django, designed to mimic the functionality of Netflix. It features an admin interface for managing video permissions, titles, and descriptions, as well as user-facing features for browsing categories such as "Most Popular," "Latest," and "Recent (History)."

## Project Structure

```
netflix-clone
├── manage.py
├── requirements.txt
├── README.md
├── streaming
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── videos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates
    ├── base.html
    └── videos
        ├── home.html
        └── category.html
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd netflix-clone
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```
   python manage.py migrate
   ```

4. **Run the development server:**
   ```
   python manage.py runserver
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- Admin interface for managing videos, titles, and descriptions.
- User features for browsing categories: Most Popular, Latest, and Recent (History).
- Home page with a top headline for movies and a left sidebar for categories.

## License

This project is licensed under the MIT License.