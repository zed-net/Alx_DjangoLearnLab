from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response, get_object_or_404 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer, UserSerializer
from .models import CustomUser
from rest_framework.decorators import action

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserViewSet(generics.ListAPIView):
    """
    Provides list/retrieve endpoints and custom actions for follow/unfollow.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."},
                        status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."},
                        status=status.HTTP_200_OK)