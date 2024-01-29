from apps.dynamic_serializer import DynamicFieldsModelSerializer
from .models import Recipe, Product

class RecipeSerializer(DynamicFieldsModelSerializer):
    ''' Сериализует данные модели рецептов. '''

    class Meta:
        model = Recipe
        fields = "__all__"


class ProductSerializer(DynamicFieldsModelSerializer):
    ''' Сериализует данные модели рецептов. '''

    class Meta:
        model = Product
        fields = "__all__"