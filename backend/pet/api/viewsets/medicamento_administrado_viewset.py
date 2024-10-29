from .base_viewset import *
from ..serializers import MedicamentoAdministradoSerializer, MedicamentoAdministradoVacinaSerializer, MedicamentoAdministradoVermifugoSerializer
from ...models import MedicamentoAdministrado, Pet
from pet_care_backend.utils import ResponseMixin

class MedicamentoAdministradoBaseViewSet(PetBaseViewSet, ResponseMixin):
    def get_queryset(self):
        petowner = self._get_petowner()
        # Obtém todos os pets do petowner que possuem um historico_medico
        pets_with_historico = Pet.objects.filter(dono=petowner, historico_medico__isnull=False)
        
        # Coleta todos os IDs dos históricos médicos dos pets encontrados
        historico_ids = [pet.historico_medico.id for pet in pets_with_historico]

        # Filtra os medicamentos administrados que estão associados a esses históricos médicos
        return MedicamentoAdministrado.objects.filter(historico_medico_id__in=historico_ids)
        
class MedicamentoAdministradoVacinaViewSet(MedicamentoAdministradoBaseViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
       return MedicamentoAdministradoVacinaSerializer
   
class MedicamentoAdministradoVermifugoViewSet(MedicamentoAdministradoBaseViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return MedicamentoAdministradoVermifugoSerializer