from django.shortcuts import render, redirect
from .models import UserProfile, FoodLog, NutritionItem
from django.utils import timezone
from django.db.models import Sum


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
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_grams = request.POST.get('food_grams')

        if food_name and food_grams:
            clean_name = food_name.strip()
            grams = int(food_grams)

            # --- THE NEW DATABASE QUERY ---
            try:
                # We use name__iexact to make the search case-insensitive
                # (so "rice", "Rice", and "RICE" all find the same database entry)
                nutrition_item = NutritionItem.objects.get(name__iexact=clean_name)
                cal_per_100g = nutrition_item.calories_per_100g
            except NutritionItem.DoesNotExist:
                # If the user types a food that isn't in your SQL database yet,
                # we fallback to an estimated 100 kcal per 100g so the app doesn't crash.
                cal_per_100g = 100

                # THE MATH: (grams / 100) * calories per 100g
            calculated_calories = round((grams / 100) * cal_per_100g)

            # Save the final meal to the FoodLog
            FoodLog.objects.create(
                name=food_name.title(),
                grams=grams,
                calories=calculated_calories
            )

        return redirect('diary')

    today = timezone.now().date()
    foods_today = FoodLog.objects.filter(date_logged__date=today).order_by('-date_logged')
    total_calories = foods_today.aggregate(Sum('calories'))['calories__sum'] or 0

    context = {
        'foods_today': foods_today,
        'total_calories': total_calories
    }
    return render(request, 'tracker/diary.html', context)