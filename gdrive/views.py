# gdrive/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .services import list_files_in_folder
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

@require_GET
def list_drive_files(request):
    folder_id = request.GET.get('folder_id')
    if not folder_id:
        return JsonResponse({'error': 'folder_id query param required'}, status=400)
    try:
        files = list_files_in_folder(folder_id)
        return JsonResponse({'files': files})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
