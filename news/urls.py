from django.urls import path
from .views import get_news, create_news, get_new, update_new, delete_new

urlpatterns = [
    path('', get_news, name='news'),
    path('create/', create_news, name = 'create'),
    path('detail/<int:pk>/', get_new, name='detail'),
    path('update/<int:pk>/',update_new, name='update'),
    path('delete/<int:pk>/', delete_new, name='delete'),
]
