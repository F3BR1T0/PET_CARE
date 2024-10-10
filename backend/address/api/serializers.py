from rest_framework import serializers
from address import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'