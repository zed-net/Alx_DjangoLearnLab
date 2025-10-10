from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from rest_framework import status



class IsOwnerOrReadOnly(permissions.BasePermission):
   
    

    def has_object_permission(self, request, view, obj):
        # Safe methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Custom Permission
class IsOwnerOrReadOnly(permissions.BasePermission):
   

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.author == request.user


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
        
        
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    
    # Get all users this user follows
    following_users = profile.following.all()
    
    # Get posts by followed users (and optionally include user’s own posts)
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    Like.objects.create(post=post, user=user)

    # ✅ Create a notification for the post author
    if post.author != user:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

