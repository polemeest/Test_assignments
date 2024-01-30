from django.db import models

# Create your models here.


class PageUrl(models.Model):
    """ Хранит данные о присутствующих страницах """
    name = models.CharField(verbose_name="Название", max_length=50)
    url = models.CharField(verbose_name="Адрес", max_length=255)

    def __str__(self) -> str:
        return f"{self.name} --- {self.url}"
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
