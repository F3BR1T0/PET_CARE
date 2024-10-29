from .base_serializer import SerializerUtils
from ...models import Doenca

class DoecaSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Doenca
        exclude = ['id']