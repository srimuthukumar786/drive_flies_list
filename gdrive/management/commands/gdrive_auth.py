#gdrive_auth.py
from django.core.management.base import BaseCommand
from gdrive.google_auth import authenticate_installed_app

class Command(BaseCommand):
    help = 'Run Google OAuth interactive flow and create token.json'

    def handle(self, *args, **options):
        creds = authenticate_installed_app()
        if creds and creds.valid:
            self.stdout.write(self.style.SUCCESS('Authenticated and token.json saved.'))
        else:
            self.stdout.write(self.style.ERROR('Authentication failed.'))

#authenticate your Django project with Google APIs (like Google Drive API) using OAuth, and then save the authentication credentials locally in a file (token.json).
