from django.urls import path
from .views import get_news, create_news

urlpatterns = [
    path('', get_news, name='news'),
    path('create/', create_news, name = 'create')
]
