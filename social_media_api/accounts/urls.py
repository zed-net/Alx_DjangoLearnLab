from django.urls import path, include
from .views import RegisterView, CustomAuthToken, UserProfileView, UserViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', CustomAuthToken.as_view(), name='login'),      # User login & token retrieval
    path('profile/', UserProfileView.as_view(), name='profile'),  # View or update user profile
    path('', include(router.urls)),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user') 
]
