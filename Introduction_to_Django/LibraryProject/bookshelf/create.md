# First, open the Django shell with: python manage.py shell

# Import your Book model
>>> from bookshelf.models import Book

# Create the new book instance
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output from the shell:
# <Book: 1984 by George Orwell>
