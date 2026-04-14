# 🛡️ My Cybersecurity & Tech Portfolio

This is the backend repository for my personal portfolio website. It serves as a central hub to showcase my certifications, technical projects, and career progress in **Cybersecurity** and **Programming**.

As I continue to gain certifications (Cisco, Ethical Hacking) and build new tools, this platform allows me to dynamically update my skills and showcase my growth.

## 🚀 Tech Stack
* **Backend Framework:** Django 5.x (Python)
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (Development) / MySQL (Production ready)
* **Security:** Environment variable management via `python-dotenv`
* **Features:**
    * **Dynamic Certification Showcase:** Renders badge images and metadata from the backend.
    * **Secure Contact API:** Integrated with Gmail SMTP for secure email delivery.
    * **Production Ready Settings:** Configured to switch safely between Debug and Production modes.

## 📈 Project Goals
This project is built to be a "living document." Unlike a static PDF resume, this site allows me to:
1.  Instantly upload new credentials (like my Cisco & Ethical Hacking badges).
2.  Demonstrate my ability to build and deploy secure web applications.
3.  Provide a direct, secure line of communication via the API contact form.

## 🔧 Setup (Run it locally)
If you want to view this code or run it on your own machine:

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/Blackout-26/my_portfolio_website.git](https://github.com/Blackout-26/my_portfolio_website.git)
    cd my_portfolio_website
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment:**
    Create a `.env` file in the root folder and add the following:
    ```
    SECRET_KEY=your_secret_key
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_app_password
    ```
5.  **Run Server:**
    ```bash
    python manage.py runserver
    ```

---
*Created by Prince Ngonyama - Aspiring Cybersecurity Professional*