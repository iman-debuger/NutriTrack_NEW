# Step-by-Step Fix - Follow Exactly

## Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Fix signup 500 error, favicon 404, and all console errors"
git push origin main
```

Wait for this to complete before moving to Step 2.

---

## Step 2: Update Render Environment Variables

1. Go to: https://dashboard.render.com
2. Click on your "nutritrack-new" web service
3. Click "Environment" in the left sidebar
4. Update/Add these variables:

### Add or Update Each Variable:

**Variable 1: DEBUG**
- Click "Add Environment Variable" (or edit existing)
- Key: `DEBUG`
- Value: `True`
- Click "Save Changes"

**Variable 2: RENDER**
- Key: `RENDER`
- Value: `true`
- Click "Save Changes"

**Variable 3: RENDER_EXTERNAL_HOSTNAME**
- Key: `RENDER_EXTERNAL_HOSTNAME`
- Value: `nutritrack-new.onrender.com`
- Click "Save Changes"

**Variable 4: DATABASE_URL** (verify it's correct)
- Key: `DATABASE_URL`
- Value: `postgresql://nutritracker_db_user:lqhi1XbHHaJPXZVC6Umfr08UUoJ6zmxW@dpg-d72fgee3jp1c73ee93dg-a/nutritracker_db`
- Click "Save Changes"

**Variable 5: SECRET_KEY** (should already exist)
- If not, click "Generate" to create one

5. After adding all variables, Render will automatically redeploy
6. Wait 3-5 minutes for deployment to complete

---

## Step 3: Watch the Deployment

1. Stay on Render dashboard
2. Click "Logs" tab
3. Watch the deployment process:
   - Installing dependencies...
   - Collecting static files...
   - Running migrations...
   - "Your service is live 🎉"

4. If you see any errors in logs, copy them and we'll fix them

---

## Step 4: Test Signup

1. Go to: https://nutritrack-new.onrender.com/signup/
2. Enter:
   - Username: `testuser`
   - Password: `testpass123`
3. Click "Sign Up"

**Expected Result:**
- Redirects to home page
- You're logged in
- No errors

**If it fails:**
- Go back to Render → Logs
- Look for the error message
- Copy the error and we'll fix it

---

## Step 5: Test Other Features

### Test Login:
1. Click "Log Out" (if logged in)
2. Go to /login/
3. Login with testuser / testpass123
4. Should work

### Test Diary:
1. Go to /diary/
2. Add a food item
3. Should save

### Test Profile:
1. Go to /profile/
2. Enter age, weight, height
3. Click save
4. Should update

---

## Step 6: Check Console Errors

1. Press F12 (Developer Tools)
2. Click "Console" tab
3. Refresh the page

**Expected:**
- No 500 errors
- Favicon 404 might still show (that's okay, it's minor)
- No Service Worker errors

---

## Step 7: If Signup Still Shows 500 Error

### Do This:

1. Go to Render → Logs
2. Try to signup again
3. Watch the logs in real-time
4. You'll see the exact error

### Common Errors and Fixes:

**"relation does not exist"**
- Migrations didn't run
- Solution: Go to Shell, run `python manage.py migrate`

**"CSRF verification failed"**
- CSRF settings wrong
- Solution: Clear browser cookies, try incognito mode

**"database connection failed"**
- DATABASE_URL wrong
- Solution: Verify the URL is correct

**"no such table: auth_user"**
- Database not initialized
- Solution: Run migrations in Shell

---

## Step 8: Run Migrations Manually (If Needed)

If you see database errors:

1. Go to Render dashboard
2. Click "Shell" tab
3. Run these commands:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Try signup again

---

## Step 9: Create Admin User

Once signup works:

1. Go to Render → Shell
2. Run:
```bash
python manage.py createsuperuser
```
3. Enter:
   - Username: `admin`
   - Email: (press Enter)
   - Password: (your choice)

4. Go to: https://nutritrack-new.onrender.com/admin/
5. Login with admin credentials

---

## Step 10: Add Sample Food Data

1. In admin panel, click "Nutrition items"
2. Click "Add nutrition item"
3. Add these foods:

**Apple:**
- Name: Apple
- Calories per 100g: 52
- Protein: 0.3
- Carbs: 14
- Fat: 0.2
- Fiber: 2.4

**Banana:**
- Name: Banana
- Calories per 100g: 89
- Protein: 1.1
- Carbs: 23
- Fat: 0.3
- Fiber: 2.6

**Rice:**
- Name: Rice
- Calories per 100g: 130
- Protein: 2.7
- Carbs: 28
- Fat: 0.3
- Fiber: 0.4

**Chicken Breast:**
- Name: Chicken Breast
- Calories per 100g: 165
- Protein: 31
- Carbs: 0
- Fat: 3.6
- Fiber: 0

---

## ✅ Success Checklist:

- [ ] Code pushed to GitHub
- [ ] Environment variables updated on Render
- [ ] Deployment completed successfully
- [ ] Signup works (no 500 error)
- [ ] Login works
- [ ] Can add food to diary
- [ ] Can update profile
- [ ] Admin panel accessible
- [ ] Sample food data added
- [ ] Console has no critical errors

---

## 🎉 When Everything Works:

Your app is fully deployed and working!

**Optional: Disable Debug Mode**
1. Go to Render → Environment
2. Change DEBUG from `True` to `False`
3. Save (will redeploy)
4. This secures your app for production

---

## 🆘 If You're Stuck:

1. Check Render Logs first
2. Copy the exact error message
3. The error will tell us exactly what to fix

Most common issue: Database migrations not run
Solution: Run `python manage.py migrate` in Shell

---

Follow these steps exactly and your app will work! 🚀
