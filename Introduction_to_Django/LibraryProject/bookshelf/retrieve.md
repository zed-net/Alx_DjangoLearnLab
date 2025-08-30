# You can retrieve the book by its title, which is now '1984'.
>>> book = Book.objects.get(title="1984")

# Display all attributes of the book.
>>> print(f"Title: {book.title}")
>>> print(f"Author: {book.author}")
>>> print(f"Publication Year: {book.publication_year}")

# Expected output from the shell:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
