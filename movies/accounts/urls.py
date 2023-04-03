from django.urls import path, re_path
from .views import sign_up_account

urlpatterns = [
    path('sign_up_account/', sign_up_account, name='sign_up_account')
]