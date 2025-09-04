>>> from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
>>> author = Author.objects.get(name="J.K. Rowling")

# List all books in a library

>>> books_in_library = Library.objects.get(name=library_name)


# Retrieve  the librarian of a library
>>> librarian = library.librarianS