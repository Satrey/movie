from django.db import models


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
