from .base_serializer import SerializerUtils
from ...models import Pet

class PetSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = Pet
        pass

class PetCreateUpdateSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = Pet
        exclude = ['dono','historico_medico']