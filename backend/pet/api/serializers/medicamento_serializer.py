from .base_serializer import *
from .vacina_serializer import VacinaSerializer
from .vermifugo_serializer import VermifugoSerialzier
from ...models import MedicamentoAdministrado

class MedicamentoAdministradoExcludeSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta:
        model = MedicamentoAdministrado

class MedicamentoAdministradoSerializer(SerializerUtils.BaseModelSerializer):
    vacina = VacinaSerializer(read_only=True)
    vermifugo = VermifugoSerialzier(read_only=True)
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = MedicamentoAdministrado
        
class MedicamentoAdministradoVacinaSerializer(MedicamentoAdministradoExcludeSerializer):
    class Meta(MedicamentoAdministradoExcludeSerializer.Meta):
        exclude=['vermifugo']
        
class MedicamentoAdministradoVermifugoSerializer(MedicamentoAdministradoExcludeSerializer):
    class Meta(MedicamentoAdministradoExcludeSerializer.Meta):
        exclude=['vacina']
        