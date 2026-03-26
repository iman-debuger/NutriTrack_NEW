# FIX DATABASE ERROR - DO THIS NOW

## The Problem:
```
relation "auth_user" does not exist
```

This means the database tables weren't created. Migrations didn't run properly during build.

## THE FIX - Run Migrations Manually:

### Step 1: Go to Render Shell

1. Go to: https://dashboard.render.com
2. Click your "nutritrack-new" web service
3. Click "Shell" tab (left sidebar)
4. Wait for shell to connect (takes 10-20 seconds)

### Step 2: Run These Commands

Copy and paste each command, press Enter after each:

```bash
python manage.py migrate
```

Wait for it to complete. You should see:
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  ...
  Applying tracker.0001_initial... OK
  ...
```

### Step 3: Verify Tables Created

Run this command:
```bash
python manage.py showmigrations
```

You should see all migrations with [X] marks (applied).

### Step 4: Create Superuser

```bash
python manage.py createsuperuser
```

Enter:
- Username: `admin`
- Email: (press Enter to skip)
- Password: (your choice, e.g., `admin123`)
- Password (again): (same password)

### Step 5: Test Signup

1. Go to: https://nutritrack-new.onrender.com/signup/
2. Enter username and password
3. Click "Sign Up"
4. Should work now! ✅

---

## Why This Happened:

During the build process, migrations tried to run but the database connection might have timed out or wasn't ready yet. Running migrations manually in the Shell ensures they complete successfully.

---

## After Migrations Work:

Your app will be fully functional:
- ✅ Signup works
- ✅ Login works
- ✅ All database operations work
- ✅ Admin panel accessible

---

## Quick Commands Summary:

```bash
# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Check everything is OK
python manage.py check
```

---

Do this now and your app will work perfectly! 🚀
