from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def sign_up_account(request):
    if not request.method == 'GET':
        return render(request, 'accounts/sign_up_account.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['password'])
            user.save()
            login(request, user)
            return redirect('home')
