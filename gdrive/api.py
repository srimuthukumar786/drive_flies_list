from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import list_files_in_folder

class DriveListAPIView(APIView):
    def get(self, request):
        folder_id = request.query_params.get('folder_id')
        if not folder_id:
            return Response({'error':'folder_id required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            files = list_files_in_folder(folder_id)
            return Response({'files': files})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
