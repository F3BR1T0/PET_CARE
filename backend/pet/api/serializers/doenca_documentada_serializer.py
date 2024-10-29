from .base_serializer import *
from ...models import DoencaDocumentada
from .doenca_serializer import DoecaSerializer

class DoencaDocumentadaBaseSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = DoencaDocumentada

class DoencaDocumentadaSerializer(DoencaDocumentadaBaseSerializer):
    doenca = DoecaSerializer(read_only=True)
    class Meta(DoencaDocumentadaBaseSerializer.Meta):
        pass
        
class DoecaDocumentadaCreateUpdateSerializer(DoencaDocumentadaBaseSerializer):
    class Meta(DoencaDocumentadaBaseSerializer.Meta):
        pass
