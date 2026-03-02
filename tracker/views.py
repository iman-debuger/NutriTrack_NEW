from django.shortcuts import render, redirect
from .models import UserProfile, FoodLog, NutritionItem
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import timedelta


def home_view(request):

    context = {
        'profile': None,  # No profile data
        'daily_kcal': None,  # No calories calculated
        'gauge_degree': -90,  # Needle safely at rest on the far left (-90 degrees)
        'bmi_category': "Calculate your metrics",
        'min_weight': None,
        'max_weight': None,
        'cal_adjustment_val': '--',
        'cal_adjustment_label': 'Adjustment'
    }


    if request.method == 'POST':
        age_val = request.POST.get('age')
        weight_val = request.POST.get('weight')
        height_val = request.POST.get('height')

        try:
            # Safely convert the text inputs into numbers
            age_clean = int(age_val) if age_val else None
            weight_clean = float(weight_val) if weight_val else None
            height_clean = float(height_val) if height_val else None

            # Only do the math if we have both weight and height
            if weight_clean and height_clean:

                # MAGIC TRICK: We create a Profile object but DO NOT call .save()
                # This lets us use all the math methods in models.py without touching the database!
                profile = UserProfile(
                    age=age_clean,
                    current_weight_kg=weight_clean,
                    height_cm=height_clean
                )

                daily_kcal = round(profile.current_weight_kg * 30)
                bmi = profile.calculate_bmi()

                # Determine the Category
                if bmi < 18.5:
                    bmi_category = "Underweight"
                elif bmi < 25:
                    bmi_category = "Healthy Weight"
                elif bmi < 30:
                    bmi_category = "Overweight"
                else:
                    bmi_category = "Obese"

                # Calculate Gauge Needle Angle (-90 to 90 degrees)
                percentage = max(0, min(100, ((bmi - 15) / 25) * 100))
                gauge_degree = (percentage / 100 * 180) - 90

                # Get the healthy ranges
                min_weight, max_weight = profile.get_healthy_weight_range()
                if bmi < 18.5:
                    cal_adjustment_val = "+500"
                    cal_adjustment_label = "Daily Surplus"
                elif bmi > 24.9:
                    cal_adjustment_val = "-500"
                    cal_adjustment_label = "Daily Deficit"
                else:
                    cal_adjustment_val = "0"
                    cal_adjustment_label = "Maintenance"
                # Update the context with the new calculated numbers
                context.update({
                    'profile': profile,
                    'daily_kcal': daily_kcal,
                    'gauge_degree': gauge_degree,
                    'bmi_category': bmi_category,
                    'min_weight': min_weight,
                    'max_weight': max_weight,
                    'cal_adjustment_val': cal_adjustment_val,
                    'cal_adjustment_label': cal_adjustment_label,
                })
        except ValueError:
            # If the user somehow inputs bad data (like text instead of numbers),
            # we just ignore it and return the blank state
            pass

    # Render the template directly. Notice we removed the "redirect()" from the POST!
    return render(request, 'tracker/home.html', context)


def diary_view(request):

    context = {'searched_food': None, 'foods_today': [], 'total_calories': 0}

    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_grams = request.POST.get('food_grams')

        if food_name and food_grams:
            clean_name = food_name.strip()
            grams = int(food_grams)

            try:
                nutrition_item = NutritionItem.objects.get(name__iexact=clean_name)
                cal_per_100g = nutrition_item.calories_per_100g
            except NutritionItem.DoesNotExist:
                cal_per_100g = 100

            calculated_calories = round((grams / 100) * cal_per_100g)


            if request.user.is_authenticated:
                FoodLog.objects.create(
                    user=request.user,
                    name=food_name.title(),
                    grams=grams,
                    calories=calculated_calories
                )
                return redirect('diary')


            else:
                context['searched_food'] = {
                    'name': food_name.title(),
                    'grams': grams,
                    'calories': calculated_calories
                }


    if request.user.is_authenticated:
        today = timezone.now().date()
        foods_today = FoodLog.objects.filter(user=request.user, date_logged__date=today).order_by('-date_logged')
        context['total_calories'] = foods_today.aggregate(Sum('calories'))['calories__sum'] or 0
        context['foods_today'] = foods_today

    return render(request, 'tracker/diary.html', context)


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # 1. Get or create the user's permanent profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # 2. Handle saving permanent metrics from the Profile page
    if request.method == 'POST':
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        if age and weight and height:
            profile.age = int(age)
            profile.current_weight_kg = float(weight)
            profile.height_cm = float(height)
            profile.save()
            return redirect('profile')

    # 3. Calculate Daily & Monthly Calories
    today = timezone.now().date()
    this_month = today.replace(day=1)

    daily_logs = FoodLog.objects.filter(user=request.user, date_logged__date=today)
    monthly_logs = FoodLog.objects.filter(user=request.user, date_logged__gte=this_month)

    daily_total = daily_logs.aggregate(Sum('calories'))['calories__sum'] or 0
    monthly_total = monthly_logs.aggregate(Sum('calories'))['calories__sum'] or 0

    # 4. Determine Target Goal & Maintenance Kcal
    target_text = "Save metrics"
    target_color = "var(--ios-secondary)"
    maint_kcal = None  # <--- NEW VARIABLE

    if profile.current_weight_kg and profile.height_cm:
        # Calculate Maintenance Kcal
        maint_kcal = round(profile.current_weight_kg * 30)

        bmi = profile.calculate_bmi()
        if bmi < 18.5:
            target_text = "Surplus (+500)"  # Shortened to fit the new grid
            target_color = "#f39c12"
        elif bmi > 24.9:
            target_text = "Deficit (-500)"  # Shortened to fit the new grid
            target_color = "#e74c3c"
        else:
            target_text = "Maintenance"
            target_color = "#2ecc71"

    context = {
        'profile': profile,
        'daily_total': daily_total,
        'monthly_total': monthly_total,
        'target_text': target_text,
        'target_color': target_color,
        'maint_kcal': maint_kcal,  # <--- PASS IT TO HTML
    }
    return render(request, 'tracker/profile.html', context)

def analyze_food_view(request):
    # Added 'error' to the context so we can show messages
    context = {'result': None, 'error': None}

    if request.method == 'POST':
        # 1. If the user clicks "Save to Journal"
        if 'save_ai_meal' in request.POST:
            if request.user.is_authenticated:
                FoodLog.objects.create(
                    user=request.user,
                    name=request.POST.get('meal_name'),
                    grams=100, # Default estimate
                    calories=int(request.POST.get('meal_calories'))
                )
                return redirect('diary')
            else:
                return redirect('login')

        # 2. If the user is uploading an image for analysis
        elif 'food_image' in request.FILES:
            uploaded_file = request.FILES['food_image']
            filename = uploaded_file.name

            # MOCK AI LOGIC: Extract the food name from the file name
            # Example: "Apple.jpg" -> "apple", "Chicken_Biryani.png" -> "chicken biryani"
            recognized_name = filename.rsplit('.', 1)[0].lower().replace('_', ' ').replace('-', ' ')

            # 3. Query the REAL SQL Database!
            try:
                # Find the exact food item in your NutritionItem table
                real_food_data = NutritionItem.objects.get(name__iexact=recognized_name)

                # Since our current DB only stores calories, we dynamically fake the macros for the UI
                cal = real_food_data.calories_per_100g

                context['result'] = {
                    'name': real_food_data.name,
                    'calories': real_food_data.calories_per_100g,
                    'protein': int(real_food_data.protein),
                    'carbs': int(real_food_data.carbs),
                    'fat': int(real_food_data.fat),
                    'fiber': real_food_data.fiber,
                    'confidence': 98.5
                }

            except NutritionItem.DoesNotExist:
                # If the filename doesn't match the database, return an error message!
                context['error'] = f"Recognized Food is'{recognized_name.title()}', but it is not in your SQL database! Try naming your file exactly like a database item (e.g., 'Apple.jpg' or 'Chicken Biryani.png')."

    return render(request, 'tracker/analyze.html', context)

def trends_view(request):
    context = {}

    if request.user.is_authenticated:
        # 1. Figure out the dates for the last 7 days
        today = timezone.now().date()
        last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]

        # 2. Grab all food logged by this user in the last 7 days
        logs = FoodLog.objects.filter(
            user=request.user,
            date_logged__date__gte=last_7_days[0],
            date_logged__date__lte=today
        )

        # 3. Sum up the calories for each specific day
        daily_totals = {}
        for log in logs:
            log_date = log.date_logged.date()
            daily_totals[log_date] = daily_totals.get(log_date, 0) + log.calories

        # 4. PURE PYTHON GRAPH CALCULATION:
        # We figure out the highest calorie day to scale the CSS bar heights properly!
        chart_data = []
        max_calories = 2500  # Our default ceiling

        if daily_totals:
            actual_max = max(daily_totals.values())
            if actual_max > max_calories:
                max_calories = actual_max

        # 5. Build the list of data to send to the HTML template
        for day in last_7_days:
            total = daily_totals.get(day, 0)

            # Calculate how tall the CSS bar should be (0% to 100%)
            height_percentage = (total / max_calories) * 100 if max_calories > 0 else 0

            chart_data.append({
                'day_name': day.strftime('%a'),  # e.g., "Mon", "Tue"
                'calories': total,
                'height': round(height_percentage)
            })

        context['chart_data'] = chart_data
        context['avg_calories'] = sum(daily_totals.values()) // 7 if daily_totals else 0

    return render(request, 'tracker/trends.html', context)

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'tracker/login.html', {'error': 'Invalid username or password'})
    return render(request, 'tracker/login.html')


def signup_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        if User.objects.filter(username=u).exists():
            return render(request, 'tracker/signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=u, password=p)
        login(request, user)
        return redirect('home')
    return render(request, 'tracker/signup.html')


def logout_view(request):
    logout(request)
    return redirect('home')