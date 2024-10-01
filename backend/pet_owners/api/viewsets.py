from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

from pet_owners.api import serializers
from pet_owners import models

class PetOwnersViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    
    serializer_class = serializers.PetOwnersSerializers
    queryset = models.PetOwners.objects.all()