from django.shortcuts import render

def home(request):
    # You can add logic here to fetch data or perform any other actions needed
    # For now, we'll just render a simple template
    return render(request, 'home/home.html')

def books(request):

    return render(request, 'books/books.html')
