from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='app/images/')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = ('Видео')
        verbose_name_plural = ('Видео')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_again = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = ('Обзор')
        verbose_name_plural = ('Обзоры')
