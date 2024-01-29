from django.urls import path
from .views import add_product_to_recipe, cook_recipe

urlpatterns = [  
   path('add_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>', add_product_to_recipe, name='main_book'), 
   path('cook_recipe/<int:recipe_id>/', cook_recipe, name='main_book'), 
]