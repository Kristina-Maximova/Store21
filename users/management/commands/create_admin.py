from django.core.management.base import BaseCommand

from users.models import StoreUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = StoreUser.objects.create(
            email='testadmin@testadmin.com',
            username='Admin',)
        user.set_password('1234Ta')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with email {user.email}'))
