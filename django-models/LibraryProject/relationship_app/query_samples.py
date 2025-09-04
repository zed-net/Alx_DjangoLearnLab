>>> from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
>>> asimov = Author.objects.get(name="Isaac Asimov")
>>> asimov_books = asimov.books.all()

# List all books in a library

>>> alexandria = Library.objects.get(name="Alexandria Library")
>>> library_books = alexandria.books.all()


# Retrieve  the librarian of a library
>>> alexandria = Library.objects.get(name="Alexandria Library")
>>> librarian = alexandria.librarian