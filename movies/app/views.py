from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie


def home(request):
    search_movie = request.GET.get('search_movie')
    print(search_movie)
    if search_movie:
        movies = Movie.objects.filter(title__iregex=search_movie)
    else:
        movies = Movie.objects.all()

    return render(request, 'app/home.html', {'name': 'Фёдор', 'search_movie': search_movie, 'movies': movies})


def about(request):
    return render(request, '<h1>Это страница о нашем замечательном проекте "MOVIES"</h1>')


def sign_up(request):
    email = request.GET.get('email')
    print(email)
    return render(request, 'app/sign_up.html', {'email': email})
