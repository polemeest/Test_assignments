from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Q

from apps.cook_book.models import Recipe
from config.settings import LOGIN_URL, LOGOUT_URL

# Create your views here.
def show_recipes_without_product(request: HttpRequest, product_id: int) -> HttpResponse:
    ''' Функция возвращает HTML страницу, на которой размещена таблица.
    В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, 
    или присутствует в количестве меньше 10 грамм. Страница должна генерироваться с использованием Django templates. 
    Качество HTML верстки не оценивается. '''
    filtered_recipes = Recipe.objects.filter(
        ~Q(recipeproduct__product_id=product_id) | 
        Q(recipeproduct__amount__lt=10)).distinct()
    return render(request, 'frontend/index.html', {'filtered_recipes': filtered_recipes,
                                                   'login': LOGIN_URL,
                                                   'logout': LOGOUT_URL})


def homepage(request: HttpRequest) -> HttpResponse:
    ''' Shows main functionality '''
    return HttpResponse('FRONTEND', status=200)
    