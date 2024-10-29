from .base_serializer import *
from ...models import Vermifugo

class VermifugoSerialzier(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Vermifugo
        exclude = ['id']