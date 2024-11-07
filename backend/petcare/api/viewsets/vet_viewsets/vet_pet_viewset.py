from .base_vet_viewset import *
from ....models import Pet, Medicine
from ...serializers import PetDetailSerializer, MedicineSaveSerializer


class VetPetBaseVewSet(BaseVetAuthenticatedViewSet):
    def get_queryset(self):
        return Pet.objects.all()

class VetPetViewSet(VetPetBaseVewSet, mixins.RetrieveModelMixin):
     
    def get_serializer_class(self):
        return PetDetailSerializer
    
class VetPetMedicineViewSet(VetPetBaseVewSet, mixins.RetrieveModelMixin):
     
    def get_serializer_class(self):
        return MedicineSaveSerializer
    
    @action(detail=True, methods=['post'], url_path="add-medicine")
    def add_medicine(self, request, pk: None):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        pet = self.get_queryset().filter(id = pk).first()
        if pet is None:
            return Response('Pet not found.')
        
        medicine_saved = serializer.save(medical_history = pet.medical_history)
        
        if medicine_saved:
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class VetPetMedicineDetailsViewSet(VetPetBaseVewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return MedicineSaveSerializer
    
    def get_queryset(self):
        return Medicine
    
    
        
        
        
        

    