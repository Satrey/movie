from django.urls import path, re_path
from .views import news


urlpatterns = [
    path('', news, name='news')
]