# NutriTrack - Quick Start Guide

## 🚀 Run Locally (Windows PowerShell)

### Option 1: Run All Commands Together
```powershell
pip install -r requirements.txt; python manage.py migrate; python manage.py runserver
```

### Option 2: Run Commands Separately
```powershell
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run migrations
python manage.py migrate

# Step 3: Start server
python manage.py runserver
```

### Access the Application
- Open browser: http://127.0.0.1:8000/
- Landing page will load automatically
- Click "Get Started" to create an account

## 📱 Features to Test

1. **Landing Page** - http://127.0.0.1:8000/
   - Professional design with animations
   - iOS Blue theme (#007aff)
   - Download buttons

2. **Sign Up** - http://127.0.0.1:8000/signup/
   - Create new account
   - Automatic login after signup

3. **Dashboard** - http://127.0.0.1:8000/dashboard/
   - BMI calculator
   - Health metrics
   - Calorie recommendations

4. **Food Diary** - http://127.0.0.1:8000/diary/
   - Log meals
   - Track calories
   - View daily totals

5. **Profile** - http://127.0.0.1:8000/profile/
   - Save personal metrics
   - View daily/monthly calories
   - Health targets

6. **Trends** - http://127.0.0.1:8000/trends/
   - 7-day calorie chart
   - Average calculations
   - Visual analytics

7. **AI Analyze** - http://127.0.0.1:8000/analyze/
   - Upload food images
   - AI recognition
   - Nutritional breakdown

8. **Windows Download** - http://127.0.0.1:8000/download/windows/
   - Downloads NutriTrack.exe
   - Desktop application

## 🔧 Troubleshooting

### PowerShell Error: "The token '&&' is not a valid statement separator"
**Solution:** Use semicolons (;) instead of && in PowerShell
```powershell
# ❌ Wrong (bash syntax)
pip install -r requirements.txt && python manage.py migrate

# ✅ Correct (PowerShell syntax)
pip install -r requirements.txt; python manage.py migrate
```

### Database Error: "no such table"
**Solution:** Run migrations
```powershell
python manage.py migrate
```

### Port Already in Use
**Solution:** Use different port
```powershell
python manage.py runserver 8080
```

## 🌐 Deploy to Render

### Prerequisites
1. Push code to GitHub
2. Create Render account
3. Create PostgreSQL database on Render

### Deployment Steps
1. Go to Render Dashboard
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure settings:
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn nutritrack_project.wsgi:application`
   - **Environment Variables:**
     - `DATABASE_URL`: Your PostgreSQL URL
     - `SECRET_KEY`: Generate random key
     - `DEBUG`: True (for testing, False for production)
     - `RENDER_EXTERNAL_HOSTNAME`: your-app.onrender.com
     - `PYTHON_VERSION`: 3.11.0

5. Click "Create Web Service"
6. Wait for deployment to complete
7. Access your app at: https://your-app.onrender.com

## 📝 Important Notes

- **Build Command MUST be:** `./build.sh` (not `pip install -r requirements.txt`)
- The build script handles migrations automatically
- Static files are collected during build
- Database connection has retry logic
- Windows app is available for download

## ✅ Verification Checklist

After starting the server, verify:
- [ ] Landing page loads without errors
- [ ] No console errors in browser
- [ ] Signup creates new user
- [ ] Login works correctly
- [ ] Dashboard shows BMI calculator
- [ ] Food diary logs meals
- [ ] Profile saves data
- [ ] Trends shows chart
- [ ] Windows download works
- [ ] All animations smooth

## 🎨 Design Features

- **Color Scheme:** iOS Blue (#007aff)
- **Animations:** Smooth transitions and floating particles
- **Responsive:** Works on mobile and desktop
- **Modern:** Clean, professional design
- **Fast:** Optimized performance

## 📞 Support

If you encounter any issues:
1. Check TEST_RESULTS.md for detailed analysis
2. Review error messages in terminal
3. Check browser console for JavaScript errors
4. Verify all migrations ran successfully

---

**Ready to go!** Run the commands above and start tracking your nutrition! 🎉
