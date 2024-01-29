from django.urls import path, include
from .views import homepage, show_recipes_without_product

urlpatterns = [  
   path('', homepage, name='homepage'),
   path('table/<int:product_id>', show_recipes_without_product, name='table'),

]