from django.urls import path, re_path
from .views import home, detail, review, update, delete


urlpatterns = [
    path('', home, name='home'),
    path('<int:movie_id>', detail, name='detail'),
    path('<int:movie_id>/review', review, name='review'),
    path('reviews/<int:review_id>', update, name='update'),
    path('reviews/<int:review_id>/delete/', delete, name='delete'),
]