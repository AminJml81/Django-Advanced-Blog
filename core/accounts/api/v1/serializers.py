from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from ...models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    password2 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']


    def validate(self, attrs):
        password, password2 = attrs['password'], attrs['password2']
        if password != password2:
            raise serializers.ValidationError({'detail': 'passwords does not match'})
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})
        return super().validate(attrs)
    

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)