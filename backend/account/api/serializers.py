from rest_framework import serializers
from pet_care_backend.utils import SerializerUtils
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()

class AccountBaseModelSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = UserModel

class AccountSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        pass
        
class AccountCreateSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        fields = ('email', 'username', 'password')
        
    def create(self, data):
        user = UserModel.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
        user.save()
        return user
    
class AccountUpdateSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        fields = ('username','email')

class AccountLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
        
class AccountRequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    def validate_email(self, value):
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('User with this email does not exist.'))
        return value
    
    def get_user(self):
        return UserModel.objects.get(email=self.validated_data.get('email'))
    
class AccountChangePasswordSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        fields = ('password',)    
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
        

