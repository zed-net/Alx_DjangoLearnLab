from rest_framework import serializers
from . models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        
    def validate_publication_year(self, value):
        if value['publication_year'] < 0 or value['publication_year'] > 2025:
            raise serializers.ValidationError("Publication year must be between 0 and 2025.")
        return value
    
    
class AuthorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        
    books = BookSerializer(many=True, read_only=True)