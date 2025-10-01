#google_auth.py
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account

BASE = os.path.dirname(os.path.dirname(__file__))
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDENTIALS_PATH = os.path.join(BASE, 'credentials', 'credentials.json')
TOKEN_PATH = os.path.join(BASE, 'token.json')
SERVICE_ACCOUNT_PATH = os.path.join(BASE, 'credentials', 'service_account.json')

def authenticate_installed_app():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return creds

def authenticate_service_account(sa_path=None):
    sa_path = sa_path or SERVICE_ACCOUNT_PATH
    creds = service_account.Credentials.from_service_account_file(sa_path, scopes=SCOPES)
    return creds

#authenticate_installed_app

# Lets real users log in with their own Google accounts.
# After first login, a token.json file is stored → no need to log in every time.
# Supports per-user access (user sees their own Google Drive files).
# Good for web apps with multiple users.

#authenticate_service_account
# No user interaction needed → completely automated.
# Best for backend/server tasks (cron jobs, scheduled backups, batch processing).
# Uses a single fixed Google account (the service account).
# Very stable (no browser flow, no token.json hassle).

