from .base_viewset import *
from ..serializers import CirurgiaSerializer
from ...models import Cirurgia, Pet

class CirurgiaViewSet(PetBaseViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_queryset(self):
        petowner = self._get_petowner()
        pets_with_historico = Pet.objects.filter(dono=petowner, historico_medico__isnull=False)
        historico_ids = [pet.historico_medico.id for pet in pets_with_historico]
        print(self.action)
        return Cirurgia.objects.filter(historico_medico_id__in=historico_ids)
    
    def get_serializer_class(self):
        return CirurgiaSerializer
    
    def create(self, request, *args, **kwargs):
        print(self.action)
        return super().create(request, *args, **kwargs)