from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .serializers import UserSerializer
from .models import User


class UserListView(ListAPIView):
    """Получить всех пользователей"""
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer(self, *args, **kwargs) -> UserSerializer:
        ''' gets none and returns serializer depending on a type of user '''
        if self.request.user.is_superuser:
            return UserSerializer()
        else:
            return UserSerializer('email', 'phone', 'first_name', 'last_name', 'created_at',
                                  'balance', 'mail_confirmed', 'phone_confirmed', 'user_type')
    
    def get_queryset(self) -> QuerySet:
        ''' gets none and returns queryset depending on a type of user '''
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.get(id=self.request.user.pk)
