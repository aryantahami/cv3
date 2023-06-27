from django.urls import path
from .views import article_detail, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
]
