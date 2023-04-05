from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Movie, Review
from .forms import ReviewForm


def home(request):
    search_movie = request.GET.get('search_movie')
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


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie_id)
    return render(request, 'app/detail.html', {'movie': movie, 'reviews': reviews})


def review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'app/review.html', {'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.movie = movie
            new_review.user = request.user
            new_review.save()
            return redirect('detail', new_review.movie_id)
        except ValueError:
            return render(request, 'app/review.html', {'form': ReviewForm(), 'error': 'Invalid request'})


def update(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'app/update.html', {'form': form, 'review': review})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'app/update.html', {'review': review, 'form': form, 'error': 'Invalid request'})


def delete(request, review_id):
    review= get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)

