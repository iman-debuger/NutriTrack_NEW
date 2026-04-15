from django.core.management.base import BaseCommand
from tracker.models import NutritionItem


class Command(BaseCommand):
    help = 'Populate the database with comprehensive food nutrition data'

    def handle(self, *args, **kwargs):
        foods = [
            # Indian Foods
            {'name': 'Chicken Biryani', 'calories': 150, 'protein': 12, 'carbs': 18, 'fat': 5, 'fiber': 1},
            {'name': 'Coconut Chutney', 'calories': 220, 'protein': 2, 'carbs': 4, 'fat': 22, 'fiber': 2},
            {'name': 'Tomato Chutney', 'calories': 85, 'protein': 1, 'carbs': 4, 'fat': 7, 'fiber': 1},
            {'name': 'Sambar', 'calories': 75, 'protein': 3, 'carbs': 10, 'fat': 2, 'fiber': 3},
            {'name': 'Dosa', 'calories': 168, 'protein': 4, 'carbs': 28, 'fat': 4, 'fiber': 2},
            {'name': 'Idli', 'calories': 58, 'protein': 2, 'carbs': 12, 'fat': 0.5, 'fiber': 1},
            {'name': 'Vada', 'calories': 200, 'protein': 5, 'carbs': 20, 'fat': 11, 'fiber': 2},
            {'name': 'Paneer Butter Masala', 'calories': 180, 'protein': 8, 'carbs': 6, 'fat': 14, 'fiber': 1},
            {'name': 'Dal Tadka', 'calories': 104, 'protein': 6, 'carbs': 15, 'fat': 2, 'fiber': 4},
            {'name': 'Roti', 'calories': 71, 'protein': 3, 'carbs': 15, 'fat': 0.4, 'fiber': 2},
            {'name': 'Naan', 'calories': 262, 'protein': 9, 'carbs': 45, 'fat': 5, 'fiber': 2},
            {'name': 'Paratha', 'calories': 126, 'protein': 3, 'carbs': 18, 'fat': 5, 'fiber': 2},
            
            # Proteins
            {'name': 'Chicken', 'calories': 239, 'protein': 27, 'carbs': 0, 'fat': 14, 'fiber': 0},
            {'name': 'Chicken Breast', 'calories': 165, 'protein': 31, 'carbs': 0, 'fat': 4, 'fiber': 0},
            {'name': 'Egg', 'calories': 155, 'protein': 13, 'carbs': 1, 'fat': 11, 'fiber': 0},
            {'name': 'Fish', 'calories': 206, 'protein': 22, 'carbs': 0, 'fat': 12, 'fiber': 0},
            {'name': 'Salmon', 'calories': 208, 'protein': 20, 'carbs': 0, 'fat': 13, 'fiber': 0},
            {'name': 'Tuna', 'calories': 132, 'protein': 28, 'carbs': 0, 'fat': 1, 'fiber': 0},
            {'name': 'Paneer', 'calories': 265, 'protein': 18, 'carbs': 3, 'fat': 20, 'fiber': 0},
            {'name': 'Tofu', 'calories': 76, 'protein': 8, 'carbs': 2, 'fat': 5, 'fiber': 1},
            {'name': 'Mutton', 'calories': 294, 'protein': 25, 'carbs': 0, 'fat': 21, 'fiber': 0},
            {'name': 'Prawns', 'calories': 99, 'protein': 24, 'carbs': 0, 'fat': 0.3, 'fiber': 0},
            
            # Carbs
            {'name': 'Rice', 'calories': 130, 'protein': 3, 'carbs': 28, 'fat': 0.3, 'fiber': 0.4},
            {'name': 'Brown Rice', 'calories': 111, 'protein': 3, 'carbs': 23, 'fat': 0.9, 'fiber': 1.8},
            {'name': 'Pasta', 'calories': 131, 'protein': 5, 'carbs': 25, 'fat': 1, 'fiber': 2},
            {'name': 'Bread', 'calories': 265, 'protein': 9, 'carbs': 49, 'fat': 3, 'fiber': 2},
            {'name': 'Oats', 'calories': 389, 'protein': 17, 'carbs': 66, 'fat': 7, 'fiber': 11},
            {'name': 'Quinoa', 'calories': 120, 'protein': 4, 'carbs': 21, 'fat': 2, 'fiber': 3},
            {'name': 'Potato', 'calories': 77, 'protein': 2, 'carbs': 17, 'fat': 0.1, 'fiber': 2},
            {'name': 'Sweet Potato', 'calories': 86, 'protein': 2, 'carbs': 20, 'fat': 0.1, 'fiber': 3},
            
            # Fruits
            {'name': 'Apple', 'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2, 'fiber': 2.4},
            {'name': 'Banana', 'calories': 89, 'protein': 1, 'carbs': 23, 'fat': 0.3, 'fiber': 2.6},
            {'name': 'Orange', 'calories': 47, 'protein': 1, 'carbs': 12, 'fat': 0.1, 'fiber': 2.4},
            {'name': 'Mango', 'calories': 60, 'protein': 0.8, 'carbs': 15, 'fat': 0.4, 'fiber': 1.6},
            {'name': 'Grapes', 'calories': 69, 'protein': 0.7, 'carbs': 18, 'fat': 0.2, 'fiber': 0.9},
            {'name': 'Watermelon', 'calories': 30, 'protein': 0.6, 'carbs': 8, 'fat': 0.2, 'fiber': 0.4},
            {'name': 'Strawberry', 'calories': 32, 'protein': 0.7, 'carbs': 8, 'fat': 0.3, 'fiber': 2},
            {'name': 'Papaya', 'calories': 43, 'protein': 0.5, 'carbs': 11, 'fat': 0.3, 'fiber': 1.7},
            {'name': 'Pineapple', 'calories': 50, 'protein': 0.5, 'carbs': 13, 'fat': 0.1, 'fiber': 1.4},
            
            # Vegetables
            {'name': 'Broccoli', 'calories': 34, 'protein': 3, 'carbs': 7, 'fat': 0.4, 'fiber': 2.6},
            {'name': 'Spinach', 'calories': 23, 'protein': 3, 'carbs': 4, 'fat': 0.4, 'fiber': 2.2},
            {'name': 'Carrot', 'calories': 41, 'protein': 1, 'carbs': 10, 'fat': 0.2, 'fiber': 2.8},
            {'name': 'Tomato', 'calories': 18, 'protein': 1, 'carbs': 4, 'fat': 0.2, 'fiber': 1.2},
            {'name': 'Cucumber', 'calories': 15, 'protein': 0.7, 'carbs': 4, 'fat': 0.1, 'fiber': 0.5},
            {'name': 'Onion', 'calories': 40, 'protein': 1, 'carbs': 9, 'fat': 0.1, 'fiber': 1.7},
            {'name': 'Cauliflower', 'calories': 25, 'protein': 2, 'carbs': 5, 'fat': 0.3, 'fiber': 2},
            {'name': 'Cabbage', 'calories': 25, 'protein': 1, 'carbs': 6, 'fat': 0.1, 'fiber': 2.5},
            
            # Nuts & Seeds
            {'name': 'Almonds', 'calories': 579, 'protein': 21, 'carbs': 22, 'fat': 50, 'fiber': 12},
            {'name': 'Cashews', 'calories': 553, 'protein': 18, 'carbs': 30, 'fat': 44, 'fiber': 3},
            {'name': 'Walnuts', 'calories': 654, 'protein': 15, 'carbs': 14, 'fat': 65, 'fiber': 7},
            {'name': 'Peanuts', 'calories': 567, 'protein': 26, 'carbs': 16, 'fat': 49, 'fiber': 9},
            {'name': 'Chia Seeds', 'calories': 486, 'protein': 17, 'carbs': 42, 'fat': 31, 'fiber': 34},
            
            # Dairy
            {'name': 'Milk', 'calories': 42, 'protein': 3, 'carbs': 5, 'fat': 1, 'fiber': 0},
            {'name': 'Yogurt', 'calories': 59, 'protein': 10, 'carbs': 4, 'fat': 0.4, 'fiber': 0},
            {'name': 'Cheese', 'calories': 402, 'protein': 25, 'carbs': 1, 'fat': 33, 'fiber': 0},
            {'name': 'Butter', 'calories': 717, 'protein': 1, 'carbs': 0.1, 'fat': 81, 'fiber': 0},
            {'name': 'Ghee', 'calories': 900, 'protein': 0, 'carbs': 0, 'fat': 100, 'fiber': 0},
            
            # Snacks & Fast Food
            {'name': 'Pizza', 'calories': 266, 'protein': 11, 'carbs': 33, 'fat': 10, 'fiber': 2},
            {'name': 'Burger', 'calories': 295, 'protein': 17, 'carbs': 24, 'fat': 14, 'fiber': 1},
            {'name': 'French Fries', 'calories': 312, 'protein': 4, 'carbs': 41, 'fat': 15, 'fiber': 4},
            {'name': 'Sandwich', 'calories': 250, 'protein': 10, 'carbs': 30, 'fat': 10, 'fiber': 2},
            {'name': 'Samosa', 'calories': 262, 'protein': 5, 'carbs': 24, 'fat': 17, 'fiber': 3},
            {'name': 'Pakora', 'calories': 250, 'protein': 4, 'carbs': 20, 'fat': 17, 'fiber': 2},
            
            # Beverages (per 100ml)
            {'name': 'Coffee', 'calories': 1, 'protein': 0.1, 'carbs': 0, 'fat': 0, 'fiber': 0},
            {'name': 'Tea', 'calories': 1, 'protein': 0, 'carbs': 0.3, 'fat': 0, 'fiber': 0},
            {'name': 'Orange Juice', 'calories': 45, 'protein': 0.7, 'carbs': 10, 'fat': 0.2, 'fiber': 0.2},
            {'name': 'Coke', 'calories': 42, 'protein': 0, 'carbs': 11, 'fat': 0, 'fiber': 0},
        ]

        created_count = 0
        updated_count = 0
        
        for food_data in foods:
            item, created = NutritionItem.objects.update_or_create(
                name=food_data['name'],
                defaults={
                    'calories_per_100g': food_data['calories'],
                    'protein': food_data['protein'],
                    'carbs': food_data['carbs'],
                    'fat': food_data['fat'],
                    'fiber': food_data['fiber'],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {item.name}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'↻ Updated: {item.name}'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Complete! Created: {created_count}, Updated: {updated_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total food items in database: {NutritionItem.objects.count()}'))
