from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, data):
        user = UserModel.objects.create_user(email=data['email'], password=data['password'])
        user.username = data['username']
        user.save()
        return user