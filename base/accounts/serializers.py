from rest_framework import serializers
from .models import MyUser


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Password do not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return MyUser.objects.create_user(**validated_data)
