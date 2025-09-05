from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', views.list_books, name='book-list'),

    # URL for the class-based view to show a specific library's details
    # The <int:pk> part captures the primary key of the library from the URL.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
     path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logout'), name='logout'),
]
