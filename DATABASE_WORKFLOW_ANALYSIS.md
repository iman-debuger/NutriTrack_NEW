# NutriTrack Database Workflow Analysis

## 📊 Database Architecture

### Current Setup

#### Local Development
- **Database:** SQLite (`db.sqlite3`)
- **Location:** Project root directory
- **Purpose:** Development and testing
- **Data:** Persists locally on your machine

#### Production (Render)
- **Database:** PostgreSQL
- **URL:** `postgresql://nutritracker_db_user:lqhi1XbHHaJPXZVC6Umfr08UUoJ6zmxW@dpg-d72fgee3jp1c73ee93dg-a/nutritracker_db`
- **Purpose:** Production deployment
- **Data:** Separate from local database

### ⚠️ Key Issue: Separate Databases

**Problem:** Local SQLite and Render PostgreSQL are COMPLETELY SEPARATE databases.

```
Local (SQLite)                    Render (PostgreSQL)
├── 25 food items                 ├── May have 0 food items
├── Your test users               ├── Different users
├── Your food logs                ├── Different food logs
└── Your profiles                 └── Different profiles
```

**This means:**
- Food data added locally does NOT appear on Render
- Users created locally do NOT exist on Render
- Food logs are separate between environments

## 🔄 Database Models

### 1. NutritionItem (Food Database)
```python
class NutritionItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories_per_100g = models.IntegerField()
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    fat = models.FloatField(default=0)
```

**Purpose:** Master food database with nutritional information

**Current Status:**
- Local: 25 items
- Render: Unknown (likely 0 or different items)

### 2. FoodLog (User's Food Diary)
```python
class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    grams = models.IntegerField(default=100)
    calories = models.IntegerField()
    date_logged = models.DateTimeField(default=timezone.now)
```

**Purpose:** Track what users eat each day

**Workflow:**
1. User enters food name and grams
2. System looks up food in NutritionItem
3. Calculates calories based on grams
4. Saves to FoodLog

### 3. UserProfile
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    current_weight_kg = models.FloatField(null=True, blank=True)
```

**Purpose:** Store user's health metrics

## 🔍 Food Data Workflow

### Diary View (Food Logging)

```python
def diary_view(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_grams = request.POST.get('food_grams')
        
        # Step 1: Try to find food in database
        try:
            nutrition_item = NutritionItem.objects.get(name__iexact=clean_name)
            cal_per_100g = nutrition_item.calories_per_100g
        except NutritionItem.DoesNotExist:
            # Step 2: If not found, use default 100 cal/100g
            cal_per_100g = 100
        
        # Step 3: Calculate calories
        calculated_calories = round((grams / 100) * cal_per_100g)
        
        # Step 4: Save to food log
        FoodLog.objects.create(
            user=request.user,
            name=food_name.title(),
            grams=grams,
            calories=calculated_calories
        )
```

**Issue:** If food doesn't exist in NutritionItem, it defaults to 100 cal/100g (inaccurate!)

### AI Analyze View (Image Recognition)

```python
def analyze_food_view(request):
    # Mock AI: Uses filename as food name
    recognized_name = filename.rsplit('.', 1)[0].lower()
    
    try:
        # Look up in database
        real_food_data = NutritionItem.objects.get(name__iexact=recognized_name)
        # Return nutritional data
    except NutritionItem.DoesNotExist:
        # Show error if not found
        context['error'] = f"Food '{recognized_name}' not in database"
```

**Issue:** Only works if filename exactly matches database entry

## ✅ Solution: Populate Food Database

### Step 1: Run Management Command Locally

```powershell
python manage.py populate_food_data
```

This will add 70+ common foods to your LOCAL database:
- Indian foods (Biryani, Dosa, Idli, Sambar, etc.)
- Proteins (Chicken, Fish, Eggs, Paneer, etc.)
- Carbs (Rice, Bread, Pasta, Oats, etc.)
- Fruits (Apple, Banana, Mango, etc.)
- Vegetables (Broccoli, Spinach, Carrot, etc.)
- Nuts & Seeds (Almonds, Cashews, Walnuts, etc.)
- Dairy (Milk, Yogurt, Cheese, etc.)
- Snacks (Pizza, Burger, Samosa, etc.)

### Step 2: Add to Build Script for Render

Update `build.sh` to populate food data on deployment:

```bash
#!/usr/bin/env bash
set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Creating staticfiles directory ==="
mkdir -p staticfiles

echo "=== Collecting static files ==="
python manage.py collectstatic --no-input --clear --verbosity 2

echo "=== Waiting for database to be ready ==="
sleep 5

echo "=== Running migrations (attempt 1) ==="
python manage.py migrate --verbosity 2 || {
    echo "Migration failed, waiting 10 seconds and retrying..."
    sleep 10
    echo "=== Running migrations (attempt 2) ==="
    python manage.py migrate --verbosity 2
}

echo "=== Populating food database ==="
python manage.py populate_food_data

echo "=== Listing applied migrations ==="
python manage.py showmigrations

echo "=== Build completed successfully! ==="
```

### Step 3: Test Food Lookup

After populating, test these foods:
- "Chicken Biryani" → 150 cal/100g
- "Apple" → 52 cal/100g
- "Rice" → 130 cal/100g
- "Egg" → 155 cal/100g

## 🔧 How to Fix Food Data Issues

### Issue 1: Food Not Found in Diary

**Symptom:** When you enter a food name, it uses 100 cal/100g default

**Solution:**
1. Check if food exists: `python manage.py shell -c "from tracker.models import NutritionItem; print(NutritionItem.objects.filter(name__icontains='chicken'))"`
2. Add missing food via admin panel or management command
3. Ensure exact name match (case-insensitive)

### Issue 2: AI Analyze Shows "Not in Database"

**Symptom:** Upload image named "Apple.jpg" but get error

**Solution:**
1. Ensure filename matches database entry exactly
2. Check database: `python manage.py shell -c "from tracker.models import NutritionItem; print([item.name for item in NutritionItem.objects.all()])"`
3. Add missing food to database

### Issue 3: Render Has No Food Data

**Symptom:** Works locally but not on Render

**Solution:**
1. Add `python manage.py populate_food_data` to `build.sh`
2. Redeploy to Render
3. Check Render logs to confirm command ran

## 📝 Database Management Commands

### Check Food Count
```powershell
python manage.py shell -c "from tracker.models import NutritionItem; print(f'Total: {NutritionItem.objects.count()}')"
```

### List All Foods
```powershell
python manage.py shell -c "from tracker.models import NutritionItem; [print(f'{i.name}: {i.calories_per_100g} kcal') for i in NutritionItem.objects.all()]"
```

### Add Single Food
```powershell
python manage.py shell -c "from tracker.models import NutritionItem; NutritionItem.objects.create(name='Chocolate', calories_per_100g=546, protein=5, carbs=61, fat=31, fiber=7); print('Added!')"
```

### Delete All Foods
```powershell
python manage.py shell -c "from tracker.models import NutritionItem; NutritionItem.objects.all().delete(); print('Deleted all')"
```

### Populate Database
```powershell
python manage.py populate_food_data
```

## 🎯 Best Practices

### 1. Keep Databases in Sync
- Use management commands to populate data
- Add `populate_food_data` to build script
- Document any manual data additions

### 2. Handle Missing Foods Gracefully
- Current: Defaults to 100 cal/100g
- Better: Show error message asking user to add food
- Best: Integrate real food API (USDA, Nutritionix, etc.)

### 3. Use Django Admin
- Access: http://127.0.0.1:8000/admin/
- Create superuser: `python manage.py createsuperuser`
- Manually add/edit foods through admin interface

### 4. Backup Data
- Local: `python manage.py dumpdata tracker.NutritionItem > food_backup.json`
- Restore: `python manage.py loaddata food_backup.json`

## 🚀 Next Steps

1. **Run locally:**
   ```powershell
   python manage.py populate_food_data
   ```

2. **Update build.sh** (add populate command)

3. **Test locally:**
   - Go to diary
   - Enter "Apple" with 100g
   - Should show 52 calories

4. **Deploy to Render:**
   - Push changes to GitHub
   - Render will run build.sh
   - Food data will populate automatically

5. **Verify on Render:**
   - Test diary with known foods
   - Check AI analyze with matching filenames

## 📊 Current Database Status

### Local SQLite
- ✅ 25 food items
- ✅ Migrations applied
- ✅ Working correctly

### Render PostgreSQL
- ⚠️ Unknown food count (likely 0)
- ✅ Migrations applied
- ⚠️ Needs food data population

## 🎉 Summary

**The Issue:** Your local database has food data, but Render's database is separate and may be empty.

**The Solution:** 
1. Created management command to populate 70+ foods
2. Add command to build script for automatic population
3. Run command locally and on Render

**Result:** Both databases will have comprehensive food data, and the diary/analyze features will work perfectly!

---

**Created:** March 27, 2026  
**Status:** ✅ Solution Ready - Run populate_food_data command
