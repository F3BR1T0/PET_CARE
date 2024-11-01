from .base_serializer import SerializerUtils
from .medicamento_serializer import MedicamentoAdministradoSerializer
from .cirurgia_serializer import CirurgiaSerializer
from .doenca_documentada_serializer import DoencaDocumentadaSerializer
from ...models import HistoricoMedico

class HistoricoMedicoBaseSerializer(SerializerUtils.BaseModelSerializer):
     class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = HistoricoMedico

class HistoricoMedicoSerializer(HistoricoMedicoBaseSerializer):
    medicamentos_administrados = MedicamentoAdministradoSerializer(many=True, read_only=True)
    cirurgias = CirurgiaSerializer(many=True, read_only=True, source='cirurgias_administradas')
    doencas_documentadas = DoencaDocumentadaSerializer(many=True, read_only=True)
    class Meta(HistoricoMedicoBaseSerializer.Meta):
        pass

class HistoricoMedicoUpdateSerializer(HistoricoMedicoBaseSerializer):
    class Meta(HistoricoMedicoBaseSerializer.Meta):
        pass