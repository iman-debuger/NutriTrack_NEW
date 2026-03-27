# NutriTrack - AI-Powered Nutrition Tracking

![NutriTrack](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Overview

NutriTrack is a modern, AI-powered nutrition tracking application that helps users monitor their diet, track calories, and achieve their health goals. Built with Django and featuring a beautiful, responsive UI.

## ✨ Features

- 🤖 **AI Food Recognition** - Identify food from photos
- 📊 **Smart Analytics** - Track progress with beautiful charts
- 📝 **Food Diary** - Log meals effortlessly
- 💪 **Health Metrics** - Monitor BMI, calories, macros
- 💻 **Desktop App** - Windows application available
- ☁️ **Cloud Sync** - Access data across devices
- 📱 **Responsive Design** - Works on mobile and desktop

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/iman-debuger/NutriTrack_NEW.git
cd NutriTrack_NEW
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Visit** http://127.0.0.1:8000/

## 📁 Project Structure

```
NutriTrack_NEW/
├── nutritrack_project/     # Django project settings
├── tracker/                # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── templates/         # HTML templates
│   └── static/            # Static files (CSS, JS)
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
└── README.md             # This file
```

## 🌐 Deployment

### Deploy to Render

1. Push code to GitHub
2. Connect repository to Render
3. Set environment variables:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `DEBUG=False`
   - `RENDER_EXTERNAL_HOSTNAME`
4. Deploy!

See `RENDER_DEPLOYMENT.md` for detailed instructions.

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render
- **Server**: Gunicorn
- **Static Files**: WhiteNoise

## 📖 Documentation

- [Setup for Developers](SETUP_FOR_DEVELOPERS.md)
- [Render Deployment Guide](RENDER_DEPLOYMENT.md)
- [Professional Website Guide](PROFESSIONAL_WEBSITE_COMPLETE.md)
- [Fix Git Errors](FIX_GIT_ERROR.md)

## 🐛 Troubleshooting

### Git Merge Error

If you see "untracked working tree files would be overwritten":
```bash
git stash
git pull origin main
```

See [FIX_GIT_ERROR.md](FIX_GIT_ERROR.md) for details.

### Module Not Found

```bash
pip install -r requirements.txt
```

### Database Errors

```bash
python manage.py migrate
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👥 Authors

- **Iman** - [GitHub](https://github.com/iman-debuger)

## 🙏 Acknowledgments

- Django Documentation
- Render Platform
- Font Awesome Icons
- All contributors

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ by the NutriTrack Team
