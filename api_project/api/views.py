from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response


class BookList(generics.ListAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    
    
# class ProtectedView(APIView):
   
#     def get(self, request):
#         # The 'request.user' object is available because the user
#         # was successfully authenticated by the DRF backend.
#         user = request.user
        
#         return Response({
#             "message": f"Hello, {user.username}! You are successfully authenticated and have accessed a protected resource."
#         })

# class PrivateDataView(APIView):
    
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({
#             "message": "This is private data, available only to logged-in users."
#         })

# class AdminDataView(APIView):
   
#     permission_classes = [IsAuthenticated, IsAdminUser]
    
#     def get(self, request):
#         return Response({
#             "message": "Welcome, Admin! This resource is for administrators only."
#         })
