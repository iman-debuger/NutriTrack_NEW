from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Get credentials from environment or use defaults
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        email = os.environ.get('ADMIN_EMAIL', 'admin@nutritrack.com')
        password = os.environ.get('ADMIN_PASSWORD', 'nutritrack2026')
        
        # Check if superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'↻ Superuser "{username}" already exists'))
            # Update to ensure they have admin privileges
            user = User.objects.get(username=username)
            if not user.is_staff or not user.is_superuser:
                user.is_staff = True
                user.is_superuser = True
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Updated "{username}" to superuser'))
        else:
            # Create new superuser
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'✓ Superuser "{username}" created successfully'))
            self.stdout.write(self.style.SUCCESS(f'  Username: {username}'))
            self.stdout.write(self.style.SUCCESS(f'  Password: {password}'))
