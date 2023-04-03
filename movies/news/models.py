from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    date = models.DateField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.headline[:50]
