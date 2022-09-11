from django.db.models import Avg
from django.db.models.functions import Round
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        exclude = ['id', 'user']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True}}
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError('Passwords don\'t match.')
        
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError('Username is taken.')
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError('Email is in use by an existing account.')
        
        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        
        return account