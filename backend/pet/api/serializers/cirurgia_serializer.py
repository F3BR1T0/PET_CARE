from .base_serializer import *
from ...models import Cirurgia

class CirurgiaSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = Cirurgia
