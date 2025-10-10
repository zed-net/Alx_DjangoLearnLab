from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

# Alias the custom user model for cleaner code
User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration. Handles password hashing on creation.
    """
    # Explicitly defined fields using serializers.CharField and serializers.EmailField
    username = serializers.CharField(
        max_length=150, 
        required=True
    )
    email = serializers.EmailField(
        required=True
    )
    # Ensure password is included and write-only, using CharField explicitly
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'bio', 'profile_picture', 
            'first_name', 'last_name'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'followers': {'read_only': True} 
        }

    def create(self, validated_data):
        """
        Creates a new user instance and hashes the password using create_user.
        (Note: User is aliased from get_user_model() for brevity).
        """
        # We use User.objects.create_user() (which is get_user_model().objects.create_user())
        # to ensure the password is automatically hashed.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login and authentication check.
    """
    # Explicit use of serializers.CharField()
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    token = serializers.CharField(label=_("Token"), read_only=True)
    
    def validate(self, attrs):
        """
        Authenticates the user using username and password.
        """
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
