from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken import views
from django.contrib import admin


router = DefaultRouter()


router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
] #+ router.urls