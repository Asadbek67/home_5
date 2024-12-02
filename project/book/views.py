from django.shortcuts import render
from .models import Author, Book, Review


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'authors/author_detail.html', {'author': author})

def review_list(request, book_id):
    reviews = Review.objects.filter(book_id=book_id)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})
