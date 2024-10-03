from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

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
        
class AccountResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True, write_only=True)
    
    def validate_email(self, value):
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('User with this email does not exist.'))
        return value
    
    def save(self):
        email = self.validated_data.get('email')
        new_password = self.validated_data.get('new_password')
        user = UserModel.objects.get(email=email)
        user.set_password(new_password)
        user.save()
    
class AccountDefaultSerializer(serializers.Serializer):
    pass