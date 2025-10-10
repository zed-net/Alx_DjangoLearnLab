from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Minimal serializer for displaying user info in Post and Comment responses."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for handling comment creation, retrieval, and display."""
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        """Attach the current user as the comment author."""
        request = self.context.get('request')
        user = request.user if request else None
        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts, including nested comments."""
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        """Assign the logged-in user as the post author."""
        request = self.context.get('request')
        user = request.user if request else None
        post = Post.objects.create(author=user, **validated_data)
        return post
