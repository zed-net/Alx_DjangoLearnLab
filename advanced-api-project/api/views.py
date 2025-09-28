from django.shortcuts import render
from . models import Book
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class ListView(generics.ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "author", "publication_year"]
    filter_backends = [filters.SearchFilter]
    SearchFilter = ['title', 'author']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    OrderingFilter = ['title', 'publication_year']

    
    
class DetailView(generics.DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    SearchFilter = ['title', 'author']
    OrderingFilter = ['title', 'publication_year']

    
    
class CreateView(generics.CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    OrderingFilter = ['title', 'publication_year']
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class UpdateView(generics.UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    OrderingFilter = ['title', 'publication_year']
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class DeleteView(generics.DestroyView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    OrderingFilter = ['title', 'publication_year']
