from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from pet_owners import models
from account.models import AppAccount

UserModel = AppAccount

class PetOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
class PetOwnerSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        exclude = ['address']
class PetOwnersOnlyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)