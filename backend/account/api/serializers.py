from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password')
    def create(self, data):
        user = UserModel.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
        user.save()
        return user
    
class AccountLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')
    
class AccountDefaultSerializer(serializers.Serializer):
    pass