from .base_serializer import *
from ...models import MedicalHistory

class MedicalHistorySerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = MedicalHistory