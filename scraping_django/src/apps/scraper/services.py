"""
Business-logics of the application
"""

from config.settings import RESOURSE
from django.http import HttpRequest
from django.db.models import QuerySet

from .serializers import KeywordsSerializer, ScrapedDataSerializer
from .models import Keywords, ScrapedData

def send_request(request: HttpRequest, serializer: KeywordsSerializer,
                 queryset: QuerySet)
    """Takes keywords from request POST method, """