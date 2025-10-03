import pytest
from django.urls import reverse
from unittest.mock import patch

pytestmark = pytest.mark.django_db

def test_home_view(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert b"<html" in response.content.lower()

def test_list_drive_files_missing_param(client):
    response = client.get(reverse("list_drive_files"))
    assert response.status_code == 400
    assert response.json() == {"error": "folder_id query param required"}

@patch("gdrive.views.list_files_in_folder")
def test_list_drive_files_success(mock_list_files, client):
    mock_list_files.return_value = [
        {"id": "123", "name": "test.txt"}
    ]
    response = client.get(reverse("list_drive_files") + "?folder_id=abc")
    assert response.status_code == 200
    assert response.json() == {"files": [{"id": "123", "name": "test.txt"}]}

@patch("gdrive.views.list_files_in_folder")
def test_list_drive_files_exception(mock_list_files, client):
    mock_list_files.side_effect = Exception("Drive API failed")
    response = client.get(reverse("list_drive_files") + "?folder_id=abc")
    assert response.status_code == 500
    assert "Drive API failed" in response.json()["error"]
