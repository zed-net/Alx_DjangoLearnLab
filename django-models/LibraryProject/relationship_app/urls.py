from django.urls import path
from . import views

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', views.book_list, name='book-list'),

    # URL for the class-based view to show a specific library's details
    # The <int:pk> part captures the primary key of the library from the URL.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
