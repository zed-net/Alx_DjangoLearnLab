from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import viewsets


class BookList(generics.ListAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    