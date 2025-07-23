# Tejas's Flask Website

A clean, minimalist, SEO-friendly, and mobile-first portfolio website built using **Flask** and **Bootstrap 5**.  
This project demonstrates best practices in performance optimization, accessibility, and modern web development.

---

## 🚀 Features

- Flask 2.x web framework
- Bootstrap 5 responsive layout
- Google Fonts (Inter) for modern typography
- Font Awesome 6 icons
- SEO optimized meta tags (Open Graph, Twitter Cards, Structured Data)
- Accessible with ARIA roles and keyboard navigation support
- Clean `base.html` for easy template inheritance
- Custom `404` error page
- Simple CSS for clarity and readability
- Pre-configured for Core Web Vitals performance

---

## 📂 Project Structure

```bash

/your_flask_app/
├── static/
│ ├── css/
│ │ └── styles.css
│ └── images/
│ ├── og-image.jpg
│ └── favicon.svg
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ ├── projects.html
│ ├── contact.html
│ ├── privacy.html
│ └── 404.html
│
├── app.py
└── requirements.txt
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt