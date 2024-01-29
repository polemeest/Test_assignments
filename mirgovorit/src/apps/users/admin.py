from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ''' Представление для продуктов в панели администратора '''
    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'created_at',
                    'is_verified', 'balance', 'user_type')

