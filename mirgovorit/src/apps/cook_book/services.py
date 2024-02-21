""" Модуль для бизнес-логики поварской книги и настраивает логирование """

import os
import logging

from config.settings import BASE_DIR
from datetime import datetime
from django.db.models import F
from django.shortcuts import get_object_or_404
from typing import Union

# Create your views here.

from .models import Recipe, Product


# настройки для логгера:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_file = os.path.join(BASE_DIR, "logs",
                        f"log_{datetime.now().strftime("%Y-%m-%d")}.txt")

file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Основные функции:
def get_recipe_model(recipe_id: int) -> Union[Recipe, dict]:
    """ Принимает ID рецепта и отрабатывает возможные ошибки при получении
    экземпляра рецепта, возвращая его, если ошибок нет. """
    try:
        return Recipe.objects.get(id=recipe_id)

    except Recipe.DoesNotExist:  # здесь можно добавить информацию из request
        logger.error(
            f"запрошена несуществующая модель рецепта с id ({recipe_id})"
        )
        return {"primary_key": [f"Нет рецепта с id {recipe_id}"]}

    except Recipe.MultipleObjectsReturned:
        last = Recipe.objects.latest("created_at")
        deletion = Recipe.objects.filter(id=recipe_id)\
            .exclude(created_at=last.created_at).delete()
        logger.debug(f"Получены множественные копии одного и того же рецепта. \
                      Удалено {deletion[0]} старых записей")
        return last


def change_recipe(model: Recipe, product_id: int, weight: int) -> None:
    """ Принимает модель рецепта, и добавляет ему продукт, если его нет, или
    меняет его вес. """
    model.recipeproduct_set.update_or_create(
        product=product_id,
        defaults={"amount": weight if weight else 1},
        create_defaults={"recipe": model,
                         "product": get_object_or_404(Product, id=product_id),
                         "amount": weight if weight else 1}
    )


def add_product_to_recipe(recipe_id: int, product_id: int,
                          weight: int) -> None:
    """ Функция добавляет к указанному рецепту указанный продукт с указанным
    весом. Если в рецепте уже есть такой продукт, то функция должна поменять
    его вес в этом рецепте на указанный. """
    model = get_recipe_model(recipe_id)
    if not isinstance(model, Recipe):
        return model
    change_recipe(model, product_id, weight)


def raise_cooking_amount(recipe_id: int) -> None:
    """ Функция увеличивает на единицу количество приготовленных блюд для
    каждого продукта, входящего в указанный рецепт. """
    model: Recipe = get_recipe_model(recipe_id)
    if not isinstance(model, Recipe):
        return model
    model.product.all().update(used=F("used") + 1)
