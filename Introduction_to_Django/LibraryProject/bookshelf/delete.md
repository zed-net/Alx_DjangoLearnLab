# Import the Book model from your app's models.py file.
from bookshelf.models import Book

# First, retrieve the book instance to be deleted.
# We'll use the title updated in the last step: "Nineteen Eighty-Four"
>>> book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book from the database.
# The .delete() method returns a tuple with the number of objects deleted.
>>> book.delete()
(1, {'your_app_name.Book': 1})

# To confirm the deletion, try to retrieve the book again.
# This should raise a DoesNotExist error.
>>> Book.objects.get(title="Nineteen Eighty-Four")

# Expected output from the shell:
# Traceback (most recent call last):
# ...
# your_app_name.models.Book.DoesNotExist: Book matching query does not exist.
