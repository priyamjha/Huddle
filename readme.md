```markdown
# 💬 Huddle - Real-time Chat App (Django + Tailwind)

Huddle is a simple **chatroom application** built with **Django** and **Tailwind CSS**.  
Users can join a chatroom using a unique **huddle key** and exchange messages.  
Messages are stored in the database, displayed in a scrollable chat box, and notifications can be sent via email.

---

## 🚀 Features

- Join or create a **Huddle (chatroom)** using a key.
- Post and display **real-time chat messages** with user & timestamp.
- Scrollable chat message box (latest messages always accessible).
- User-friendly **Tailwind CSS UI**.
- Email notifications for new messages.
- Automatic cleanup of **old huddles** (24+ hours inactivity).

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: SQLite (default, can switch to Postgres/MySQL)
- **Email Service**: Django `send_mail`

---

## 📂 Project Structure

```

huddle\_project/
│
├── huddle/                # Main Django app
│   ├── models.py          # Huddle & Item models
│   ├── forms.py           # ItemForm (message form)
│   ├── views.py           # Views (index, huddle)
│   ├── utilities.py       # Email notifications + cleanup
│   ├── templates/huddle/  # HTML templates
│   ├── urls.py
│
├── huddle\_project/        # Django project configs
│   ├── settings.py
│   ├── urls.py
│
└── manage.py

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/priyamjha/Huddle.git
   cd huddle
````

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv env
   source env/bin/activate    # (Linux/Mac)
   env\Scripts\activate       # (Windows)

   pip install django
   ```

3. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

4. **Run development server**

   ```bash
   python manage.py runserver
   ```

5. Open in browser:
   👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✨ Usage

1. Go to the homepage and **enter your email + huddle key**.
2. If the huddle key doesn’t exist, a new huddle is created.
3. Send messages in the chatbox (they appear instantly in the scrollable area).
4. All users in the huddle get **email notifications**.

---

## 📧 Email Setup

Configure your email in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## 🧹 Auto Cleanup

* Huddles older than **24 hours** are automatically removed by the utility function `remove_old_huddles()`.

---

## 🔮 Future Improvements

* Real-time updates with **WebSockets (Django Channels)**.
* User authentication system.
* Typing indicators & read receipts.
* File & image sharing.

---