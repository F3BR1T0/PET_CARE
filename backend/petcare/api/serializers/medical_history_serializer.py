from .base_serializer import *
from ...models import MedicalHistory
from .medicine_serializer import MedicineSerializer

class MedicalHistorySerializer(BaseModelSerializer):
    medicines = MedicineSerializer(read_only=True, many=True)
    class Meta(BaseModelSerializer.Meta):
        model = MedicalHistory