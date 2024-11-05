from .base_vet_viewset import *
from ....models import Pet
from ...serializers import PetDetailSerializer, MedicineSaveSerializer

class VetPetViewSet(BaseVetAuthenticatedViewSet, mixins.RetrieveModelMixin):
    
    def get_serializer_class(self):
        return PetDetailSerializer
    
    def get_queryset(self):
        return Pet.objects.all()

    