from .base_serializer import *

class AccountSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        fields = ('username','email')
        
class AccountCreateSerializer(AccountBaseModelSerializer):
    class Meta(AccountBaseModelSerializer.Meta):
        fields = ('username', 'email', 'password')
        
    def create(self, data):
        user = UserModel.objects.create_user(email=data['email'], username=data['username'], password=data['password'])
        user.save()
        return user
    
class AccountLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
