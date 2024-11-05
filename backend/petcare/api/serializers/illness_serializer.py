from .base_serializer import *
from ...models import IllnessStatus, Illness

class IllnessStatusSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = IllnessStatus
        
        
class IllnessSerializr(serializers.ModelSerializer):
    class Meta(serializers.ModelSerializer):
        model = Illness
        exclude = ('medical_history',)