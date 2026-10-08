# Tejas Dixit — Personal Website

Source code for my personal website.

**Website:** https://tejasdixit.in  
**Repository:** https://github.com/PANDATD/my-site

## About

This repository contains a Flask application for my personal website, including pages for the site, portfolio/projects, contact, and user authentication.

## Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Jinja2
- SQLite
- Bootstrap/CSS and HTML templates

The exact dependency versions are listed in [requirements.txt](requirements.txt).

## Project structure

```text
.
├── app/
│   ├── auth/          # Registration, login and logout
│   ├── contact/       # Contact form
│   ├── main/          # Main site routes and portfolio content
│   ├── templates/     # Jinja templates
│   ├── static/        # CSS, images and other static files
│   ├── models.py      # SQLAlchemy models
│   └── __init__.py    # Flask application factory
├── requirements.txt
└── run.py
```

## Run locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```text
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python run.py
```

The development server runs on:

```text
http://127.0.0.1:5000
```

## Database

The current application configuration uses SQLite through Flask-SQLAlchemy.

The database URI is defined in `app/__init__.py`:

```python
sqlite:///site.db
```

## Authentication

The application includes registration, login and logout routes.

Passwords are stored using Werkzeug password hashes rather than plaintext passwords.

## Configuration

The current application configuration is defined in `app/__init__.py`. Review configuration values before using this code in another environment, particularly the Flask secret key and database configuration.

Do not commit passwords, API keys, tokens, or other credentials to the repository.

## Development notes

This README documents the repository as it exists on the `main` branch. It intentionally does not describe features, services, performance characteristics, or deployment arrangements that are not represented by the current source code.

For the published website, visit:

https://tejasdixit.in
