# Retrieve the book instance you want to update.
# Its title is currently '1984'
>>> book = Book.objects.get(title="1984")

# Change the value of the 'title' attribute.
>>> book.title = "Nineteen Eighty-Four"

# Save the changes back to the database.
>>> book.save()

# To confirm the update, you can retrieve the book again using the new title.
>>> updated_book = Book.objects.get(title="Nineteen Eighty-Four")
>>> print(updated_book.title)

# Expected output from the shell:
# Nineteen Eighty-Four
