from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/article_detail.html', {'article': article})


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

