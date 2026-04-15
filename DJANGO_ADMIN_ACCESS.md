# Django Admin Access Guide

## 🔐 Creating Admin Account

Django doesn't have a default admin password. You need to create a superuser account.

### Step 1: Create Superuser

```powershell
python manage.py createsuperuser
```

### Step 2: Enter Details

The command will prompt you for:

```
Username: admin
Email address: (press Enter to skip or enter your email)
Password: (enter your password - won't show on screen)
Password (again): (re-enter password)
```

**Example:**
```
Username: admin
Email address: admin@nutritrack.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### Step 3: Access Admin Panel

1. Start server:
   ```powershell
   python manage.py runserver
   ```

2. Open browser:
   ```
   http://127.0.0.1:8000/admin/
   ```

3. Login with credentials you just created:
   - Username: admin
   - Password: (your password)

## 📊 What You Can Do in Admin

Once logged in, you can:

### 1. Manage Users
- View all registered users
- Create new users
- Edit user details
- Delete users

### 2. Manage Food Database (Nutrition Items)
- View all 70 food items
- Add new foods
- Edit existing foods
- Delete foods
- Search foods

### 3. Manage Food Logs
- View all user food entries
- See what users are eating
- Edit/delete entries

### 4. Manage User Profiles
- View user health metrics
- Edit age, height, weight
- See BMI calculations

### 5. Manage Weight Logs
- Track weight changes over time

## 🎯 Quick Admin Tasks

### Add a New Food Item

1. Go to: http://127.0.0.1:8000/admin/
2. Click "Nutrition items"
3. Click "Add nutrition item" (top right)
4. Fill in:
   - Name: "Chocolate"
   - Calories per 100g: 546
   - Protein: 5
   - Carbs: 61
   - Fat: 31
   - Fiber: 7
5. Click "Save"

### View All Foods

1. Go to: http://127.0.0.1:8000/admin/
2. Click "Nutrition items"
3. See list of all 70 foods
4. Use search box to find specific foods

### View User Activity

1. Go to: http://127.0.0.1:8000/admin/
2. Click "Food logs"
3. See what users have logged
4. Filter by user or date

## 🔧 Troubleshooting

### Forgot Admin Password?

Reset it:
```powershell
python manage.py changepassword admin
```

Then enter new password twice.

### Create Another Admin User

```powershell
python manage.py createsuperuser
```

Use different username (e.g., "admin2", "superadmin", etc.)

### Can't Access Admin Panel?

Check:
1. Server is running: `python manage.py runserver`
2. URL is correct: `http://127.0.0.1:8000/admin/`
3. Superuser was created successfully
4. Using correct username and password

## 📝 Recommended Admin Credentials

For development, you can use:
- **Username:** admin
- **Password:** admin123 (or something you'll remember)
- **Email:** admin@nutritrack.com

⚠️ **For production (Render), use a strong password!**

## 🚀 Admin on Render

To create admin on Render (production):

### Option 1: Via Shell (Requires Paid Plan)
Render free tier doesn't have shell access.

### Option 2: Create During Build
Add to `build.sh`:

```bash
echo "=== Creating superuser ==="
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@nutritrack.com', 'your-strong-password-here')
    print('Superuser created')
else:
    print('Superuser already exists')
"
```

⚠️ **Security Warning:** Don't commit passwords to GitHub! Use environment variables instead.

### Option 3: Via Management Command (Best)

Create `tracker/management/commands/create_admin.py`:

```python
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        email = os.environ.get('ADMIN_EMAIL', 'admin@nutritrack.com')
        password = os.environ.get('ADMIN_PASSWORD', 'changeme123')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'✓ Admin user created: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'↻ Admin user already exists: {username}'))
```

Then add to `build.sh`:
```bash
python manage.py create_admin
```

And set environment variables on Render:
- `ADMIN_USERNAME`: admin
- `ADMIN_EMAIL`: your@email.com
- `ADMIN_PASSWORD`: your-strong-password

## 🎉 Quick Start

**Right now, to access admin:**

```powershell
# 1. Create superuser
python manage.py createsuperuser

# 2. Start server
python manage.py runserver

# 3. Open browser
# http://127.0.0.1:8000/admin/

# 4. Login with your credentials
```

---

**Note:** There is NO default password. You must create a superuser first!
