from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def books_view(request):
    
    return render(request, 'books/books.html') 

def add_book(request):
    
    return render(request, 'books/add_book.html')
