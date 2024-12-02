from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Kitoblar ro'yxatini ko'rsatish
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Muayyan kitob detali
]
