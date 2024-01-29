from apps.dynamic_serializer import DynamicFieldsModelSerializer
from .models import User

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = "__all__"