from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book, Author, Library, Librarian
from django.views.generic import DetailView

def book_list(request):
    # Retrieve all Book objects from the database
    books = Book.objects.all()
    
    book_list_string = "List of Books:\n\n"
    for book in books:
        # Assuming the Book model has a `title` and a `author` field.
        book_list_string += f"Title: {book.title}, Author: {book.author}\n"
        
    return HttpResponse(book_list_string)

class LibraryDetailView(DetailView):
    
    # The model this view will operate on
    model = Library
    
    # The name of the template file to render
    template_name = 'library_detail.html'
    
    # The name of the variable that will hold the library object in the template.
    context_object_name = 'library'
