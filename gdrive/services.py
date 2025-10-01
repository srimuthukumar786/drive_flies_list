# gdrive/services.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("drive", "v3", credentials=creds)
    return service

def list_files_in_folder(folder_id, service=None, parent_path=""):
    """Recursively fetch all files in folder & subfolders with path"""
    if service is None:
        service = get_service()

    files = []

    query = f"'{folder_id}' in parents and trashed = false"
    page_token = None
    while True:
        response = service.files().list(
            q=query,
            fields="nextPageToken, files(id, name, mimeType, webViewLink)",
            pageSize=100,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            corpora="allDrives",
            pageToken=page_token,
        ).execute()

        for f in response.get("files", []):
            # Full path (parent_path + name)
            current_path = f"{parent_path}/{f['name']}" if parent_path else f['name']
            f["path"] = current_path

            files.append(f)

            # If folder → recurse
            if f["mimeType"] == "application/vnd.google-apps.folder":
                sub_files = list_files_in_folder(f["id"], service, current_path)
                files.extend(sub_files)

        page_token = response.get("nextPageToken", None)
        if page_token is None:
            break

    return files
