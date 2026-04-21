# Prince Ngonyama | Cybersecurity Portfolio

**[LIVE DEMO](https://prince-portfolio-tgs7.onrender.com)**

A high-performance, terminal-themed personal portfolio showcasing my journey as a Computer Science student and Ethical Hacker. Built with a Django backend and an interactive React frontend.

---

## Overview

This project serves as a centralized hub for my professional identity. It’s not just a static site; it's a hybrid architecture designed to be secure, scalable, and visually representative of the cybersecurity field.

### Key Features:

* **Interactive Terminal:** A custom-built React terminal component that supports functional commands (e.g., `about`, `projects`, `clear`).
* **Cyber-Aesthetic UI:** Dark-mode focused design using Tailwind CSS with glassmorphism and circuit-pattern overlays.
* **Hybrid Architecture:** Django handles the heavy lifting (server-side rendering, static file management via WhiteNoise), while React manages the dynamic UI.
* **Production Grade:** Deployed on Render with a serverless PostgreSQL database (Neon).

---

## Technology Stack

| Component        | Technology                |
| :--------------- | :------------------------ |
| **Frontend**     | React (SPA), Tailwind CSS |
| **Backend**      | Django (Python 3.11)      |
| **Database**     | PostgreSQL (Neon.tech)    |
| **Static Files** | WhiteNoise                |
| **Deployment**   | Render.com                |

---

## System Architecture

The site uses a **"Template-Injection"** approach where Django serves a single-page React application through its templating engine. This allows for:

1. **Fast Loading:** Compressed static assets served via WhiteNoise.
2. **Scalability:** Easy migration to a full REST API if I decide to move project data to the database.
3. **Security:** Django’s built-in CSRF and security headers are active.

---

## Getting Started (Local Dev)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Blackout-26/my_portfolio_website.git
   cd portfolio_backend
   ```

2. **Setup Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Run Migrations & Server:**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## Security Audit

As an Ethical Hacker, this site is built with a focus on security:

* **Environment Isolation:** No secrets are hardcoded; all keys are managed via `.env`.
* **Secure Headers:** Configured for production deployment with `DEBUG=False`.
* **Dependency Scanning:** Regular audits of Python packages to prevent supply chain vulnerabilities.

---

## Connect With Me

* **LinkedIn:** Prince Ngonyama
* **GitHub:** @Blackout-26
