from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .services import get_recipe_model, change_recipe, raise_cooking_amount
# Create your views here.

def main(request: HttpRequest) -> HttpResponse:
    ''' main func '''
    return HttpResponse('cook_book', status=200)

'''
 Ниже будут функции представлений. Выбираю писать не через классы, чтобы соблюсти нейминг
'''

def add_product_to_recipe(request: HttpRequest, recipe_id: int, product_id: int, 
                          weight: int) -> None:
    ''' Функция добавляет к указанному рецепту указанный продукт с указанным весом. 
    Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте 
    на указанный. '''   
    model = get_recipe_model(recipe_id)
    if isinstance(model, HttpResponseRedirect):
        return model
    change_recipe(model, product_id, weight)
    

def cook_recipe(request: HttpRequest, recipe_id: int) -> None:
    ''' Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, 
    входящего в указанный рецепт. '''
    model = get_recipe_model(recipe_id)
    raise_cooking_amount(model)

   