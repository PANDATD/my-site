# Application

This directory contains the Flask application used by the personal website.

## Main components

- `__init__.py` — Flask application factory, database and login manager setup.
- `auth/` — registration, login and logout routes.
- `contact/` — contact form routes and forms.
- `main/` — main site routes and portfolio content.
- `models.py` — SQLAlchemy models.
- `templates/` — Jinja templates.
- `static/` — static assets.

## Run the application

Run these commands from the repository root:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

On Windows, activate the environment with `venv\Scripts\activate`.

See the repository root `README.md` for the complete setup guide.
