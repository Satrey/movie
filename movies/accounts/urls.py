from django.urls import path, re_path
from .views import sign_up_account, logout_account, login_account

urlpatterns = [
    path('sign_up_account/', sign_up_account, name='sign_up_account'),
    path('logout/', logout_account, name='logout_account'),
    path('login/', login_account, name='login_account'),
]