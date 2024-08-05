from django.shortcuts import render
from .models import Book

def book_list(request):
    # Without select_related
    books = Book.objects.all()
    for book in books:
        print(book.title, book.author.name)
    print('************************************************')
    # With select_related
    books = Book.objects.select_related('author').all()
    for book in books:
        print(book.title, book.author.name)

    return render(request, 'book_list.html', {'books': books})
