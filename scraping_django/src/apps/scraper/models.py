"""All models are described here as there aren"t many of them and it"s a 
    simple application. 
        ScrapedData: contains data for each article gathered from a resourse.
        Keywords: contains keyword for scraping resourse."""

from django.db import models


class ScrapedData(models.Model):
    """Table for storing main scraped data from given resourse. 
    Main rows: headline, text. Info rows: timestamp, author."""
    headline = models.CharField(verbose_name="Заголовок",
                                null=False,  blank=False, max_length=200)
    timestamp = models.DateTimeField(verbose_name="Дата публикации",
                                     null=False, blank=False)
    author = models.CharField(verbose_name="Автор",
                                null=True,  blank=True, max_length=125)
    text = models.TextField(verbose_name="Текст статьи", 
                            null=False, blank=False)
    
    class Meta:
        verbose_name="Собранные данные"
        verbose_name_plural="Собранные данные"
        ordering=["-timestamp"]


class Keywords(models.Model):
    """Table for storing searching keywords. The only field:keyword is a pk."""
    keyword = models.CharField(verbose_name="Ключевое слово", null=False,
                               blank=False, primary_key=True, unique=True,
                               max_length=100)
    class Meta:
        verbose_name="Ключевое слово"
        verbose_name_plural="Ключевые слова"
        ordering=["keyword"]