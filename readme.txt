1. Go to Google Cloud Console → APIs & Services → Library → enable Google Drive API.
2. Go to Google Cloud Console → APIs & Services → OAuth consent screen -> Click Configure consent screen.
3. Choose User Type
	Internal: Only users in your Google Workspace organization can log in.
	External: Any Google user can log in (recommended if you’re using a personal Gmail account or plan to let others test).
	For personal projects → choose External.
4. App Information
	App name: e.g. "Django Drive Explorer".
	User support email: your Gmail (or project owner’s email).
5. Developer Contact Information
	Add your email address (so Google can contact you about this app).
	Click Save and Continue.
6. APIs & Services → Credentials → Create Credentials → OAuth client ID → choose Desktop app (or Web application for redirect URIs). Download credentials.json.
7. Rename file name as credentials.json and Put credentials.json into your Django project (secure location).

****************************************************************************************************************

Note: if error while Authenticating:

Go to Google Cloud Console → APIs & Services → OAuth consent screen -> Audience -> Add user under Test User -> Add your Gmail account under Test Users.
Save changes.
Now, when you log in with that Gmail, it should work (with a “Google hasn’t verified this app” warning).