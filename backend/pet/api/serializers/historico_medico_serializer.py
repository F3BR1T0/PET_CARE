from .base_serializer import SerializerUtils
from .medicamento_serializer import MedicamentoAdministradoSerializer
from ...models import HistoricoMedico

class HistoricoMedicoSerializer(SerializerUtils.BaseModelSerializer):
    medicamentos_administrados = MedicamentoAdministradoSerializer(read_only=True)
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = HistoricoMedico