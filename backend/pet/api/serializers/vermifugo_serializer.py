from .base_serializer import *
from ...models import Vermifugo

class VermifugoSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Vermifugo
        exclude = ['id']