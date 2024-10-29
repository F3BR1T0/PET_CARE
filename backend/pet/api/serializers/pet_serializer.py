from .base_serializer import SerializerUtils
from .historico_medico_serializer import HistoricoMedicoSerializer
from ...models import Pet

class PetSerializer(SerializerUtils.BaseModelSerializer):
    historico_medico = HistoricoMedicoSerializer(read_only=True)
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = Pet
        pass

class PetCreateUpdateSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Pet
        exclude = ['dono','historico_medico']