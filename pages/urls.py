from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]

