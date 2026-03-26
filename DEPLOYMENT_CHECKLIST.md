# Quick Deployment Checklist

## ✅ Files Ready
- [x] render.yaml - Render configuration
- [x] requirements.txt - Python dependencies
- [x] build.sh - Build script
- [x] settings.py - Updated for production
- [x] .gitignore - Ignore unnecessary files
- [x] sw.js - Service worker template

## 🚀 Deploy Now

### 1. Push to GitHub
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### 2. On Render.com

#### Create Database:
1. New + → PostgreSQL
2. Name: `nutritrack_db`
3. Plan: Free
4. Copy "Internal Database URL"

#### Create Web Service:
1. New + → Web Service
2. Connect your GitHub repo
3. Settings:
   - Build: `./build.sh`
   - Start: `gunicorn nutritrack_project.wsgi:application`
   - Plan: Free

#### Add Environment Variables:
```
PYTHON_VERSION = 3.11.0
DATABASE_URL = [paste from database]
SECRET_KEY = [generate new]
DEBUG = False
RENDER_EXTERNAL_HOSTNAME = [your-app-name].onrender.com
```

### 3. After Deployment

#### Create Admin User:
1. Go to Web Service → Shell
2. Run: `python manage.py createsuperuser`
3. Access: https://[your-app].onrender.com/admin/

#### Add Sample Food Data:
1. Login to /admin/
2. Add Nutrition Items (Apple, Banana, Rice, etc.)

## 🔍 Test Your App

Visit these URLs:
- `/` - Home page
- `/signup/` - Create account
- `/login/` - Login
- `/diary/` - Food diary
- `/profile/` - User profile
- `/analyze/` - Food analyzer
- `/trends/` - Calorie trends
- `/admin/` - Admin panel

## ⚠️ Common Issues

### 500 Error?
- Check Render logs
- Verify DATABASE_URL is set
- Ensure SECRET_KEY is generated

### Static files not loading?
- Check build logs for collectstatic errors
- Verify WhiteNoise is in MIDDLEWARE

### Slow first load?
- Normal for free tier (cold start)
- Takes 30-60 seconds after inactivity

## 📝 Notes

- Free database expires in 90 days
- Service spins down after 15 min inactivity
- First request after sleep is slow

Your app is ready to deploy! 🎉
