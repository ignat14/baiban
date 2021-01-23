from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create test superuser, use for DEV environment only!'

    def handle(self, **_):
        User = get_user_model()
        if not hasattr(settings, 'DEV_SUPERUSER_EMAIL'):
            self.stdout.write(self.style.ERROR('DEV_SUPERUSER_EMAIL is not set.'))
            return

        if not hasattr(settings, 'DEV_SUPERUSER_PASSWORD'):
            self.stdout.write(self.style.ERROR('DEV_SUPERUSER_PASSWORD is not set.'))
            return

        if not User.objects.filter(email=settings.DEV_SUPERUSER_EMAIL).exists():
            User.objects.create_superuser(
                settings.DEV_SUPERUSER_EMAIL, settings.DEV_SUPERUSER_PASSWORD
            )
        self.stdout.write(self.style.SUCCESS(
            f"DEV Superuser '{settings.DEV_SUPERUSER_EMAIL}/{settings.DEV_SUPERUSER_PASSWORD}'"
        )
        )
