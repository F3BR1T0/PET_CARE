from django.utils import timezone
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from pet_owners import models
from account.models import AppAccount

UserModel = AppAccount

class PetOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
        
class PetOwnerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
        
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.foto = validated_data['foto']
        instance.cpf = validated_data['cpf']
        instance.email = validated_data['email']
        instance.telefone = validated_data['telefone']
        instance.updated_at = timezone.now()
        instance.save()
        return instance
class PetOwnersOnlyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)