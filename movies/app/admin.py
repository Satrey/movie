from django.contrib import admin
from .models import Movie, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'text', 'user', 'date')
    list_filter = ('movie', 'user', 'date')
    search_fields = ('movie', 'text', )


admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)
