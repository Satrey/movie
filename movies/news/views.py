from django.shortcuts import render
from .models import News


def news(request):
    newss = News.objects.all().order_by('-date')
    data = {'newss': newss}
    return render(request, 'news/news.html', context=data)
