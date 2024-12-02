"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('reviews/<int:book_id>/', views.review_list, name='review_list'),
    path('author/<int:id>/', views.author_detail, name='author_detail'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
