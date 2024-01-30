''' модуль для обработки логики отображения форм и их процессинга '''

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.forms import Form
from django.shortcuts import redirect, render
from django.urls import reverse

from apps.cook_book.services import add_product_to_recipe, cook_recipe


def process_main_post(request: HttpRequest, raw_form: Form) -> HttpResponse:
    ''' Принимает запрос и форму, и отдаёт серверный ответ с дополнительным контекстом. '''
    form = raw_form(request.POST)
    if form.is_valid():
        match request.POST['func']:
            case 'add_to_recipe':
                data = form.cleaned_data
                res = add_product_to_recipe(data['recipe'].id, data['product'].id, data['amount'])
                extra = f'Успешно изменен рецепт {data['recipe'].name}'
                return render(request, 'frontend/homepage.html',
                              {'extra': extra, 'form': raw_form}) if res is None else res
            case 'cook_recipe':
                res = cook_recipe(form.cleaned_data['recipe'].id)
                extra = f'Приготовили {form.cleaned_data['recipe'].name}'
                return render(request, 'frontend/homepage.html',
                              {'extra': extra, 'form': raw_form}) if res is None else res
            case 'show':
                if data := form.cleaned_data['product']:
                    return redirect(reverse('table', args=[data.id]))
                return HttpResponseNotFound("Not found")
            case _:
                return HttpResponseNotFound("Not found")
    else:
        return render(request, 'frontend/homepage.html', {"form": form, "errors": form.errors})
