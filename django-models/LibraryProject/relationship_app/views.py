from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


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
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    
    
    template_name = 'relationship_app/registration/login.html'

class LogoutView(LogoutView):
    

    template_name = 'relationship_app/registration/logout.html'


def is_admin(user):
    """Checks if the user has the 'Admin' role."""
    # Assuming the UserProfile model is linked to the User model
    # and has a 'role' field.
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Role-Based Views ---
@user_passes_test(is_admin)
def AdminView(request):
    """A view accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def LibrarianView(request):
    """A view accessible only to Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def MemberView(request):
    """A view accessible only to Member users."""
    return render(request, 'relationship_app/member_view.html')

# --- Access Denied View ---
def not_allowed(request):
    """A view to show when a user does not have permission."""
    return render(request, 'not_allowed.html')
