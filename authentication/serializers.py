from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password', 'role', 'phone_number', 'address']

    def validate(self, data):
        # Check if username already exists
        if CustomUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already taken."})

        # Check if email already exists
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "An account with this email already exists."})

        # Check if passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid email or password.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username"]