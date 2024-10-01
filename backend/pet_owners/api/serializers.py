from rest_framework import serializers
from pet_owners import models

class PetOwnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PetOwners
        fields = '__all__'