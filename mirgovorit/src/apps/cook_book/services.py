""" Модуль для бизнес-логики поварской книги. Настраивает логирование, и:
        Содержит функции: 
            :get_recipe_model: - Принимает ID рецепта и отрабатывает возможные ошибки при получении
    экземпляра рецепта, возвращая его, если ошибок нет.
            :change_recipe: - Принимает модель рецепта, и добавляет ему продукт, если его нет, или
    меняет его вес."""

import os
import logging

from config.settings import BASE_DIR
from datetime import datetime
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from typing import Union

from .models import Recipe, RecipeProduct, Product


# настройки для логгера:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file = os.path.join(BASE_DIR, "logs", f"log_{datetime.now().strftime("%Y-%m-%d")}.txt")

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Основные функции:
def get_recipe_model(recipe_id: int) -> Union[Recipe, redirect]:
    """ Принимает ID рецепта и отрабатывает возможные ошибки при получении
    экземпляра рецепта, возвращая его, если ошибок нет. """
    try:
        return Recipe.objects.get(id=recipe_id)
    
    except Recipe.DoesNotExist as e:                 ## здесь можно добавить информацию из request, но сейчас не будем
        logging.error(f"запрошена несуществующая модель рецепта с id ({recipe_id})") 
        return redirect(reverse("homepage") + f"?error_param={e}") 
    
    except Recipe.MultipleObjectsReturned as e:
        count = 0, 
        for index, instance in enumerate(Recipe.objects.all().order_by("-created_at")):
            if index == 0:
                continue
            instance.delete()
            count += 1
        logging.debug(f"Получены множественные копии одного и того же рецепта. Удалено {count} старых записей")
        return redirect(reverse("homepage") + f"?error_param={e}") 
    

def change_recipe(model: Recipe, product_id: int, weight: int) -> None:
    """ Принимает модель рецепта, и добавляет ему продукт, если его нет, или
    меняет его вес. """
    try:
        product = Product.objects.get(id=product_id)
    except (Product.DoesNotExist, Product.MultipleObjectsReturned):
        logger.error(f"У нас проблемы с продуктом под id {product_id}")
        return HttpResponseNotFound
    products = model.product.all()
    # Если продукт уже есть:
    if product in [prod for prod in products]:
        product.amount = weight
        product.save()
    # Если его нет:
    else:
        new_product = RecipeProduct.objects.create(recipe=model,
                                                   product=product,
                                                   amount=weight)
        new_product.save()


def raise_cooking_amount(recipe: Recipe) -> None:
    """ Принимает id рецепта, и увеличивает популярность продуктов, в составе на 1. """
    for prod in recipe.product.all():
        prod.used += 1
        prod.save()


    