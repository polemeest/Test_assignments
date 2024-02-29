"""
Main views for the application. 
"""

from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAdminUser

from .serializers import KeywordsSerializer, ScrapedDataSerializer
from .models import Keywords, ScrapedData


class ShowDataApiView(APIView):
    """Class for showing scraped data."""
    permission_classes = [IsAdminUser]

    def get(self, requst, *args, **kwargs):
        """Shows scraped data."""
        serializer_class = ScrapedDataSerializer
        queryset = ScrapedData.objects.all()
        serializer = serializer_class(ScrapedData, many=True)
        return Response(serializer.data)
    

class SendRequestToResourse(APIView):
    """Sends request to the presetted resourse."""

    


