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
    
    path('admin-view/', views.admin_view, name='admin_view'),
    
    # URL for the Librarian-only view, accessible at /librarian-view/
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    
    # URL for the Member-only view, accessible at /member-view/
    path('member-view/', views.member_view, name='member_view'),
    
    # Optional URL for an access denied page
    path('not-allowed/', views.not_allowed, name='not_allowed'),
    
    path('add/', views.add_book, name='add_book'),

    # Path for editing an existing book, identified by its primary key (pk).
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),

    # Path for deleting a book, also identified by its primary key.
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]
