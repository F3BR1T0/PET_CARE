from rest_framework import serializers
from address import models
from pet_care_backend.utils import SerializerUtils

class AddressSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = models.Address