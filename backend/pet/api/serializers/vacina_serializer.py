from .base_serializer import *
from ...models import Vacina

class VacinaSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Vacina
        exclude = ['id']
