from .views import get_url, create_url, url_detail, redirect_url, stats_url
from django.urls import path

# from . import views
# from django.views import defaults
urlpatterns = [
    path('URLs', get_url, name='get_url'),
    path('', create_url, name='create_url'),  
    path('<int:pk>', url_detail, name='detail_url'), 
    path('<str:shortCode>', url_detail, name='redirect_url'), #redirect_url
    path('<str:shortCode>/stats', stats_url, name='stats_url')
]