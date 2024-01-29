from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Recipe, RecipeProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ''' Представление для продуктов в панели администратора '''
    list_display = ('name', 'used', 'id')


class RecipeProductInline(admin.TabularInline):
    ''' Представление для полей заполнения промежуточной таблицы '''
    model = RecipeProduct
    extra = 1  # Number of empty forms to display


class RecipeAdminForm(forms.ModelForm):
    ''' Необходимо, чтобы убрать лишнее поле из модели в панели администратора'''
    class Meta:
        model = Recipe
        exclude = ['product']  

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ''' Представление для рецептов в панели администратора '''
    form = RecipeAdminForm
    inlines = [RecipeProductInline]

    def products_list_display(self, obj: Recipe):
        # Custom method to display a summary of related products in the list display
        prods = [f'{prod.product.name} - {prod.amount} гр' for prod in obj.recipeproduct_set.all()]
        return format_html(',<br>'.join(prods))
    products_list_display.short_description = 'Продукты'  # Column header in the list display

    list_display = ('name', 'products_list_display', 'id') 


