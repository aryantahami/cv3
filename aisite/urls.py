from django.urls import path
from .views import site_list, site_detail

urlpatterns = [
    path('sites/', site_list, name='site_list'),
    path('sites/<int:site_id>/', site_detail, name='site_detail'),
]
