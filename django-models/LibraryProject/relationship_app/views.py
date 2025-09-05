from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book, Author, Library, Librarian
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    
    # The model this view will operate on
    model = Library
    
    # The name of the template file to render
    template_name = 'library_detail.html'
    
    # The name of the variable that will hold the library object in the template.
    context_object_name = 'library'
    

