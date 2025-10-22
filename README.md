<h1 align="center">🔐 Django Authentication System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.2.7-brightgreen?style=for-the-badge&logo=django" alt="Django Badge" />
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap" alt="Bootstrap Badge" />
</p>

<p align="center">
  A complete <b>Django Authentication System</b> with custom email verification, password reset functionality, and a beautiful glassmorphic UI 💎
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🪪 User Registration and Login using Django’s built-in <code>auth</code> system</li>
  <li>📨 Email verification and password reset with HTML email templates</li>
  <li>💎 Glassmorphic and responsive UI design for all auth pages</li>
  <li>📋 Floating Django messages without moving form elements</li>
  <li>⚙️ Clean modular structure (base template + page-specific templates)</li>
  <li>🔒 Secure token-based password reset URLs</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
auth_system/
├── auth_app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── password_reset.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_confirm.html
│   │   │   └── password_reset_complete.html
│   │   └── emails/
│   │       ├── verification_email.html
│   │       └── reset_password_email.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── models.py
├── manage.py
└── README.md
</pre>

<hr>

<h2>⚙️ Setup & Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/django-auth-system.git</code></pre>
  </li>
  <li>Move into the project directory:
    <pre><code>cd django-auth-system</code></pre>
  </li>
  <li>Create and activate a virtual environment:
    <pre><code>python -m venv venv
venv\Scripts\activate  # for Windows
source venv/bin/activate  # for macOS/Linux</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Apply migrations:
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li>Run the server:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>Visit: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></li>
</ol>

<hr>

<h2>💌 Email Configuration</h2>

<p>To enable email verification and password reset, configure your <code>settings.py</code> as follows:</p>

<pre><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
</code></pre>

<hr>

<h2>🎨 UI Preview</h2>

<p align="center">
  <img src="https://github.com/yourusername/django-auth-system/blob/main/screenshots/login_page.png" width="45%" alt="Login Page" />
  <img src="https://github.com/yourusername/django-auth-system/blob/main/screenshots/register_page.png" width="45%" alt="Register Page" />
</p>

<p align="center">
  <img src="https://github.com/yourusername/django-auth-system/blob/main/screenshots/password_reset_email.png" width="70%" alt="Password Reset Email" />
</p>

<hr>

<h2>🧠 Tech Stack</h2>
<ul>
  <li><b>Backend:</b> Django (Python)</li>
  <li><b>Frontend:</b> HTML, CSS, Bootstrap 5</li>
  <li><b>Database:</b> SQLite (default) or PostgreSQL</li>
  <li><b>Email Service:</b> Gmail SMTP</li>
</ul>

<hr>

<h2>🚀 Key Highlights</h2>
<ul>
  <li>✅ Responsive design with glassmorphic containers</li>
  <li>✅ Floating messages without form overlap</li>
  <li>✅ Secure password reset and email links using Django tokens</li>
  <li>✅ Organized template structure for scalability</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Want to improve this project? Fork it, make your changes, and open a pull request!</p>

<pre><code>git clone https://github.com/yourusername/django-auth-system.git
git checkout -b feature-name
git commit -m "Add new feature"
git push origin feature-name
</code></pre>

<hr>

<h2>📜 License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>

<hr>

<h2 align="center">⭐ Star this repo if you like the project!</h2>
<p align="center">Your support motivates me to build more projects like this 🚀</p>
