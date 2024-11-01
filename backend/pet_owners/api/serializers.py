from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from ..models import PetOwner
from address.api.serializers import AddressSerializer

from pet_care_backend.utils import SerializerUtils

class PetOwnerSerializer(SerializerUtils.BaseModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = PetOwner
        
class PetOwnerCreateUpdateSerializer(SerializerUtils.BaseModelExcludeSerializer):
    class Meta(SerializerUtils.BaseModelExcludeSerializer.Meta):
        model = PetOwner
        exclude = ['endereco']
        
class PetOwnerEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)