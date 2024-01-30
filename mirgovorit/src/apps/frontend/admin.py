from django.contrib import admin
from .models import PageUrl
# Register your models here.


@admin.register
class PageUrlAdmin(PageUrl):
    """ Представление в панели администратора """
    list_display = ("name", "url", "id")
