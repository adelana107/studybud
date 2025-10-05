# StudyBud 🎓

A simple Django-based study management platform that helps users organize, track, and manage study materials efficiently.

---

## 📚 Overview
**StudyBud** is a web app built with **Django** that provides a digital environment for learners to collaborate, create study rooms, share resources, and track study progress.  
It allows users to log in, join discussions, and access topics across different subjects.

---

## 🚀 Features
- 🔐 User authentication (Register, Login, Logout)
- 💬 Create and join study rooms
- 🗂️ Manage study topics and messages
- 🧾 CRUD operations for rooms and discussions
- 🕹️ Responsive user interface using HTML & CSS
- 🧩 SQLite database for development
- 🛠️ Django admin dashboard support

---

## 🧱 Project Structure


studybud/
├── static/ # Static files (CSS, JS, images)
├── templates/ # HTML templates
├── studybud/ # Django app source code (models, views, urls)
├── db.sqlite3 # Local database
├── manage.py # Django project manager
└── .hintrc # HTMLHint configuration file



---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/adelana107/studybud.git
cd studybud


2️⃣ Create and activate a virtual environment

Windows

python3 -m venv env
source env/bin/activate

Mac/Linux

python3 -m venv env
source env/bin/activate

3️⃣ Install dependencies

If a requirements.txt file exists:

pip install -r requirements.txt


Otherwise, install Django manually:

pip install django

4️⃣ Run database migrations
python manage.py migrate

5️⃣ Create an admin superuser (optional)
python manage.py createsuperuser

6️⃣ Start the development server
python manage.py runserver

7️⃣ Open in your browser

Go to:

http://127.0.0.1:8000/

🎯 Usage

Once the server is running:

Register a new account or log in

Create or join study rooms

Post and reply to messages in rooms

Manage topics and room visibility

Explore the admin dashboard (/admin) if you’re a superuser

🧰 Built With

Python 3

Django Framework

SQLite Database

HTML, CSS, JavaScript

Git & GitHub

HTMLHint for linting (.hintrc)

🧪 Testing & Debugging

Run the server in debug mode:

python manage.py runserver --settings=studybud.settings


Use Django’s admin panel to inspect models and data

Check browser console for frontend issues

Use print() or Django logging for backend debugging

🧳 Deployment (Optional)

To deploy your app:

Set DEBUG = False in settings.py

Add your production domain to ALLOWED_HOSTS

Use PostgreSQL or MySQL for production

Configure static files with WhiteNoise or a CDN

Deploy with Gunicorn and Nginx or a platform like Render, Railway, or Heroku

👨🏽‍💻 Contributing

Contributions are welcome! Follow these steps:

Fork this repository

Create a new branch (git checkout -b feature-name)

Make your changes and commit (git commit -m "Added feature X")

Push to your branch (git push origin feature-name)

Create a Pull Request

📜 License

This project is licensed under the MIT License.
You’re free to use, modify, and distribute it with proper attribution.

✨ Author

Adelana Oluwafunmibi
GitHub Profile

🌟 Acknowledgements

Thanks to the Django community and open-source contributors who made frameworks and tools that power this project possible.
