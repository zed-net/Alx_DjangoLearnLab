from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer, UserSerializer
from .models import CustomUser
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

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


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow_user(self, request, pk=None):
        """Allows an authenticated user to toggle following/unfollowing another user.
        
        This action is named 'follow_user' to resolve the reported AttributeError.
        """
        
        # self.get_object() is the standard way to retrieve the detail object and handles 404
        user_to_toggle = self.get_object() 
        follower_user = request.user 

        if user_to_toggle == follower_user:
            return Response(
                {"detail": "You cannot follow or unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Assumes the 'following' M2M field exists on the User model
        is_following = follower_user.following.filter(pk=user_to_toggle.pk).exists()

        if is_following:
            # Unfollow logic
            follower_user.following.remove(user_to_toggle)
            return Response(
                {"detail": f"You have unfollowed {user_to_toggle.username}."}, 
                status=status.HTTP_200_OK # 200 OK for successful removal/change
            )
        else:
            # Follow logic
            follower_user.following.add(user_to_toggle)
            return Response(
                {"detail": f"You are now following {user_to_toggle.username}."}, 
                status=status.HTTP_201_CREATED # 201 Created for a new relationship
            )

