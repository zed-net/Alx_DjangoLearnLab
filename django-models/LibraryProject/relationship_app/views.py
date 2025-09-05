from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    
    # The model this view will operate on
    model = Library
    
    # The name of the template file to render
    template_name = 'relationship_app/library_detail.html'
    
    # The name of the variable that will hold the library object in the template.
    context_object_name = 'library'
    
    
def register(request):
    
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    else:
            form = UserCreationForm()
    return render(request, 'relationship_app/registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    
    
    template_name = 'relationship_app/registration/login.html'

class CustomLogoutView(LogoutView):
    

    template_name = 'relationship_app/registration/logout.html'


