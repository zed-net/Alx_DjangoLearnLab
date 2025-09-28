from django.shortcuts import render
from . models import Book
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework import permissions


class ListView(generics.ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
class DetailView(generics.DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class CreateView(generics.CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class UpdateView(generics.UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class DeleteView(generics.DestroyView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 
