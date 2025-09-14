>>> from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
>>> Author.objects.get(name=author_name), objects.filter(author=author)

# List all books in a library

>>> Library.objects.get(name=library_name)
>>> books.all()


# Retrieve  the librarian of a library

>>> Librarian.objects.get(library=librarian_name)