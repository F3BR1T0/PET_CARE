from .base_viewset import *
from ...models import HistoricoMedico, Pet
from ..serializers.historico_medico_serializer import HistoricoMedicoSerializer, HistoricoMedicoUpdateSerializer

class PetHistoricoMedicoViewSet(PetBaseViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    def get_serializer_class(self):
        action_serializers = {
            "update": HistoricoMedicoUpdateSerializer
        }
        return action_serializers.get(self.action, HistoricoMedicoSerializer)
    
    def get_queryset(self):
        petowner = self._get_petowner()
    
        # Obtém os pets do petowner que possuem um histórico médico associado
        pets_with_historico = Pet.objects.filter(dono=petowner, historico_medico__isnull=False)
        
        # Recupera os objetos HistoricoMedico associados a esses pets
        historicos_medicos = HistoricoMedico.objects.filter(id__in=[pet.historico_medico.id for pet in pets_with_historico])

        # Verifica se há históricos médicos encontrados
        if not historicos_medicos.exists():
            raise HistoricoMedico.DoesNotExist("Nenhum histórico médico encontrado para este dono.")
        
        return historicos_medicos
    