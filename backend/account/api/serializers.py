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
    
class AccountLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
        
class AccountResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, write_only=True)
    
    def save(self, id):
        new_password = self.validated_data.get('new_password')
        user = UserModel.objects.get(id=id)
        user.set_password(new_password)
        user.save()
        
class AccountRequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    def validate_email(self, value):
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('User with this email does not exist.'))
        return value
    
    def get_user(self):
        return UserModel.objects.get(email=self.validated_data.get('email'))

class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.save()
        return instance
    
class AccountChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)

    def get_user(id):
        return UserModel.objects.get(id=id)
    
    def update(self,instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
        
class AccountDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        
class AccontSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
class AccountLogoutSerializer(serializers.Serializer):
    pass