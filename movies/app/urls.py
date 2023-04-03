from django.urls import path, re_path
from .views import home, detail


urlpatterns = [
    path('', home, name='home'),
    path('<int:movie_id>', detail, name='detail'),
]