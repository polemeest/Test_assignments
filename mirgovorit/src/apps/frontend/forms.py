from django import forms
from apps.cook_book.models import Recipe, Product


class AddProductForm(forms.Form):
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all(), empty_label="Выбрать рецепт",
                                    label="Рецепт", required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="Выбрать продукт",
                                     label="Продукт", required=False)
    amount = forms.IntegerField(min_value=1, label="Вес в граммах", required=False)

    def clean(self):
        cleaned_data = super().clean()
        if (not cleaned_data.get('recipe') or not cleaned_data.get('product')) \
                and self.data['func'] != 'show':
            empty = ('recipe', 'product')[bool(cleaned_data['recipe'])]
            raise forms.ValidationError({empty: "Нужно выбрать один из вариантов"})
        return cleaned_data
