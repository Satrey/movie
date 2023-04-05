from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm, UserAuthForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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


def logout_account(request):
    logout(request)
    return redirect('home')


def login_account(request):
    if request.method == 'GET':
        return render(request, 'accounts/login_account.html', {'form': UserAuthForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/login_account.html', {'form': UserAuthForm(),
                                                                   'error': 'Username or password do not match'})
        else:
            login(request, user)
            return redirect('home')