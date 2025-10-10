from django.urls import path
from .views import RegisterView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', CustomAuthToken.as_view(), name='login'),      # User login & token retrieval
    path('profile/', UserProfileView.as_view(), name='profile'),  # View or update user profile
]
