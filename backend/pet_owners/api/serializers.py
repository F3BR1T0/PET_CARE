from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from pet_owners import models
from account.models import AppAccount

UserModel = AppAccount

class PetOwnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
    
        
class PetOwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'
        
class PetOwnersOnlyEmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = ('email',)