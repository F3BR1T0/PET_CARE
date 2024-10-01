from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pet_owners.api import serializers
from pet_owners import models
from pet_owners.api.permissions import HasShareJunoApiKey

class PetOwnersViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.PetOwnersSerializers
    queryset = models.PetOwners.objects.all()
    
    def get_serializer_class(self):
        if self.action == "find_by_email":
            return serializers.PetOwnersOnlyEmailSerializers
        return super().get_serializer_class()
        
    @action(detail=False, methods=['post'], permission_classes=[HasShareJunoApiKey], url_path='findbyemail')
    def find_by_email(self, request):
        email = request.data['email']
        pet_owner = models.PetOwners.objects.filter(email=email).first()
        if pet_owner:
            response_serializer = serializers.PetOwnersSerializers(pet_owner)
            return Response(response_serializer.data, status=200)
        return Response({'detail': 'Pet owner not found'}, status=404)
    
    
 
    