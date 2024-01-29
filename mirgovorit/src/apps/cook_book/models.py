from django.db import models

# Create your models here.
class Product(models.Model):
    ''' Хранит название и количество приготовленных с продуктом блюд. '''
    name = models.CharField(verbose_name='название_продукта', max_length=75, null=False,  ## Явное лучше чем неявное
                            blank=False, unique=True)
    used = models.PositiveBigIntegerField(verbose_name='популярность', default=0, null=True,
                                  blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ''' Прописанные имена для панели администратора '''
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Recipe(models.Model):
    ''' Хранит название и продукты, используемые в рецепте. '''
    name = models.CharField(verbose_name='название рецепта', max_length=100, null=False,
                            blank=False, unique=True)
    product = models.ManyToManyField(Product, through='RecipeProduct', verbose_name='продукты',
                                     null=False, blank=False, related_name='products')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True,
                                      null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ''' Прописанные имена для панели администратора '''
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeProduct(models.Model):
    ''' Хранит связь между продуктом и рецептом. '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.PositiveIntegerField(verbose_name='вес в граммах', null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.product} - {self.amount}'
