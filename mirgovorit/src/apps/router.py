from django.urls import path, include


urlpatterns = [
   path('api/v1/users/', include('apps.users.urls'), name='users_api'),
   path('', include('apps.frontend.urls'), name='home'),
]
