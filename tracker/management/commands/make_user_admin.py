from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Make existing users admin/staff'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to make admin')

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = kwargs['username']
        
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'✓ User "{username}" is now an admin!'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'✗ User "{username}" does not exist'))
