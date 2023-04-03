from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def sign_up_account(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up_account.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'accounts/sign_up_account.html',
                              {'form': UserCreateForm, 'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'accounts/sign_up_account.html', {'form': UserCreateForm,
                                                                     'error': 'Password do not match'})
