# Setup Guide for Developers

## 🚨 If You Get Git Merge Errors:

If you see this error when pulling:
```
error: The following untracked working tree files would be overwritten by merge:
  .gitignore
  tracker/templates/tracker/sw.js
Please move or remove them before you merge.
```

### Solution:

**Option 1: Backup and Remove (Safest)**
```bash
# Backup your local changes
cp .gitignore .gitignore.backup
cp tracker/templates/tracker/sw.js tracker/templates/tracker/sw.js.backup

# Remove the conflicting files
rm .gitignore
rm tracker/templates/tracker/sw.js

# Now pull
git pull origin main
```

**Option 2: Force Pull (If you don't have local changes)**
```bash
git fetch origin
git reset --hard origin/main
```

**Option 3: Stash Local Changes**
```bash
git stash
git pull origin main
git stash pop
```

---

## 📋 Complete Setup Instructions:

### Step 1: Clone the Repository

```bash
git clone https://github.com/iman-debuger/NutriTrack_NEW.git
cd NutriTrack_NEW
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup Database

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 🔧 Common Issues & Solutions:

### Issue 1: ModuleNotFoundError: No module named 'dj_database_url'

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 2: Database errors

**Solution:**
```bash
python manage.py migrate
```

### Issue 3: Static files not loading

**Solution:**
```bash
python manage.py collectstatic --no-input
```

### Issue 4: Git merge conflicts

**Solution:**
```bash
# Save your work
git stash

# Pull latest changes
git pull origin main

# Restore your work
git stash pop

# Resolve any conflicts manually
```

---

## 📁 Project Structure:

```
NutriTrack_NEW/
├── nutritrack_project/      # Django project settings
│   ├── settings.py          # Main settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI config
├── tracker/                 # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URLs
│   ├── templates/           # HTML templates
│   │   └── tracker/
│   │       ├── landing.html # Landing page
│   │       ├── base.html    # Base template
│   │       ├── home.html    # Dashboard
│   │       └── ...
│   └── static/              # Static files
│       └── tracker/
│           └── css/
├── manage.py                # Django management
├── requirements.txt         # Python dependencies
├── build.sh                 # Render build script
└── .gitignore              # Git ignore rules
```

---

## 🌐 Environment Variables:

For local development, create a `.env` file (optional):

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

For production (Render), these are set in the dashboard.

---

## 🧪 Testing:

### Run Tests:
```bash
python manage.py test
```

### Check for Issues:
```bash
python manage.py check
```

### Create Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📦 Dependencies:

All dependencies are in `requirements.txt`:
- Django 4.2+
- psycopg2-binary (PostgreSQL)
- gunicorn (Production server)
- whitenoise (Static files)
- dj-database-url (Database config)

---

## 🚀 Deployment:

See `RENDER_DEPLOYMENT.md` for complete deployment instructions.

---

## 🆘 Getting Help:

1. Check the error message carefully
2. Search the issue in project documentation
3. Check Django documentation
4. Ask the team

---

## ✅ Checklist Before Committing:

- [ ] Code runs without errors locally
- [ ] All tests pass
- [ ] Migrations created if models changed
- [ ] No sensitive data in code
- [ ] Code follows project style
- [ ] Commit message is clear

---

## 🔄 Workflow:

### Daily Workflow:
```bash
# 1. Pull latest changes
git pull origin main

# 2. Create a branch for your feature
git checkout -b feature/your-feature-name

# 3. Make your changes
# ... code ...

# 4. Test your changes
python manage.py runserver

# 5. Commit your changes
git add .
git commit -m "Add: your feature description"

# 6. Push your branch
git push origin feature/your-feature-name

# 7. Create a Pull Request on GitHub
```

### Before Pushing:
```bash
# Check for errors
python manage.py check

# Run migrations
python manage.py migrate

# Test locally
python manage.py runserver
```

---

## 📝 Notes:

- Always work in a virtual environment
- Never commit `db.sqlite3` or `.env` files
- Keep `requirements.txt` updated
- Test before pushing
- Write clear commit messages

---

Happy coding! 🎉
