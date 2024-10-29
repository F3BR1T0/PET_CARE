from .base_viewset import *
from ..serializers import PetCreateUpdateSerializer, PetSerializer
from pet_care_backend.utils import ResponseMixin
from ...models import Pet, HistoricoMedico

class PetViewSet(PetBaseViewSet, ResponseMixin, viewsets.ModelViewSet):
    def get_queryset(self):
        petowner = self._get_petowner()
        queryset = Pet.objects.filter(dono = petowner)
        return queryset
    
    def get_serializer_class(self):
        action_serializers = {
            "create": PetCreateUpdateSerializer,
            "update": PetCreateUpdateSerializer
        }
        return action_serializers.get(self.action, PetSerializer)
    
    def partial_update(self, request, *args, **kwargs):
         return http.response_bad_request_400("Not implemented.")
     
    def create(self, request, *args, **kwargs):
        petowner = self._get_petowner()
        if petowner is None:
            return http.response_bad_request_400("Pet Owner does not exist.")
        
        # Valida os dados do serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Cria o histórico médico e salva o pet
        historico_medico = HistoricoMedico.objects.create()
        pet = serializer.save(dono=petowner, historico_medico=historico_medico)
        
        
        return http.response_as_json(PetSerializer(pet).data, status.HTTP_201_CREATED)
