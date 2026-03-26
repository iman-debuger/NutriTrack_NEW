# Your NutriTrack Deployment Steps

## ✅ Database Already Created!
Your database is ready:
- URL: `postgresql://nutritracker_db_user:lqhi1XbHHaJPXZVC6Umfr08UUoJ6zmxW@dpg-d72fgee3jp1c73ee93dg-a/nutritracker_db`

## 🚀 Deploy Your Web Service Now

### Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Configure for Render deployment"
git push origin main
```

### Step 2: Create Web Service on Render

1. Go to: https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Click "Connect a repository"
4. Select your repository

### Step 3: Configure Web Service

Fill in these settings:

**Basic:**
- Name: `nutritrack-new` (or any name you want)
- Region: **Same region as your database** (check your database page)
- Branch: `main`
- Root Directory: (leave blank)
- Runtime: `Python 3`
- Build Command: `./build.sh`
- Start Command: `gunicorn nutritrack_project.wsgi:application`
- Instance Type: `Free`

### Step 4: Add Environment Variables

Click "Advanced" → "Add Environment Variable"

Add these 5 variables:

**Variable 1:**
```
Key: PYTHON_VERSION
Value: 3.11.0
```

**Variable 2:**
```
Key: DATABASE_URL
Value: postgresql://nutritracker_db_user:lqhi1XbHHaJPXZVC6Umfr08UUoJ6zmxW@dpg-d72fgee3jp1c73ee93dg-a/nutritracker_db
```

**Variable 3:**
```
Key: SECRET_KEY
Value: [Click "Generate" button]
```

**Variable 4:**
```
Key: DEBUG
Value: False
```

**Variable 5:**
```
Key: RENDER_EXTERNAL_HOSTNAME
Value: nutritrack-new.onrender.com
(use whatever name you chose in Step 3)
```

### Step 5: Deploy!

1. Click "Create Web Service"
2. Wait 5-10 minutes for deployment
3. Watch the logs for any errors
4. Once you see "Your service is live 🎉", click the URL

### Step 6: Create Admin User

1. In your Web Service dashboard, click "Shell" (left sidebar)
2. Run this command:
```bash
python manage.py createsuperuser
```
3. Enter:
   - Username: `admin`
   - Email: (press Enter to skip)
   - Password: (type your password)
   - Password (again): (confirm)

### Step 7: Add Food Data

1. Go to: `https://[your-app-name].onrender.com/admin/`
2. Login with admin credentials
3. Click "Nutrition items" → "Add nutrition item"
4. Add some foods:

**Example Foods:**
```
Apple: 52 cal, 0.3g protein, 14g carbs, 0.2g fat, 2.4g fiber
Banana: 89 cal, 1.1g protein, 23g carbs, 0.3g fat, 2.6g fiber
Chicken Breast: 165 cal, 31g protein, 0g carbs, 3.6g fat, 0g fiber
Rice: 130 cal, 2.7g protein, 28g carbs, 0.3g fat, 0.4g fiber
Egg: 155 cal, 13g protein, 1.1g carbs, 11g fat, 0g fiber
```

### Step 8: Test Your App

Visit these pages:
- `/` - Home page
- `/signup/` - Create account
- `/login/` - Login
- `/diary/` - Food diary
- `/profile/` - Profile
- `/trends/` - Trends
- `/analyze/` - Food analyzer

## 🎉 Done!

Your app should now be live at:
`https://[your-app-name].onrender.com`

## ⚠️ Important Notes

1. **First load is slow** - Free tier spins down after 15 min
2. **Database expires in 90 days** - Backup your data!
3. **Auto-deploy** - Push to GitHub = auto-deploy

## 🐛 Troubleshooting

**500 Error?**
- Check Logs tab in Render dashboard
- Verify DATABASE_URL is correct
- Ensure SECRET_KEY is generated

**Static files not loading?**
- Check build logs
- Verify collectstatic ran successfully

**Can't connect to database?**
- Make sure web service and database are in same region
- Use Internal Database URL (not External)

---

Need help? Check the Render logs first!
