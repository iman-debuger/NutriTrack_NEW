from django.contrib import admin
from .models import UserProfile, FoodLog, WeightLog, NutritionItem

admin.site.register(UserProfile)
admin.site.register(FoodLog)
admin.site.register(WeightLog)
admin.site.register(NutritionItem)