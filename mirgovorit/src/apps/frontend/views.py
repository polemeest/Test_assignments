from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Q


from apps.cook_book.models import Recipe
from config.settings import LOGIN_URL, LOGOUT_URL
from .forms import AddProductForm
from .services import process_main_post


# Create your views here.
def show_recipes_without_product(request: HttpRequest, product_id: int) -> \
                                                                HttpResponse:
    """ Функция возвращает HTML страницу, на которой размещена таблица.
    В таблице отображены id и названия всех рецептов, в которых указанный
    продукт отсутствует, или присутствует в количестве меньше 10 грамм.
    Страница должна генерироваться с использованием Django templates. """
    filtered_recipes = Recipe.objects.filter(
        ~Q(recipeproduct__product_id=product_id) |
        Q(recipeproduct__amount__lt=10)).distinct()
    return render(request, "frontend/table.html",
                  {"filtered_recipes": filtered_recipes,
                   "login": LOGIN_URL,
                   "logout": LOGOUT_URL})


def homepage(request: HttpRequest) -> HttpResponse:
    """ Shows main functionality """

    if request.method == "GET":
        form = AddProductForm()
        return render(request, "frontend/homepage.html", {"form": form})

    if request.method == "POST":
        return process_main_post(request, AddProductForm)
