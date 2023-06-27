from django.shortcuts import render
from article.models import Article


def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)
