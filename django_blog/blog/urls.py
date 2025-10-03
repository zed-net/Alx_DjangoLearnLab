from django.urls import path
from .views import (
PostListView, PostDetailView,
PostCreateView, PostUpdateView, PostDeleteView
)
from django.urls import path
from . import views


urlpatterns = [
path('post/', PostListView.as_view(), name='post-list'),
path('post/new/', PostCreateView.as_view(), name='post-create'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),   
path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-edit'),
path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),


path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]