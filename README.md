# 🧠 StudyBud

StudyBud is a full-featured **Django web application** that allows users to create and join study rooms, chat in real time, and collaborate with others around shared topics.  
It’s designed as a learning and discussion platform for students and developers to share ideas and resources.

---

## 🚀 Features

✅ **User Authentication**
- Register, login, and logout functionality (custom user model with email authentication)  
- Profile management with editable user details and avatars  

✅ **Rooms and Topics**
- Create, edit, or delete study rooms  
- Organize rooms by topics  
- Dynamic topic search and filtering  

✅ **Discussions**
- Send and delete messages inside a room  
- See recent activity across rooms  
- Automatically add participants to a room upon message  

✅ **Responsive UI**
- Clean layout using Django templates and static files (HTML, CSS, JS)

---

## 🏗️ Tech Stack

**Backend:**  
- Django  
- Python  

**Frontend:**  
- HTML5  
- CSS3  

**Database:**  
- SQLite (default)  
- Easily configurable to PostgreSQL or MySQL  

**Authentication:**  
- Django’s built-in auth system  
- Custom `MyUserCreationForm` and `UserForm` for profile handling  

---

## 📂 Project Structure

studybud/
│
├── base/
│ ├── templates/
│ │ ├── home.html
│ │ ├── room.html
│ │ ├── profile.html
│ │ ├── topics.html
│ │ ├── activity.html
│ │ ├── login_register.html
│ │ └── delete.html
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── studybud/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── requirements.txt

yaml


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/adelana107/studybud.git
cd studybud
2️⃣ Create a virtual environment
bash

python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux
3️⃣ Install dependencies
bash

pip install -r requirements.txt
4️⃣ Run migrations
bash

python manage.py makemigrations
python manage.py migrate
5️⃣ Start the development server
bash

python manage.py runserver
Now open your browser and go to:
👉 http://127.0.0.1:8000/

🔐 Default Pages
Page	URL	Description
Home	/	Lists all rooms and topics
Room	/room/<id>/	View a specific study room
Login	/login/	User login page
Register	/register/	User sign-up page
Profile	/profile/<id>/	User profile with rooms and messages
Topics	/topics/	Browse all available topics
Activity	/activity/	View all recent messages

🧑‍💻 Author
Adelana Oluwafunmibi
💼 GitHub Profile
📧 You can fork, star, or contribute to this project to improve it.

⭐ Future Improvements
Add real-time chat with WebSockets (via Django Channels)

Add notifications and private messaging

Add profile pictures using Cloudinary or AWS S3

Implement user search and following system


🪪 License

This project is open source and available under the MIT License
.

🏁 Quick Demo

Coming soon — screenshots or hosted version can be added here!
