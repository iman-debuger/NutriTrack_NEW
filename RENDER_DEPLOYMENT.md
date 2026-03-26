# Complete Render Deployment Guide for NutriTrack

## Step 1: Prepare Your Code

All files are now configured. Make sure you have:
- ✅ render.yaml
- ✅ requirements.txt
- ✅ build.sh
- ✅ Updated settings.py
- ✅ .gitignore

## Step 2: Push to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit changes
git commit -m "Configure for Render deployment"

# Create main branch
git branch -M main

# Add your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git push -u origin main
```

## Step 3: Create Render Account

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub
4. Authorize Render to access your repositories

## Step 4: Create PostgreSQL Database

1. In Render Dashboard, click "New +" → "PostgreSQL"
2. Fill in:
   - Name: `nutritrack_db`
   - Database: `nutritrack_db`
   - User: `nutritrack_user`
   - Region: Choose closest to you (e.g., Oregon, Frankfurt)
   - PostgreSQL Version: 16 (latest)
   - Plan: **Free**
3. Click "Create Database"
4. Wait 1-2 minutes for provisioning
5. **IMPORTANT**: Copy the "Internal Database URL" - you'll need this!

## Step 5: Create Web Service

1. Click "New +" → "Web Service"
2. Click "Connect a repository"
3. Find and select your `nutritrack` repository
4. Configure the service:

### Basic Settings:
- **Name**: `nutritrack-new` (or any unique name)
- **Region**: Same as your database
- **Branch**: `main`
- **Root Directory**: (leave blank)
- **Runtime**: Python 3
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn nutritrack_project.wsgi:application`

### Instance Type:
- **Plan**: Free

## Step 6: Add Environment Variables

Click "Advanced" → "Add Environment Variable" and add these:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `DATABASE_URL` | Paste the Internal Database URL from Step 4 |
| `SECRET_KEY` | Click "Generate" or use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `RENDER_EXTERNAL_HOSTNAME` | `nutritrack-new.onrender.com` (use your actual service name) |

## Step 7: Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies
   - Run migrations
   - Collect static files
   - Start the server

3. Watch the logs for any errors
4. First deployment takes 5-10 minutes

## Step 8: Verify Deployment

1. Once deployed, click the URL (e.g., https://nutritrack-new.onrender.com)
2. You should see your home page
3. Test these pages:
   - `/` - Home
   - `/signup/` - Sign up
   - `/login/` - Login
   - `/diary/` - Food diary
   - `/admin/` - Django admin

## Step 9: Create Superuser (Admin Access)

You need to run this command in Render's Shell:

1. Go to your Web Service dashboard
2. Click "Shell" tab on the left
3. Run:
```bash
python manage.py createsuperuser
```
4. Enter username, email (optional), and password
5. Now you can access `/admin/` with these credentials

## Step 10: Add Sample Data

1. Go to https://nutritrack-new.onrender.com/admin/
2. Login with superuser credentials
3. Add some NutritionItems:
   - Click "Nutrition items" → "Add"
   - Example: Name: "Apple", Calories: 52, Protein: 0.3, Carbs: 14, Fat: 0.2, Fiber: 2.4
   - Add more foods as needed

## Troubleshooting

### Error 500 - Server Error
Check Render logs:
1. Go to your Web Service
2. Click "Logs" tab
3. Look for Python errors

Common fixes:
- Ensure DATABASE_URL is set correctly
- Verify SECRET_KEY is generated
- Check RENDER_EXTERNAL_HOSTNAME matches your URL

### Static Files Not Loading
1. Check build logs for collectstatic errors
2. Verify STATICFILES_DIRS in settings.py
3. Ensure WhiteNoise is in MIDDLEWARE

### Database Connection Failed
1. Verify DATABASE_URL is the "Internal Database URL"
2. Check database is in same region as web service
3. Ensure database is running (not suspended)

### Cold Start (Slow First Load)
- Free tier spins down after 15 minutes
- First request takes 30-60 seconds
- This is normal for free tier

## Important Notes

### Free Tier Limitations:
- Database: 90 days free trial, then expires
- Web Service: Spins down after 15 minutes of inactivity
- 750 hours/month of runtime
- 1GB database storage
- No custom domain on free tier

### Before Database Expires (90 days):
1. Export your data:
```bash
python manage.py dumpdata > backup.json
```
2. Either upgrade to paid tier or migrate to another service

### Keeping Service Awake:
Use a service like UptimeRobot to ping your URL every 5 minutes (prevents spin-down)

## Success Checklist

- ✅ Database created and running
- ✅ Web service deployed successfully
- ✅ Environment variables set
- ✅ Home page loads without errors
- ✅ Can sign up and login
- ✅ Can access admin panel
- ✅ Static files loading correctly
- ✅ Database queries working

Your Django app is now live on Render! 🎉
