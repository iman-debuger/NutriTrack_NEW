from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    age = models.IntegerField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    current_weight_kg = models.FloatField(null=True, blank=True)

    def calculate_bmi(self):
        if self.height_cm and self.current_weight_kg:
            height_m = self.height_cm / 100
            return round(self.current_weight_kg / (height_m ** 2), 1)
        return None

    # --- NEW ADVANCED METRICS ---
    def get_healthy_weight_range(self):
        if self.height_cm:
            height_m = self.height_cm / 100
            # Standard healthy BMI is 18.5 to 24.9
            min_weight = round(18.5 * (height_m ** 2), 1)
            max_weight = round(24.9 * (height_m ** 2), 1)
            return min_weight, max_weight
        return None, None

    def get_weight_target(self):
        if not self.current_weight_kg or not self.height_cm:
            return None
        min_w, max_w = self.get_healthy_weight_range()
        if self.current_weight_kg > max_w:
            return f"Lose {round(self.current_weight_kg - max_w, 1)} kg to reach a healthy BMI"
        elif self.current_weight_kg < min_w:
            return f"Gain {round(min_w - self.current_weight_kg, 1)} kg to reach a healthy BMI"
        return "You are currently at a healthy weight"

    def calculate_ponderal_index(self):
        if self.height_cm and self.current_weight_kg:
            height_m = self.height_cm / 100
            # Ponderal index formula: kg / m^3
            return round(self.current_weight_kg / (height_m ** 3), 1)
        return None

    def __str__(self):
        return f"Profile (Age: {self.age}, BMI: {self.calculate_bmi()})"

class NutritionItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories_per_100g = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.calories_per_100g} kcal/100g)"

class FoodLog(models.Model):  # Fixed
    name = models.CharField(max_length=100)
    grams = models.IntegerField(default=100)
    calories = models.IntegerField()
    date_logged = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.calories} kcal"


class WeightLog(models.Model):  # Fixed
    weight_kg = models.FloatField()
    date_logged = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.weight_kg} kg on {self.date_logged.strftime('%Y-%m-%d')}"